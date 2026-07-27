---
name: skill-lifecycle-management
description: "Use when authoring, validating, maintaining, consolidating, or archiving Hermes skills. Covers SKILL.md structure, support-file packaging, local vs in-repo placement, and curator-safe umbrella building."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [skills, skill-authoring, curator, consolidation, hermes-agent, documentation]
    related_skills: [hermes-agent]
---

# Skill Lifecycle Management

## Overview

Use this umbrella whenever a task is about creating, editing, validating, consolidating, or archiving skills. Skills should capture class-level reusable procedures and experiential knowledge. They are not per-session bug logs; narrow session details belong in labeled subsections or support files under a broader umbrella.

## When to Use

- Writing a new `SKILL.md`.
- Editing frontmatter, descriptions, triggers, or related skills.
- Adding `references/`, `templates/`, `scripts/`, or `assets/` files.
- Consolidating narrow sibling skills into an umbrella.
- Archiving stale or absorbed skills safely.
- Debugging why a skill does not load or validate.

## Required SKILL.md Shape

Minimum validator requirements:

- File starts at byte 0 with `---`.
- YAML frontmatter closes with a standalone `---` line.
- Frontmatter parses as a mapping.
- `name` and `description` are present.
- Description stays within the current validator limit.
- Body after frontmatter is non-empty.

Peer-quality structure:

```yaml
---
name: my-skill-name
description: "Use when <trigger class>. <what this skill helps do>."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [short, descriptive, tags]
    related_skills: [other-skill]
---
```

Recommended body sections: Overview, When to Use, workflow sections, Common Pitfalls, and Verification Checklist.

## Placement

- **User-local skills:** `~/.hermes/skills/<category>/<name>/SKILL.md`; create and edit with `skill_manage`.
- **Bundled/in-repo skills:** repository `skills/<category>/<name>/SKILL.md`; edit files directly in the repo and commit changes.
- **Profiles:** each profile has its own skills tree under `~/.hermes/profiles/<profile>/skills/`; do not modify another profile unless explicitly requested.

## Support Files

Use support directories instead of bloating `SKILL.md`:

- `references/<topic>.md` — API notes, provider quirks, long recipes, research excerpts.
- `templates/<name>` — starter files intended to be copied and modified.
- `scripts/<name>` — static helpers, probes, generators, and verification scripts.
- `assets/<name>` — images/media/data fixtures used by the skill.

If `SKILL.md` links to support files, keep those paths valid when moving or merging. A markdown file copied into another skill's `references/` directory is not itself a skill root and will not get linked-file discovery.

## Umbrella Consolidation Workflow

1. Scan the candidate list for prefix/domain clusters.
2. For each cluster, ask: would a maintainer write one class-level skill with subsections?
3. Pick an existing umbrella if one is already broad enough; otherwise create a new umbrella.
4. Preserve unique insights as labeled sections or support files.
5. Inspect the full source package before archiving: support files, relative links, scripts, templates, and assets.
6. Archive absorbed skills with an explicit `absorbed_into` target so downstream references can migrate.
7. Never archive pinned/protected skills.

## Common Pitfalls

1. **One-session-one-skill sprawl.** Session-specific details should become support files or subsections.
2. **Flattening packages.** Do not copy only `SKILL.md` when the source relies on support files.
3. **Over-specific names.** PR numbers, exact error strings, and codename artifacts usually signal a subsection, not a skill.
4. **Current-session cache confusion.** Newly created/archived skills may require `/reload-skills` or a new session to appear/disappear.
5. **Deleting instead of archiving.** Curator-style maintenance should preserve recoverability.

## Verification Checklist

- [ ] Skill frontmatter validates.
- [ ] Description names the trigger class, not one incident.
- [ ] Support-file links resolve after edits or consolidation.
- [ ] Archive/consolidation decisions are recorded with `absorbed_into` where applicable.
- [ ] Remaining active skills are class-level and discoverable by description search.
