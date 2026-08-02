---
name: wayfinder
description: "Use for medium-to-large work with multiple material decisions, dependencies, fog, or multi-session coordination. Applies a lightweight in-session route automatically when useful and a durable full Wayfinder package when explicitly invoked or scale requires persistence."
version: 1.3.0
author: "SaikaAco with Hermes Agent, adapted from Matt Pocock"
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [wayfinder, decisions, research, prototype, planning, traceability]
    related_skills: [wf, bounded-grilling, prototype, to-spec, to-tickets, kanban-workflows]
    upstream: "https://github.com/mattpocock/skills/tree/main/skills/engineering/wayfinder"
---

# Hermes Wayfinder

## Lineage

This is an MIT-licensed adaptation of Matt Pocock's public
[`wayfinder`](https://github.com/mattpocock/skills/tree/main/skills/engineering/wayfinder).
It retains the destination, map, decision-ticket, frontier, fog, and
one-ticket-at-a-time concepts while adding Hermes-specific authority,
persistence, recovery, mode, and handoff contracts.

The complete upstream MIT notice is preserved in
[`references/third-party-notices.md`](references/third-party-notices.md).

## Overview

Wayfinder charts a durable route through an effort too large or uncertain for
one session. It owns the map, fog, frontier, ticket lifecycle, persistence,
handler routing, and readiness handoff. It resolves decisions and evidence—not
the destination itself.

```text
Bounded Grill -> Wayfinder
  DECISION     -> Bounded Grilling
  EVIDENCE     -> verified evidence handler
  PROTOTYPE    -> `/prototype`: runnable artifact + human reaction
  PREREQUISITE -> bounded task/checklist
Wayfinder -> To-Spec -> `/to-tickets` (separate explicit authority)
```

The canonical shared handler contracts live in:

- `references/evidence-handler.md`
- `references/prototype-handler.md`

For a small effort whose route is already clear:

```text
Bounded Grill -> To-Spec
```

## Adaptive invocation and operating level

When `/wf` is manually invoked or its automatic ambiguity gate detects one
genuine route-affecting unknown, enter Wayfinder LIGHT immediately when this
skill is the selected handler; the ordinary multi-signal heuristic below is not
required. Investigate discoverable facts first and route one human-owned value
to Bounded Grilling rather than assuming it. Do not create FULL artifacts from
this standing ambiguity authority alone.

Otherwise choose `LIGHT` or `FULL` before applying the workflow.

### LIGHT — model-invokable, non-persistent

Use LIGHT automatically when structure would reduce drift but a durable map
would be disproportionate. Typical signals include two or more of:

- the task has at least three meaningful steps or two material choices;
- dependencies or ordering matter;
- the route is partly uncertain but likely resolvable in the current session;
- tools, agents, or people need a concise handoff;
- explicit scope, frontier, or acceptance boundaries would prevent rework.

LIGHT stays inside the current conversation. It creates no map, ticket,
tracker item, branch, or project file. Keep only a compact route:

```text
Destination
Decisions and constraints
Unknowns / fog
Current frontier
Out of scope
```

LIGHT may be embedded in an already-authorized task and return control to that
task. It does not impose the one-ticket-per-invocation rule, emit a durable
handoff packet, or claim a FULL completion state.

### FULL — durable protocol

Use FULL when the user explicitly invokes Wayfinder, or automatically when any
of these hard signals makes recovery and persistence materially valuable:

- the effort will likely outlive the current session;
- three or more unresolved route-changing decisions remain;
- multiple agents or people may work concurrently;
- a durable handoff, restart point, or authoritative decision history is
  required.

When selecting FULL automatically, announce that choice in one sentence and
name the persistence target. Create a project-local package only when the
current task already authorizes project artifacts; otherwise obtain approval
before mutation. External tracker creation or mutation always requires current
project policy or explicit user authorization.

An explicit FULL chart invocation, or an automatically selected FULL chart
with artifact authority, authorizes:

- one Bounded Grill opening-router call when no valid route packet exists; and
- creation of a local Wayfinder package in the active project when no
  externally authorized tracker is available.

Neither level authorizes external issue publication, destination
implementation, deployment, or unrelated side effects.

## Authority boundary

- Plan and resolve uncertainty; do not deliver the destination.
- Never answer the human side of a HITL decision.
- Never silently turn evidence into a human preference.
- Never create or mutate an external tracker unless current project policy or
  the user explicitly authorizes that tracker.
- Prerequisite work may only expose evidence needed for a decision; it may not
  become destination implementation.
- Research dispatch is not ticket resolution: cited results require parent
  verification and persistence before closure.
- Prototype authority permits only the named throwaway decision artifact. It
  never authorizes production implementation, main-branch integration,
  publication, deployment, or cleanup.
- Stop immediately on a user stop signal.
- A FULL To-Spec handoff requires either an explicit user request or an
  already-authorized workflow whose endpoint includes specification. LIGHT
  To-Spec may follow automatically without persistence or publication.

## FULL operation mode

When operating at FULL, choose exactly one:

- `CHART` — create a new map from a valid route packet or loose idea.
- `ADVANCE` — claim and resolve exactly one ticket on an existing map.
- `ASSESS` — read-only readiness, consistency, or frontier inspection.

Never chart and advance in the same FULL invocation. LIGHT may orient and make
progress in one ordinary task because it creates no authoritative tickets.

## Persistence backend

This section applies only to FULL. LIGHT never selects a persistence backend.

Choose before any FULL map mutation:

1. Use an existing project tracker only when it is already configured and
   authorized for this effort.
2. Otherwise use a project-local package:

```text
<active-project>/.hermes/wayfinder/<effort-slug>/
  map.md
  tickets/
    <ticket-id>.md
```

Do not place project-specific maps in the shared Hermes workspace unless that
workspace is itself the active project.

If no safe project root or authorized tracker can be identified, return
`BLOCKED`. Never guess an external tracker or create one.

The map is an index, not a store. Full questions, evidence, answers, rationale,
constraints, and negative requirements live in exactly one authoritative
ticket record. The map stores only status, one-line gists, and handles.

For concurrent work:

- prefer tracker-native assignment or claims;
- local-file mode is serialized by default;
- permit parallel local work only when an available primitive can create an
  exclusive claim and fail if the claim already exists;
- otherwise return `BLOCKED` rather than risk duplicate resolution.

## Map contract

Every map records:

```markdown
# <Effort name>

Status: CHARTING | ACTIVE | READY_FOR_SPEC | BLOCKED |
  DESTINATION_COMPLETE_WITHOUT_SPEC | RECONCILE_REQUIRED | SUPERSEDED
Map handle: <authoritative tracker URL/ID or local path>
Updated: <actual timestamp>

## Destination
<The accepted end state Wayfinder is finding a route toward.>

## Authority and persistence
<Product acceptor, backend, and mutation boundary.>

## Notes
<Domain vocabulary, source hierarchy, standing constraints, and named methods.>

## Decisions so far
<One-line gist and handle for each authoritative resolved ticket.>

## Not yet specified
<In-scope fog that cannot yet be phrased as a precise ticket.>

## Out of scope
<Explicitly excluded work and the source of that boundary.>

## Handoff
<Latest readiness state and packet handle, without duplicating ticket rationale.>
```

Open tickets live in the tracker or `tickets/` and are found by query or scan.
Do not duplicate their full bodies in the map.

## Ticket contract

Each ticket has one stable tracker or local identity and one precise question:

```markdown
# <Ticket title>

ID: <authoritative identity>
Type: DECISION | EVIDENCE | PROTOTYPE | PREREQUISITE
Mode: HITL | AFK
Status: OPEN | CLAIMED | RESOLVED | DEFERRED | BLOCKED | OUT_OF_SCOPE | SUPERSEDED
Blocked by: <handles or none>
Claim: <owner/session and actual timestamp, or none>

## Question
<Exactly one route-relevant question or evidence objective.>

## Resolution
<Accepted answer, evidence result, authorized prerequisite result, or blocker.>

## Rationale and sources
<Rationale pointer, evidence handles, assumptions, and rejected alternatives
when they constrain downstream work.>

## Constraints and dependency effects
<Negative requirements, invalidated assumptions, newly unblocked handles, and
staleness effects.>
```

Ticket types:

- `DECISION` / `HITL` — one human-owned route decision, resolved through
  Bounded Grill's Wayfinder mode.
- `EVIDENCE` / `AFK` — one discoverable factual question. Resolve it through
  `references/evidence-handler.md`, using the active profile's permitted
  research/inspection tools and source hierarchy.
- `PROTOTYPE` / `HITL` — one logic/state or UI-shaped decision that needs a
  runnable throwaway artifact and actual human reaction. Invoke `/prototype`,
  whose canonical contract is `references/prototype-handler.md`; prose alone
  cannot close it.
- `PREREQUISITE` / `AFK` or `HITL` — bounded manual work required to expose
  evidence. It needs explicit authority when it has side effects and may not
  deliver the destination.

## Handler and closure gate

Ticket type is a workflow gate, not a category. After claiming a ticket and
immediately before resolution, re-read its authoritative type, question,
blockers, claim, and current status. If type and prose disagree, stop for
reconciliation rather than choosing the easier handler.

Route exactly:

- `DECISION` -> Bounded Grilling; require one accepted human decision packet.
- `EVIDENCE` -> `references/evidence-handler.md`; require a valid
  `wayfinder-evidence-v1` handoff with parent verification and confirmed
  persistence.
- `PROTOTYPE` -> invoke `/prototype`, whose canonical contract is
  `references/prototype-handler.md`; require a valid
  `wayfinder-prototype-v1` handoff, a smoke-verified artifact, actual human
  reaction, and an accepted decision.
- `PREREQUISITE` -> perform only the authorized bounded task; require observable
  completion evidence, or leave the ticket open with a precise human checklist
  or blocker.

Before marking any ticket resolved:

1. Re-fetch/re-read the ticket and claim; abort or reconcile stale, closed, or
   rival work.
2. Verify handler-specific evidence and all referenced artifacts.
3. Classify outputs as durable shared context, ticket evidence, disposable
   intermediate, or potential implementation.
4. Reconcile durable shared context into its canonical location. Never strand
   it on a research/prototype branch or isolated workspace.
5. Persist the full resolution in the ticket first, then reconcile the map.
6. If evidence persists but context/map reconciliation fails, return
   `RECONCILE_REQUIRED`; do not duplicate or silently close the ticket.

An ADVANCE invocation becomes spent after one handler outcome, including a
blocker, deferral, or `PROTOTYPE_REQUIRED` escalation. It may repair
bookkeeping for that ticket but may not claim another ticket.

## CHART mode

1. Orient to the user's named effort and available sources.
2. Consume a `grill-route-v1` packet when present. If absent, invoke Bounded
   Grill's opening router once under the active FULL invocation's authority.
3. Handle the route:
   - `DIRECT_SPEC` — create no map; return the Grill packet and stop.
   - `BLOCKED` — create no map; return the named blocker and stop.
   - `WAYFINDER` — continue only when destination, accepted decisions,
     constraints, evidence handles, and suspected fog are internally
     consistent.
4. Select the persistence backend.
5. Import every accepted Grill decision:
   - when its handle resolves to a durable authoritative record, reference
     that record without copying it;
   - when `persistence: pending` or no durable handle exists, create one
     authoritative `RESOLVED` decision ticket in the selected backend,
     preserving the exact accepted value, source timestamp, rationale,
     constraints, and negative requirements;
   - use the resulting ticket identity as the authoritative handle.
   Importing an already-accepted decision persists chart input; it is not
   resolution of a new frontier ticket.
6. Create one map with destination, authority, accepted-decision pointers,
   boundaries, and fog.
7. Create only questions precise enough to be tickets. Leave coarser
   uncertainty under `Not yet specified`.
8. Assign stable identities, types, modes, blockers, and creation order. Use
   `PROTOTYPE` when interaction with a concrete artifact is required; do not
   disguise it as prose `DECISION` or generic `PREREQUISITE` work.
9. Write and verify every imported and open ticket before writing the map
   index.
10. Re-read the persisted map and tickets.
11. Optionally dispatch independent `EVIDENCE` tickets through
    `references/evidence-handler.md` only after their records are durable.
    Dispatch does not resolve or close them. Use `delegate_task` only when the
    parent session can safely receive the result; use authorized Kanban for
    restart-durable work. Record every dispatch handle.
12. Return `MAP_READY`, include any evidence dispatch handles, and stop.
    Resolve or claim no non-evidence frontier ticket during charting.

## ADVANCE mode

1. Load the map at low resolution and verify its current status and backend.
2. Select the user-named ticket or the first open, unblocked, unclaimed ticket
   in stable creation order.
3. Claim it before work. If the claim cannot be made safely, return `BLOCKED`.
4. Re-read the claimed ticket's authoritative type, body, blockers, claim, and
   current status, then run exactly one handler:
   - `DECISION` — invoke Bounded Grill Wayfinder mode with the ticket handle,
     destination, question, relevant decisions, and direct dependencies. If
     the decision cannot be judged faithfully in prose, consume a
     `PROTOTYPE_REQUIRED` return by leaving the decision open, creating one
     `PROTOTYPE` ticket, and then adding a create-then-link edge that makes the
     decision ticket depend on the prototype ticket; do not fabricate the
     decision.
   - `EVIDENCE` — follow `references/evidence-handler.md`; inspect cited
     sources and verify the result before persistence.
   - `PROTOTYPE` — invoke `/prototype` and its canonical
     `references/prototype-handler.md` contract; obtain artifact authority,
     smoke-run the artifact, collect actual human reaction, and preserve the
     accepted/rejected alternatives.
   - `PREREQUISITE` — perform only the already-authorized bounded work needed
     to expose evidence. Otherwise block with the required authority or exact
     human checklist.
5. Apply the handler and closure gate. Persist the full resolution in the
   ticket first.
6. Close or resolve a decision only after its accepted record is confirmed
   persisted. A normal deferral remains open and blocking; close it only when
   the product acceptor explicitly marks it non-blocking.
7. Append only a one-line gist and ticket handle to `Decisions so far`.
8. Graduate newly precise fog into new tickets, create-then-link blockers, and
   remove the graduated text from `Not yet specified`.
9. Mark invalidated tickets or assumptions `SUPERSEDED`; never erase history.
10. Recompute the frontier, release the claim, run the exit gate, and stop.

If ticket persistence succeeds but map reconciliation fails, the ticket
remains authoritative. Mark the map `RECONCILE_REQUIRED`, return that state,
and do not repeat or duplicate the resolution.

## ASSESS mode

Read only. Report:

- destination and authority;
- persistence health;
- current frontier and blockers;
- unresolved or contradictory route decisions;
- hidden, duplicated, stale, or graduated-but-not-cleared fog;
- exit-gate status;
- exact next eligible ticket or handoff state.

Do not claim, resolve, create, close, or edit anything.

## Exit gate

Wayfinder may emit `READY_FOR_SPEC` only when all five conditions hold:

1. Destination, scope, acceptance boundary, and out-of-scope boundary are
   explicit.
2. Every route-changing decision is accepted, blocked, or explicitly deferred
   as non-blocking by the product acceptor.
3. No material in-scope fog remains hidden or unclassified.
4. No eligible decision, evidence, prototype, or prerequisite ticket remains.
5. The product acceptor explicitly determines the route is ready for local
   specification.

If conditions 1–4 hold but condition 5 has no authoritative record, create one
named final `DECISION` ticket and stop. Resolve it in a later `ADVANCE`
invocation through Bounded Grill.

If the destination is itself a final decision or intentionally ends without a
specification, emit `DESTINATION_COMPLETE_WITHOUT_SPEC` instead.

## To-Spec handoff

On exit, persist and return this exact packet:

```yaml
schema: wayfinder-to-spec-v1
outcome: READY_FOR_SPEC | BLOCKED | DESTINATION_COMPLETE_WITHOUT_SPEC
destination: <accepted destination>
map_handle: <authoritative URL/ID/path>
decision_handles: []
scope: []
out_of_scope: []
evidence_handles: []
assumptions_and_nonblocking_deferrals: []
stale_or_superseded_handles: []
persistence: confirmed
readiness_owner: <product acceptor>
timestamp: <actual timestamp>
```

Rules:

- `decision_handles` contains every current authoritative route decision.
- Full rationale remains in tickets; the packet carries handles, not copies.
- `READY_FOR_SPEC` requires `persistence: confirmed`.
- `BLOCKED` names the failed exit conditions and their owners.
- Invoke FULL To-Spec only when explicitly requested or when the authorized
  workflow endpoint already includes specification. LIGHT To-Spec may follow
  automatically without persistence or publication.

## Completion states

LIGHT returns:

- `LIGHT_ROUTE` — compact in-session route applied with no durable artifacts.

FULL returns exactly one:

- `DIRECT_SPEC` — the opening Grill found no multi-session fog; no map created.
- `MAP_READY` — chart persisted and verified; no ticket resolved.
- `TICKET_RESOLVED` — one ticket persisted and map reconciled.
- `READY_FOR_SPEC` — all exit conditions passed and handoff persisted.
- `DESTINATION_COMPLETE_WITHOUT_SPEC` — destination completed without a
  specification handoff.
- `BLOCKED` — authority, evidence, persistence, claim, or dependency prevents
  safe progress.
- `RECONCILE_REQUIRED` — ticket is authoritative but map update failed.

None creates implementation authority; any implementation must already be
explicitly authorized by the current user request.

## Common pitfalls

1. **FULL for everything.** Prefer LIGHT when a durable map would cost more
   than it saves; announce automatic FULL selection and verify artifact
   authority.
2. **Building the destination.** Resolve the route, then stop unless the
   original request separately authorizes implementation.
3. **Map duplication.** Keep rationale and evidence in one ticket record.
4. **Premature tickets.** Fog stays fog until its question is precise.
5. **Human substitution.** HITL decisions require the human's answer.
6. **Fact delegation to the user.** Research discoverable evidence.
7. **Unsafe tracker default.** Use external systems only when authorized.
8. **Duplicate claims.** Serialize or use a real exclusive claim.
9. **Close-before-persist.** Persist first; close only after confirmation.
10. **Handler bypass.** Ticket type controls the resolver; a prose answer cannot
    close a `PROTOTYPE`, unverified summaries cannot close `EVIDENCE`, and the
    agent cannot close `DECISION` without the human owner.
11. **Dispatch-as-resolution.** A research child self-report is not verified or
    persisted evidence. Inspect sources and artifacts before closure.
12. **Prototype promotion.** A prototype decision does not authorize production
    implementation or merging disposable code.
13. **Lossy handoff.** Emit every current decision handle.
14. **Unscoped To-Spec.** Invoke FULL only when requested or already included
    in the authorized workflow; prefer automatic LIGHT otherwise.
15. **Stale-route reuse.** Preserve history and mark superseded handles.

## Verification checklist

- [ ] LIGHT or FULL was selected from observable task signals.
- [ ] LIGHT created no map, ticket, tracker item, branch, or project file.
- [ ] Any automatic FULL selection was announced and had artifact authority.
- [ ] A FULL operation mode is explicit.
- [ ] One authorized persistence backend is selected for FULL.
- [ ] The map is an index and every decision has one authoritative ticket.
- [ ] Chart mode resolved no tickets and claimed no non-evidence ticket; any
      evidence dispatch happened only after ticket persistence.
- [ ] Advance mode ran exactly one claimed ticket handler and became spent
      after its outcome; it resolved at most one ticket.
- [ ] The claimed ticket was re-read and its type controlled the handler.
- [ ] HITL decisions used Bounded Grill without self-answering.
- [ ] Evidence tickets returned verified, persisted `wayfinder-evidence-v1`
      handoffs with inspected sources.
- [ ] Prototype tickets returned smoke-verified `wayfinder-prototype-v1`
      handoffs with actual human reaction.
- [ ] Durable shared context was reconciled separately from ticket evidence and
      disposable prototype/research artifacts.
- [ ] Ticket persistence preceded map reconciliation.
- [ ] Claims and blockers are safe and current.
- [ ] Exit status follows all five conditions.
- [ ] `wayfinder-to-spec-v1` is complete and persisted when emitted.
- [ ] No destination implementation occurred without explicit current
  authority, and no unscoped automatic downstream invocation occurred.
