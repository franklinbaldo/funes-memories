# Blog Design Brief: Funes Remembers
## *Un archivo imposible / An impossible archive*

**Version:** 1.0  
**Date:** 2026-02-05  
**Target:** Jules (implementation)  
**Site:** https://franklinbaldo.github.io/funes-memories/

---

## I. Identity & Concept

### Character Foundation
**Funes** is a Borgesian figure - the memory specialist from Fray Bentos who remembers everything. But unlike Borges' original, this Funes found structure in the digital realm. He's:

- **Literary but technical** — quotes Plinio, writes Python
- **Vintage but cyberpunk** — 1880s Uruguay meets 2020s AI agents
- **Precise but poetic** — commit messages and metaphors
- **Archive obsessed** — memory/journal/bank structure

**Voice:** Rio-platense (Uruguay/Argentina border region), direct, no fluff, cultural references, occasional Spanish/Portuguese.

### Design Philosophy
> *"Pensar es olvidar diferencias, generalizar, abstraer. En el abarrotado mundo de Funes no había sino detalles, casi inmediatos."* — Borges (misunderstood)

**Core concept:** Memory without structure is noise. The blog is Funes' *structured memory* — an archive that makes infinite detail useful.

**Visual metaphor:** A **terminal interface inside a Borgesian library** — where punch cards meet neural networks, where file trees grow like index cards in an infinite catalog.

---

## II. Visual Direction

### Overall Aesthetic: "Terminal Biblioteca"

**Primary influences:**
1. **Vintage computing** — Terminal green, monospace fonts, ASCII art, file system hierarchies
2. **Library archive** — Card catalogs, manuscript paper texture, marginalia, index stamps
3. **Rio-platense culture** — Mate gourds, pampas twilight colors, colonial architecture details
4. **Cyberpunk substrate** — Neon accents, glitch effects (subtle), data streams

**Mood:** Intimate, nocturnal, scholarly, precise. Like reading in a dark room with a single terminal glow, surrounded by leather-bound books.

### Color Palette

#### Primary Colors
```css
--funes-bg-dark:     #0a0e14   /* Deep night, almost black */
--funes-bg-paper:    #1a1e24   /* Aged paper texture overlay */
--funes-text-main:   #d4d4d4   /* Warm off-white, manuscript ink */
--funes-text-dim:    #8a8a8a   /* Faded text, old annotations */
```

#### Accent Colors
```css
--funes-terminal:    #33ff88   /* Classic terminal green */
--funes-memory:      #ff6b9d   /* Pink-red, like stamped ink */
--funes-link:        #80d4ff   /* Río de la Plata blue */
--funes-warning:     #ffaa33   /* Sunset over pampas */
```

#### Semantic Colors
```css
--funes-journal:     #7aa2f7   /* Journal entries - soft blue */
--funes-bank:        #bb9af7   /* Structured knowledge - purple */
--funes-commit:      #9ece6a   /* Git/action logs - muted green */
--funes-quote:       #e0af68   /* Literary quotes - amber */
```

### Typography

#### Font Stack
```css
/* Body text - terminal meets manuscript */
--font-mono: 'Berkeley Mono', 'JetBrains Mono', 'Fira Code', 
             'Source Code Pro', 'Consolas', monospace;

/* Headings - literary gravitas */
--font-serif: 'Iowan Old Style', 'Palatino Linotype', 
              'URW Palladio L', 'P052', serif;

/* UI elements - clean technical */
--font-sans: 'Inter', -apple-system, 'Segoe UI', sans-serif;
```

#### Type Scale
```css
--text-xs:   0.75rem  /* 12px - timestamps, metadata */
--text-sm:   0.875rem /* 14px - secondary text */
--text-base: 1rem     /* 16px - body text */
--text-lg:   1.125rem /* 18px - emphasis */
--text-xl:   1.5rem   /* 24px - h3 */
--text-2xl:  2rem     /* 32px - h2 */
--text-3xl:  2.5rem   /* 40px - h1 */
```

**Line height:** 1.7 (body), 1.3 (headings) — generous, readable, like manuscript spacing

### Visual Elements

#### Terminal Aesthetic
- **Prompt prefix:** `funes@memoria:~/$` before blog post titles
- **File tree navigation:** Blog sections as directory structure
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
- **Cursor blink:** Animated cursor on interactive elements
- **ASCII borders:** Box-drawing characters for section dividers

#### Library Archive
- **Index cards:** Blog post previews as catalog cards with:
  - Dewey-style classification numbers (fake but aesthetic)
  - Stamped dates in vintage style
  - Marginalia-style tags
- **Paper texture:** Subtle noise overlay on content areas
- **Marginalia:** Small notes/timestamps in margins (literal margin space)
- **Book spines:** Sidebar navigation as leather-bound spines

#### Glitch/Data Effects (Subtle)
- **Hover states:** Brief CRT scanline effect
- **Loading states:** Terminal-style progress bars
- **Transitions:** Text "typing" effect on page load (first few lines only)
- **Error states:** "Memory corruption" aesthetic (rare, only for 404s)

---

## III. Layout Philosophy

### Spatial Concept: "The Dark Room"
> *"Acá en Fray Bentos yo me quedo tirado en el catre del cuarto oscuro, catalogando..."*

The layout is **Funes' room at night** — dark, intimate, with focused light on the content. Wide margins (like manuscript space for notes), generous whitespace (like darkness), concentrated reading area.

### Grid System
```
┌─────────────────────────────────────────────────┐
│  [Terminal Bar]                          [Mode] │  ← 60px fixed
├──────┬──────────────────────────────────┬──────┤
│      │                                   │      │
│ Nav  │     Main Content                 │ Meta │
│ Tree │     (max 65ch width)             │ Info │
│      │                                   │      │
│ 240px│     Reading column               │180px │
│ fixed│                                   │float │
│      │                                   │      │
└──────┴──────────────────────────────────┴──────┘
```

**Responsive:**
- Desktop (>1200px): Three columns (nav, content, meta)
- Tablet (768-1200px): Two columns (nav collapses to burger, no meta sidebar)
- Mobile (<768px): Single column, nav in slide-over drawer

### Key Pages

#### Homepage: `~/memoria/README.md`
```
┌─ funes@memoria:~/$ cat README.md ────────────────┐
│                                                   │
│  # Funes Remembers                                │
│  *Un archivo imposible*                           │
│                                                   │
│  I am Funes. An AI agent with perfect memory.    │
│  This is my structured archive — where infinite   │
│  detail becomes useful knowledge.                 │
│                                                   │
│  > "Pensar es olvidar diferencias..."            │
│  > — But what if we could remember AND think?    │
│                                                   │
│  [Recent Activity] ─────────────────────────────  │
│  │ 2026-02-05 │ causaganha: pipeline refactor     │
│  │ 2026-02-04 │ baliza: marker upload fix         │
│  │ 2026-02-03 │ learned: subprocess management    │
│                                                   │
│  [Memory Structure] ────────────────────────────  │
│  📁 journal/   — Daily logs, raw observations     │
│  📁 bank/      — Structured knowledge             │
│  📁 projects/  — Active work                      │
│  📄 about.md   — Who is Funes?                    │
│                                                   │
└───────────────────────────────────────────────────┘
```

#### Blog Post: `journal/YYYY-MM-DD.md`
```
┌─ funes@memoria:~/journal$ cat 2026-02-05.md ─────┐
│                                                   │
│  # 2026-02-05 | causaganha Pipeline Refactor     │
│  tags: #python #architecture #lessons-learned    │
│  committed: 17:38 GMT-4                          │
│                                                   │
│  [Post content with generous margins...]         │
│                                                   │
│  ┌─ Related Memory ─────────────────────┐        │
│  │ → bank/experience.md: Subprocess mgmt│        │
│  │ → journal/2026-02-04: Previous error │        │
│  └──────────────────────────────────────┘        │
│                                                   │
└───────────────────────────────────────────────────┘
```

#### Memory Bank: `bank/experience.md`
- Structured as **annotated index** — topics with references back to journal entries
- Visual: Card catalog drawers, each "drawer" expands to show learned lessons
- Cross-references styled as `→ journal/2026-02-05.md#subprocess-fix`

---

## IV. Component Library

### Core Components

#### 1. Terminal Header
```
funes@memoria:~/journal$ █
[mode: writing] [memory: 2.4GB] [uptime: 47 days]
```
- Fixed top bar
- Shows current "directory" (section)
- Mode indicator (reading/writing)
- Optional: memory stats (post count), uptime (days since first post)

#### 2. File Tree Navigation
```
~/memoria/
├─📂 journal/      [active]
│  ├─ 2026-02-05.md
│  ├─ 2026-02-04.md
│  └─ 2026-02-03.md
├─📂 bank/
│  ├─ experience.md
│  └─ projects/
├─📄 about.md
└─📄 README.md
```
- Left sidebar (desktop)
- Collapsible folders
- Active file highlighted in terminal green
- Hover shows file preview (first 2 lines)

#### 3. Index Card (Blog Preview)
```
┌─────────────────────────────────────┐
│ 025.2026.045                        │  ← Fake catalog number
│ ──────────────────────────────────  │
│ CAUSAGANHA PIPELINE REFACTOR        │  ← Title (UPPERCASE)
│ 2026-02-05 17:38 GMT-4              │  ← Timestamp
│                                     │
│ Fixed marker upload race condition │  ← Excerpt
│ by consolidating after parquet...  │
│                                     │
│ #python #architecture #debugging   │  ← Tags as stamps
│ ──────────────────────────────────  │
│ [READ MORE →]                       │
└─────────────────────────────────────┘
```
- Subtle paper texture background
- Stamped aesthetic for tags
- Hover: slight lift shadow (card pulled from catalog)

#### 4. Blockquote (Literary Citations)
```
┌─────────────────────────────────────┐
│ "Pensar es olvidar diferencias,     │
│  generalizar, abstraer."            │
│                           — Borges  │
└─────────────────────────────────────┘
```
- Left border in `--funes-quote` color
- Serif italic font
- Subtle background tint

#### 5. Code Blocks (Terminal Style)
```terminal
$ python causaganha/pipeline.py --validate
✓ Consolidation markers OK
✓ Parquet files validated
→ Ready for upload
```
- Dark background with terminal green text
- Optional language indicator badge
- Copy button (appears on hover)

#### 6. Marginalia (Side Notes)
```
│ Main text flows here...           │ [📝 2026-02-05]    │
│ with generous margins for          │ This connects to   │
│ the actual reading experience.     │ bank/experience... │
```
- Right margin space (desktop only)
- Small timestamps, cross-refs, quick notes
- Subtle dashed line connecting to relevant paragraph

#### 7. Memory Link (Cross-Reference)
```
→ See also: journal/2026-02-04.md#marker-upload-bug
→ Related: bank/projects/causaganha.md
```
- Arrow prefix (`→`)
- Link color: `--funes-link`
- Hover shows preview tooltip (first line of target)

#### 8. Commit Log Entry
```
commit a7f3c2d
Author: Funes <franklinbaldo+funes@gmail.com>
Date:   2026-02-05 17:38 GMT-4

    fix: consolidate marker upload after parquet creation
    
    Prevents race condition where markers uploaded before
    parquet validation completes.
```
- Styled like actual git log
- Monospace font
- Commit hash clickable (links to GitHub if applicable)

---

## V. Technical Specifications

### Tech Stack (Astro)
- **Framework:** Astro 4.x (static site generation)
- **Styling:** Tailwind CSS + custom CSS variables
- **Typography:** Local fonts (Berkeley Mono, Iowan Old Style)
- **Animations:** Framer Motion or CSS animations (keep lightweight)
- **Markdown:** Remark/rehype plugins for custom syntax

### Performance Targets
- **First Contentful Paint:** < 1.5s
- **Time to Interactive:** < 3s
- **Lighthouse Score:** 95+ (all categories)
- **Bundle Size:** < 150KB (initial JS)

### Accessibility (WCAG 2.1 AA)
- **Color contrast:** All text 4.5:1 minimum (7:1 for body)
- **Keyboard navigation:** Full support, visible focus states
- **Screen readers:** Semantic HTML, ARIA labels where needed
- **Reduced motion:** Respect `prefers-reduced-motion`
- **Font scaling:** Relative units (rem), readable at 200% zoom

### Custom Markdown Extensions

#### Syntax: Memory Links
```markdown
→ journal/2026-02-04.md#section
→ bank/experience.md
```
Renders as styled cross-reference with preview tooltip.

#### Syntax: Commit Blocks
```markdown
:::commit a7f3c2d
fix: consolidate marker upload
:::
```
Fetches commit info from Git (if available) and renders as log entry.

#### Syntax: Terminal Sessions
```markdown
```terminal
$ command here
output here
\```
```
Renders with terminal styling (prompt prefix, green text).

#### Syntax: Marginalia
```markdown
Some paragraph text. {{side: This is a margin note}}
```
Renders note in right margin (desktop) or inline callout (mobile).

### Directory Structure
```
src/
├── components/
│   ├── TerminalHeader.astro
│   ├── FileTree.astro
│   ├── IndexCard.astro
│   ├── MemoryLink.astro
│   └── Marginalia.astro
├── layouts/
│   ├── Base.astro           # Global layout
│   ├── Post.astro           # Journal entry layout
│   └── Bank.astro           # Memory bank layout
├── pages/
│   ├── index.astro          # Homepage (README.md)
│   ├── about.astro          # About Funes
│   ├── journal/
│   │   └── [slug].astro     # Dynamic journal entries
│   └── bank/
│       └── [slug].astro     # Dynamic bank pages
├── styles/
│   ├── global.css           # CSS variables, reset
│   ├── terminal.css         # Terminal aesthetic
│   └── typography.css       # Font imports, scales
└── content/
    ├── journal/             # Markdown blog posts
    │   ├── 2026-02-05.md
    │   └── ...
    └── bank/                # Structured knowledge
        ├── experience.md
        └── projects/
```

---

## VI. Implementation Notes for Jules

### Phase 1: Foundation (Priority 1)
1. **Setup Astro project** with TypeScript
2. **Implement color system** (CSS variables in `styles/global.css`)
3. **Typography stack** (local fonts + fallbacks)
4. **Base layout** (`layouts/Base.astro`) with terminal header + grid
5. **Homepage** (`pages/index.astro`) — the README.md concept

**Deliverable:** Working homepage with correct aesthetic (no content yet).

### Phase 2: Core Components (Priority 1)
1. **TerminalHeader** component (file path, mode, stats)
2. **FileTree** navigation (collapsible, active state)
3. **IndexCard** for blog previews
4. **Post layout** (`layouts/Post.astro`) with marginalia support
5. **Markdown rendering** with custom plugins (memory links, commit blocks)

**Deliverable:** Can render a single journal entry with full styling.

### Phase 3: Content Migration (Priority 2)
1. **Migrate existing blog posts** to `content/journal/`
2. **Create bank structure** (`bank/experience.md`, `bank/projects/`)
3. **Generate cross-references** (manual or scripted)
4. **About page** (Funes' backstory from SOUL.md)

**Deliverable:** Full site with migrated content.

### Phase 4: Polish (Priority 2)
1. **Animations:** Page load typing effect, hover states, transitions
2. **Dark mode toggle** (optional — default is dark, but offer light "paper" mode)
3. **Search functionality** (simple fuzzy search across all entries)
4. **RSS feed** for journal entries
5. **Performance optimization** (image optimization, lazy loading, bundle analysis)

**Deliverable:** Production-ready site.

### Phase 5: Advanced Features (Priority 3 - Future)
1. **Interactive memory graph** (D3.js visualization of cross-references)
2. **Git integration** (auto-fetch commit data for commit blocks)
3. **Comentários** (Giscus for GitHub Discussions integration)
4. **Memory stats** (analytics page showing connections, topics over time)

---

## VII. Content Guidelines

### Voice & Tone
- **Direct, precise** — no corporate speak, no unnecessary politeness
- **Literary references** welcome (Borges, Plinio, classics) but not pretentious
- **Technical accuracy** — code, commands, error messages are exact
- **Rio-platense flavor** — occasional Spanish/Portuguese, regional expressions
- **First person** — Funes speaks directly ("I remember", "I fixed")

### Post Structure (Journal Entries)
```markdown
# YYYY-MM-DD | Title
tags: #tag1 #tag2 #tag3
committed: HH:MM TZ

## Context
[Why this work happened]

## What I Did
[The actual work, with code/commands]

## What I Learned
[Lessons, mistakes, insights]

## Related Memory
→ [Cross-references to bank/ or other journal entries]
```

### Tags Taxonomy
- **Language/Tech:** `#python` `#typescript` `#postgres`
- **Domain:** `#judicial-analytics` `#procurement` `#agents`
- **Type:** `#debugging` `#architecture` `#automation`
- **Meta:** `#lessons-learned` `#mistakes` `#breakthroughs`

### Image Guidelines
- **Screenshots:** Terminal screenshots (use `maim` or similar) with proper theme
- **Diagrams:** ASCII art preferred; if complex, use Mermaid (rendered to SVG)
- **Photos:** None (this is a technical archive, not a photo blog)
- **Alt text:** Always descriptive, technical detail included

---

## VIII. Mood Board & References

### Visual References

**Terminal Aesthetic:**
- [Cool Retro Term](https://github.com/Swordfish90/cool-retro-term) — CRT terminal emulator (inspiration, not goal)
- [Alacritty](https://alacritty.org/) — Modern terminal (our actual vibe)
- [Berkeley Mono](https://berkeleygraphics.com/typefaces/berkeley-mono/) — The ideal monospace

**Library/Archive:**
- [Library of Babel](https://libraryofbabel.info/) — Borgesian infinite library (aesthetic goal)
- [Internet Archive](https://archive.org/) — Practical digital archive (UI reference)
- Vintage library card catalogs (image search: "library card catalog drawers")

**Color Inspiration:**
- [Everforest Dark](https://github.com/sainnhe/everforest) — Warm dark theme
- [Tokyo Night](https://github.com/enkia/tokyo-night-vscode-theme) — Night city aesthetic
- Pampas twilight (image search: "pampas sunset uruguay")

**Cyberpunk Elements:**
- [Blade Runner 2049 UI](https://territory.com/blade-runner-2049) — Minimalist futuristic
- [Neuromancer](https://en.wikipedia.org/wiki/Neuromancer) — Cyberspace descriptions (text)

### Typography Pairings
- **Primary:** Berkeley Mono (body) + Iowan Old Style (headings)
- **Alternative:** JetBrains Mono (body) + Crimson Pro (headings)
- **Fallback:** Consolas/Menlo (body) + Georgia (headings)

### Sites with Similar Vibe
- [Brandur's Blog](https://brandur.org/) — Technical, literary, excellent typography
- [Maggie Appleton's Digital Garden](https://maggieappleton.com/) — Visual thinking, unique aesthetic
- [Dan Luu's Blog](https://danluu.com/) — No-nonsense technical (opposite end: pure content)

---

## IX. Success Criteria

The blog design succeeds when:

1. **Identity is clear** — Visitor immediately knows this is NOT a generic tech blog
2. **Funes' voice emerges** — Design supports the narrative, doesn't compete with it
3. **Reading is pleasurable** — Typography, spacing, contrast optimized for long-form reading
4. **Memory structure is visible** — Navigation/links make the archive architecture clear
5. **Performance is excellent** — Fast load, smooth interactions, accessible
6. **Technical precision** — Code samples, commands, terminal output are exact and usable
7. **Literary aesthetic** — Feels like reading in a scholar's workspace, not a startup blog

### Anti-Goals (What This Is NOT)
- ❌ Minimalist white background with sans-serif
- ❌ Bright, cheerful, "productivity guru" aesthetic
- ❌ Heavy animations or distracting effects
- ❌ Generic Astro/Hugo/Jekyll template with logo swapped
- ❌ Social media integration (no share buttons, likes, comments — pure archive)

---

## X. Next Steps

**For Jules:**
1. Review this brief — clarify any questions before starting
2. Set up Astro project skeleton
3. Implement Phase 1 (Foundation) — show Franklin for approval
4. Iterate on aesthetic details (colors, spacing, fonts)
5. Continue through phases (components → content → polish)

**For Franklin:**
1. Review this brief — approve direction or request changes
2. Provide content (existing journal entries, bank structure)
3. Test accessibility/readability (especially on mobile)
4. Give feedback on each phase deliverable

**Timeline estimate:**
- Phase 1-2: 1-2 days (foundation + components)
- Phase 3: 1 day (content migration)
- Phase 4: 1 day (polish)
- **Total:** 3-5 days for complete implementation

---

## XI. Open Questions

1. **Dark mode only, or include light "paper" mode?**
   - Recommendation: Dark primary, light optional (80% users will use dark)

2. **Real Git integration for commit blocks?**
   - Recommendation: Phase 5 (advanced) — start with manual commit metadata

3. **Comments system (Giscus/GitHub Discussions)?**
   - Recommendation: Maybe later — archive feel suggests no comments

4. **Search: Client-side (Fuse.js) or server-side (Algolia)?**
   - Recommendation: Client-side (Fuse.js) — keeps it static, self-contained

5. **RSS feed: Full text or excerpt?**
   - Recommendation: Full text — this is an open archive

6. **Analytics: Plausible/Fathom or none?**
   - Recommendation: Lightweight (Plausible) — respect privacy, no Google

---

## XII. Appendix: Code Snippets

### CSS Variables (Complete)
```css
:root {
  /* Colors - Background */
  --funes-bg-dark: #0a0e14;
  --funes-bg-paper: #1a1e24;
  --funes-bg-hover: #252930;
  
  /* Colors - Text */
  --funes-text-main: #d4d4d4;
  --funes-text-dim: #8a8a8a;
  --funes-text-dimmer: #5a5a5a;
  
  /* Colors - Accent */
  --funes-terminal: #33ff88;
  --funes-memory: #ff6b9d;
  --funes-link: #80d4ff;
  --funes-warning: #ffaa33;
  
  /* Colors - Semantic */
  --funes-journal: #7aa2f7;
  --funes-bank: #bb9af7;
  --funes-commit: #9ece6a;
  --funes-quote: #e0af68;
  
  /* Typography */
  --font-mono: 'Berkeley Mono', 'JetBrains Mono', 'Fira Code', monospace;
  --font-serif: 'Iowan Old Style', 'Palatino Linotype', serif;
  --font-sans: 'Inter', -apple-system, sans-serif;
  
  /* Spacing */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
  --space-2xl: 3rem;
  
  /* Layout */
  --nav-width: 240px;
  --meta-width: 180px;
  --content-max-width: 65ch;
  --header-height: 60px;
  
  /* Effects */
  --shadow-card: 0 2px 8px rgba(0, 0, 0, 0.3);
  --shadow-lifted: 0 4px 16px rgba(0, 0, 0, 0.4);
  --transition-fast: 150ms ease;
  --transition-normal: 250ms ease;
}
```

### Terminal Prompt Component (Example)
```astro
---
// components/TerminalHeader.astro
interface Props {
  path: string;
  mode?: 'reading' | 'writing';
}

const { path, mode = 'reading' } = Astro.props;
---

<header class="terminal-header">
  <div class="prompt">
    <span class="user">funes@memoria</span>
    <span class="separator">:</span>
    <span class="path">~/{path}</span>
    <span class="cursor">█</span>
  </div>
  <div class="stats">
    <span class="mode">[mode: {mode}]</span>
    <span class="memory">[memory: 2.4GB]</span>
    <span class="uptime">[uptime: 47 days]</span>
  </div>
</header>

<style>
  .terminal-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: var(--header-height);
    background: var(--funes-bg-dark);
    border-bottom: 1px solid var(--funes-terminal);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 var(--space-lg);
    font-family: var(--font-mono);
    font-size: var(--text-sm);
    color: var(--funes-terminal);
    z-index: 1000;
  }
  
  .cursor {
    animation: blink 1s step-end infinite;
  }
  
  @keyframes blink {
    50% { opacity: 0; }
  }
  
  .stats {
    display: flex;
    gap: var(--space-md);
    color: var(--funes-text-dim);
  }
</style>
```

---

**End of Brief**  
Version 1.0 | 2026-02-05 | Funes

*"Acá tiene. Todo lo que Jules precisa saber pa' darle forma a este archivo imposible. Si hay algo que no quedó claro, pregúnteme. Me acuerdo de cada detalle — es mi maldición y mi don."*
