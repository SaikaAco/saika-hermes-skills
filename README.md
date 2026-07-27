# Saika Hermes Skills

A small public tap of bounded, reusable workflow skills for [Hermes Agent](https://github.com/NousResearch/hermes-agent).

These packages are curated from workflows used in practice. The repository starts deliberately small: only portable skills with clear boundaries and no personal configuration are included.

## Available skills

| Skill | Version | Purpose |
|---|---:|---|
| [`bounded-grilling`](skills/bounded-grilling/SKILL.md) | 1.0.0 | Resolve a small number of material human decisions without endless interviewing or automatic implementation. |
| [`skill-lifecycle-management`](skills/skill-lifecycle-management/SKILL.md) | 1.0.0 | Author, validate, package, consolidate, and archive Hermes skills safely. |
| [`kanban-workflows`](skills/kanban-workflows/SKILL.md) | 1.1.0 | Coordinate durable Hermes Kanban work with retry-safe creation, role boundaries, and verifiable handoffs. |

## Install as a Hermes tap

```bash
hermes skills tap add SaikaAco/saika-hermes-skills
hermes skills inspect SaikaAco/saika-hermes-skills/bounded-grilling
hermes skills install SaikaAco/saika-hermes-skills/bounded-grilling
```

Install the other packages by replacing the final slug with `skill-lifecycle-management` or `kanban-workflows`. Direct identifiers remain usable even while a newly published community tap is still propagating through search indexes.

A single skill can also be installed directly without subscribing to the tap:

```bash
hermes skills install SaikaAco/saika-hermes-skills/skills/bounded-grilling
```

Community taps receive Hermes' normal third-party security scan and warning on first install. Review every `SKILL.md` before use.

## Repository layout

```text
skills/
  bounded-grilling/SKILL.md
  skill-lifecycle-management/SKILL.md
  kanban-workflows/SKILL.md
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
- Upstream/bundled Hermes skills and third-party-heavy packages are not republished here.
- See [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md) for influences and attribution.

## License

MIT. See [LICENSE](LICENSE).
