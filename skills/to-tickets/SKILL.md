---
name: to-tickets
description: "Use when the user explicitly asks to turn an approved specification, plan, or settled contract into agent-sized implementation tickets with requirement coverage and blocking edges. Drafts first; publishes only with separate authority."
disable-model-invocation: true
version: 2.0.0
author: "SaikaAco with Hermes Agent, adapted from Matt Pocock"
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [tickets, tracer-bullets, vertical-slices, dependencies, specification, kanban]
    related_skills: [to-spec, wayfinder, plan, kanban-workflows]
    upstream: "https://github.com/mattpocock/skills/tree/main/skills/engineering/to-tickets"
---

# Traceable To-Tickets

## Lineage

This is an MIT-licensed Hermes adaptation of Matt Pocock's public
[`to-tickets`](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-tickets).
The complete upstream notice is preserved in
[`references/third-party-notices.md`](references/third-party-notices.md).

Compile one exact, user-accepted source snapshot into an agent-sized delivery
graph. Initial invocation authorizes a chat draft only.

`DRAFT_READY` means an honest reviewable draft exists; it does not mean
grounding is complete or authorize publication or implementation. Pending
pre-publication grounding, graph rechecks, or fresh approval may coexist with
`DRAFT_READY` when accepted facts already determine the safe draft shape. Use
`BLOCKED` when missing facts prevent an honest draft or materially change its
graph, sizing, sequencing, or safety. For decision-only decomposition, do not
block merely because later implementation details remain unknown.

## Source and grounding

Accept one exact source snapshot with identifiable scope, owner, requirements,
decision/evidence handles, constraints, negatives/exceptions, out-of-scope
boundaries, observable acceptance, and required evidence. Do not infer acceptance
or current truth from an old conversation, a similarly named file, or mere
draft existence. Keep `source_snapshot` exactly equal to the accepted version,
revision, fingerprint, or message handle. Put drift history or missing-revision
explanations in `lineage`, `blockers`, or a separate drift field; never append
those explanations to the snapshot value.

Before slicing, inspect only current repository and record evidence needed to
validate implementation-facing claims: active project/tracker policy, governing
decisions and vocabulary, relevant interfaces, seams, behavior and tests, plus
source negatives, exceptions, and acceptance methods. Prior exploration does
not validate a specific claim. A direction to reuse an unnamed “existing seam”
does not itself verify that seam.

Verify every claim that determines ticket size, blocker edges, blast radius, or
acceptance. For an actual ticket bundle, do not claim `DRAFT_READY` or grounding
passed when unavailable evidence would require route-changing guesswork. Never
invent a seam, cohort, owner, dependency, acceptance boundary, or implementation
fact. Exact files belong to later Plan work, but uncertainty that changes graph,
sizing, sequencing, coverage, or safety blocks drafting. Name the missing
evidence and required regeneration checks rather than emitting placeholder
tickets.

## Compile the graph

### Ordinary work

Prefer narrow **vertical slices**. Each ticket must:

- deliver one observable end-to-end behavior across every required layer;
- fit one fresh implementation context and leave the repository green;
- own source-derived positive and negative acceptance plus evidence across every
  applicable behavior class: validation/failure, authorization, retry and
  idempotency, atomicity and rollback, audit, confidentiality/metadata, and
  temporal or compatibility transitions;
- preserve source semantics exactly: never strengthen, relax, or redefine an
  exception, grace period, compatibility window, security boundary, or non-goal;
- be independently demonstrable, with no hidden half-feature or follow-up needed
  to satisfy the behavior it claims;
- preserve atomic requirements together: do not split required audit, security,
  idempotency, rollback, or failure behavior from the operation whose safe
  completion depends on it.

For each applicable behavior, make cross-effects explicit:

- authorization failure, expiry, revocation, or a nonexistent handle causes no
  protected mutation, no success audit, and no protected metadata or secret
  disclosure unless the source explicitly permits an effect;
- same-key retry duplicates none of the source-required persisted effects,
  including primary records, audit records, events, or handles;
- temporal and grace behavior is verified before, during, at the boundary, and
  after transition without redefining the source contract.

Split large work by independently usable behavior, not schema/API/UI or other
horizontal layers. A separate infrastructure or preparation ticket is allowed
only when independently verifiable and a genuine blocker. Preserve unrelated
parallelism; never add edges for review order or convenience.

### Wide migrations

When the source establishes a wide mechanical change, use
**expand → independently green migration batches → contract**:

1. add a backward-compatible expansion and mixed-version contract evidence;
2. migrate explicitly bounded, owned, independently testable cohorts in
   parallel where safe;
3. remove the old contract only after every cohort is verified migrated.

If intermediate batches cannot be independently green, name the integration
boundary and add final integration verification instead of claiming each batch
is releasable. Missing cohort membership, ownership, transition semantics,
conflict behavior, or contraction evidence that changes sizing or safety is
`BLOCKED`, not a placeholder ticket.

### Coverage and graph checks

Use stable draft IDs and only real blockers. Reject missing, self, or cyclic
edges and compute the true frontier. `frontier` is stage-specific: a
`DRAFT_READY` bundle may show structural start nodes for review but creates no
implementation authority; `BLOCKED` and `RECONCILE_REQUIRED` bundles always use
`frontier: []`. Never expose a blocked, unknown-body, or reconciliation-pending
ticket as actionable.

Cycle-check completeness concerns the
intended ticket-ID/blocker-edge set, not ticket bodies, acceptance, or source
mappings. If all intended IDs and edges are known, run the check even when
grounding or coverage remains blocked. If that ID/edge set is unavailable or
incomplete, set `cycle_check: not_run`; never claim `passed` for an unaudited
graph. Prove both directions: every current requirement/constraint maps to
tickets or an explicit owner-accepted disposition, and every ticket maps to
source requirements, decisions/evidence, and acceptance. Omission, orphan
scope, silent expansion, or self-accepted disposition is `BLOCKED`.

## Canonical schemas

Every ticket uses this contract:

```yaml
id: <stable draft ID or published handle>
status: DRAFT | READY | BLOCKED | PUBLISHED
parent: <source snapshot handle>
source_snapshot: <hash, version, timestamp, or accepted message handle>
owner: <real owner>
source_requirements: [<IDs>]
source_decisions_evidence: [<IDs or handles>]
blocked_by: [<ticket IDs>]
delivers: <one observable behavior>
acceptance_criteria: [<observable positive and negative checks>]
verification_evidence: [<tests, artifacts, or observations>]
constraints: [<source-derived constraints>]
exclusions: [<explicit non-goals>]
authorization: <draft/publication/implementation boundary>
```

The bundle uses this contract:

```yaml
schema: to-tickets-bundle-v1
state: DRAFT_READY | PUBLISHED | BLOCKED | RECONCILE_REQUIRED
source: <path, handle, or conversation reference>
source_snapshot: <hash, version, timestamp, or accepted message handle>
source_owner: <name>
lineage: <source -> ticket graph>
tickets: [<canonical ticket objects>]
frontier: [<currently unblocked ticket IDs>]
coverage:
  requirement_to_tickets: <map>
  ticket_to_source: <map>
  dispositions: <map>
  uncovered_requirements: []
  orphan_tickets: []
cycle_check: passed | failed | not_run
grounding_status: passed | blocked
publication:
  backend: none | local | tracker
  approval_binding: none | <exact opaque graph fingerprint copied verbatim, e.g. G14; never append backend, status, or prose>
  persistence: none | partial | confirmed
  published_handles: []
  readback_verified: false
```

Additional presentation fields are allowed, but these meanings and types must
not be silently replaced by an ad-hoc schema.

## Authority, drift, and recovery

- Publication requires later approval bound to the exact reviewed graph and one
  named backend. A configured tracker, old access, source approval, draft
  request, or generic “go ahead” is not publication authority.
- Graph approval and backend authorization are separate. Naming or approving a
  backend does not invalidate approval of an unchanged graph; source or graph
  changes do.
- `RECONCILE_REQUIRED` preserves the exact approval binding for an unchanged
  graph. Uncertain, partial, or unverified persistence alone never clears that
  graph approval.
- An approved ticket ID whose source mapping is temporarily unavailable remains
  approved-but-unresolved, not an orphan. Keep `orphan_tickets: []` unless
  evidence proves a ticket lacks source authority; represent unknown mappings as
  blocked or unknown coverage instead.
- Source drift invalidates coverage and approval. Graph mutation requires
  affected grounding, bidirectional coverage, cycle/frontier checks, and new
  exact publication approval.
- Create blockers first where handles are needed, then bodies and real edges;
  read back bodies, edges, labels, and handles before claiming `PUBLISHED` or
  applying `ready-for-agent` to verified approved child tickets.
- On uncertain or partial writes, preserve known handles, search stable
  idempotency keys before retry, never recreate blindly, and return
  `RECONCILE_REQUIRED` until reconciled.
- Never plan implementation, dispatch agents, create Kanban, implement, commit,
  deploy, complete tickets, or modify/close/label the parent specification.
  A ticket graph never creates implementation authority.
- A request for exact files, code, tests, or commands for one existing ticket
  routes to Plan, not To-Tickets.
