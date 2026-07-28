# Acknowledgments

This repository is curated by SaikaAco with Hermes Agent.

## Matt Pocock’s Wayfinder and To-Spec

The following packages are MIT-licensed adaptations of Matt Pocock’s public skills:

- [`skills/wayfinder/SKILL.md`](skills/wayfinder/SKILL.md), adapted from [Matt Pocock’s Wayfinder](https://github.com/mattpocock/skills/tree/main/skills/engineering/wayfinder);
- [`skills/to-spec/SKILL.md`](skills/to-spec/SKILL.md), adapted from [Matt Pocock’s To-Spec](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-spec).

The adapted Wayfinder retains the destination, map, decision-ticket, frontier, fog, and one-ticket-at-a-time concepts. The adapted To-Spec retains the synthesis of already-settled context into a specification without another interview.

The Saika/Hermes adaptations add adaptive LIGHT/FULL invocation, Hermes metadata, authority and persistence gates, source traceability, coverage checks, recovery states, negative requirements, acceptance evidence, and explicit boundaries against silent publication or implementation.

These adaptations are maintained independently. Matt Pocock has not reviewed or endorsed them. His complete 2026 MIT copyright and permission notice is preserved in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Hermes Agent

The skills target the public [Hermes Agent](https://github.com/NousResearch/hermes-agent) skill format and operating model. Hermes Agent is maintained by Nous Research and its contributors. This community repository is not an official Nous Research distribution.

## Bounded Grilling

`bounded-grilling` was informed by the broader decision-interview pattern and by Matt Pocock's public [`grilling`](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) and [`grill-me`](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) work.

The published skill is a deliberately bounded adaptation: it limits opening decisions, requires an evidence/value gate, separates interviewing from persistence, and forbids automatic implementation or publication.

## Artifact lifecycle

`burnable-visual-briefs` and `hermes-workspace-hygiene` were developed from Saika/Hermes operating practice. They pair temporary, diagram-first communication with manifest-bound, approval-gated artifact cleanup.

## Context Budget Orchestration

`context-budget-orchestration` is an original Saika/Hermes operational synthesis. It combines proportional phase budgeting, context containment, bounded delegation contracts, retry circuit breakers, recovery ledgers, and parent-side verification. Its public edition removes operator-specific profile, provider, billing, and model policy.

## Other packages

`skill-lifecycle-management` and `kanban-workflows` were developed from practical Hermes skill-maintenance and durable-work orchestration needs.

Linked projects retain their own names, trademarks, copyrights, and licenses. Inclusion here is attribution, not endorsement.
