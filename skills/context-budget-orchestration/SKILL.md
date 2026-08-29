---
name: context-budget-orchestration
description: "Use when work is multi-step, context-heavy, research-heavy, or delegated. Contains bulky context, phases work, bounds retries, delegates independent reasoning, and reserves capacity for verification."
version: 1.2.0
author: "SaikaAco with Hermes Agent"
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [context-budget, delegation, orchestration, subagents, long-work, verification]
    related_skills: [wayfinder, to-spec, hermes-agent]
---

# Context Budget Orchestration

## Overview

Keep the parent Hermes session effective when a task can expand through tool output, long files, research trails, implementation loops, or multi-agent reasoning.

The method has three layers:

1. **Contain:** keep bulky deterministic material out of the parent context.
2. **Orchestrate:** delegate bounded, independent reasoning with explicit contracts.
3. **Reserve:** stop expanding early enough to verify artifacts and deliver a grounded result.

This skill defines methodology, not permission. It does not authorize paid providers, external side effects, persistent changes, or broader delegation than the user and runtime permit.

## When to use

Use when one or more conditions hold:

- the task has three or more meaningful phases;
- many files, long logs, PDFs, webpages, or past sessions may be involved;
- research, implementation, review, and verification must be coordinated;
- independent subproblems can run in parallel;
- raw tool output would crowd out synthesis;
- the work may continue across sessions;
- the user explicitly requests delegation or subagents.

Use lightly or skip for a quick lookup, a small local edit, one short file, or a deterministic operation whose orchestration overhead exceeds the work. Respect an explicit request not to delegate.

## Context-budget preflight

Before heavy work, state a compact budget:

```markdown
## Context budget
- Task size: small | medium | large | huge
- Parent role: execute | orchestrate | synthesize | verify
- Bulk-output strategy: direct tools | deterministic reduction | subagent summaries | external ledger
- Delegation: none | one bounded child | parallel children | map-reduce
- Verification reserve: what must remain possible before finalization
```

### Size heuristic

| Size | Typical shape | Default response |
|---|---|---|
| Small | no more than two sources/files and a few calls | direct work |
| Medium | several files/sources or commands | batch reads; consider one bounded child |
| Large | broad research, test/build loops, many files | delegate independent reasoning early |
| Huge | repository-wide, multi-phase, or multi-session | external ledger plus map-reduce |

Task shape matters more than raw file count. One enormous log may need containment more than ten tiny files.

## Proportional phase gates

Treat the available interaction/call budget as a phase budget, not a target to consume.

| Budget point | Phase | Required behavior |
|---:|---|---|
| first 10% | Scope and route | Lock endpoint, success criteria, source/tool matrix, delegation choice, and stop conditions. |
| 10–60% | Collect or implement | Batch independent calls, dispatch required children early, and write artifacts incrementally. |
| 60–67% | Close collection | Finish required collection only; start no optional source, feature, or diagnostic branch. |
| 67–75% | Freeze and reconcile | Join required results, resolve contradictions, persist compact state, and stop creating work. |
| final 25% | Verify and deliver | Run acceptance checks, bounded repair, and final synthesis. |

If the runtime exposes no explicit budget, estimate from task size and expected output. Preserve enough capacity to rerun failed checks and report honestly.

### Phase contracts

- One phase should have one dominant contract: discovery, test design, implementation, rollout, visual QA, or final verification.
- If the request materially expands, finish the current phase and record state before absorbing adjacent work.
- Dispatch required children during planning or early collection, never as a last-minute substitute for verification.
- Do not synthesize a conclusion that depends on a child until its result arrives and the parent verifies its evidence handles.
- If required work cannot fit inside the reserve, stop optional branches and continue in a fresh phase rather than claiming completion.

## Choose the cheapest correct surface

| Work type | Preferred surface |
|---|---|
| one lookup, edit, command, or API call | direct tool |
| deterministic filtering, counting, parsing, or aggregation | programmatic reduction |
| independent evidence collection or judgment-heavy analysis | bounded subagent |
| durable waiting, retries, or scheduled work | background process, scheduler, or task system |
| user decision with material trade-offs | concise decision brief and clarification |

Do not spawn agents merely to move mechanical output elsewhere. Do not read large raw outputs into the parent when line-limited reads, search, or reduction can answer the question.

## Delegation decision rules

Delegate when a subtask is independent, bulky, or benefits from fresh context. Keep it in the parent when tight coordination, user interaction, or a small local change makes delegation slower or less reliable.

Good targets:

- codebase reconnaissance with file/line handles;
- parallel evidence collection across distinct source classes;
- independent design alternatives under identical constraints;
- diff or plan review after an artifact exists;
- isolated failure triage;
- long-document synthesis;
- adversarial verification of a material claim.

Poor targets:

- one command or simple lookup;
- tiny edits;
- tasks requiring user clarification;
- durable work that must survive the current session;
- external side effects the parent cannot independently verify.

### Reasoning effort

Use the lowest effort that can reliably satisfy the contract. Escalate after failed verification, material uncertainty, conflicting evidence, missed constraints, or substantial repair—not merely because a higher tier exists. Respect runtime floors, ceilings, and provider policy.

Mechanical work belongs in tools, not a low-effort reasoning child. High effort is never a substitute for a clear endpoint, lean context, or verification.

## Standard subagent contract

Every delegated task should include:

- **Goal:** exact deliverable.
- **Context:** only necessary facts, paths, constraints, and acceptance criteria.
- **Boundaries:** what not to modify, assume, or contact.
- **Output schema:** concise result with verifiable handles.
- **Budget:** no raw logs or transcript unless essential.

Recommended response:

```markdown
## Result
<one to three sentences>

## Evidence / handles
- <file and line range, URL, command, test, artifact, or ID>

## Key details
- <up to five bullets>

## Risks / uncertainty
- <remaining uncertainty>

## Suggested next step
- <one action>
```

For implementations and reviews, require files touched or inspected, tests run or recommended, exact blockers, and no success claim without a handle the parent can verify.

## Parent verification gate

A subagent summary is a lead, not proof. Before reporting completion, the parent must verify material claims and external side effects against the original surface:

- read back changed files;
- inspect diffs;
- run tests/builds/validators;
- fetch published URLs;
- compare identifiers or bytes where appropriate;
- distinguish “reported by child” from “verified by parent.”

The parent owns the final synthesis and decision.

## Circuit breakers

- Retry the same failed GUI, API, browser, or command surface at most once unless the second attempt uses new evidence and a materially different hypothesis.
- After that, switch surface: DOM/accessibility/direct file/API before more coordinate clicking; deterministic probes before visual guesses; exported data before private-history pagination.
- For bounded background processes, use completion notification rather than repeated polling when available.
- Batch screenshots, viewport checks, and console inspection into one verification pass per implemented state.
- Stop broad collection when outputs repeat, contradict without new evidence, or no longer change the decision.

## Hard first-attempt sizing and retry embargo

Optimize for one robust run rather than repeated cheap attempts. When elapsed
time matters more than token economy, spend the necessary reasoning budget in
the first attempt through deterministic reduction and independently
completable parallel shards.

### Mandatory first-attempt sizing record

Before every nontrivial delegation, record internally:

- the number and total expected bytes of named input artifacts;
- the number of independent reasoning domains;
- expected tool or API calls;
- serial dependencies;
- target wall time per shard;
- deterministic work that should remain in the parent or a programmatic tool.

A single reasoning child is admissible only when all of these are true:

- the task has one reasoning domain;
- it names no more than four input artifacts;
- total expected input is no more than 100 KiB;
- it requires no repository-wide or full-tree search;
- it expects no more than eight tool or API calls;
- it does not combine discovery, derivation, and review in one worker.

Crossing any threshold requires a parent-written task DAG and either direct
parallel children or a bounded orchestrator. Keep every shard independently
completable and target roughly four to eight minutes per reasoning shard.

### Material expansion invalidates strategy reuse

A previously successful strategy applies only to materially comparable scope.
Do not reuse it unchanged when:

- a new reasoning domain is added;
- named artifacts or expected bytes grow by more than twofold;
- discovery expands into derivation, implementation, or adversarial review;
- a second independent verdict is required;
- expected calls cross the single-child ceiling.

When strategy or precedent identifiers are available, material expansion
requires a new task class or an explicitly scope-qualified strategy. A pass on
a smaller task does not validate the same topology for a larger one.

### First-run resource preference

When the user prioritizes elapsed time over token economy:

- reduce deterministic inputs before delegation;
- dispatch every independent required shard in the first attempt;
- use higher reasoning effort for review or architecture and reserve the
  highest permitted effort for a decisive shard whose complexity or failed
  verification warrants it;
- give every shard exact artifacts, output schema, stop conditions, and a word
  cap;
- preserve sibling results independently so one timeout cannot hide them;
- prefer one bounded, adequately resourced fan-out over serial trial and error.

### Retry embargo and acceptance test

After any timeout, do not dispatch another attempt until all are true:

- the prior handle is verified no longer live;
- available call count, timeline, partial output, and kill condition are
  inspected;
- useful artifacts and sibling results are salvaged;
- the cause is classified;
- a compact postmortem and revised task DAG exist;
- the new attempt changes scope or topology in a way that addresses the
  classified cause.

For that task, quarantine the timed-out strategy identifier, worker count,
serial-dependency structure, and any materially equivalent contract. More
effort or a longer prompt is not a topology change.

Before retrying, the parent must be able to support this sentence with
evidence:

```text
The previous attempt failed because <classified cause>; this attempt removes that cause by <material DAG or topology change>.
```

If the sentence cannot be supported, do not retry.

## Timeout and exhaustion postmortem

A timeout or exhausted budget is diagnostic evidence, not permission to retry
the same topology with more effort or a longer wall clock. Apply the sizing and
retry embargo above, then use this diagnostic workflow.

1. **Stop and inspect.** Verify that the previous worker or process is no
   longer live. Inspect the parent and child timelines, actual fan-out,
   longest tool or model calls, context growth, partial outputs, and the exact
   timeout or exhaustion condition.
2. **Salvage completed work.** Preserve useful sibling results, artifacts,
   tests, and evidence handles. One failed shard does not invalidate successful
   independent work.
3. **Classify the cause.** Distinguish oversized scope, serial dependency,
   unbounded collection, external latency, deterministic test duration,
   provider failure, and a genuine concurrency or call-budget cap.
4. **Write the retry DAG.** Before another orchestrated attempt, define bounded
   shards, dependencies, exact source or file scopes, output contracts, stop
   conditions, and verification owners.
5. **Retry only incomplete shards.** Prefer independently completable fan-out
   so one timeout cannot hide or cancel successful siblings. Avoid broad
   repository-wide scans unless their scope and stopping rule are explicit.
6. **Use orchestrators for coordination.** Supply the task DAG, existing
   evidence, contradictions, and bounded decisions. Do not place discovery,
   implementation, testing, and review serially behind one worker deadline.
7. **Separate execution surfaces.** Assign one implementation owner per
   overlapping file cluster; use deterministic tools for builds and tests;
   freeze the artifact before independent review.
8. **Audit the actual topology.** Compare requested versus dispatched workers,
   require evidence handles, verify writes and tests at the parent, and treat
   omitted or unverified work as incomplete.
9. **Escalate surgically.** Raise effort or narrow the contract only for the
   failed shard. Increase global timeout, concurrency, or budget only when the
   postmortem shows that resource limit was causal.

Never treat silence, an absent result, a timeout notice, or an exhaustion
summary as success. Record the repaired topology in the project ledger when
the same task class may recur.

## Fan-out / fan-in patterns

### Scout → implement → verify

1. Parent locks endpoint and acceptance criteria.
2. Scout finds relevant files, APIs, tests, and pitfalls.
3. Parent or bounded implementer makes the smallest correct change.
4. Independent reviewer checks the artifact.
5. Parent runs real verification and reports grounded results.

### Map-reduce research

1. Parent defines question, source hierarchy, and freshness rule.
2. Children collect evidence from separate source classes or subtopics.
3. Parent deduplicates, checks contradictions, and labels confidence.
4. Parent writes the synthesis and preserves durable evidence when required.

### Candidate alternatives

Give independent children identical constraints. Compare options by correctness, simplicity, risk, testability, and operational cost. Prefer the smallest design that satisfies the endpoint.

### Independent verifier

Provide only the claim, artifact handles, and success criteria. Ask the verifier to find missing evidence, tests, or constraints. The parent checks every decisive handle.

## External state ledger

For huge or multi-session work, keep a compact factual ledger under the active workspace, for example:

```text
.hermes/state/<task-slug>.md
```

Suggested shape:

```markdown
# <Task>

## Endpoint
<what done means>

## Current state
- <facts that survive context resets>

## Decisions
- <decision and reason>

## Artifacts / evidence
- <path or URL and purpose>

## Verification
- <command/check and last real result>

## Open blockers
- <unresolved items only>

## Next action
- <one action>
```

Keep the ledger short. It is recovery state, not a transcript or log dump.

## Context-pressure recovery

When the parent starts repeating calls, losing constraints, or depending on memory of a long transcript:

1. stop broad reading and optional branches;
2. finish or safely pause the current phase;
3. update the state ledger;
4. delegate only isolated missing facts;
5. resume from the ledger in a fresh phase or allow compression as a backstop;
6. never turn a fallback summary into an unverified completion claim.

## Common pitfalls

1. **Over-delegation:** children add latency and noise to tiny tasks.
2. **Under-delegation:** broad raw reading destroys parent context quality.
3. **Late delegation:** required results arrive after the verification window.
4. **Raw-summary bloat:** bounded tasks still need concise output contracts.
5. **Unverified side effects:** child reports do not prove publication or mutation.
6. **Transcript as database:** durable projects need external recovery state.
7. **Maximal effort everywhere:** expensive reasoning does not repair unclear scope.
8. **Retry loops:** repeated use of a failed surface without new evidence is not progress.
9. **Optional-branch creep:** collection expands until no verification reserve remains.
10. **Permission drift:** methodology does not grant provider, payment, or external-action authority.
11. **Precedent overreach:** a topology that passed for a small task is not evidence that it fits materially expanded scope.

## Verification checklist

- [ ] Endpoint, success criteria, stop conditions, and reserve were stated before heavy work.
- [ ] Deterministic bulk output was reduced to decision-relevant summaries before parent synthesis.
- [ ] Required independent reasoning was delegated early with bounded contracts.
- [ ] User and runtime delegation/provider limits were respected.
- [ ] Every nontrivial delegation was sized before dispatch; single-child work stayed within all ceilings or used a parent-written DAG.
- [ ] Same-surface retries were capped and switched after failure.
- [ ] Every timeout retry passed the embargo and changed topology or scope to remove the classified cause.
- [ ] Required child results arrived before synthesis.
- [ ] Material claims and side effects were verified by the parent.
- [ ] New branches froze before the final verification phase.
- [ ] Huge or multi-session work has a compact state ledger.
- [ ] Final claims cite tool output, files, URLs, tests, or user-provided evidence.
