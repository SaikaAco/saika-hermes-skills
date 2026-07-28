---
name: to-spec
description: "Use when settled requirements need a clear execution contract. Applies a lightweight in-session specification automatically for medium jobs and a durable traceable draft when explicitly requested or when complex work needs persistent acceptance evidence."
version: 1.1.0
author: "SaikaAco with Hermes Agent, adapted from Matt Pocock"
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [specification, requirements, traceability, acceptance, wayfinder]
    related_skills: [bounded-grilling, wayfinder, plan]
    upstream: "https://github.com/mattpocock/skills/tree/main/skills/engineering/to-spec"
---

# Traceable To-Spec

## Lineage

This is an MIT-licensed adaptation of Matt Pocock's public
[`to-spec`](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-spec).
It retains conversation-to-spec synthesis without another interview while
adding Hermes-specific authority, traceability, coverage, blocking, safety,
and persistence contracts.

## Overview

To-Spec compiles already-settled decisions, evidence, and project context into
a reviewable specification. It preserves authoritative source handles, makes
negative requirements explicit, and proves coverage. It does not itself create
publication, task-creation, or implementation authority.

It is a compiler, not an interview or planning loop:

```text
clear route:
  Bounded Grill or settled conversation -> To-Spec

large or foggy route:
  Bounded Grill -> Wayfinder -> To-Spec
```

## Adaptive invocation and operating level

Choose `LIGHT` or `FULL` before compiling.

### LIGHT — model-invokable, embedded contract

Use LIGHT automatically when a concise contract would reduce drift but a
persistent specification would be disproportionate. Typical signals include
two or more of:

- the goal is settled and at least two constraints or acceptance conditions
  matter;
- the job has at least three meaningful steps or touches multiple seams;
- the user has already authorized planning, building, shipping, or review and
  a short requirements check would improve fidelity;
- a LIGHT Wayfinder route is ready to become concrete;
- scope, out-of-scope, assumptions, or recovery boundaries need to be explicit.

LIGHT remains in the current conversation and creates no file, issue, label,
tracker item, or durable handoff. Keep it compact:

```text
Goal
Scope / out of scope
Requirements and constraints
Observable acceptance
Assumptions / gaps
Authorized next action
```

LIGHT may be embedded inside an already-authorized task and then return control
to that task. It does not create new authority, but it also does not cancel
planning or implementation that the user already explicitly authorized.

### FULL — durable traceable draft

Use FULL when the user explicitly requests a specification, when a valid FULL
Wayfinder handoff is ready, or automatically when any of these hard signals
makes durable coverage materially valuable:

- the work will likely span sessions or reviewers;
- three or more authoritative decisions or source handles must remain
  traceable;
- an external interface, migration, safety boundary, or costly rollback is
  involved;
- persistent acceptance evidence is needed for implementation or handoff.

When selecting FULL automatically, announce that choice in one sentence and
name the intended artifact path or `chat-only`. Persist only to an already
authorized project convention or path. External publication, tracker mutation,
labels, notifications, tasks, and implementation remain separately governed
by the current user request.

## Authority boundary

- FULL produces a `DRAFT` specification unless the user explicitly assigns
  another reviewed state. LIGHT produces only an in-session contract.
- Do not interview the user or reopen settled decisions.
- Do not silently choose among unresolved route-changing alternatives.
- Do not publish to an external tracker, apply labels, notify collaborators,
  create implementation tickets, invoke `plan`, implement, commit, or deploy
  unless that exact downstream action is independently authorized by the
  current user request.
- A specification never creates new implementation authority. After LIGHT or
  FULL, continue only with downstream actions the user already explicitly
  authorized; otherwise stop at the contract or draft.
- External publication, task creation, planning, and implementation each
  require explicit authority; one never implies another.

## Accepted inputs

Use one or more of:

- a Bounded Grill `DIRECT_SPEC` packet;
- a settled conversation with identifiable decisions and evidence;
- a `wayfinder-to-spec-v1` packet plus its authoritative map and decision
  tickets;
- existing project requirements, policy records, ADRs, or specifications;
- relevant codebase and documentation evidence.

Do not require a specific tracker or named research skill. Use the tools and
source hierarchy available in the active profile.

LIGHT may compile an ordinary settled task or LIGHT Wayfinder route without a
schema packet. The strict handoff contracts below apply to FULL.

## FULL Grill handoff contract

When the source is Bounded Grill:

1. Require `schema: grill-route-v1`.
2. Continue only for `route: DIRECT_SPEC`.
3. Require destination, accepted decision handles or exact accepted values,
   constraints, negative requirements, evidence handles, suspected fog,
   out-of-scope boundaries, and persistence status.
4. Treat suspected fog as empty or explicitly non-route-changing. Otherwise
   return `BLOCKED` and route to Wayfinder.
5. Allow `persistence: pending` only when exact accepted values and actual
   source timestamps are present; the resulting specification must preserve
   them as its first durable consumer.

For `WAYFINDER`, return the packet for Wayfinder and stop. For `BLOCKED`,
preserve the named evidence or authority blocker and stop.

## FULL Wayfinder handoff contract

When the source is Wayfinder:

1. Require `schema: wayfinder-to-spec-v1`.
2. Continue only for `outcome: READY_FOR_SPEC`.
3. Require destination, map handle, every current decision handle, scope,
   out-of-scope boundaries, evidence handles, assumptions/non-blocking
   deferrals, stale/superseded handles, readiness owner, actual timestamp, and
   `persistence: confirmed`.
4. Resolve each handle from its authoritative record; do not treat the packet
   gist as a replacement for ticket rationale.
5. Return `BLOCKED` when the packet is incomplete, stale, contradictory, or
   not durably persisted.

For `DESTINATION_COMPLETE_WITHOUT_SPEC`, report that To-Spec is not applicable
and stop. For `BLOCKED`, preserve Wayfinder's blockers and stop.

## Readiness gate

For LIGHT, run a compact readiness check and expose material gaps instead of
inventing decisions. For FULL, inspect the supplied sources and classify every
material gap before drafting.

Return `BLOCKED` instead of a specification when any of these remain:

- an unresolved decision can change scope, destination, architecture or
  execution class, supported cohort, authority or safety boundary, dependency
  structure, or acceptance method;
- accepted decisions materially contradict one another;
- a required authoritative record is stale, superseded, or unavailable;
- critical evidence cannot be obtained without guessing;
- the requested output would require authority the user has not granted.

For each blocker, return:

```text
gap
why it changes the route or authority
decision/evidence owner
recommended route: bounded-grilling | wayfinder | evidence lookup
```

Do not ask the missing questions inside To-Spec. Route them to the owning
workflow and stop.

Non-route-changing implementation details may remain explicit assumptions or
local-spec choices when they are safe, reversible, and testable.

## Source precedence

Apply this order:

1. current accepted Wayfinder or project decision records;
2. the user's current explicit direction;
3. applicable project instructions, policies, and requirements;
4. verified repository state and source documentation;
5. explicit assumptions.

When a higher-priority source supersedes a lower-priority record, preserve the
old handle, mark it stale or superseded, and explain the replacement. Never
resolve a contradiction by silently blending incompatible statements.

## Grounding pass

Inspect only the relevant context needed to ground the specification:

- project instructions and accepted requirements;
- authoritative decision records and their current status;
- domain vocabulary and applicable ADRs;
- current interfaces, seams, behavior, and prior tests;
- primary sources for externally constrained facts.

Separate:

- observed facts with handles;
- accepted human decisions with handles;
- safe local-spec choices;
- explicit assumptions requiring later verification.

Do not write code or mutate the inspected project during this pass.

## FULL compilation process

1. Inventory all current decision IDs or source handles.
2. Preserve the exact force of each accepted value, including exceptions,
   constants, ordering, defaults, retry behavior, negative requirements, and
   rejected alternatives that constrain implementation.
3. Assign spec-local requirement IDs such as `REQ-001`. These identify
   requirements only; they never replace or renumber authoritative decision
   IDs.
4. Draft the specification using the template below.
5. Map every current decision/source handle to its concrete coverage.
6. Audit for omission, weakening, contradiction, unsupported expansion, stale
   references, and unverifiable acceptance language.
7. Return `BLOCKED` if the audit exposes a route-changing gap; otherwise emit
   the draft and completion report.

Prefer complete coverage over extensive prose. Merge redundant user stories
or requirements rather than repeating them.

## FULL specification template

```markdown
# <Specification title>

Status: DRAFT
Generated: <actual timestamp from a time tool>
Destination/source: <Wayfinder map, Grill packet, conversation, or project handles>

## Problem and destination

<Current problem, intended outcome, and why it matters.>

## Users and observable outcomes

<Actors, affected cohorts, and independently observable outcomes.>

## Scope

<Included behavior and boundaries.>

## Out of scope

<Explicit exclusions and reasons when material.>

## Requirements

### REQ-001 — <short requirement name>

- Requirement:
- Source decisions/evidence:
- Constraints and exceptions:
- Negative requirements:
- Observable acceptance:

## Accepted decisions and constraints

<Authoritative decision handles, accepted values, and rationale pointers.
Do not replace the authoritative record with a weaker summary.>

## Solution and seams

<High-level solution shape and the stable interfaces, operational boundaries,
or domain-specific seams where behavior can be observed and verified.>

## Acceptance and verification evidence

| Requirement | Observable outcome | Verification method | Required evidence |
|---|---|---|---|
| REQ-001 | ... | ... | ... |

## Safety, recovery, and authority boundaries

<Side-effect limits, failure handling, rollback/recovery expectations, and
actions that still require human authorization.>

## Assumptions and non-blocking deferrals

<Explicit, testable assumptions and deferred details that do not change the
selected route.>

## Decision coverage

| Decision/source handle | Status | Covered by | Fidelity check |
|---|---|---|---|
| ... | current | REQ-001 / constraint / out-of-scope | exact / strengthened / gap |
```

Adapt section vocabulary to the domain. For software, seams may be APIs,
modules, user interfaces, or integration tests. For non-software work, use the
relevant operational boundaries and evidence surfaces instead.

## FULL coverage gate

The draft passes only when:

- every current authoritative decision/source handle has a row;
- every row maps to a requirement, constraint, acceptance item, or explicit
  out-of-scope disposition;
- every negative requirement and material exception remains visible;
- no stale or superseded record is treated as current;
- every acceptance statement names an observable outcome and evidence method;
- every unsupported claim is marked as an assumption;
- no requirement expands scope without an authoritative source.

Use `gap` rather than pretending coverage when a decision was weakened,
omitted, contradicted, or cannot be verified. A route-changing gap changes the
result to `BLOCKED`.

## Output and persistence

LIGHT stays in chat and reports its compact contract plus the authorized next
action; it writes no artifact.

For FULL, if the user supplied an authorized local path or the active project
has a clear specification convention, write the `DRAFT` there. Otherwise
return the complete draft in chat and ask where it should be saved only if
persistence is needed.

Unless the current user request explicitly authorized the named downstream
action, do not:

- create a tracker issue or external document;
- apply `ready-for-agent` or any equivalent execution-facing state;
- mark the specification accepted on the user's behalf;
- create implementation tickets or modify a FULL Wayfinder map;
- start planning or implementation.

After producing the draft, report:

- artifact path or `chat-only`;
- source handles consumed;
- requirement and decision-coverage counts;
- assumptions, deferrals, and gaps;
- any external publications, tasks, labels, planning, or implementation
  actions actually taken, plus their explicit authority source; normally
  `none`.

## Completion states

LIGHT returns exactly one:

- `LIGHT_READY` — compact in-session contract is complete and may return to an
  already-authorized task;
- `BLOCKED` — a route-changing decision, contradiction, authority gap, or
  critical evidence gap remains.

FULL returns exactly one:

- `DRAFT_READY` — the durable specification and coverage audit are complete;
- `BLOCKED` — a route-changing decision, contradiction, authority gap, or
  critical evidence gap remains.

`LIGHT_READY` and `DRAFT_READY` describe contract readiness only. Neither means
accepted, published, ready for an agent, or newly authorized for
implementation.

## Common pitfalls

1. **Re-interviewing.** Route missing decisions to Bounded Grill or Wayfinder.
2. **Conversation-only synthesis.** Use authoritative source handles.
3. **Summary weakening.** Preserve exceptions, negatives, constants, and
   rationale pointers.
4. **Prose inflation.** Optimize for complete coverage, not maximum length.
5. **Assumption laundering.** Mark unsupported claims explicitly.
6. **Stale decisions.** Preserve history but compile only current records.
7. **Premature publication.** A draft is local/chat-only without approval.
8. **Execution signaling.** Never apply an agent-ready label automatically.
9. **Task leakage.** Requirements and acceptance evidence are not an
   implementation task list.
10. **Implementation drift.** FULL stops after the draft unless the current
    request already authorized downstream work; LIGHT returns only to work
    already authorized.
11. **FULL for every job.** Prefer LIGHT when persistence and complete coverage
    would cost more than they save.

## Verification checklist

- [ ] LIGHT or FULL was selected from observable task signals.
- [ ] LIGHT created no file, issue, label, tracker item, or durable handoff.
- [ ] Any automatic FULL selection was announced with an authorized path or
  `chat-only` target.
- [ ] Any FULL Grill input passed the `grill-route-v1` contract.
- [ ] Any FULL Wayfinder input passed the `wayfinder-to-spec-v1` contract.
- [ ] Readiness was checked before drafting.
- [ ] No unresolved route-changing decision was silently answered.
- [ ] Relevant project and source evidence was inspected.
- [ ] Facts, decisions, local choices, and assumptions are distinct.
- [ ] For FULL, every current decision/source handle has coverage.
- [ ] Negative requirements and exceptions remain explicit at the selected
  operating level.
- [ ] Acceptance outcomes and evidence methods are observable at the selected
  operating level.
- [ ] The output state is `LIGHT_READY`, `DRAFT_READY`, or `BLOCKED`.
- [ ] No external publication, label, task, plan, or implementation occurred
  without explicit authority from the current user request.
