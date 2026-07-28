# Saika Hermes Skills

A small public tap of bounded, reusable workflow skills for [Hermes Agent](https://github.com/NousResearch/hermes-agent).

These packages are curated from workflows used in practice. The repository remains deliberately focused: only portable skills with clear boundaries and no personal configuration are included.

## Available skills

| Skill | Version | Purpose |
|---|---:|---|
| [`bounded-grilling`](skills/bounded-grilling/SKILL.md) | 1.0.0 | Resolve a small number of material human decisions without endless interviewing or automatic implementation. |
| [`burnable-visual-briefs`](skills/burnable-visual-briefs/SKILL.md) | 1.1.0 | Create temporary, diagram-first HTML briefs with strict privacy, expiry, validation, and rendering gates. |
| [`context-budget-orchestration`](skills/context-budget-orchestration/SKILL.md) | 1.0.1 | Contain bulky context, phase long work, bound delegation and retries, and reserve capacity for verification. |
| [`hermes-workspace-hygiene`](skills/hermes-workspace-hygiene/SKILL.md) | 1.0.0 | Keep generated artifacts scoped and make cleanup manifest-bound, approval-gated, and recoverable. |
| [`skill-lifecycle-management`](skills/skill-lifecycle-management/SKILL.md) | 1.0.0 | Author, validate, package, consolidate, and archive Hermes skills safely. |
| [`kanban-workflows`](skills/kanban-workflows/SKILL.md) | 1.1.0 | Coordinate durable Hermes Kanban work with retry-safe creation, role boundaries, and verifiable handoffs. |
| [`to-spec`](skills/to-spec/SKILL.md) | 1.1.0 | Adaptive LIGHT/FULL compilation of settled decisions into traceable requirements and acceptance evidence. |
| [`wayfinder`](skills/wayfinder/SKILL.md) | 1.1.0 | Adaptive LIGHT/FULL route finding for dependent, foggy, or multi-session work. |

## Install as a Hermes tap

```bash
hermes skills tap add SaikaAco/saika-hermes-skills
hermes skills inspect SaikaAco/saika-hermes-skills/bounded-grilling
hermes skills install SaikaAco/saika-hermes-skills/bounded-grilling
```

Install the other packages by replacing the final slug with `burnable-visual-briefs`, `context-budget-orchestration`, `hermes-workspace-hygiene`, `skill-lifecycle-management`, `kanban-workflows`, `to-spec`, or `wayfinder`. Direct identifiers remain usable even while a newly published community tap is still propagating through search indexes.

A single skill can also be installed directly without subscribing to the tap:

```bash
hermes skills install SaikaAco/saika-hermes-skills/skills/bounded-grilling
```

Community taps receive Hermes' normal third-party security scan and warning on first install. Review every `SKILL.md` before use.

## Repository layout

```text
skills/
  bounded-grilling/SKILL.md
  burnable-visual-briefs/
    SKILL.md
    scripts/validate_brief.py
    templates/burnable-visual-brief.html
  context-budget-orchestration/SKILL.md
  hermes-workspace-hygiene/SKILL.md
  skill-lifecycle-management/SKILL.md
  kanban-workflows/SKILL.md
  to-spec/SKILL.md
  wayfinder/SKILL.md
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
