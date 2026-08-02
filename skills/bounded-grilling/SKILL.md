---
name: bounded-grilling
description: "Use only when the user explicitly asks to be grilled, interviewed, or stress-tested, when /wf routes one genuine human-owned ambiguity, or when a named Wayfinder HITL decision ticket invokes it. Resolves bounded human decisions with evidence, recommendations, traceable records, and no implementation."
version: 1.2.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [grilling, wayfinder, decisions, prototype, product-planning, hitl]
    related_skills: [wf, kanban-workflows, research-intelligence, wayfinder, to-spec]
---

# Bounded Grilling

## Overview

Bounded Grilling exposes and resolves material human decisions without turning
an interview into an endless session or implementation. The human owns value
judgments and authority decisions. The agent discovers facts, frames options,
recommends a default, returns a traceable decision packet, and stops.

## Invocation gate

Run only when:

- the user explicitly asks to be grilled, interviewed, or stress-tested; or
- the shared `/wf` router invokes one genuine human-owned ambiguity under the
  user's standing ask-not-assume instruction; or
- the user explicitly invokes Wayfinder charting, which authorizes one bounded
  opening-router call; or
- an existing, named Wayfinder HITL decision ticket invokes the skill.

Outside those cases, an agent may briefly offer Bounded Grilling when a
route-changing decision is blocking progress, but must not begin until the
user accepts. Complexity or ambiguity alone is not permission to start.

## Authority boundary

- Ask the human only for decisions; investigate discoverable facts first.
- Never answer the human side of a HITL decision.
- Never implement, publish, install, configure, activate, or otherwise mutate
  the product because the interview ended.
- Bounded Grilling does not claim, edit, close, link, or create tracker items.
- The invoking Wayfinder workflow owns all authorized tracker persistence and
  map, fog, frontier, and dependency updates.
- Stop immediately on a user stop signal.

## Choose one mode

### Opening router

Use for a loose plan or destination before choosing the planning route.

1. Resolve no more than three distinct route-changing human decisions.
2. Stop earlier when remaining uncertainty is non-blocking.
3. Return exactly one route:
   - `DIRECT_SPEC` — the route is clear enough for local specification;
   - `WAYFINDER` — material multi-session fog or dependent decisions remain;
   - `BLOCKED` — required evidence or decision authority is unavailable.
4. Return the compact decision packet and stop.
5. Do not create a specification, Wayfinder map, task, or other artifact.

### Opening route handoff

Return this exact versioned handoff with the compact decision packet:

```yaml
schema: grill-route-v1
route: DIRECT_SPEC | WAYFINDER | BLOCKED
destination: <settled destination or explicit unknown>
accepted_decision_handles: []
constraints: []
negative_requirements: []
evidence_handles: []
suspected_fog: []
out_of_scope: []
persistence: confirmed | pending
```

Use existing project or ticket handles. When none exist, preserve the exact
accepted value with an actual timestamp rather than inventing a parallel
decision-ID system.

- `DIRECT_SPEC` is consumable by `to-spec`.
- `WAYFINDER` is consumable by Wayfinder chart mode.
- `BLOCKED` names the missing evidence or authority.

Do not invoke either consumer automatically. Return the handoff and stop.

### Wayfinder HITL decision

Use only with one existing, named human-decision ticket.

1. Require the ticket name/ID, destination, decision question, relevant
   accepted decisions, and direct dependencies. Return `BLOCKED` if the
   minimum context is unavailable.
2. Resolve exactly one decision branch.
3. Ask follow-ups only when needed to clarify that same branch.
4. Open no second ticket and resolve no unrelated decision.
5. Return exactly one outcome:
   - `RESOLVED` — one accepted value is ready to persist;
   - `DEFERRED` — the human explicitly deferred the decision;
   - `BLOCKED` — evidence or authority is insufficient;
   - `PROTOTYPE_REQUIRED` — the decision cannot be judged faithfully in prose
     and needs one bounded runnable artifact plus human reaction.
6. For `PROTOTYPE_REQUIRED`, name exactly one decision question, choose `LOGIC`
   or `UI`, state artifact constraints/authority still needed, and return no
   accepted value. The invoking Wayfinder keeps this decision open and owns any
   prototype ticket creation/linking.
7. Otherwise return the compact decision packet to the invoking Wayfinder
   workflow.
8. The ticket remains unresolved until Wayfinder confirms persistence.
9. After authorized persistence and map/dependency updates, stop. Do not
   select or begin the next ticket.

## Prototype escalation gate

Use `PROTOTYPE_REQUIRED` only when concrete interaction would materially reduce
uncertainty that questioning cannot, such as:

- legal/illegal state transitions or behavior at difficult edges (`LOGIC`);
- UI hierarchy, navigation, layout, or primary affordance (`UI`);
- multiple plausible structures whose consequences cannot be compared reliably
  from prose.

Do not escalate merely because a prototype would be interesting or because the
human dislikes choosing. A prototype must still answer one route-changing
question. Return the proposed branch, minimum cases/variants, standing
constraints, and missing artifact authority. Do not build it inside Bounded
Grilling.

## Decision-value gate

Ask a question only when its answer can materially change at least one of:

- scope or destination;
- architecture or execution class;
- supported user/cohort or support burden;
- authority, safety, privacy, or recovery boundary;
- dependency or credential structure;
- acceptance or release method.

Do not ask ordinary implementation, schema, command, fixture-count, naming, or
milestone details when they can safely remain local-spec work. Do not reopen a
settled decision without new evidence, a material contradiction, or an
explicit user request.

## Question loop

For the current decision:

1. State the decision and why it blocks downstream work.
2. Inspect available files, tracker records, documentation, and appropriate
   primary sources for answerable facts.
3. Separate observed facts, assumptions, and value judgments.
4. Ask exactly one question.
5. Include:
   - the minimum relevant facts and constraints;
   - one recommended answer;
   - the principal trade-off;
   - at most four materially distinct selectable options when options help;
   - free-form input through `Other`.
6. Wait for the answer.
7. If the answer is ambiguous, ask only the smallest follow-up needed for the
   same decision.
8. Confirm the normalized accepted value before returning it when an
   interpretation could change scope or authority.

Use `clarify` for selectable questions. Never place choices only in prose.
Do not force artificial choices when an open-ended answer is necessary.

## Compact decision packet

Reuse an existing Wayfinder ticket ID or project decision ID. Do not create a
parallel identity system.

Every accepted decision record must contain:

- existing ticket/decision ID or source handle;
- accepted value and human owner;
- concise rationale;
- evidence handles or explicit assumptions;
- material constraints and negative requirements;
- dependencies affected, invalidated, or newly unblocked;
- an actual timestamp obtained from the tracker or a time tool.

Add conditional fields only when applicable:

- recommendation rejected or materially modified;
- prior value revised or superseded;
- explicit deferral or blocker;
- opening-router outcome.

Preserve superseded records and mark them stale; never silently overwrite
decision history. A Wayfinder map indexes the authoritative record rather than
duplicating its full rationale.

In opening-router mode, if no authorized durable artifact exists, return the
packet in chat with `persistence: pending`; do not create a file or tracker
item. In Wayfinder mode, return `persistence: pending` until the invoking
workflow confirms the record was written.

## Completion and handoff

Opening-router mode is complete only when:

- up to three route-changing decisions are resolved, or the route is known
  earlier;
- the packet is returned;
- a valid `grill-route-v1` handoff is returned;
- `DIRECT_SPEC`, `WAYFINDER`, or `BLOCKED` is returned; and
- no artifact or implementation phase has begun.

Wayfinder mode is complete only when:

- one branch is `RESOLVED`, `DEFERRED`, `BLOCKED`, or
  `PROTOTYPE_REQUIRED`;
- a `PROTOTYPE_REQUIRED` return names one question, branch, constraints, and
  missing authority without claiming an accepted decision;
- the compact packet is returned for every other outcome;
- the invoking Wayfinder workflow reports whether persistence succeeded;
- authorized map/dependency effects are reported; and
- no next ticket, prototype build, or implementation phase has begun.

Returning a resolved WF clarification to the already-authorized parent task is
not a new planning or implementation phase; that task may resume within its
existing scope. Any downstream phase not already authorized by the parent
request requires a fresh user action.

## Common pitfalls

1. **Unsolicited grilling.** Outside explicit, `/wf`-routed, or named-ticket
   authority, offer it; do not auto-start.
2. **Endless interrogation.** Enforce the opening-router and one-ticket bounds.
3. **Low-value questions.** Apply the decision-value gate before asking.
4. **Asking for facts.** Research them and cite the evidence.
5. **Batching decisions.** Ask one question and wait.
6. **Leading choices.** Recommend clearly, but keep alternatives materially
   distinct and explain the principal trade-off.
7. **Decision loss.** Return the compact packet and require persistence status.
8. **Summary weakening.** Downstream work should reference authoritative
   decision IDs rather than rely only on compressed prose.
9. **Tracker coupling.** Grill returns the packet; Wayfinder owns mutations.
10. **Prototyping inside the interview.** Return `PROTOTYPE_REQUIRED`; do not
    build, select, or imply acceptance inside Bounded Grilling.
11. **Implementation drift.** Stop after route or persistence.

## Verification checklist

- [ ] Invocation was explicit, routed by `/wf` for one genuine human-owned
      ambiguity, or attached to one named Wayfinder HITL ticket.
- [ ] Every question passed the decision-value gate.
- [ ] Discoverable facts were investigated instead of delegated to the user.
- [ ] Only one question was active at a time.
- [ ] Recommendation, trade-off, and options were clear.
- [ ] Opening mode resolved at most three route-changing decisions.
- [ ] Opening mode returned a valid `grill-route-v1` handoff.
- [ ] Wayfinder mode resolved exactly one decision branch or returned one
      bounded `PROTOTYPE_REQUIRED` handoff.
- [ ] `PROTOTYPE_REQUIRED` was used only when interaction adds decision value,
      and no artifact was built inside Grill.
- [ ] The compact packet contains every required core field when applicable.
- [ ] Grill performed no tracker mutation.
- [ ] Persistence status and dependency effects are explicit.
- [ ] The correct mode-specific route or outcome was returned.
- [ ] No next phase or unauthorized side effect occurred.
