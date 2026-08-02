---
name: wf
description: "Use automatically when genuine confusion, vagueness, missing authority, contradictory evidence, or unclear acceptance could change the work. Research discoverable facts first; route a gap resolvable by one human decision to Bounded Grilling, and larger or dependent fog—where one decision would not settle the route—to Wayfinder LIGHT. Use FULL only for its existing persistence signals; also use when the user invokes /wf."
version: 1.0.1
author: SaikaAco with Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [wf, wayfinder-flow, ambiguity, clarification, decisions, research, prototype, specification, tickets]
    related_skills: [bounded-grilling, wayfinder, prototype, to-spec, to-tickets, kanban-workflows]
---

# WF — Wayfinder Flow

## Purpose

WF is the short entry point and ambiguity router for the full decision-to-work
system:

```text
facts unclear       -> evidence handler / research
human choice unclear -> Bounded Grilling (`clarify`, one question)
interaction unclear -> `/prototype` + human reaction
many dependent unknowns -> Wayfinder LIGHT or FULL
route settled       -> To-Spec when a contract is needed
approved spec needs decomposition -> `/to-tickets`
execution needs durability -> separately authorized Kanban
```

Manual invocation is `/wf`. Automatic invocation follows the standing user
instruction: when work contains genuine doubt or something required is unclear,
do not silently assume; investigate discoverable facts, then ask the human
through this flow when a human-owned value remains.

## Trigger gate

Invoke WF automatically before proceeding when at least one unresolved item can
change the action, output, safety, or acceptance and any of these holds:

- two or more reasonable interpretations remain;
- a required value, scope boundary, destination, priority, or success condition
  is missing or ambiguous;
- authority for a mutation, publication, cost, credential use, cleanup,
  irreversible step, or cross-profile action is unclear;
- sources or instructions materially contradict one another;
- the applicable artifact, environment, target, owner, or backend cannot be
  identified confidently;
- a human preference or trade-off is being treated as if it were a factual
  lookup;
- the work would require inventing acceptance criteria, an exception, or an
  unsupported assumption;
- interaction with a concrete artifact is needed to judge logic or UI.

Do not manufacture doubt. WF is not required when one interpretation is plainly
supported by the current request, authoritative project convention, and
observable evidence. A discoverable fact is not automatically a user question:
look it up first. An obvious default supported by current evidence is not a
silent assumption; state it when material and proceed under the original
authority.

## Authority boundary

- WF may pause the current work to investigate and ask; it does not expand the
  original task's mutation or publication authority.
- Returning to an already-authorized parent task after clarification is not a
  new phase and may resume automatically.
- A new specification artifact, prototype mutation, ticket publication,
  Kanban board, implementation phase, deployment, or cleanup still follows its
  owning skill and approval boundary.
- Never use a recommendation, model confidence, or common practice as a
  substitute for a required human decision.
- Never ask the human to perform discoverable evidence gathering.
- Stop immediately on a user stop signal.

## Manual `/wf` behavior

When invoked without arguments, use the current conversation and active task.
When invoked with a named source or decision, bind the flow to that object.

1. Identify the current destination and the earliest unresolved ambiguity that
   can affect it.
2. Start at LIGHT unless FULL persistence criteria are already met.
3. Run the routing procedure below.
4. Ask at most one human question at a time.
5. After the answer, re-evaluate the route and either resume the already-
   authorized parent task or return the next bounded blocker.

Manual `/wf` does not itself authorize FULL artifacts, prototype code, ticket
publication, Kanban, or implementation.

## Routing procedure

### 1. Contain before acting

Before any action affected by the ambiguity:

- state the uncertain item internally;
- identify what would differ between plausible answers;
- pause only the affected mutation or output;
- preserve unrelated safe progress when it cannot bias the decision.

### 2. Investigate discoverable facts

Use direct tools and authoritative local/primary sources first. For a named
Wayfinder `EVIDENCE` ticket, or when durable evidence is needed, load
Wayfinder's `references/evidence-handler.md` and follow
`wayfinder-evidence-v1`.

Classify the result:

- **fact resolved** — cite the evidence and continue;
- **fact conflicted/stale/unsupported** — expose the uncertainty and its effect;
- **human value remains** — route to Bounded Grilling;
- **interaction required** — route to Prototype;
- **dependent fog remains** — route to Wayfinder.

### 3. Ask one human decision

For a human-owned scope, preference, authority, trade-off, or acceptance value,
invoke Bounded Grilling under WF standing authority.

Use `clarify` and provide:

- a concise self-contained decision context;
- the one decision that currently blocks progress;
- the relevant verified facts and constraints;
- one recommendation and its principal trade-off;
- up to four materially distinct options when options help;
- free-form `Other` automatically supplied by the interface.

Never put selectable choices only in prose. Never batch independent questions.
If the answer is ambiguous, ask only the smallest follow-up for that same
branch.

### 4. Prototype when prose is insufficient

If a state/behavior or UI choice cannot be judged faithfully through words,
return or consume `PROTOTYPE_REQUIRED`, then invoke `/prototype` under its
artifact-authority, smoke-verification, evidence, human-reaction, and
no-promotion gates.

A prototype ticket or standalone prototype cannot resolve from a model-written
recommendation. It needs actual human reaction and one accepted decision.

### 5. Escalate dependent uncertainty

Use Wayfinder LIGHT when the ambiguity is bounded to the current session and no
durable map is warranted. Use Wayfinder FULL only when its existing hard
signals and artifact authority are satisfied, such as multi-session lifetime,
three or more dependent route decisions, concurrent actors, or required durable
recovery.

Automatic WF invocation does not by itself authorize FULL persistence. If a
safe project root/backend or artifact authority is missing, ask before creating
it.

### 6. Compile and decompose only when earned

- Use To-Spec after the route is settled and a requirements/acceptance contract
  is useful or already authorized.
- Use `/to-tickets` only when the user explicitly asks to decompose one named
  approved source snapshot.
- Ticket publication remains a second approval bound to the exact graph and
  backend.
- Plan and Kanban remain downstream, separately authorized consumers.

## Multiple uncertainties

Order by dependency and risk:

1. safety, authority, target, and irreversible-action uncertainty;
2. destination, scope, and acceptance;
3. architecture/execution class and external dependencies;
4. interaction/prototype decisions;
5. reversible local details.

Ask one question, wait, persist or carry the answer, then recompute. Do not
present a questionnaire or silently answer later items. If several facts are
independently discoverable, research them in parallel before asking the next
human decision.

## Handoff

When a durable handoff is useful, return:

```yaml
schema: wf-route-v1
trigger: manual | automatic
parent_task: <current authorized task or none>
uncertainty: <one earliest unresolved item>
classification: fact | human-decision | prototype | dependent-fog | resolved
handler: evidence | bounded-grilling | prototype | wayfinder-light | wayfinder-full | to-spec | to-tickets
status: RESOLVED | QUESTION_PENDING | BLOCKED | ROUTED
source_or_decision_handles: []
resume_authority: existing-parent-task | none
persistence: none | pending | confirmed
```

Do not create this packet merely for ceremony in a tiny in-session question.
Use it when another session/agent must recover the route or when an owning skill
already requires persistence.

## Completion

WF is complete for the current ambiguity when exactly one holds:

- evidence resolved it and the parent task can continue;
- one human question is pending through `clarify`;
- one accepted human answer is returned/persisted and the parent task can
  resume;
- one prototype or Wayfinder route is explicitly returned;
- a named authority/evidence blocker prevents safe progress.

WF does not claim the whole parent task is complete.

## Common pitfalls

1. **Assuming to preserve momentum.** Pause the affected action and route the
   ambiguity.
2. **Asking for facts.** Investigate before questioning the human.
3. **Artificial uncertainty.** Do not ask when the request and evidence support
   one obvious interpretation.
4. **Question batching.** One blocking human decision at a time.
5. **Recommendation as consent.** A recommended default is not an accepted
   value.
6. **Automatic FULL escalation.** Persist only with an earned need and artifact
   authority.
7. **Pipeline autopilot.** To-Spec, To-Tickets publication, Plan, Kanban, and
   implementation retain their own invocation/approval gates.
8. **Failure to resume.** After clarification, return to the already-authorized
   parent task without demanding redundant approval.

## Verification checklist

- [ ] WF was manually invoked or a genuine route-affecting ambiguity existed.
- [ ] The affected action paused before an assumption became a side effect.
- [ ] Discoverable facts were investigated with authoritative evidence.
- [ ] Human values were not answered by the model.
- [ ] At most one human question was active.
- [ ] Any `clarify` prompt contained context, recommendation, and trade-off.
- [ ] Prototype and FULL Wayfinder routes respected artifact authority.
- [ ] To-Tickets decomposition/publication and downstream execution remained
      separately authorized.
- [ ] The parent task resumed only within its existing authority.
- [ ] No artificial question or unauthorized pipeline step was introduced.
