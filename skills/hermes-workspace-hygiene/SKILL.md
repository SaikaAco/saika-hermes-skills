---
name: hermes-workspace-hygiene
description: "Use when Hermes may create, move, clean up, or audit transient and generated files. Keeps artifacts in predictable workspace folders and requires manifests, approval, and rollback planning before cleanup."
version: 1.0.0
author: "SaikaAco with Hermes Agent"
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [workspace-hygiene, cleanup, manifests, hermes, filesystem, artifacts]
    related_skills: [hermes-agent, burnable-visual-briefs]
---

# Hermes Workspace Hygiene

## Overview

Keep Hermes-generated artifacts predictable, scoped, and recoverable:

- temporary/intermediate files go under `<active-workspace>/scratch/`;
- generated reports intended for reading or sending go under `<active-workspace>/reports/`;
- explicit user-requested exports go under `<active-workspace>/exports/`;
- project source remains in its project root;
- existing user files are never moved or deleted without explicit approval.

Resolve the active workspace from project instructions or the current working directory. If no safe workspace root is clear, ask before writing rather than defaulting to a personal home directory.

## When to use

Use when:

- a task will create scripts, intermediate JSON/CSV/HTML, screenshots, downloads, report assets, or exports;
- the user asks to audit or clean generated files;
- generated artifacts appear in a high-level personal directory;
- a recurring job needs a predictable artifact and cleanup lifecycle;
- a report or export needs the correct destination.

Do not use for normal source edits inside an existing project, read-only inspection, or durable knowledge and policy files that already have an authoritative location.

## Canonical workspace shape

```text
<active-workspace>/
  scratch/   temporary and intermediate artifacts
  reports/   generated reports intended for reading or delivery
  exports/   explicit user-requested exports
```

Prefer topic/profile subfolders:

```text
scratch/<topic>/
reports/<report-class>/
exports/<task-slug>/
```

Do not create one-off files at a home-directory root. Do not move project-specific source into a generic scratch tree.

## Operating rules

1. **Before writing:** choose the narrowest appropriate workspace subfolder.
2. **Before cleanup:** inspect the exact candidates and produce a manifest.
3. **Before moving or deleting existing files:** obtain explicit approval for that manifest.
4. **Prefer reversible moves over deletion** unless deletion is explicitly requested.
5. **Keep rollback possible:** record source, destination, size, reason, and timestamp.
6. **Fail closed:** missing, changed, moved, symlinked, or ambiguous targets require a fresh audit and approval.
7. **Do not expand scope:** newly discovered or newly stale paths do not inherit an older approval.
8. **Report honestly:** distinguish proposed, moved, deleted, skipped, and failed items.

## Cleanup manifest

Use a machine-readable manifest such as:

```json
{
  "manifest_id": "<stable approval identifier>",
  "created_at": "<actual UTC timestamp>",
  "operation": "move | delete",
  "items": [
    {
      "from": "<absolute inspected source>",
      "to": "<destination or null>",
      "size_bytes": 12345,
      "reason": "generated temporary artifact",
      "identity_check": "<hash, inode, or other stable evidence when available>"
    }
  ]
}
```

The user-facing summary must include item count, total size, operation type, destination, rollback method, and the approval requirement.

An approval binds only to the exact manifest and targets shown to the user. Re-running an audit creates a new scope and requires new approval.

## Audit procedure

1. Define the allowed root and artifact classes.
2. Inspect candidates without mutation.
3. Exclude normal user folders, source trees, hidden configuration, and ambiguous files unless explicitly in scope.
4. Resolve symlinks and record stable target evidence.
5. Produce the manifest and concise decision summary.
6. Wait for approval.
7. Re-verify every target against the approved manifest immediately before execution.
8. Execute only the approved operation and paths.
9. Verify resulting locations or absence.
10. Report completed, skipped, changed, and failed items plus recovery instructions.

## Burnable brief lifecycle

Temporary visual briefs belong under `scratch/visual-briefs/`. A brief may carry an expiry timestamp, but expiry only makes it eligible for a cleanup proposal; it never authorizes automatic deletion. Durable evidence must remain elsewhere so the brief can expire safely.

## Common pitfalls

1. **Home-root clutter.** Tool defaults are not a safe artifact policy.
2. **Audit-as-approval.** Discovering a candidate does not authorize mutation.
3. **Scope drift.** A second audit cannot be executed under the first manifest.
4. **Path-only identity.** Re-check symlinks and changed targets before execution.
5. **Delete-first cleanup.** Prefer recoverable moves when they meet the goal.
6. **Ambiguous ownership.** Ask rather than classifying personal files as generated clutter.
7. **Artifact/source confusion.** Scratch space is not a project source root.

## Verification checklist

- [ ] Workspace root and artifact class were resolved before writing.
- [ ] Temporary files, reports, and exports use their intended subfolders.
- [ ] No one-off artifact was written to a personal home-directory root.
- [ ] Cleanup remained read-only until an exact manifest was approved.
- [ ] The execution scope exactly matched the approved manifest.
- [ ] Targets were re-verified immediately before mutation.
- [ ] Every move has a rollback path; every deletion was explicitly approved.
- [ ] Results distinguish completed, skipped, changed, and failed items.
