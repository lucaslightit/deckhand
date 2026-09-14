# deckhand

Slide decks as a single HTML file, written by Claude.

deckhand is a [Claude Code](https://claude.com/claude-code) skill. Ask for a presentation and
Claude builds a dark, keyboard-navigable deck from a library of ready-made components: no
build step, no dependencies, one file you open in a browser and present offline.

## What you get

- **A component library.** Numbered rows, ribbon banners, stacked cards, chevron process,
  stepper, bridge diagram, timeline, versus, quote, quadrant, meters, checklist, people,
  section dividers, card grids, stat rows, flows and tables. Every component reads the
  theme tokens, so a theme swap restyles the whole deck.
- **A template that is also the showcase.** Open `assets/template.html` and page through one
  slide per component.
- **Icons, not emoji.** Any [Iconify](https://iconify.design) set (Lucide by default),
  inlined as SVG while authoring, so a deck never loads anything at runtime.
- **Shareable slides.** The current slide lives in the URL (`deck.html?page=7`).
- **A full example.** `assets/example.html` is a 21-slide project kickoff that uses every
  component, in the Light-it theme.

## Install

The folder name must match the skill name, `generate-presentation`:

```bash
git clone <repo-url> ~/.claude/skills/generate-presentation
```

Then, in Claude Code: *"make a slide deck about our caching layer"*.

## Layout

```
SKILL.md                     how Claude builds a deck, step by step
references/components.md     component catalog: markup, limits, picking table, themes
assets/template.html         engine + component CSS + showcase slides
assets/example.html          complete example deck
assets/brand/                brand files inlined on title slides
scripts/icon.py              Iconify helper
```

## Icons

Write placeholders while authoring, then inline them:

```bash
python3 scripts/icon.py search database          # find ids (Lucide by default)
python3 scripts/icon.py inline path/to/deck.html  # <i data-icon="lucide:database"></i> → inline SVG
```

`inline` fetches all icons in one request per set and leaves the file untouched if any id
does not exist.

## Growing the library

Decks never carry their own component CSS. A new component lands in the skill, in two
places: its CSS and a showcase slide in `assets/template.html`, and its markup in
`references/components.md`.

## Brand assets

The Light-it logo in `assets/brand/` belongs to Light-it and is included for Light-it
decks only.
