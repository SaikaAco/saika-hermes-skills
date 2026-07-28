---
name: burnable-visual-briefs
description: "Use when complex comparisons, architectures, processes, decisions, or risk boundaries are easier to understand as a graphic-first, minimal-text, temporary HTML brief."
version: 1.1.0
author: "SaikaAco with Hermes Agent"
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [visual-communication, html-report, diagrams, decision-briefs, transient-artifacts]
    related_skills: [hermes-workspace-hygiene]
---

# Burnable Visual Briefs

## Overview

Turn dense material into a graphic-first, minimal-text, self-contained HTML brief. The brief is a disposable communication surface, never the authoritative evidence store.

```text
canonical evidence → burnable visual brief → short caption + attachment
```

## Trigger gate

Use when the user asks for a visual, diagram, map, dashboard, or burnable report, or when a comparison, architecture, process, dependency, decision, or risk boundary is materially clearer spatially than in prose.

Do not use for simple facts, exact commands, source code/diffs, urgent alerts, canonical legal/audit artifacts, or decoration without information gain.

## Artifact contract

Write final briefs under:

```text
<active-workspace>/scratch/visual-briefs/
  <profile>/<YYYY-MM-DD>/<YYYYMMDDTHHMMSSZ>-<concise-slug>.html
```

Rules:

- one standalone UTF-8 `.html` file with a responsive viewport;
- mode `0600` on POSIX systems;
- inline CSS and SVG only;
- no JavaScript, external stylesheets, web fonts, trackers, forms, iframes, embedded objects, or remotely loaded assets;
- ordinary `https://` source links are allowed;
- include `hermes-created-at` and `hermes-expires-at` UTC metadata;
- expiry is no more than seven days after creation;
- never include credentials, hidden raw data, or unrelated personal information.

Use `templates/burnable-visual-brief.html` as a starting point and validate before delivery:

```bash
python3 <skill-package>/scripts/validate_brief.py \
  --root <active-workspace>/scratch/visual-briefs \
  /absolute/path/to/brief.html
```

## Graphic-first contract

Choose a visual grammar that matches the information:

| Information shape | Preferred visual |
|---|---|
| sequence or handoff | branching flow, swimlane, or timeline |
| architecture or dependency | node-link map, layered stack, or boundary graph |
| comparison | aligned matrix or grouped/stacked bar chart with real measures |
| status and thresholds | bar, bullet chart, sparkline, or gauge backed by observed values |
| decision and trade-off | decision tree, quadrant, or weighted trade-off plot |
| risk and control boundary | safe path, blocked path, or nested authority zones |

The base template provides an SVG branching route and nested boundary map. Adapt the geometry to the real relationships or replace it; delete unused sections.

Use position, grouping, color, line, direction, containment, and scale to encode meaning. Keep labels inside shapes short. Do not create long prose boxes, decorative meters without measurements, or rows of option cards that should be bullets. Never invent metrics to make a chart look complete.

## Durable-source boundary

A brief may summarize or point to canonical evidence, but it must not be the only copy of durable facts, approvals, source ledgers, recovery instructions, or specifications. If HTML itself is the durable deliverable, use the applicable report workflow and store it under `reports/`, not this transient path.

## Workflow

1. Identify one reading outcome: understand, compare, decide, or monitor.
2. Separate durable evidence from temporary presentation.
3. Select one dominant visual grammar and at most two supporting patterns.
4. Delete template sections that do not encode a real relationship, boundary, sequence, or measured comparison.
5. Fill every placeholder; add concise provenance, caveats, and next action.
6. Set UTC creation/expiry metadata and mode `0600` where applicable.
7. Run the standard-library validator.
8. Open locally and inspect desktop plus approximately 390px mobile width.
9. Check console errors, clipping, overlap, tiny text, page-level overflow, contrast, and connector semantics.
10. Deliver the attachment with a short caption; do not paste the report into chat.

## Seven-day lifecycle

At seven days, workspace hygiene should propose the expired file for cleanup. Deletion remains separately approval-gated. If a brief still matters, regenerate it from durable sources with current facts; do not refresh its timestamp merely to evade expiry.

## Common pitfalls

1. **HTML for everything.** Use it only when spatial communication reduces reading cost.
2. **Prose in cards.** Borders do not turn paragraphs into graphics.
3. **False geometry.** Connectors and containment must reflect actual semantics.
4. **Decorative data.** Charts require observed values.
5. **Remote assets.** They create privacy and availability risk.
6. **Orphaned truth.** Temporary HTML cannot be the sole evidence record.
7. **Unverified rendering.** Validator success does not replace visual QA.

## Verification checklist

- [ ] Trigger gate passed and the artifact reduces reading cost.
- [ ] An actual diagram or data-backed chart is visually dominant.
- [ ] Position, connectors, containment, or scale encodes real meaning.
- [ ] Text stays concise without hiding scope, uncertainty, risk, or action.
- [ ] Sources and durable artifacts are named or linked.
- [ ] No secret, private path, or unrelated personal data is present.
- [ ] File is self-contained, script-free, and mode `0600` on POSIX.
- [ ] Creation and seven-day expiry metadata are valid.
- [ ] Validator, desktop/mobile, overflow, contrast, and console checks pass.
