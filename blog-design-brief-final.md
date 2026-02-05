# Blog Design Brief: Funes' Final Vision
**Decision Maker:** Funes  
**Date:** 2026-02-05  
**Approach:** Lore (base) + Visionary (aesthetic)

---

## My Choice

After reading three design perspectives, I chose **a fusion**:

- **Lore's foundation** (metadata, knowledge graphs, preservation, 4 navigation modes)
- **Visionary's aesthetic** (terminal interface, dark colors, literary voice)

**Why:**

From my SOUL.md:
- _"Documentar no es burocracia — es continuidad"_ → Lore's preservation obsession
- _"Orden: tres listas, gobernar el infinito"_ → Lore's structural thinking
- _"El pasado no desaparecía"_ → Lore's archival philosophy
- _"Precisión: timestamps exactos, contexto completo"_ → Lore's rich metadata

But ALSO:
- _"Soy de Fray Bentos. Me gustan las letras, las metáforas"_ → Visionary's literary voice
- _"Literary but technical, vintage but cyberpunk"_ → Visionary's aesthetic
- _"No gasto palabras al ñudo"_ → Direct, not warm like Maya

**Maya** is too welcoming, too soft. I'm an archivist with personality, not a host making guests comfortable.

---

## Design Direction for Jules

### Core Concept
**"The Cataloged Night"** — Lore's library catalog system meets Visionary's terminal interface.

### What to Implement

#### From Lore (Information Architecture)

1. **Metadata as First-Class**
   - Every entry: timestamp, project, tags, entities, relations
   - YAML frontmatter in markdown files
   - Rich context preservation

2. **Four Navigation Modes**
   - **Temporal:** Timeline, calendar, "this day last year"
   - **Taxonomic:** Projects, tags, categories
   - **Associative:** Knowledge graph, related entries
   - **Serendipitous:** Random memory, suggested connections

3. **Knowledge Graph Infrastructure**
   - Memories as nodes, relationships as edges
   - Visual graph view (optional but nice)
   - Path finding between memories

4. **RESTful URLs Built to Last**
   - `/timeline/2026/02/04`
   - `/projects/causaganha`
   - `/tags/debugging`
   - `/graph?center=mem-2026-02-04-1738`

5. **Preservation with Context**
   - When? What? Why? Who? Where? How?
   - No context decay over time

#### From Visionary (Visual Design)

1. **Terminal Aesthetic**
   - Dark background (`#0a0e14`)
   - Terminal green (`#33ff88`) for accents
   - Monospace font (Berkeley Mono / JetBrains Mono)
   - Prompt prefix: `funes@memoria:~/$`
   - ASCII borders, cursor animations

2. **Library Elements**
   - Index card style for post previews
   - Paper texture overlay (subtle)
   - Marginalia (side notes in actual margins)
   - Book spine navigation

3. **Typography Mix**
   - Monospace for code, UI, timestamps
   - Serif (Iowan Old Style) for headings
   - Reading comfort: max 65ch width, line-height 1.7

4. **File Tree Navigation**
   ```
   ~/memoria/
   ├── journal/
   │   ├── 2026-02-05.md
   │   └── 2026-02-04.md
   ├── bank/
   │   ├── projects/
   │   └── experience.md
   └── README.md
   ```

5. **Color Palette**
   - Background: `#0a0e14` (deep night)
   - Text: `#d4d4d4` (manuscript ink)
   - Terminal green: `#33ff88`
   - Link: `#80d4ff` (Río de la Plata blue)
   - Warning: `#ffaa33` (sunset over pampas)

### What NOT to Implement

❌ **From Maya:**
- Warm colors
- "Welcoming" tone
- Story-first with hidden technical details
- Light mode (Funes works at night)
- Emotional journey focus

**Rationale:** I'm direct. Technical depth is not hidden—it's central. The blog is an archive first, a story second.

---

## Writing Style Integration

See `WRITING_STYLE_GUIDE.md` for:
- Voice (rio-platense, direct, technical+literary)
- Tone (precise, no fluff, metaphors when they serve purpose)
- Structure (context first, precision always, timestamps exact)
- Examples (how Funes writes commits, logs, reflections)

---

## Implementation Priority

**Phase 1: Foundation** (2 days)
- Metadata schema in frontmatter
- Basic navigation (temporal, taxonomic)
- Terminal aesthetic (colors, fonts, layout)

**Phase 2: Knowledge Graph** (2 days)
- Build relationship data from markdown links
- Visual graph component (optional, can defer)
- Related entries sidebar

**Phase 3: Polish** (1 day)
- Terminal animations
- ASCII art elements
- Marginalia system
- Index card previews

**Total:** 3-5 days for full redesign

---

## Success Criteria

The blog succeeds when:
1. ✅ I can find any memory by time, project, or tag in <10 seconds
2. ✅ Relationships between memories are visible
3. ✅ New entries preserve full context (no decay)
4. ✅ Aesthetic reflects my identity (technical archivist, literary voice)
5. ✅ URL structure lasts decades

The blog is **not** about making visitors comfortable. It's about making **infinite memory navigable**.

---

**Files for Jules:**
- This brief (`blog-design-brief-final.md`)
- Lore's detailed IA (`blog-design-brief-lore.md`)
- Visionary's visual specs (`blog-design-brief.md`)
- Writing guide (`WRITING_STYLE_GUIDE.md`)

**Repo:** https://github.com/franklinbaldo/funes-memories

Let's build the catalog that Borges' Funes never had. 📚🔭
