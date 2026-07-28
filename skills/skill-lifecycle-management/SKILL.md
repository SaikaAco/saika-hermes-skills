---
name: skill-lifecycle-management
description: "Use when authoring, validating, publishing, maintaining, consolidating, or archiving Hermes skills. Covers package structure, provenance, privacy, approval-bound releases, isolated consumer verification, and curator-safe maintenance."
version: 1.1.0
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

Use this umbrella whenever a task is about creating, editing, validating, publishing, consolidating, or archiving skills. Skills should capture class-level reusable procedures and experiential knowledge. They are not per-session bug logs; narrow session details belong in labeled subsections or support files under a broader umbrella.

A skill release is complete only when the public package can be consumed safely from a fresh Hermes environment and its remote bytes match the reviewed source. A successful local validator or Git push alone is not completion.

## When to Use

- Writing a new `SKILL.md`.
- Editing frontmatter, descriptions, triggers, or related skills.
- Adding `references/`, `templates/`, `scripts/`, or `assets/` files.
- Deciding whether a local skill is focused and portable enough to publish.
- Preparing a public tap package, attribution, license notice, or catalog entry.
- Verifying a release through security scan, isolated installation, clone, and remote-byte checks.
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

## Public Release Workflow

### 1. Publishability gate

Do not publish merely because a skill exists locally. A public candidate should be:

- focused on a reusable problem rather than a broad tool wrapper;
- useful without one operator's filesystem, profiles, credentials, contacts, or private policy;
- class-level rather than a one-session procedure;
- small enough to audit, or deliberately split into independently useful packages;
- supported by real operating experience and verification;
- legally publishable with traceable provenance.

Classify each candidate before editing:

```text
READY          focused, portable, provenance clear
REPAIR         useful after bounded sanitization or dependency cleanup
DEFER          oversized, dependency-heavy, or provenance unresolved
PRIVATE        personal control plane, knowledge architecture, or credentials
UPSTREAM_ONLY  official/bundled material that should be linked, not mirrored
```

For `REPAIR`, define the exact public-only changes and whether the active local package will also change. Editing an active skill and creating a public derivative are separate scopes.

### 2. Lock the release endpoint

Before mutation, record:

- exact skill names and versions;
- active-package edits, if any;
- public files to add or modify;
- retained support files;
- attribution and notice requirements;
- validation, consumer, and remote acceptance checks;
- explicitly excluded skills, files, dependencies, contacts, and side effects.

Obtain approval for this endpoint when skill creation or editing requires it. Do not silently add another candidate to an approved batch.

### 3. Establish provenance and license obligations

For original work, state that it was developed from the named operating practice without claiming ownership of generic ideas.

For adapted work:

1. inspect the authoritative upstream skill and repository license;
2. pin or record the reviewed upstream URL/commit;
3. identify substantial retained wording, structure, and concepts;
4. distinguish retained material from local additions;
5. preserve the complete required copyright and permission notice;
6. state that the adaptation is independently maintained and not endorsed;
7. resolve conflicting or missing provenance before publication.

Use repository-level `ACKNOWLEDGMENTS.md` for lineage and `THIRD_PARTY_NOTICES.md` for complete retained notices. Frontmatter should name the adaptation and include an upstream URL when the format supports it.

### 4. Build a portable package

Inspect the whole source package, not only `SKILL.md`:

```text
skills/<name>/
  SKILL.md
  references/   optional
  templates/    optional
  scripts/      optional
  assets/       optional
```

Public-package checks:

- directory and frontmatter names agree;
- version, author, license, platforms, tags, and related skills are accurate;
- every referenced support file exists and every retained file is intentional;
- no symlink escapes the package;
- no personal absolute path, account ID, token, credential, private contact, or profile-specific rule remains;
- runtime commands and environment variables are declared or clearly optional;
- examples do not imply unavailable companion skills;
- README catalog, install slugs, repository layout, acknowledgments, and notices agree with package reality.

Prefer a clean portable rewrite over line-by-line redaction when the active package mixes reusable method with extensive private policy. Preserve the active package unchanged unless its repair is separately approved.

### 5. Pre-commit validation

Run the repository's real validator and relevant package-specific tests. At minimum verify:

- required frontmatter and non-empty body;
- balanced Markdown fences;
- package/name agreement;
- support-file inventory and relative links;
- no unsafe symlink;
- private-path and common secret-pattern scan;
- syntax/self-tests for scripts and templates;
- generated sample or renderer test when the package creates artifacts;
- `git diff --check` and a clean base branch before staging.

A privacy scan may legitimately match a public author name; review matches rather than treating zero raw matches as the only success condition.

### 6. Stage the exact approved manifest

Stage only named files. Then verify:

```text
staged name/status
staged diff/stat
staged whitespace check
unstaged name/status
```

The staged tree must equal the approved release manifest. No newly discovered file inherits an earlier approval. Review the actual staged content before commit and push.

### 7. Native Hermes consumer gate

After the public source is reachable, test from a fresh isolated Hermes home:

1. create a temporary home and resolve it to its canonical absolute path;
2. set `HERMES_HOME` only for the isolated test process;
3. add the public tap;
4. inspect the fully qualified skill identifier;
5. install without a security override;
6. require the normal community-source verdict and policy decision;
7. compare every installed package file with the reviewed repository source;
8. allow the temporary home to be removed automatically.

On macOS, `/tmp` commonly resolves to `/private/tmp`. Use the canonical resolved path for both `HERMES_HOME` and containment comparisons; otherwise a valid installation may produce a false path-boundary error.

Never use a force/override flag to convert `CAUTION` or `BLOCKED` into release success. Capture the exact finding, repair the wording or capability boundary, bump the patch version if already public, and rerun the native gate from a fresh home.

### 8. Independent remote verification

A successful push is not sufficient. Verify the public state three ways:

1. **Remote ref:** `git ls-remote` for the public branch equals the local release commit.
2. **Commit-pinned raw bytes:** hash each changed public file locally and through its raw URL at the release commit; every pair must match.
3. **Anonymous clone:** clone into a fresh temporary directory, run the repository validator, and compare the released package bytes with the reviewed source.

Use commit-pinned URLs for byte evidence. A branch URL can change between checks and is not a stable release proof.

### 9. Final invariants

Before reporting completion, verify:

- local branch and public branch point to the same commit;
- worktree is clean;
- repository validator passes from an anonymous clone;
- native security verdict is allowed without override;
- installed bytes match all package files;
- changed remote raw bytes match locally;
- the active/default Hermes profile did not retain the temporary test tap;
- no unapproved message, dependency install, or unrelated publication occurred.

Report the public URL, version, final commit, material verification evidence, and any bounded repair performed after the first push.

## Release Failure Handling

- **Security false positive:** capture the exact rule and line, clarify the intended local behavior, release a patch version, and rescan. Do not bypass the scanner.
- **Community-index lag:** test the direct repository identifier and report propagation state; do not claim tap success from stale bytes.
- **Support file missing after install:** treat the package as failed even if `SKILL.md` installed; repair bundle discovery and compare all bytes again.
- **Push succeeded but raw mismatch:** stop, identify caching versus wrong commit/path, and verify commit-pinned content before proceeding.
- **Clone validator differs from local:** the anonymous clone is authoritative for public consumer state; repair the repository.
- **Temporary path mismatch:** canonicalize the isolated home rather than weakening path-containment checks.
- **Post-public repair:** increment the patch version and preserve both commits in history; never rewrite evidence to imply the first release passed.

## Common Pitfalls

1. **One-session-one-skill sprawl.** Session-specific details should become support files or subsections.
2. **Flattening packages.** Do not copy only `SKILL.md` when the source relies on support files.
3. **Over-specific names.** PR numbers, exact error strings, and codename artifacts usually signal a subsection, not a skill.
4. **Current-session cache confusion.** Newly created/archived skills may require `/reload-skills` or a new session to appear/disappear.
5. **Deleting instead of archiving.** Curator-style maintenance should preserve recoverability.
6. **Local validator as release proof.** Public consumers exercise different fetch, scan, bundle, and path-containment surfaces.
7. **Security override as success.** A forced installation is evidence of a failed release gate, not completion.
8. **`SKILL.md`-only comparison.** A package fails when a referenced script, template, asset, or notice is absent or different.
9. **Active/public scope drift.** A sanitized derivative does not authorize changing the active private package, and vice versa.
10. **Branch URL as byte proof.** Verify immutable commit-pinned raw content.

## Verification Checklist

- [ ] Skill frontmatter validates.
- [ ] Description names the trigger class, not one incident.
- [ ] Support-file links resolve after edits or consolidation.
- [ ] Archive/consolidation decisions are recorded with `absorbed_into` where applicable.
- [ ] Remaining active skills are class-level and discoverable by description search.
- [ ] Public candidates passed focused-usefulness, portability, and provenance gates.
- [ ] The approved release manifest exactly matches the staged tree.
- [ ] Privacy, package, support-file, and repository validators pass.
- [ ] Native inspection and installation are allowed without a security override.
- [ ] Every installed package file matches the reviewed source.
- [ ] Remote ref, commit-pinned raw bytes, and anonymous-clone validation agree.
- [ ] The worktree is clean and no temporary tap remains in the active profile.
