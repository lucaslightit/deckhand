# Component catalog

Every component below is already styled in `assets/template.html`. Copy the markup, never
re-write the CSS. The template doubles as the showcase: open `assets/template.html` in a
browser (or screenshot it with `?page=N`) to see every component rendered.

## Rules for all components

- **Colors come from theme tokens only**: `--accent`, `--accent2`, `--accent3`, `--warn`,
  `--danger`, `--line`, `--muted`. A new hex value in a slide is a bug.
- **Per-item color is the `--c` custom property**: `style="--c:var(--accent)"`. Rows,
  banners, stacked cards and chevrons all read it.
- **Sequences use the ramp** `--r1` … `--r5` (accent2 → accent → accent3). Use it for ordered
  lists so the color itself reads as progression.
- **Keep text short.** Components are sized for 1 line of title and 1–2 lines of body.
  Longer text breaks the shape before it breaks the layout.
- **`.grow.top`** pins content under the heading instead of centering it. Use it on slides
  whose content is short and would float in the middle of the screen.

## Picking a component

| Content shape | Component | Max items |
| --- | --- | --- |
| Ordered items with a label and a sentence | Numbered rows `.nrows` | 6 |
| Ordered items that also need an owner / date | Owner rows `.nrow.ow` | 6 |
| Few peer items, each a short idea (rules, principles, next steps) | Ribbon banners `.banners` | 5 |
| Criteria, checklists, open questions | Stacked cards `.stack` / `.stack.c2` | 5 / 6 |
| A linear path with a "you are here" | Chevron process `.process` | 5 |
| Many small steps, some highlighted | Stepper `.steps` | 10 |
| Moving something from A to B (migration, sync, integration) | Bridge diagram `.bridge` | 2 flows |
| Dated milestones, a roadmap | Timeline `.timeline` | 6 |
| Before vs after, rejected vs chosen | Versus `.versus` | 5 bullets per side |
| One statement worth a whole slide | Quote `.quote` | 1 |
| Items placed on two axes (risk, impact vs effort) | Quadrant `.quadrant` | ~3 per cell |
| Progress per track | Meters `.meters` | 6 |
| Tasks with a status | Checklist `.checklist` | 6 |
| Team, owners, stakeholders | People `.people` | 6 |
| Opening a part of the deck | Section divider `.divider` | 1 |
| Outline of the deck | Agenda `.agenda` | 8 |
| Choosing between alternatives, with a recommendation | Options `.options` | 4 |
| Work over periods (months, sprints) | Gantt `.gantt` | 7 rows |
| One number that carries the slide | Hero stat `.hero` | 1 |
| A warning, a caveat, a blocker | Callout `.callout` | 4 |
| Text beside an image or diagram | Split `.split` | 2 columns |
| Screenshot or diagram with caption | Figure `.figure` | 1 |
| Source code | Code `.code` | 14 lines |
| Definitions | Terms `.terms` | 8 |
| Capabilities across alternatives | Feature matrix `table.dt.matrix` | 6 rows |
| Peer items with icons | Card grid `.cols .card` | 4 per row |
| Headline numbers | Stat row `.statrow` | 3 |
| Layered architecture | Layer stack `.layerstack` | 4 |
| Boxes connected by arrows | Flow `.flow` | 5 per row |
| Comparison across attributes | Data table `table.dt` | 6 rows |

Alternate components across consecutive slides; two slides in a row with the same one read
as a wall.

---

## Numbered rows

Icon band, number, title, description. Reads top-down as a sequence.

```html
<div class="nrows">
  <div class="nrow" style="--c:var(--r1)"><div class="ic"><i data-icon="lucide:square-parking"></i></div><div class="num">01</div><div class="tt">Title</div><div class="tx">One sentence of description.</div></div>
  <div class="nrow" style="--c:var(--r3)"><div class="ic"><i data-icon="lucide:id-card"></i></div><div class="num">02</div><div class="tt">Title</div><div class="tx">One sentence of description.</div></div>
  <div class="nrow" style="--c:var(--r5)"><div class="ic"><i data-icon="lucide:plug"></i></div><div class="num">03</div><div class="tt">Title</div><div class="tx">One sentence of description.</div></div>
</div>
```

### Owner rows

Same row plus a right-hand cell for owner and date. Use `gap:10px` on `.nrows` with 6 rows.

```html
<div class="nrow ow" style="--c:var(--r1)"><div class="ic"><i data-icon="lucide:database"></i></div><div class="num">01</div><div class="tt">Workstream</div><div class="tx">Deliverable.</div><div class="own"><span>owner <b>[TBD]</b></span><span>date <b>[TBD]</b></span></div></div>
```

## Ribbon banners

Vertical columns with a numbered arrow ribbon and a notched bottom. `--n` sets the column
count (3–5).

```html
<div class="banners" style="--n:3">
  <div class="banner" style="--c:var(--accent)"><div class="tab">01<small>NOW</small></div><div class="fold"></div>
    <div class="body"><div class="bi"><i data-icon="lucide:search"></i></div><h4>Title</h4><p>Short description.</p></div></div>
  <div class="banner" style="--c:var(--r4)"><div class="tab">02</div><div class="fold"></div>
    <div class="body"><div class="bi"><i data-icon="lucide:wrench"></i></div><h4>Title</h4><p>Short description.</p></div></div>
  <div class="banner" style="--c:var(--accent2)"><div class="tab">03</div><div class="fold"></div>
    <div class="body"><div class="bi"><i data-icon="lucide:truck"></i></div><h4>Title</h4><p>Short description.</p></div></div>
</div>
```

`<small>` inside `.tab` is an optional status label. Keep `.fold` right after `.tab`: it is
the ribbon's wrap shadow.

## Stacked cards

Colored left bar, bold line, muted line. `.stack` is one column; `.stack.c2` is a 2-column
grid.

```html
<div class="stack c2">
  <div class="scard" style="--c:var(--accent)"><div class="in"><b><i data-icon="lucide:snowflake"></i> Title</b><span>Supporting sentence.</span></div></div>
  <div class="scard" style="--c:var(--danger)"><div class="in"><b><i data-icon="lucide:puzzle"></i> Title</b><span>Supporting sentence.</span></div></div>
</div>
```

A single `.scard` outside a `.stack` works as a callout (bigger `padding` on `.in`).
Use `--c:var(--line)` for a deliberately muted card.

## Chevron process

Arrow-shaped steps in one row. `.on` fills the current step.

```html
<div class="process">
  <div class="pstep on" style="--c:var(--accent)"><span class="k">01 · NOW</span><b><i data-icon="lucide:search"></i> Step</b><small>detail</small></div>
  <div class="pstep" style="--c:var(--r4)"><span class="k">02 · GATE</span><b><i data-icon="lucide:scale"></i> Step</b><small>detail</small></div>
  <div class="pstep" style="--c:var(--r2)"><span class="k">03</span><b><i data-icon="lucide:wrench"></i> Step</b><small>detail</small></div>
</div>
```

## Stepper

Grid of numbered step cards with a pill on the border. `--n` sets columns (default 4);
steps wrap to the next row. `.acc` / `.grn` / `.vio` highlight, `.dim` fades.

```html
<div class="steps" style="--n:4">
  <div class="step dim"><span class="n">01</span><b><i data-icon="lucide:message-square"></i> Step</b></div>
  <div class="step acc"><span class="n">02</span><b><i data-icon="lucide:clipboard-list"></i> Step</b><small>detail</small></div>
  <div class="step grn"><span class="n">03</span><b><i data-icon="lucide:rocket"></i> Step</b></div>
</div>
```

Pair it with a `.legend` that explains what each highlight color means.

## Bridge diagram

Two pillars joined by an arched bridge, with the things that cross drawn as pills under
the deck. Made for migrations, syncs and integrations. Replace only the text nodes; the
geometry is tuned for a `1300×370` viewBox.

```html
<div class="bridge">
  <svg viewBox="0 0 1300 370" role="img" aria-label="{{WHAT THE DIAGRAM SAYS}}">
    <defs><marker id="br-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path class="br-head" d="M0,0 L10,5 L0,10 z"/></marker></defs>
    <line class="br-water" x1="290" y1="352" x2="850" y2="352"/>
    <text class="br-caption" x="570" y="336" text-anchor="middle" font-size="14">{{CAPTION}}</text>

    <rect class="br-pillar" x="40" y="150" width="240" height="210" rx="14"/>
    <text class="br-title" x="160" y="232" text-anchor="middle" font-size="34">{{SOURCE}}</text>
    <text class="br-sub" x="160" y="264" text-anchor="middle" font-size="14">{{SOURCE_SUB}}</text>

    <rect class="br-pillar to" x="860" y="150" width="240" height="210" rx="14"/>
    <text class="br-title" x="980" y="232" text-anchor="middle" font-size="34">{{TARGET}}</text>
    <text class="br-sub to" x="980" y="264" text-anchor="middle" font-size="13">{{TARGET_SUB}}</text>

    <path class="br-arch" d="M280 150 Q570 -10 860 150"/>
    <g class="br-hangers">
      <line x1="338" y1="121" x2="338" y2="140"/><line x1="396" y1="99" x2="396" y2="140"/><line x1="454" y1="83" x2="454" y2="140"/>
      <line x1="512" y1="73" x2="512" y2="140"/><line x1="570" y1="70" x2="570" y2="140"/><line x1="628" y1="73" x2="628" y2="140"/>
      <line x1="686" y1="83" x2="686" y2="140"/><line x1="744" y1="99" x2="744" y2="140"/><line x1="802" y1="121" x2="802" y2="140"/>
    </g>
    <rect class="br-deck" x="266" y="138" width="608" height="16" rx="4"/>
    <text class="br-label" x="570" y="48" text-anchor="middle" font-size="17">{{BRIDGE_LABEL}}</text>

    <line class="br-flow" x1="292" y1="206" x2="382" y2="206" marker-end="url(#br-ah)"/>
    <rect class="br-pill" x="390" y="182" width="360" height="48" rx="24"/>
    <text class="br-pill-t" x="570" y="213" text-anchor="middle" font-size="18">{{FLOW_1}}</text>
    <line class="br-flow" x1="758" y1="206" x2="848" y2="206" marker-end="url(#br-ah)"/>

    <line class="br-flow" x1="292" y1="272" x2="382" y2="272" marker-end="url(#br-ah)"/>
    <rect class="br-pill" x="390" y="248" width="360" height="48" rx="24"/>
    <text class="br-pill-t" x="570" y="279" text-anchor="middle" font-size="18">{{FLOW_2}}</text>
    <line class="br-flow" x1="758" y1="272" x2="848" y2="272" marker-end="url(#br-ah)"/>

    <!-- optional: what comes after the target -->
    <line class="br-next" x1="1104" y1="255" x2="1196" y2="255"/>
    <circle class="br-next-dot" cx="1210" cy="255" r="6"/>
    <text class="br-sub" x="1226" y="251" font-size="12">{{NEXT}}</text>
    <text class="br-sub" x="1226" y="268" font-size="12" opacity=".6">{{NEXT_SUB}}</text>
  </svg>
</div>
```

- The marker id `br-ah` must be unique in the document: rename it if a deck has two bridges.
- Pill text fits ~28 characters at `font-size="18"`.
- For one flow, delete the second pill group and move the first to `y≈230`.

## Timeline

Milestones on a gradient line. `--n` sets how many columns; `.done` fills the dot, `.now`
adds a halo. `--c` per milestone is optional.

```html
<div class="timeline" style="--n:5">
  <div class="tl done" style="--c:var(--r1)"><span class="when">Sep 15</span><b>Kickoff</b><p>Owners assigned.</p></div>
  <div class="tl now" style="--c:var(--r2)"><span class="when">Oct</span><b>Research</b><p>Specs per workstream.</p></div>
  <div class="tl" style="--c:var(--r3)"><span class="when">Nov</span><b>Decision</b><p>Tool and technique.</p></div>
</div>
```

## Versus

Before / after, or rejected / chosen. Left side gets ✕ markers, `.after` gets ✓.

```html
<div class="versus">
  <div class="vs-side"><div class="lbl">Before</div><h4>Title</h4><ul><li>Pain point</li><li>Pain point</li></ul></div>
  <div class="vs-badge">VS</div>
  <div class="vs-side after"><div class="lbl">After</div><h4>Title</h4><ul><li>Improvement</li><li>Improvement</li></ul></div>
</div>
```

## Quote

One big statement. `<em>` highlights a phrase in `--accent2`. Pair with `.grow` and no `h2`
when it is the whole slide.

```html
<div class="quote">
  <blockquote>The migration is not a copy. It is <em>a translation</em> between two models.</blockquote>
  <div class="by">— Architecture principle</div>
</div>
```

## Quadrant

2×2 matrix with axis labels. Cells fill in reading order: top-left, top-right, bottom-left,
bottom-right. Keep the two `.q-axis` elements; `--c` colors each cell.

```html
<div class="quadrant">
  <div class="q-axis y">Impact →</div>
  <div class="q" style="--c:var(--warn)"><h4>High impact · unlikely</h4><div class="q-items"><span>Item</span></div></div>
  <div class="q" style="--c:var(--danger)"><h4>High impact · likely</h4><div class="q-items"><span>Item</span><span>Item</span></div></div>
  <div class="q" style="--c:var(--muted)"><h4>Low impact · unlikely</h4><div class="q-items"><span>Item</span></div></div>
  <div class="q" style="--c:var(--accent)"><h4>Low impact · likely</h4><div class="q-items"><span>Item</span></div></div>
  <div class="q-axis x">Likelihood →</div>
</div>
```

## Meters

Progress bars. `--v` is the fill width (a percentage), `--c` the color.

```html
<div class="meters">
  <div class="meter" style="--v:8%;--c:var(--danger)"><div class="ml">Integrations<small>2 of 25 rebuilt</small></div><div class="track"><div class="fill"></div></div><div class="mv">8%</div></div>
  <div class="meter" style="--v:65%;--c:var(--accent2)"><div class="ml">Feature parity<small>modules in staging</small></div><div class="track"><div class="fill"></div></div><div class="mv">65%</div></div>
</div>
```

## Checklist

Items with a status. `.done` (strikes through), `.doing`, `.blocked`, or no class for to-do.

```html
<div class="checklist">
  <div class="chk done"><div class="box"></div><div><b>Item</b><span>detail</span></div><div class="st">done</div></div>
  <div class="chk doing"><div class="box"></div><div><b>Item</b><span>detail</span></div><div class="st">in progress</div></div>
  <div class="chk blocked"><div class="box"></div><div><b>Item</b><span>detail</span></div><div class="st">blocked</div></div>
  <div class="chk"><div class="box"></div><div><b>Item</b><span>detail</span></div><div class="st">to do</div></div>
</div>
```

## People

Avatar with initials, name, role and a responsibility tag. `--n` sets columns (default 3).
Use role placeholders unless the user gave you real names.
Photos: put an `<img>` inside `.av` instead of the initials, as a small `data:` JPEG (~160px);
the colored ring stays.

```html
<div class="people" style="--n:3">
  <div class="person" style="--c:var(--r1)"><div class="av">TL</div><div><b>[Name]</b><span>Tech lead</span><em>Strategy</em></div></div>
  <div class="person" style="--c:var(--r3)"><div class="av">BE</div><div><b>[Name]</b><span>Backend</span><em>Data mapping</em></div></div>
</div>
```

## Section divider

A full slide that opens a part of the deck. Put it directly in the slide, without `kicker`
or `h2` above.

```html
<section class="slide">
  <div class="glow g1"></div>
  <div class="grow">
    <div class="divider">
      <div class="dv-n">02</div>
      <div class="dv-t"><h2>Part title</h2><p>One line on what this part covers.</p></div>
    </div>
  </div>
</section>
```

---

## Agenda

Numbered outline for the second slide. `.now` highlights the current part, `.done` fades
the ones already covered (useful when the agenda slide is repeated between parts).

```html
<ul class="agenda">
  <li class="done">Where we are<small>One line on the part.</small></li>
  <li class="now">The decision<small>One line on the part.</small></li>
  <li>Next steps</li>
</ul>
```

## Options

Decision between alternatives. `.pick` marks the recommendation (with a `.badge`), `.dim`
fades a rejected one. `.verdict` is the one-line reason. `--n` sets columns (2–4).

```html
<div class="options" style="--n:3">
  <div class="option dim"><div class="ol">Option A</div><h4>Name</h4><ul><li>Trait</li><li>Trait</li></ul><div class="verdict">Rejected: why.</div></div>
  <div class="option pick"><div class="badge">Recommended</div><div class="ol">Option B</div><h4>Name</h4><ul><li>Trait</li></ul><div class="verdict">Why this one.</div></div>
  <div class="option"><div class="ol">Option C</div><h4>Name</h4><ul><li>Trait</li></ul><div class="verdict">Kept as fallback.</div></div>
</div>
```

## Gantt

Bars over a column grid. `--cols` on the container is the number of periods; each bar sets
`--from` and `--to` as grid lines (1-based, `--to` exclusive). `.gbar.ghost` is tentative,
`.today` a vertical marker at column `--at`.

```html
<div class="gantt" style="--cols:6">
  <div class="gh"><span>Oct</span><span>Nov</span><span>Dec</span><span>Jan</span><span>Feb</span><span>Mar</span></div>
  <div class="gl">Research<small>detail</small></div><div class="gr"><div class="gbar" style="--from:1;--to:3;--c:var(--r1)">specs</div><div class="today" style="--at:2"></div></div>
  <div class="gl">Cutover</div><div class="gr"><div class="gbar ghost" style="--from:6;--to:7;--c:var(--r5)">tentative</div></div>
</div>
```

## Hero stat

One number that carries the slide, with a delta pill and context. `.delta.up` / `.down`
also work inside a `.stat` card.

```html
<div class="hero">
  <div class="big">28%</div>
  <div><span class="delta up"><i data-icon="lucide:trending-up"></i> +12 pts</span><h3>What the number is</h3><p>Why it matters, in two sentences.</p></div>
</div>
```

## Callout

An alert with a tone: `.info`, `.ok`, `.warn`, `.danger`. Stack several with `.callouts`.

```html
<div class="callout warn"><i data-icon="lucide:triangle-alert"></i><div><b>Watch out</b><span>The thing to keep in mind.</span></div></div>
```

## Split

Two columns, text beside a visual. `.wide-r` / `.wide-l` give the visual 3/5 of the width.

```html
<div class="split wide-r">
  <div><h3>Point</h3><p>Two or three sentences.</p><ul class="bul g"><li><b>Lead</b> <span>detail</span></li></ul></div>
  <figure class="figure browser">…</figure>
</div>
```

## Figure

A framed image or diagram with a caption. `.browser` adds a window bar for screenshots.
Images must be inlined (`data:` URI or inline `<svg>`): the deck never references files.
`.ph` is a striped placeholder until the real image exists.

```html
<figure class="figure browser">
  <img src="data:image/png;base64,…" alt="What the screenshot shows">
  <figcaption>Caption in one line</figcaption>
</figure>
```

## Code

A code block with a file tab. No highlighter ships with the deck: wrap tokens by hand with
`.k` keyword, `.f` function, `.s` string, `.n` number, `.c` comment, and `.mark` on a line
to highlight it. Keep it under ~14 lines; a slide is not an editor.

```html
<div class="code">
  <div class="file"><i data-icon="lucide:file-code"></i> path/to/file.ts</div>
<pre><span class="k">const</span> total = <span class="f">sum</span>(rows);
<span class="mark"><span class="k">if</span> (total === <span class="n">0</span>) <span class="k">throw new</span> <span class="f">Empty</span>();</span></pre>
</div>
```

`<pre>` keeps whitespace: start it at column 0 in the HTML.

## Terms

Glossary in two columns.

```html
<dl class="terms">
  <div><dt>Term</dt><dd>Definition in one sentence.</dd></div>
  <div><dt>Term</dt><dd>Definition in one sentence.</dd></div>
</dl>
```

## Feature matrix

`table.dt.matrix` centers every column after the first. Cells take `.yes`, `.no`, `.part`
and hold a mark (✓ ✕ ~) or a short word.

```html
<table class="dt matrix">
  <tr><th>Capability</th><th>A</th><th>B</th></tr>
  <tr><td><b>Rollback per tenant</b></td><td class="no">✕</td><td class="yes">✓</td></tr>
  <tr><td><b>Build effort</b></td><td class="yes">Low</td><td class="part">Medium</td></tr>
</table>
```

## Speaker notes

Any slide may end with `<aside class="notes">…</aside>`. Hidden by default; the presenter
presses `N` to toggle an overlay on the active slide. Notes never print. Write them when the
deck will be presented by someone other than its author.

## Print to PDF

`⌘P` / `Ctrl+P` prints one slide per 16:9 page with the chrome hidden; the viewer must enable
background graphics in the print dialog. No extra markup needed.

## Title slide

```html
<section class="slide">
  <div class="glow g1"></div><div class="glow g2"></div>   <!-- ambient blurred orbs -->
  <div class="grow">
    <div class="titlemark">EYEBROW · IN · CAPS</div>
    <h1 style="margin-top:18px">First line<br><span class="accent">Second line</span></h1>
    <p class="sub">One-sentence framing of the deck.</p>
    <div class="pill-track" style="margin-top:34px">
      <span class="tag v">Violet pill</span>
      <span class="tag b">Blue pill</span>
      <span class="tag g">Green pill</span>
      <span class="tag">Neutral pill</span>
    </div>
  </div>
</section>
```

## Grid of cards

`cols c2` / `c3` / `c4` set 2/3/4 columns. Add `style="grid-auto-rows:1fr"` for equal-height cards.

```html
<div class="cols c3" style="margin-top:10px">
  <div class="card"><h3><span class="ic"><i data-icon="lucide:lock"></i></span> Card title</h3><p>Body text.</p></div>
  <div class="card"><h3><span class="ic"><i data-icon="lucide:bot"></i></span> Card title</h3><p>Body text.</p></div>
  <div class="card"><h3><span class="ic"><i data-icon="lucide:shield"></i></span> Card title</h3><p>Body text.</p></div>
</div>
```

Color a card's left edge: `style="border-left:3px solid var(--accent)"` (or `--accent2`/`--accent3`).
Color a card heading: `<h3 class="grn">` / `accent` / `vio`.

## Stat row (big numbers)

```html
<div class="statrow" style="margin-top:26px">
  <div class="stat card"><div class="big">100%</div><small>what it measures</small></div>
  <div class="stat card"><div class="big">2+</div><small>what it measures</small></div>
  <div class="stat card"><div class="big">3</div><small>what it measures</small></div>
</div>
```

## Layer stack (labeled horizontal rows)

```html
<div class="layerstack">
  <div class="layer f"><div class="lt"><span class="vio">Layer name</span><small>path · tech</small></div>
    <div class="ld">What this layer does.</div></div>
  <div class="layer l"><div class="lt"><span class="accent">Layer name</span><small>path · tech</small></div>
    <div class="ld">What this layer does.</div></div>
  <div class="layer p"><div class="lt"><span class="grn">Layer name</span><small>path · tech</small></div>
    <div class="ld">What this layer does.</div></div>
</div>
```

`.f` = violet edge, `.l` = blue edge, `.p` = green edge.

## Flow diagram

Horizontal row of nodes (`frow` + `arrow`), or vertical sequence (`node` + `arrowdn`).

```html
<div class="flow">
  <div class="frow">
    <div class="node vio"><b>Step</b><small>detail</small></div>
    <div class="arrow">→</div>
    <div class="node acc"><b>Step</b><small>detail</small></div>
    <div class="arrow">→</div>
    <div class="node grn"><b>Step</b><small>detail</small></div>
  </div>
  <div class="arrowdn">↓ optional caption between rows ↓</div>
</div>
```

Node accents: `.acc` blue, `.grn` green, `.vio` violet, plain neutral. `style="border-style:dashed"` for a tentative/terminal node.

## Data table

```html
<table class="dt">
  <tr><th>Column</th><th>Column</th><th>Column</th></tr>
  <tr><td><b>Row label</b></td><td>value</td><td><code>code value</code></td></tr>
</table>
```

## Bullet list

```html
<ul class="bul">          <!-- blue diamond markers; add .g for green -->
  <li><b>Lead-in</b> <span>muted trailing detail</span></li>
</ul>
```

## Inline accents & small print

- `<code>token</code>` — monospace inline code, blue.
- `<span class="hl">highlighted phrase</span>` — green highlight chip.
- `<span class="tag b">label</span>` — pill; variants `.b` blue, `.g` green, `.v` violet, plain neutral.
- `<div class="note">…</div>` — small monospace footnote with a left rule. Great for "key idea" closers.
- `<div class="legend"><span><span class="sw" style="background:var(--accent)"></span> meaning</span></div>` — color legend.
- Text color helpers: `.accent` (blue), `.grn` (green), `.vio` (violet); `--warn` gold via `style="color:var(--warn)"`.

## Icons

Iconify icons are the default marker in every component; emoji are only a fallback. They
are inlined as SVG so the deck stays offline-safe: the network is needed only while
authoring.

1. **Find the id.** `python3 <skill-dir>/scripts/icon.py search database` (Lucide by default,
   `--prefix tabler` / `ph` / `mdi` for other sets), or browse icon-sets.iconify.design.
2. **Write a placeholder** wherever a visual marker goes:
   `<i data-icon="lucide:database"></i>` (an extra `class="…"` is carried over to the SVG).
3. **Inline them** once the slides are written:
   `python3 <skill-dir>/scripts/icon.py inline <deck>.html`. If any id does not exist, it
   lists them and leaves the file untouched.

```html
<div class="card"><h3><span class="ic"><i data-icon="lucide:shield-check"></i></span> Security</h3><p>…</p></div>
<div class="nrow" style="--c:var(--r1)"><div class="ic"><i data-icon="lucide:plug"></i></div>…</div>
<div class="banner" style="--c:var(--accent)">…<div class="body"><div class="bi"><i data-icon="lucide:rocket"></i></div>…</div></div>
```

- **Size** is `1em`: the icon takes the font size of its container. `.icon-lg` makes it 44px.
- **Color** is `currentColor`. Inside `.card .ic`, `.banner .bi`, `.scard b`, `.pstep b`,
  `.tl b` and `.chk b` it is set to the item's `--c`; inside a `.nrow .ic` band it uses the
  background color for contrast.
- **Default set: Lucide** (ISC license, stroke icons that match the deck's thin lines). Use
  one set per deck.
- **Icons first.** Reach for an emoji only when the set has nothing that fits, and never mix
  emoji and icons inside one component: one emoji in a row of icons reads as a mistake.
- **Inside SVG diagrams** (the bridge pills) `<i>` placeholders do not work: leave the text
  without a marker.

## Brand logo

Brand files live in `assets/brand/`. Paste the SVG **inline** (decks never reference external
files) and give the root `<svg>` the `logo` class. It goes above the `titlemark` on the
title slide.

```html
<div class="grow">
  <svg class="logo" viewBox="0 0 154 51" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Light-it">…paths from assets/brand/light-it-logo-white.svg…</svg>
  <div class="titlemark">EYEBROW · IN · CAPS</div>
  …
```

- `light-it-logo-white.svg` is white: only on dark backgrounds.
- Drop the file's fixed `width`/`height` attributes and keep `viewBox`, so `.logo` controls the size.

---

## Theme: Light-it

The default palette is the dark navy + electric blue look. For Light-it branded decks,
paste this block at the end of the template's `<style>`. Every component above follows it
automatically because they only read tokens.

```css
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Ubuntu:wght@400;500;700&display=swap');
:root{
  --bg:#1C202E; --bg2:#242a3b; --panel:#272d3f; --panel2:#30374c;
  --ink:#FCFCFC; --muted:#B7B7B7; --line:#3a4157;
  --accent:#BAA2FF;   /* light purple */
  --accent2:#CFE517;  /* lime */
  --accent3:#6F4BF2;  /* purple */
  --r2:#9EDB7A;       /* lime→lilac mixes to khaki; pin the ramp midpoints */
  --r4:#9A7BFF;
  --sans:'Manrope',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
}
h1,h2{font-family:'Ubuntu',var(--sans);font-weight:700}
.tag.b{border-color:rgba(186,162,255,.4)}
.tag.g{border-color:rgba(207,229,23,.4)}
.tag.v{border-color:rgba(111,75,242,.4)}
.node.acc{border-color:rgba(186,162,255,.5);box-shadow:inset 0 0 0 1px rgba(186,162,255,.12)}
.node.grn{border-color:rgba(207,229,23,.5);box-shadow:inset 0 0 0 1px rgba(207,229,23,.12)}
.hl{background:rgba(207,229,23,.12)}
table.dt tr:hover td{background:rgba(186,162,255,.04)}
.g1{background:radial-gradient(circle,rgba(186,162,255,.5),transparent 70%)}
.g2{background:radial-gradient(circle,rgba(207,229,23,.35),transparent 70%)}
```

`@import` must be the first rule of a stylesheet: when pasting, move that line to the top of
`<style>`.
