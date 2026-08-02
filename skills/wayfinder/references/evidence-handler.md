# Wayfinder Evidence Handler

This is the shared adapter between a Wayfinder `EVIDENCE` ticket and the active
profile's research capabilities. It does not replace domain research skills or
source policy.

## Purpose

Resolve one discoverable factual question that blocks the route, preserve a
cited artifact or authoritative record, and return a verified handoff to
Wayfinder. The handler discovers facts; it never makes the human side of a
product decision.

## Required input

Require:

- Wayfinder map and ticket handles;
- destination and one precise evidence question;
- direct blockers and the decision(s) this evidence informs;
- freshness requirement;
- applicable project/profile source hierarchy;
- authorized persistence target, or `chat-only` when no artifact authority
  exists.

Return `BLOCKED` rather than inventing any missing route-changing context.

## Execution routing

Use the smallest durable mechanism that fits:

1. **Direct tools** for a short deterministic lookup.
2. **`delegate_task`** for bounded independent reading that can complete while
   the parent session remains alive. Delegation means GPT/Codex, never Fable.
3. **Authorized Kanban** for research that must survive restart, wait on an
   external event, retry independently, or span profiles.

A background result is evidence, not truth. The parent must inspect cited
sources and verify any written artifact before Wayfinder can close the ticket.
Never claim persistence from a subagent self-report alone.

## Research standard

Follow the active project's research procedure and source hierarchy:

- define object, deliverable, freshness, and risk;
- prefer primary sources such as official documentation, source code, specs,
  and first-party APIs;
- use secondary sources to discover leads, not to overstate conclusions;
- search for material contradiction and stale evidence when relevant;
- label confidence no stronger than the evidence permits;
- cite every route-changing factual claim.

Do not force a domain-wide evidence ledger for a tiny project lookup. Use the
active profile's compounding rules when the finding is durable beyond this
Wayfinder effort.

## Artifact and persistence contract

Prefer an existing authorized project convention for research notes. If none
exists:

- keep the result in the authoritative Wayfinder ticket when that record is
  durable and sufficient; or
- return `chat-only` and leave persistence pending;
- never choose a new tracker, branch, repository path, or external publication
  target without authority.

Classify outputs before closure:

- **durable shared context** — must be reconciled into the canonical project
  source used by later sessions;
- **ticket evidence** — may remain at a stable cited artifact handle;
- **disposable intermediate** — cannot be the only support for the finding.

A throwaway branch may hold ticket evidence only when its ref is durable and
resolvable. It must not strand shared context. If reconciliation fails, return
`RECONCILE_REQUIRED` and keep the evidence ticket authoritative and open.

## Handoff schema

Return:

```yaml
schema: wayfinder-evidence-v1
outcome: RESOLVED | BLOCKED | RECONCILE_REQUIRED
ticket_handle: <authoritative Wayfinder ticket>
question: <exact evidence question>
finding: <bounded answer or named blocker>
confidence: Confirmed | Likely | Plausible | Unconfirmed | Conflicted | Stale | Unsupported
primary_source_handles: []
secondary_source_handles: []
contradictions_or_limitations: []
freshness_checked_at: <actual timestamp>
artifact_handle: <durable URL/path/ticket record or chat-only>
durable_context_handles: []
parent_verification: passed | failed | pending
persistence: confirmed | pending
```

`RESOLVED` requires:

- at least one inspected authoritative source for every material finding, or an
  explicit lower-confidence explanation when no primary source exists;
- `parent_verification: passed`;
- `persistence: confirmed`;
- a resolvable artifact or ticket record.

Otherwise return `BLOCKED` or `RECONCILE_REQUIRED`. Wayfinder owns the ticket
and map mutation after consuming the handoff.

## Chart-time dispatch

After CHART persists the map and tickets, it may dispatch independent
`EVIDENCE` tickets in parallel. Dispatch is the only chart-time exception:

- CHART must not mark those tickets resolved from dispatch alone;
- non-research tickets must not be claimed or worked;
- every child gets a bounded question, source policy, output schema, and
  persistence boundary;
- the parent verifies and persists each returned result before closure;
- if the session cannot safely receive the result, use durable Kanban or leave
  the ticket undispatched.

## Verification checklist

- [ ] One precise evidence ticket was handled.
- [ ] The active source hierarchy and freshness requirement were used.
- [ ] Material claims have inspected source handles and calibrated confidence.
- [ ] Any subagent result was verified by the parent.
- [ ] Durable context is reconciled; ticket evidence has a stable handle.
- [ ] The handoff conforms to `wayfinder-evidence-v1`.
- [ ] No human decision, destination implementation, or unauthorized
      publication occurred.
