# Acknowledgments

This repository is curated by SaikaAco with Hermes Agent.

## Matt Pocock’s Wayfinder, To-Spec, Prototype, and To-Tickets

The following packages are MIT-licensed adaptations of Matt Pocock’s public skills:

- [`skills/wayfinder/SKILL.md`](skills/wayfinder/SKILL.md), adapted from [Matt Pocock’s Wayfinder](https://github.com/mattpocock/skills/tree/main/skills/engineering/wayfinder);
- [`skills/to-spec/SKILL.md`](skills/to-spec/SKILL.md), adapted from [Matt Pocock’s To-Spec](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-spec);
- [`skills/prototype/SKILL.md`](skills/prototype/SKILL.md) and [`skills/wayfinder/references/prototype-handler.md`](skills/wayfinder/references/prototype-handler.md), adapted from [Matt Pocock’s Prototype](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype);
- [`skills/to-tickets/SKILL.md`](skills/to-tickets/SKILL.md), adapted from [Matt Pocock’s To-Tickets](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-tickets).

The adapted Wayfinder retains destination, map, decision-ticket, frontier, fog, and one-ticket-at-a-time concepts. To-Spec retains synthesis of settled context into a specification without another interview. Prototype retains runnable throwaway decision artifacts. To-Tickets retains tracer-bullet and vertical-slice decomposition into implementation tickets.

The Saika/Hermes adaptations add adaptive LIGHT/FULL invocation, typed handler and handoff contracts, Hermes metadata, authority and persistence gates, source traceability, coverage checks, recovery states, negative requirements, acceptance evidence, and explicit boundaries against silent publication, production promotion, or implementation.

These adaptations are maintained independently. Matt Pocock has not reviewed or endorsed them. His complete 2026 MIT copyright and permission notice is preserved in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Jesse Vincent’s Superpowers Writing Plans

[`skills/plan/SKILL.md`](skills/plan/SKILL.md) is an MIT-licensed adaptation of Jesse Vincent’s [Superpowers `writing-plans`](https://github.com/obra/superpowers/tree/3dcbd5c4b48e02263fbf4a3c01e3fe4f81d584d9/skills/writing-plans).

The adaptation retains comprehensive implementation planning, exact paths, task decomposition, test-first examples, DRY/YAGNI discipline, interface contracts, placeholder checks, self-review, and execution handoff. It adds strict Hermes plan-only authority, backend-relative `.hermes/plans/` storage, project mutation boundaries, task right-sizing without minute quotas, conditional execution routes, and explicit separation between planning and implementation authorization.

This adaptation is maintained independently. Jesse Vincent and the Superpowers project have not reviewed or endorsed it. The complete 2025 MIT copyright and permission notice is preserved in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Hermes Agent

The skills target the public [Hermes Agent](https://github.com/NousResearch/hermes-agent) skill format and operating model. Hermes Agent is maintained by Nous Research and its contributors. This community repository is not an official Nous Research distribution.

## Bounded Grilling

`bounded-grilling` was informed by the broader decision-interview pattern and by Matt Pocock's public [`grilling`](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) and [`grill-me`](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) work.

The published skill is a deliberately bounded adaptation: it limits opening decisions, requires an evidence/value gate, separates interviewing from persistence, and forbids automatic implementation or publication.

## Artifact lifecycle

`burnable-visual-briefs` and `hermes-workspace-hygiene` were developed from Saika/Hermes operating practice. They pair temporary, diagram-first communication with manifest-bound, approval-gated artifact cleanup.

## Context Budget Orchestration

`context-budget-orchestration` is an original Saika/Hermes operational synthesis. It combines proportional phase budgeting, context containment, bounded delegation contracts, retry circuit breakers, recovery ledgers, and parent-side verification. Its public edition removes operator-specific profile, provider, billing, and model policy.

## Hermes Backup and Recovery

`hermes-backup-recovery` is an original Saika/Hermes method developed from operating encrypted Hermes backups and clean-room recovery drills. It combines a secret-free Git control-plane layer with atomic encrypted Restic snapshots, WAL-safe SQLite capture, exact exclusion/completion manifests, retention gates, and verified restore-before-cutover procedures. Public instructions omit concrete storage endpoints, schedules, credentials, and personal source roots.

## Other packages

`skill-lifecycle-management`, `kanban-workflows`, and `wf` were developed from practical Hermes skill-maintenance, durable-work orchestration, and ambiguity-routing needs.

Linked projects retain their own names, trademarks, copyrights, and licenses. Inclusion here is attribution, not endorsement.
