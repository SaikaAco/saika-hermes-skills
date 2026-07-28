---
name: plan
description: "Use when the user wants an actionable implementation plan instead of execution. Produces a project-local markdown contract with exact paths, interfaces, tests, constraints, reviewable tasks, and no mutation beyond the plan file."
version: 2.1.0
author: "SaikaAco with Hermes Agent, adapted from Jesse Vincent's Superpowers"
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [planning, plan-mode, implementation, workflow, design, documentation]
    related_skills: [wayfinder, to-spec, context-budget-orchestration]
    upstream: "https://github.com/obra/superpowers/tree/3dcbd5c4b48e02263fbf4a3c01e3fe4f81d584d9/skills/writing-plans"
---

# Hermes Plan Mode

## Lineage

This is an MIT-licensed adaptation of Jesse Vincent's Superpowers
[`writing-plans`](https://github.com/obra/superpowers/tree/3dcbd5c4b48e02263fbf4a3c01e3fe4f81d584d9/skills/writing-plans), reviewed at upstream commit `3dcbd5c4b48e02263fbf4a3c01e3fe4f81d584d9`.

It retains comprehensive implementation planning, exact file paths, task decomposition, test-first examples, DRY/YAGNI discipline, explicit commands and expected results, interface contracts, placeholder checks, self-review, and execution handoff.

The Hermes adaptation adds strict plan-only authority, backend-relative `.hermes/plans/` storage, project mutation boundaries, context-aware inference, task right-sizing without minute quotas, conditional execution routes, and explicit separation between planning and implementation authorization.

This adaptation is independently maintained and is not endorsed by Jesse Vincent or the Superpowers project. The complete upstream MIT notice is preserved in the repository's `THIRD_PARTY_NOTICES.md`.

## Core behavior

Use this skill when the user wants a plan rather than implementation.

For this invocation:

- inspect the project and requirements read-only as needed;
- do not implement code;
- do not edit project files except the approved plan markdown file;
- do not run mutating project commands, commit, push, deploy, or contact external systems;
- save one actionable markdown plan under the active project;
- report the saved path and stop unless execution is separately authorized.

A plan is an execution contract, not execution authority. Creating it does not authorize the changes it describes.

## When to use

Use when:

- the user explicitly asks for a plan or invokes plan mode;
- settled requirements need implementation decomposition;
- a multi-step change needs exact files, interfaces, tests, and sequencing;
- work will be delegated and each implementer needs a self-contained task;
- implementation risk justifies design and verification review before mutation.

Do not use when the user asks for immediate execution and the route is already small and clear, or when material requirements remain unsettled. Use Wayfinder for route-changing uncertainty and To-Spec for a durable requirements/acceptance contract before planning implementation.

## Save location

Save the plan with the file tool under:

```text
.hermes/plans/YYYY-MM-DD_HHMMSS-<concise-slug>.md
```

Treat this as relative to the active project/backend working directory. If the runtime or user supplies an exact target path, use it. If no safe project root is identifiable, ask before writing rather than placing the plan in a personal home directory.

Only the plan file is mutable in plan mode. Creating the containing `.hermes/plans/` directory is part of that approved plan-file operation.

## Inputs and scope check

Before writing:

1. identify the implementation goal and acceptance boundary;
2. read settled requirements, specifications, and relevant project instructions;
3. inspect existing code, tests, build commands, and similar features;
4. list material assumptions and unresolved blockers;
5. decide whether the work is one coherent implementation plan.

If the request spans independent subsystems that can ship and verify separately, propose separate plans. Do not hide a portfolio of unrelated work inside one large plan.

If a missing decision would change architecture, scope, or acceptance, stop and resolve it rather than encoding a guess as an implementation task.

## Plan document contract

Every plan starts with:

```markdown
# <Feature> Implementation Plan

**Goal:** <one sentence>

**Architecture:** <two or three sentences describing the minimal approach>

**Tech stack:** <relevant languages, frameworks, tools, and version constraints>

## Global constraints
- <project-wide requirement copied exactly from the accepted source>

## Acceptance evidence
- <test, build, artifact, or observable result proving completion>

---
```

Then include:

- current context and authoritative requirement handles;
- assumptions, exclusions, and unresolved blockers;
- file/responsibility map;
- ordered implementation tasks;
- exact verification commands and expected outcomes;
- migration, rollback, or recovery steps when relevant;
- risks and review gates;
- final end-to-end acceptance check.

## File and interface map

Before decomposing tasks, map the files that will be created or modified and give each one a clear responsibility.

```markdown
## File map

| File | Operation | Responsibility |
|---|---|---|
| `src/example.py` | create | owns one defined behavior |
| `tests/test_example.py` | create | verifies that behavior and edge cases |
| `config/example.toml` | modify | exposes the minimum required configuration |
```

Follow the existing project structure. Do not introduce a broad refactor merely to make the plan aesthetically cleaner. A planned split is justified when it is necessary for testability, safety, or comprehensible ownership.

For neighboring tasks, record exact interfaces:

```markdown
**Interfaces**
- Consumes: `parse_input(raw: str) -> ParsedInput`
- Produces: `build_result(parsed: ParsedInput) -> Result`
- Invariants: <values or behavior later tasks rely on>
```

Names, parameter types, return types, configuration keys, and file formats must remain consistent across the plan.

## Task right-sizing

A task is the smallest unit that:

- produces an independently testable or inspectable result;
- carries a coherent test/change/review cycle;
- can be accepted or rejected without conflating unrelated work;
- is substantial enough to justify its own checkpoint.

Do not use a rigid minute quota. Fold setup, scaffolding, configuration, and documentation into the task whose deliverable needs them. Split a task when a reviewer could meaningfully approve one part while rejecting another, or when failure recovery requires an independent boundary.

Every task should leave the project in a valid, reviewable state unless the plan explicitly labels and contains a temporary migration phase.

## Task structure

Use this shape when relevant:

````markdown
### Task N: <Descriptive result>

**Objective:** <one sentence>

**Requirements covered:** <IDs or source handles>

**Files:**
- Create: `exact/path/to/new_file.py`
- Modify: `exact/path/to/existing.py` — <named section or symbol>
- Test: `tests/exact/path/to/test_file.py`

**Interfaces:**
- Consumes: <exact signatures/data>
- Produces: <exact signatures/data>
- Invariants: <cross-task assumptions>

- [ ] **Step 1: Write the failing test**

```python
def test_specific_behavior():
    result = function(input_value)
    assert result == expected
```

- [ ] **Step 2: Run the focused test and verify the expected failure**

Run: `pytest tests/path/test_file.py::test_specific_behavior -v`
Expected: FAIL because `<specific missing behavior>`

- [ ] **Step 3: Implement the minimum behavior**

```python
def function(input_value):
    return expected
```

- [ ] **Step 4: Run focused and regression checks**

Run: `pytest tests/path/test_file.py -v`
Expected: PASS

Run: `<project regression command>`
Expected: `<grounded success condition>`

- [ ] **Step 5: Review the task diff**

Check: requirement coverage, interface consistency, error paths, and unrelated changes.
````

Use complete code where exact implementation is necessary to prevent guessing. For mechanical or project-specific sections whose content cannot be known until execution, provide the governing interface, algorithm, constraints, and verification—not invented code.

A commit may be recommended after a coherent verified task, but do not require one commit for every tiny action. Follow the project's existing commit policy.

## No placeholders

A plan fails when it delegates essential reasoning to the implementer through phrases such as:

- `TBD`, `TODO`, “implement later,” or “fill in details”;
- “add validation/error handling” without rules and expected behavior;
- “write tests” without named behaviors and verification commands;
- “similar to Task N” when the task must be independently readable;
- references to undefined types, symbols, configuration keys, or requirements;
- plausible-looking commands or expected output that were never inspected.

Unknowns must be explicit blockers, assumptions, or execution-time discovery steps with bounded outcomes. Do not fabricate repository facts to make the plan look complete.

## Testing and verification strategy

Select checks from the actual project:

- focused unit tests;
- integration or contract tests;
- static analysis and formatting;
- build/package commands;
- migrations and rollback verification;
- security/privacy checks;
- visual desktop/mobile QA;
- deployment smoke tests when separately authorized;
- final acceptance evidence mapped to requirements.

A test command must name what a pass proves. If expected output is uncertain because it has not been run, describe the required condition rather than inventing a numeric result.

## Self-review gate

After writing the complete plan, review it against the authoritative requirements:

1. **Coverage:** every requirement and negative requirement maps to a task or explicit exclusion.
2. **Scope:** no task implements unrequested adjacent work.
3. **Placeholders:** no essential reasoning is deferred through vague language.
4. **Interface consistency:** symbols, types, paths, keys, and formats agree across tasks.
5. **Buildability:** an implementer can proceed without guessing hidden project facts.
6. **Verification:** every task and the whole plan have observable acceptance evidence.
7. **Recovery:** migrations, destructive actions, and external side effects have approval and rollback gates.

Fix discovered gaps in the plan file before reporting completion. Do not dispatch implementation as part of self-review.

## Execution handoff

After saving, report:

- the plan path;
- one-sentence approach;
- material assumptions or blockers;
- whether it is ready for implementation.

Offer only execution routes actually available in the runtime, such as:

- execute inline with checkpoints;
- delegate bounded independent tasks under Context Budget Orchestration;
- hand the plan to another authorized implementer.

Do not force a companion skill that is unavailable. Do not begin implementation until the user or existing project authority explicitly authorizes it.

## Common pitfalls

1. **Planning while requirements are moving.** Resolve route-changing uncertainty first.
2. **Plan as hidden execution.** Only the plan file may change in plan mode.
3. **Minute-driven fragmentation.** Reviewable deliverables matter more than arbitrary duration.
4. **Vague completeness.** More words do not replace exact paths, interfaces, and evidence.
5. **Invented repository facts.** Inspect or label uncertainty; never fabricate output.
6. **Unavailable handoff.** Offer only execution methods present in the runtime.
7. **One giant task.** Split where testing, review, or rollback boundaries differ.
8. **One task per keystroke.** Fold mechanical steps into the result they support.
9. **Missing global constraints.** Project-wide rules must not be rediscovered independently by each task.
10. **Automatic implementation.** A completed plan is not authorization to execute it.

## Verification checklist

- [ ] The invocation requested planning rather than execution.
- [ ] Only the plan file and its containing directory were created or modified.
- [ ] The plan is saved under the active project or exact user-supplied path.
- [ ] Goal, architecture, global constraints, exclusions, and acceptance evidence are explicit.
- [ ] File responsibilities and cross-task interfaces are consistent.
- [ ] Tasks are reviewable, independently testable, and not minute-driven fragments.
- [ ] Exact commands and expected conditions come from inspected project evidence.
- [ ] No essential placeholder, undefined symbol, or fabricated result remains.
- [ ] Requirement coverage, scope, verification, and recovery self-review passed.
- [ ] Execution routes are conditional, available, and separately authorized.
