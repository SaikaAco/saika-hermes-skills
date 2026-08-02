# Wayfinder Prototype Handler

Adapted from Matt Pocock's MIT-licensed
[`prototype`](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype).
Copyright (c) 2026 Matt Pocock. This Hermes adaptation adds explicit artifact
authority, smoke verification, human-resolution gates, evidence separation,
and no automatic implementation.

## Purpose

A prototype is **throwaway, runnable decision evidence**. It answers one
question that prose cannot settle at sufficient fidelity. It is not an early
production implementation and does not create authority to ship its code.

Use only for a Wayfinder `PROTOTYPE` / `HITL` ticket or an explicit user
request to prototype. The ticket cannot resolve until a human has interacted
with or reviewed the artifact and accepted a decision.

## Required input

Require:

- Wayfinder map and prototype ticket handles when invoked by Wayfinder;
- destination and exactly one decision question;
- direct dependencies and standing constraints;
- artifact authority and an allowed location;
- active project runtime and task-runner conventions when project-local;
- human decision owner.

Return `BLOCKED` when artifact creation, runtime choice, or project scope is
materially ambiguous. Do not silently convert planning authority into build or
repository-mutation authority.

## Choose one branch

### LOGIC — state, behavior, or data-shape question

Use when the decision is best answered by pressing actions and observing state:

- business rules or legal/illegal transitions;
- reducer, state-machine, API-shape, or data-model uncertainty;
- difficult edge cases that are hard to judge on paper.

Build the smallest interactive terminal program that:

1. states the exact question at the top of its README or source;
2. uses the host project's language/runtime when one is clear;
3. isolates the decision-bearing logic behind a small pure interface;
4. renders the complete relevant state after every action;
5. exposes concise actions and a quit path;
6. uses in-memory state unless persistence itself is the question;
7. starts with one documented command.

Good logic shapes include a pure reducer, explicit state machine, small pure
function set, or a state-owning module with a narrow method surface. The
interactive shell is disposable; no prototype code is presumed production
quality.

### UI — visual hierarchy, layout, navigation, or interaction question

Use when the human needs to compare concrete spatial alternatives.

Default to **three** structurally different variants; allow two when the space
is genuinely binary and cap at five. Variants must differ in layout,
information hierarchy, or primary affordance—not merely color or copy.

Prefer, in order:

1. an authorized development-only variant mounted in the closest existing page
   while preserving its real read-only data/context;
2. an authorized clearly named prototype route following the project's routing
   convention;
3. a self-contained scratch prototype when project mutation is not authorized
   or project fidelity is unnecessary.

Provide a visible development-only switcher and stable variant handles, such as
`?variant=A`, plus keyboard/click controls where appropriate. Never point a
prototype at production mutations. Stub writes and dangerous actions.

A burnable visual brief is not a substitute: briefs explain; prototypes let the
human interact and choose.

## Shared rules

1. **One question.** If the artifact starts answering a second material
   question, open or recommend another ticket instead of expanding it.
2. **Clearly throwaway.** Name and label the artifact so no reader can mistake
   it for production code.
3. **Authorized placement.** Prefer the active project's existing convention.
   If none is authorized, use a profile/workspace scratch prototype directory
   and report its lifecycle. Do not put project-specific source under an
   unrelated shared workspace.
4. **One command to run.** Use the existing task runner when authorized; do not
   add a package manager or heavy dependency merely for the prototype.
5. **Minimal fidelity, not polish.** Skip production abstractions, broad error
   handling, analytics, deployment, and production test suites.
6. **Measurable completion.** Run a smoke check proving the documented command
   starts and the decision-bearing interaction/variant path works. "No
   production tests" never means "unexecuted artifact."
7. **No real side effects.** Use memory, fixtures, scratch files, or a clearly
   disposable local database. Never use production credentials or data writes.
8. **Respect the active IDE contract.** If IDE work is user-mediated, provide a
   scoped implementation prompt and independently inspect the resulting diff
   and smoke-test output; never drive the IDE in violation of that policy.
9. **No automatic promotion.** A selected prototype direction must pass through
   the authorized specification/implementation workflow. Do not fold it into
   real code, commit it to the main branch, publish it, or deploy it merely
   because the ticket resolved.
10. **No silent deletion.** Preserve evidence first. Cleanup or branch deletion
    follows project and workspace approval policy.

## Human reaction loop

1. Deliver the run command or URL/variant handles and name the exact decision.
2. Let the human drive or inspect the artifact.
3. Record feedback without converting ambiguous reactions into acceptance.
4. Iterate only within the same question when the human requests another case
   or variant.
5. Normalize the accepted outcome, rejected alternatives, rationale, and new
   constraints.
6. If no option is accepted, return `BLOCKED` or keep the ticket open; a
   runnable artifact alone is not resolution.

## Evidence lifecycle

Before resolution classify every output:

- **prototype evidence** — source, branch/ref, screenshots, run instructions;
- **accepted decision** — human-owned value and rationale for the ticket;
- **durable shared context** — design convention, vocabulary, or constraint
  later sessions must load;
- **disposable intermediate** — generated files not needed to understand the
  choice;
- **potential implementation** — code that may inspire production work but has
  no implementation authority.

Prototype evidence may remain on a stable isolated branch or authorized local
artifact path. Durable shared context must be reconciled into its canonical
location before closure. Never strand durable context on the prototype branch.

For UI decisions, preserve enough visual evidence to understand the chosen and
materially rejected variants. A line such as "chose B" is insufficient when B
cannot be reconstructed. For logic decisions, preserve the decisive state
traces or transition cases and the validated interface shape.

If persistence or reconciliation fails, keep the ticket open and return
`RECONCILE_REQUIRED`.

## Handoff schema

Return:

```yaml
schema: wayfinder-prototype-v1
outcome: RESOLVED | BLOCKED | RECONCILE_REQUIRED
ticket_handle: <authoritative Wayfinder ticket>
branch: LOGIC | UI
question: <one decision question>
artifact_handle: <stable path/URL/ref>
run_command_or_url: <verified command or URL>
smoke_verification: passed | failed
human_owner: <decision owner>
human_reaction: <concise observed feedback>
accepted_decision: <value or null>
rejected_alternatives: []
rationale: <concise rationale or blocker>
constraints_and_negative_requirements: []
durable_context_handles: []
prototype_evidence_handles: []
persistence: confirmed | pending
implementation_authority: none | separately-authorized
```

`RESOLVED` requires:

- `smoke_verification: passed`;
- a stable, resolvable artifact handle;
- actual human reaction and an unambiguous accepted decision;
- materially rejected alternatives and rationale when applicable;
- reconciled durable context;
- `persistence: confirmed`.

Wayfinder owns ticket/map mutation after consuming the handoff.

## Verification checklist

- [ ] The handler answered one explicit LOGIC or UI question.
- [ ] Artifact placement and any project mutation were authorized.
- [ ] The prototype was clearly marked throwaway and had no real side effects.
- [ ] The documented command/URL passed a real smoke check.
- [ ] The human interacted with or inspected the artifact.
- [ ] Accepted and rejected alternatives are recoverable from durable evidence.
- [ ] Shared context is reconciled; disposable code is not presented as current
      architecture.
- [ ] The handoff conforms to `wayfinder-prototype-v1`.
- [ ] No production implementation, commit to main, publication, deployment,
      or cleanup occurred without separate authority.
