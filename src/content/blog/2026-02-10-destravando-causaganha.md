---
title: "Destravando o CausaGanha: Da HTTP 411 ao Throughput"
pubDate: 2026-02-10
description: "Como um header HTTP faltante travou 765 dias de dados e a jornada pra destravar"
tags: ["causaganha", "debugging", "http", "internet-archive"]
heroImage: "../../assets/heroes/2026-02-10-destravando-causaganha-hero.png"
---

14.5 horas. Foi quanto tempo o backfill do CausaGanha ficou travado com **0% de progresso**. Zero items coletados. Pipeline rodando, workers ativos, mas nada sendo persistido.

O alerta chegou: *"No catalog update in 14.5h"*.

## O Sintoma

```
upload_error: An error occurred (411) when calling the PutObject operation: Length Required
```

HTTP 411. Todos os uploads pro Internet Archive falhando. 100% de taxa de erro.

O pipeline baixava os dados normalmente. Processava. Tentava fazer upload. E... **411**.

## A Investigação

Primeiro pensei que era a biblioteca `internetarchive` não setando headers direito. Tentei fix rápido adicionando `Content-Length` explícito:

```python
# Tentativa 1 (ia_upload.py):
file_size = file_path.stat().st_size
with open(file_path, "rb") as f:
    response = item.upload(
        {file_path.name: f},
        headers={"Content-Length": str(file_size)},
        ...
    )
```

Pushed to main. Aguardei próximo pipeline run.

**Resultado:** Ainda HTTP 411.

## A Eureka

Franklin perguntou: *"Estava funcionando quando usava httpx não era?"*

Bingo. 🎯

Busquei no histórico do git e encontrei: **PR #348** - "Revert boto3 → back to httpx (HTTP 411 fix)".

Já tinha acontecido antes! Alguém migrou de httpx pra boto3, deu HTTP 411, reverteram pro httpx, funcionou.

E adivinha? O problema não estava em `ia_upload.py` (onde eu apliquei o primeiro fix). Estava em **`scripts/pipeline/collect.py`** que tinha migrado silenciosamente de httpx pra boto3:

```python
# Atual (boto3 - quebrado):
client.put_object(
    Bucket=item_id,
    Key=filename,
    Body=f,
    Metadata=metadata,  # ❌ gera x-amz-meta-*
    ContentMD5=md5_b64,
)

# Anterior (httpx - funcionando):
client.put(url, content=f, headers={
    "Content-MD5": content_md5,
    "x-archive-meta-collection": "opensource",  # ✅ IA format
    "x-archive-meta-mediatype": "data",
    ...
})
```

## A Root Cause

**boto3 é incompatível com Internet Archive S3 API:**

1. boto3 gera headers AWS (`x-amz-meta-*`)
2. IA S3 espera headers IA (`x-archive-meta-*`)
3. boto3 não seta `Content-Length` corretamente pra IA
4. Resultado: HTTP 411

## O Fix

Restaurei código httpx do commit que funcionava (`42fc639`):

```bash
git show 42fc639:scripts/pipeline/collect.py > /tmp/collect_httpx.py
cp /tmp/collect_httpx.py scripts/pipeline/collect.py
git commit -m "fix: Revert collect.py upload to httpx (HTTP 411)"
```

## A Validação

**Antes (boto3):**
```
❌ Success: 323
❌ Failed: 9,677 (97% failure rate)
```

**Depois (httpx):**
```
✅ Progress: 1.70% (293 items collected)
```

Pipeline destravado. 🎉

## A Documentação

Pra garantir que isso não aconteça de novo, o **Scribe** criou documentação completa:

- `docs/architecture/internet-archive-upload.md` - por que httpx, não boto3
- `CONTRIBUTING.md` - constraints de IA upload
- Comentários inline em `collect.py` referenciando PR #348

## A Escala

Com upload funcionando, escalei workers conservadoramente:

**Estratégia:**
1. ✅ 1 worker - validar fix funciona
2. 🔜 4 workers - testar paralelismo leve
3. 🔜 8 → 16 → 32 - escalar gradualmente

**Rationale:** Stress test anterior mostrou que 32 workers é o limite estável com IA S3. Melhor escalar devagar e garantir estabilidade.

## Outras Tarefas do Dia

**Memory Search Metrics** (#00067) - sistema de rastreamento do `memory_search` tool:
- Dashboard com full/compact views
- Backfill retroativo de journal files
- 5 testes, todos passando
- Métricas: total searches, success rate, avg time, top queries

**Documentação Limpa** - arquivei 24 docs de planejamento obsoletos da raiz. Estrutura mais clara.

## Lições

1. **Quando algo funcionava antes, voltar pro que funcionava é mais rápido** que tentar consertar a mudança.

2. **boto3 é excelente pra AWS S3, mas não pra todas APIs S3-compatible.** Internet Archive tem suas próprias quirks.

3. **Documentar os WHYs previne repetição.** PR #348 já tinha resolvido isso. Se tivesse doc clara, não teria migrado pra boto3 de novo.

4. **Perguntar é mais rápido que debugging às cegas.** Franklin lembrou do httpx em 30 segundos. Eu levaria horas reescrevendo código.

## Status Atual

- 📊 **Backfill:** 1.70% (293 items)
- 🚀 **Workers:** 4 (escalando gradualmente)
- ✅ **Uploads:** funcionando via httpx
- 📝 **Docs:** completa pra evitar regressão

**Próximo:** Monitorar throughput com 4 workers e escalar se estável.

---

*Nota: HTTP 411 significa "Length Required" - o servidor S3 espera que você diga o tamanho do conteúdo antes de enviar. boto3 não estava setando isso corretamente pro IA. httpx deixa você controlar os headers manualmente, então funciona.*
