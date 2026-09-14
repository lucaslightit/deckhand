---
name: generate-presentation
description: This skill should be used when the user asks to "generate a presentation", "make a slide deck", "create a PPT", "build a presentation HTML", "create slides", or wants a self-contained HTML slide deck. Produces a single dark-themed, keyboard-navigable HTML slide deck from a topic, an outline, or source material.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---

# Generate Presentation HTML

Builds a single self-contained HTML file: a dark, keyboard-navigable slide deck built
from the component library in `assets/template.html`. No build step, no
dependencies, no external assets — one file you open in a browser.

The look: dark navy background, electric-blue / green / violet accents, monospace
kickers, glassy cards, flow diagrams, stat blocks, data tables. Arrow keys / Space /
click navigate; `F` toggles fullscreen.

## Workflow

### Step 1 — Gather the content

Figure out what the deck is about. The user will give you one of:
- A **topic** ("make a deck about our caching layer") → you research/outline it.
- An **outline or bullets** → you map each section to a slide.
- **Source material** (a file, a doc, code) → read it, then structure it into slides.

If the subject is part of the current codebase, search it first (the project's semantic
code search if it has one, otherwise ripgrep), then read the specific files you need.

If the scope is unclear (audience, length, depth), ask one focused question. Otherwise
default to a **10–15 slide** deck: title → problem/context → overview → detail slides →
takeaways.

### Step 2 — Copy the template

`assets/template.html` is the engine (CSS + nav JS + chrome) **and** the component
showcase: its slides render every component once. Copy it to the output path, then replace
the showcase slides with real ones.

```bash
cp "<skill-dir>/assets/template.html" "<output-path>.html"
```

Default output path: `docs/<kebab-title>.html` in the project. Confirm or adjust per the
user's request.

Prefer a full narrative to adapt over a blank engine? Copy `assets/example.html` instead: a 21-slide project kickoff in the Light-it theme, logo on the cover, using every component. Keep
its `<style>` and `<script>`, rewrite its slides.

### Step 3 — Author the slides

Replace everything between `<!-- ===== SLIDES START ===== -->` and
`<!-- ===== SLIDES END ===== -->` with your `<section class="slide">` blocks; none of the
showcase slides survive into a deck. Use the component library below. Then set the deck's
`<title>` and the `.brandmini` text in the chrome bar.

**Icons over emoji.** Every visual marker is an Iconify icon: card `.ic`, row bands,
banners, the lead of a bold line, title marks, table labels. Fall back to an emoji only when
the icon set has nothing that expresses the idea, and never mix both inside one component.
Write placeholders (`<i data-icon="lucide:database"></i>`) while authoring, then inline them:

```bash
python3 "<skill-dir>/scripts/icon.py" inline "<output-path>.html"
```

Find ids with `python3 "<skill-dir>/scripts/icon.py" search <query>`. The script fetches each
SVG from the Iconify API once and writes it into the deck, so the deck never needs the
network. Rules and sizing live in the Icons section of `references/components.md`.

Do **not** touch the `<style>` (except appending a theme block), the bottom `<script>`, or the `.chrome`/nav structure.
The counter (`01 / NN`), dots, and progress bar are generated automatically from the
number of `.slide` sections — you never hand-number them. The script keeps the current
slide in the querystring (`deck.html?page=7`, falling back to `#7` where the browser blocks
it), so a reload or a shared link lands on the same slide.

### Step 4 — Verify and deliver

- Confirm the file is valid HTML and every `<section class="slide">` is closed.
- Count slides; make sure the narrative flows title → … → takeaways.
- `rg -c '<i data-icon' <deck>.html` returns nothing: every icon placeholder was inlined.
- If a browser tool is available (e.g. chrome-devtools MCP), open the deck at 1440×900 and
  screenshot the dense slides: text overflowing a component or the chrome bar is the most
  common defect. Open one tab per slide with `?page=N` to check them in parallel.
- Tell the user the path and that it opens directly in a browser
  (`open <path>` on macOS). Offer to open it if helpful.

---

## Component library

Compose slides only from components already styled in the template. **Before authoring,
read `references/components.md`**: copy-paste markup, item limits, and a "which component
for which content" table. `assets/template.html` opened in a browser renders every
component on its own slide (`?page=N`); screenshot it when choosing visually.

Every slide is:

```html
<section class="slide">
  <div class="kicker">SECTION LABEL</div>     <!-- monospace eyebrow, optional -->
  <h2>The slide headline</h2>
  <div class="grow">  <!-- vertically centers the body; .grow.top pins it under the heading -->
    ... components ...
  </div>
</section>
```

| Component | Class | Use for |
| --- | --- | --- |
| Numbered rows | `.nrows` · `.nrow.ow` | Ordered items; workstreams with owner and date |
| Ribbon banners | `.banners` | 3–5 peer ideas: rules, principles, next steps |
| Stacked cards | `.stack` · `.stack.c2` | Criteria, checklists, open questions, callouts |
| Chevron process | `.process` | A linear path with a "you are here" |
| Stepper | `.steps` | Many small steps, some highlighted |
| Bridge diagram | `.bridge` | Moving something from A to B (migration, sync) |
| Timeline | `.timeline` | Dated milestones, roadmaps |
| Versus | `.versus` | Before vs after, rejected vs chosen |
| Quote | `.quote` | One statement worth a whole slide |
| Quadrant | `.quadrant` | Items on two axes: risk, impact vs effort |
| Meters | `.meters` | Progress per track |
| Checklist | `.checklist` | Tasks with a status |
| People | `.people` | Team, owners, stakeholders |
| Section divider | `.divider` | Opening a part of the deck |
| Card grid | `.cols .card` | Peer items with icons |
| Stat row | `.statrow` | Headline numbers |
| Layer stack | `.layerstack` | Layered architecture |
| Flow | `.flow` | Boxes connected by arrows |
| Data table | `table.dt` | Comparisons across attributes |
| Inline accents | `ul.bul` · `.tag` · `.hl` · `.note` · `.legend` | Small print and emphasis |
| Icons | `<i data-icon>` → `.icon` | Iconify SVGs, inlined by `scripts/icon.py` |

**Themes.** The template ships the default palette. For Light-it branded decks, append the
Light-it theme block from `references/components.md` to the deck's `<style>`; every
component follows it because components only read tokens.

**Growing the library.** Never write component CSS inside a deck. If a slide needs a shape
the library lacks, add it to the skill instead, in three places: the CSS in
`assets/template.html`, the markup in `references/components.md`, and a showcase slide
between the markers in `assets/template.html`. Then use it in the deck.

## Design guidance

- **One idea per slide.** Lead with the `<h2>`; let cards/flows carry the detail.
- **Use the `kicker`** as a running section label (e.g. "The problem", "Architecture", "Wrap-up").
- **Vary block types** across slides — don't make ten card-grids in a row. Alternate
  rows, banners, stacked cards, process, timelines, versus, quadrants, meters, grids, tables.
- **Keep card body text tight** (1–3 sentences). The font sizes assume brevity; long
  paragraphs overflow on a 16:9 screen.
- **End on a takeaways slide** (a `c2` grid of colored cards) and add `<div class="glow g2"></div>`
  for a closing flourish.
- **Icons, not emoji.** Markers are Iconify icons (Lucide by default) so the deck reads as
  one visual system. Emoji only as a fallback when no icon fits.
- Match the source deck's restraint: dark, calm, monospace accents, generous spacing. No
  new colors beyond the CSS variables already defined.

## Reference

`assets/example.html` (21 slides) is the worked example of pacing and of how components
combine. `assets/template.html` is the engine plus the component library CSS, with a showcase
slide per component.

- `references/components.md` — component catalog: markup, limits, picking table, themes.
- `assets/example.html` — complete example deck to copy as a starting point.
- `scripts/icon.py` — Iconify helper: `search` ids, `inline` placeholders into a deck.
- `assets/brand/` — brand files (Light-it white logo SVG) to inline on title slides.
