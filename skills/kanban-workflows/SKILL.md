---
name: kanban-workflows
description: "Use when coordinating Hermes Kanban work as either orchestrator or worker. Covers decomposition, ticket lifecycle, worker updates, anti-temptation rules, and handoff discipline."
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [kanban, orchestration, workers, project-management, devops, coordination]
    related_skills: [hermes-agent]
---

# Kanban Workflows

## Overview

Use this umbrella for Hermes Kanban work regardless of whether the current agent is acting as the orchestrator or as a worker. The old orchestrator/worker split encoded two roles of the same class-level workflow; keeping them together makes it easier to load the right lifecycle and avoid role confusion.

## When to Use

- The user asks to coordinate a multi-step effort through Kanban.
- You are operating under a Kanban orchestrator profile.
- You are a worker assigned a Kanban ticket and need lifecycle/pitfall guidance.
- Work requires decomposition, ticket updates, acceptance criteria, or handoff notes.

Don't use this for a normal one-agent todo list; use the session todo tool unless a real Kanban board/workflow is in scope.

## Route before creating work

| Work shape | Use |
|---|---|
| Short deterministic work in the current turn | Direct tools or `execute_code` |
| Short bounded reasoning that can fork and rejoin the live parent | `delegate_task` |
| Work that must survive restart, carry dependencies, retry, wait for human review, or run across profiles | Kanban |

Do not use `delegate_task` for work whose result must outlive the parent
process. Do not use Kanban for a quick lookup or one-agent session todo.

## Retry-safe task creation

- Discover real profile names before assignment; never invent an assignee.
- Supply a stable `idempotency_key` for any task creation that may be retried.
  Reuse the same key after transport uncertainty so the kernel returns the
  existing non-archived task instead of creating a duplicate.
- Set `max_runtime_seconds` for bounded workers.
- Agent tool-created tasks use configured `kanban.failure_limit`; operators
  using the CLI/API may additionally set per-task `max_retries`.
  After repeated failure, block for review or reassign; never respawn the same
  unchanged task indefinitely.
- Create parent cards first and pass `parents=[...]` when creating children.
  Do not create children as ready and link them afterward.

## Workspace durability

| Workspace | Durability contract |
|---|---|
| `scratch` | Ephemeral; use only for reproducible intermediates. It may be garbage-collected when archived. |
| `dir` | Persistent shared state at an absolute path; use for durable non-Git artifacts. |
| `worktree` | Persistent Git-isolated implementation; commit verified work before handoff. |

Never place the only copy of an irreplaceable result in a scratch workspace.

## Structured handoff metadata

Every completion or review-required block must name:

- artifact paths or URLs;
- files changed;
- commands/tests and actual outcomes;
- decisions and unresolved risks;
- parent inputs consumed and child tasks created;
- the exact next action.

For code changes requiring human review, comment the structured handoff and
block with a `review-required:` reason instead of marking terminal completion.

## Orchestrator Mode

The orchestrator's job is to decompose, route, verify, and unblock — not to quietly do all the work.

1. **Define outcome and constraints**: user-visible deliverable, acceptance criteria, repo/path scope, deadlines, and dependencies.
2. **Create small tickets**: each ticket should have a clear owner, input context, expected artifact, and verification step.
3. **Sequence dependencies**: avoid assigning blocked work without noting the prerequisite ticket.
4. **Monitor updates**: look for stale tickets, ambiguous blockers, missing verification, and duplicated work.
5. **Verify integration**: read artifacts, run checks, and reconcile conflicting worker outputs before reporting completion.

Anti-temptation rule: if the Kanban process exists to coordinate workers, do not bypass it by completing hidden substantial work yourself. Do only the lightweight verification and glue needed to keep the board honest.

## Worker Mode

The worker's job is to complete the assigned ticket and make the next state obvious.

1. Read the ticket, linked context, and acceptance criteria.
2. Ask for clarification only if the ticket is not actionable; otherwise proceed.
3. Keep changes within scope. If you discover adjacent work, report it or create/follow-up instead of silently expanding.
4. Update status with concrete progress: files touched, commands run, blockers, and verification results.
5. Handoff with enough detail for another worker or orchestrator to continue.

## Status Update Template

```markdown
Status: in_progress | blocked | ready_for_review | done
Scope worked: <paths, services, docs>
Changes made: <short bullets>
Verification: <commands/checks and results>
Blockers/questions: <none or explicit blocker>
Next handoff: <what the orchestrator/next worker should do>
```

## Common Pitfalls

1. **Role bleed.** Orchestrators implement too much; workers redesign the plan. Stay in role.
2. **Ticket vagueness.** A ticket without an artifact and verification step is not ready.
3. **Silent blockers.** Report blocked status with the exact missing input or failing command.
4. **Unverified done.** A task is not done just because files changed.
5. **Board drift.** Keep ticket state synchronized with actual work so other agents do not duplicate effort.
6. **Duplicate cards after uncertain create.** Reuse a stable idempotency key.
7. **Infinite respawn.** Respect runtime/retry circuit breakers and block for review.
8. **Ephemeral-only handoff.** Move durable artifacts out of scratch before completion.

## Verification Checklist

- [ ] Every active ticket has an owner, artifact, and verification step.
- [ ] Blockers are explicit and routed to the right owner.
- [ ] Completed work was checked by command output or artifact inspection.
- [ ] Handoffs are detailed enough for continuation without transcript archaeology.
