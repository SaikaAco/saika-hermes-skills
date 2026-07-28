---
name: hermes-backup-recovery
description: "Use when designing, operating, or verifying encrypted backups and disaster recovery for Hermes state. Combines sanitized Git history, atomic Restic snapshots, WAL-safe SQLite copies, manifest checks, retention gates, and clean-room restore drills."
version: 1.0.0
author: "SaikaAco with Hermes Agent"
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [backup, recovery, restic, sqlite, disaster-recovery, integrity, hermes]
    related_skills: [hermes-workspace-hygiene]
---

# Hermes Backup and Recovery

## Overview

Protect Hermes with two complementary recovery layers:

```text
sanitized control-plane text → local Git history → readable rollback
raw recovery state + safe databases → encrypted Restic snapshot → disaster recovery
```

The Git layer is intentionally incomplete and secret-free. The encrypted snapshot is the recovery layer and may contain credentials, sessions, logs, source state, databases, and other sensitive files according to the operator's approved scope.

A backup is not complete because a command exited successfully. Completion requires an atomic snapshot manifest, database consistency evidence, repository checks, and periodic restore verification.

## When to use

Use when:

- backing up Hermes configuration, profiles, skills, plugins, cron state, sessions, logs, source trees, or memory databases;
- designing an encrypted Restic repository over local, S3-compatible, or rclone-backed storage;
- capturing live SQLite databases safely;
- defining backup retention and integrity gates;
- verifying that a snapshot can restore on a clean machine;
- documenting disaster-recovery credentials and cutover controls.

Do not use as a substitute for service-specific exports, application-level replication, or legal retention policy. Never assume a cloud provider's account recovery replaces independent recovery credentials.

## Required tools and operator inputs

Typical prerequisites:

- Restic;
- Git;
- Python with the standard-library `sqlite3` module;
- rclone only when the chosen backend requires it;
- a credential manager independent of both the backup destination and protected machine.

The operator must define:

- approved source roots;
- encrypted repository endpoint;
- exclusion policy;
- credential-file locations;
- retention schedule;
- verification frequency;
- recovery machine and cutover authority.

This skill does not install tools, create remotes, or request secrets. Authentication material must be entered through trusted local tooling and must never be pasted into an agent conversation.

## Layer 1: sanitized Git control plane

Create a generated tree containing only durable, reviewable text needed to understand and roll back the Hermes control plane.

Include only approved text such as:

- configuration with secret values removed;
- profile and routing structure;
- public/local skill text;
- runbooks and policy documents;
- scheduler definitions with credentials removed;
- recovery documentation.

Exclude:

- environment files and authentication material;
- databases, sessions, logs, caches, and runtime state;
- binaries and generated assets;
- encrypted repository credentials;
- raw private data not needed for readable rollback.

Required gates before every Git commit:

1. the redactor/importer self-test passes;
2. the generated tree is rebuilt from approved sources;
3. the generated tree is scanned for credential signatures and private material;
4. the complete reachable Git history is scanned when the redaction policy changes;
5. the diff is reviewed before commit;
6. `git fsck --full` passes periodically and after restore.

Never treat sanitized Git as a full backup. It is a readable audit and rollback layer only.

## Layer 2: encrypted atomic snapshot

Use client-side Restic encryption for the approved raw recovery state. The repository password and backend credentials must be preserved independently of:

- the protected machine;
- the Restic repository;
- the cloud/storage account that hosts it.

The raw file stream may include approved Hermes state, source trees including Git metadata, explicit reports/exports, external memory state, and the generated sanitized Git repository. Exclude reinstallable dependencies, caches, build output, scratch artifacts, prior backup trees, and live SQLite files handled by the safe database stream.

### Snapshot completeness contract

One completed snapshot must contain:

```text
raw approved files
sqlite-safe/             consistent database copies
SQLITE_MANIFEST.json     source/copy identity and hashes
EXCLUSION_AUDIT.json     exact excluded live DBs and sidecars
COMPLETION_MANIFEST.json run identity, scope, counts, hashes, and status
```

Tag or identify completed snapshots distinctly, for example `hermes-complete`. A failed or partial run must never receive the completion identity.

Raw files, safe database copies, and all manifests must be committed in one Restic snapshot. Retention must operate only after that atomic snapshot succeeds.

## WAL-safe SQLite capture

Do not stream a live SQLite database and its WAL/SHM sidecars as ordinary files.

For every `.db`, `.sqlite`, or `.sqlite3` candidate:

1. identify valid SQLite databases recursively within approved roots;
2. create a consistent copy with Python `sqlite3.Connection.backup()` or an equivalent application-supported mechanism;
3. run `PRAGMA quick_check` on the safe copy;
4. hash the safe copy and record source/copy metadata in `SQLITE_MANIFEST.json`;
5. exclude the live database's exact absolute path plus `-wal`, `-shm`, and `-journal` sidecars from the raw stream;
6. record every exclusion in `EXCLUSION_AUDIT.json`;
7. require a one-to-one match between discovered databases, safe copies, manifest rows, and raw-stream exclusions.

Fail the run if any candidate cannot be classified, copied, checked, hashed, or reconciled. Do not silently fall back to raw live files.

## Backup run sequence

1. Acquire an exclusive process lock.
2. Resolve and validate approved source roots and repository configuration.
3. Rebuild and scan the sanitized Git layer.
4. Discover databases and produce WAL-safe copies.
5. Reconcile database inventory, safe-copy manifest, and exact exclusions.
6. Create completion metadata with a unique run identity.
7. Commit raw files, safe database staging, and manifests in one encrypted snapshot.
8. Read back the completion manifest from the snapshot.
9. Verify expected file/database counts and hashes.
10. Run Restic structural and configured data-subset checks.
11. Only then apply retention and pruning.
12. Run a post-prune repository check and write a non-secret report.

A failure before step 8 produces no completed backup. A failure after snapshot creation but before retention leaves the recoverable snapshot intact and skips destructive retention.

## Retention gates

Use retention appropriate to the operator's recovery objectives; a common starting shape is daily, weekly, and monthly generations. Apply retention independently to source/path groups when one policy could otherwise erase a needed class of history.

Before `forget --prune` or equivalent destructive retention:

- a new atomic completed snapshot exists;
- its manifests were read back successfully;
- database verification passed;
- a deterministic repository data subset and structural check passed;
- the exact retention command and repository are approved by standing policy or the operator.

After pruning, run another repository check. Retention failure must not invalidate the newly completed snapshot.

## Verification levels

### Routine status

Check repository reachability, latest completed run identity, age, lock state, manifest presence, and last verification result. Status is not a restore test.

### Database restore verification

From one completed snapshot:

1. restore every safe database copy into an empty temporary root;
2. compare hashes with `SQLITE_MANIFEST.json`;
3. run `PRAGMA integrity_check` on every restored database;
4. verify inventory counts and original destination mappings;
5. record failures without overwriting live state.

### Full clean-room drill

Periodically restore one complete snapshot to an empty recovery directory or clean machine using only independently preserved credentials and public recovery instructions.

Verify:

- completion and exclusion-manifest hashes;
- all required raw files;
- every database hash and integrity check;
- sanitized Git repository with `git fsck --full`;
- configuration readability and expected profile/skill structure;
- documented mapping from staging paths to final destinations;
- ability to recover without credentials stored inside the backup repository.

Do not claim disaster-recovery readiness without a clean-room drill.

## Recovery and cutover

1. Prepare an isolated recovery machine or empty staging root.
2. Install trusted versions of required tools.
3. restore backend configuration and credentials from the independent credential store;
4. locate one completed atomic snapshot and read its completion manifest first;
5. restore the snapshot to the empty staging root;
6. verify manifests, hashes, database integrity, and Git integrity;
7. inspect destination mappings and identify stale or incompatible configuration;
8. stop Hermes gateways and writers before final database/file placement;
9. obtain explicit approval for cutover over an existing installation;
10. move verified files into final locations with a rollback copy;
11. start the minimum required service and run health checks before enabling the rest.

Never restore directly over a live Hermes installation as the first verification attempt.

## Failure handling

- **Repository absent:** initialize only when the backend explicitly reports “not found”; authentication, lock, and transport failures must fail closed.
- **Database mismatch:** preserve staging and manifests, exclude the run from completion, and repair discovery/reconciliation.
- **Snapshot uploaded but manifest unreadable:** do not tag it complete or run retention.
- **Credential loss:** encrypted data is unrecoverable; restore credentials from the independent store rather than weakening encryption.
- **Integrity failure:** stop cutover, preserve the failing restore, select an older completed snapshot, and investigate repository health.
- **Path drift:** require manifest review and explicit remapping; never guess destinations.
- **Live writer detected:** stop or block cutover until application writes are quiesced.

## Common pitfalls

1. **Sync mistaken for backup.** Mirrored corruption or deletion is not versioned recovery.
2. **Git mistaken for full recovery.** Sanitized text omits secret and runtime state by design.
3. **Raw live SQLite copies.** File-level capture can split database and WAL state.
4. **Retention before verification.** A new object is not recoverable until read back and checked.
5. **Credentials stored with the backup.** One account failure then destroys both data and access.
6. **Provider-specific runbook only.** Recovery should describe capability and evidence, not depend on one remote name.
7. **Restore over live state.** Always verify in isolation first.
8. **Success without drill.** Repository checks cannot prove complete application recovery.

## Verification checklist

- [ ] Sanitized Git and encrypted raw recovery are separate layers with explicit scopes.
- [ ] Backup credentials are independently recoverable and absent from generated Git.
- [ ] Every live SQLite database has one checked safe copy and exact raw exclusion.
- [ ] Raw files, databases, and manifests share one atomic completed snapshot.
- [ ] Retention runs only after read-back and integrity gates.
- [ ] Post-prune repository checks pass.
- [ ] Database restore verification checks hashes and `PRAGMA integrity_check`.
- [ ] A periodic full clean-room drill verifies files, databases, Git, and credentials.
- [ ] Cutover never overwrites live Hermes state without manifest review and approval.
- [ ] Reports contain evidence and errors but no secrets.
