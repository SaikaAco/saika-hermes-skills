# Saika Hermes Skills

A small public tap of bounded, reusable workflow skills for [Hermes Agent](https://github.com/NousResearch/hermes-agent).

These packages are curated from workflows used in practice. The repository remains deliberately focused: only portable skills with clear boundaries and no personal configuration are included.

## Available skills

| Skill | Version | Purpose |
|---|---:|---|
| [`bounded-grilling`](skills/bounded-grilling/SKILL.md) | 1.2.0 | Resolve a small number of material human decisions without endless interviewing or automatic implementation. |
| [`burnable-visual-briefs`](skills/burnable-visual-briefs/SKILL.md) | 1.1.0 | Create temporary, diagram-first HTML briefs with strict privacy, expiry, validation, and rendering gates. |
| [`context-budget-orchestration`](skills/context-budget-orchestration/SKILL.md) | 1.2.0 | Contain bulky context, size delegation correctly on the first attempt, embargo unchanged timeout retries, and reserve capacity for verification. |
| [`hermes-backup-recovery`](skills/hermes-backup-recovery/SKILL.md) | 1.0.0 | Build encrypted, atomic Hermes backups with WAL-safe databases, manifest gates, and verified clean-room recovery. |
| [`hermes-workspace-hygiene`](skills/hermes-workspace-hygiene/SKILL.md) | 1.0.0 | Keep generated artifacts scoped and make cleanup manifest-bound, approval-gated, and recoverable. |
| [`skill-lifecycle-management`](skills/skill-lifecycle-management/SKILL.md) | 1.1.0 | Author, package, attribute, publish, consumer-test, consolidate, and archive Hermes skills safely. |
| [`kanban-workflows`](skills/kanban-workflows/SKILL.md) | 1.1.0 | Coordinate durable Hermes Kanban work with retry-safe creation, role boundaries, and verifiable handoffs. |
| [`plan`](skills/plan/SKILL.md) | 2.1.1 | Produce plan-only implementation contracts with exact files, interfaces, tests, reviewable tasks, and no automatic execution. |
| [`prototype`](skills/prototype/SKILL.md) | 1.0.0 | Build one runnable throwaway artifact as decision evidence, require human reaction, and forbid automatic production promotion. |
| [`to-spec`](skills/to-spec/SKILL.md) | 1.2.0 | Adaptive LIGHT/FULL compilation of settled decisions into traceable requirements and acceptance evidence. |
| [`to-tickets`](skills/to-tickets/SKILL.md) | 2.0.0 | Compile one accepted source snapshot into a traceable implementation-ticket graph with separate publication authority. |
| [`wayfinder`](skills/wayfinder/SKILL.md) | 1.3.0 | Adaptive LIGHT/FULL route finding with typed evidence, prototype, decision, and prerequisite handlers. |
| [`wf`](skills/wf/SKILL.md) | 1.0.1 | Route genuine ambiguity to evidence, one human decision, a prototype, or Wayfinder without expanding authority. |

## Install as a Hermes tap

```bash
hermes skills tap add SaikaAco/saika-hermes-skills
hermes skills inspect SaikaAco/saika-hermes-skills/bounded-grilling
hermes skills install SaikaAco/saika-hermes-skills/bounded-grilling
```

Install the other packages by replacing the final slug with `burnable-visual-briefs`, `context-budget-orchestration`, `hermes-backup-recovery`, `hermes-workspace-hygiene`, `skill-lifecycle-management`, `kanban-workflows`, `plan`, `prototype`, `to-spec`, `to-tickets`, `wayfinder`, or `wf`. Direct identifiers remain usable even while a newly published community tap is still propagating through search indexes.

A single skill can also be installed directly without subscribing to the tap:

```bash
hermes skills install SaikaAco/saika-hermes-skills/skills/bounded-grilling
```

Community taps receive Hermes' normal third-party security scan and warning on first install. Review every `SKILL.md` before use.

### Decision-to-delivery suite

`wf` routes across the companion workflow skills, and `prototype` loads the canonical prototype handler from `wayfinder`. Install the suite companions together when using that flow:

```bash
hermes skills install SaikaAco/saika-hermes-skills/wf
hermes skills install SaikaAco/saika-hermes-skills/bounded-grilling
hermes skills install SaikaAco/saika-hermes-skills/wayfinder
hermes skills install SaikaAco/saika-hermes-skills/prototype
hermes skills install SaikaAco/saika-hermes-skills/to-spec
hermes skills install SaikaAco/saika-hermes-skills/to-tickets
```

Each package remains independently inspectable. Installation never grants publication, implementation, prototype promotion, or external tracker authority.

## Repository layout

```text
skills/
  bounded-grilling/SKILL.md
  burnable-visual-briefs/
    SKILL.md
    scripts/validate_brief.py
    templates/burnable-visual-brief.html
  context-budget-orchestration/SKILL.md
  hermes-backup-recovery/SKILL.md
  hermes-workspace-hygiene/SKILL.md
  skill-lifecycle-management/SKILL.md
  kanban-workflows/SKILL.md
  plan/
    SKILL.md
    references/third-party-notices.md
  prototype/
    SKILL.md
    references/third-party-notices.md
  to-spec/
    SKILL.md
    references/third-party-notices.md
  to-tickets/
    SKILL.md
    references/third-party-notices.md
  wayfinder/
    SKILL.md
    references/evidence-handler.md
    references/prototype-handler.md
    references/third-party-notices.md
  wf/SKILL.md
scripts/
  validate_skills.py
```

Each package follows the standard `SKILL.md` format and can later add `references/`, `templates/`, `scripts/`, or `assets/` inside its own directory.

## Validate locally

```bash
python3 scripts/validate_skills.py
```

The validator checks required frontmatter, directory/name agreement, balanced Markdown fences, symlinks, personal absolute paths, and common secret formats.

## Scope and provenance

- This is a curated community repository, not an official Nous Research distribution.
- Personal profile maps, local filesystem policy, credentials, memory, and private operational configuration are intentionally excluded.
- Upstream or bundled Hermes skills are not mirrored wholesale; adapted third-party material is published only after review with its required notices.
- See [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md) for provenance and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for retained license notices.

## License

MIT. See [LICENSE](LICENSE).
