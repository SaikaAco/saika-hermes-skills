---
name: prototype
description: "Use when the user explicitly asks for a prototype or when a named Wayfinder PROTOTYPE ticket needs runnable logic/UI decision evidence. Builds one throwaway artifact, obtains human reaction, and never promotes it to production automatically."
version: 1.0.0
author: "SaikaAco with Hermes Agent, adapted from Matt Pocock"
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [prototype, logic, ui, decision-evidence, wayfinder, hitl]
    related_skills: [wayfinder, bounded-grilling, burnable-visual-briefs, to-spec]
    upstream: "https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype"
---

# Prototype

## Lineage and canonical protocol

This is an MIT-licensed Hermes entry point adapted from Matt Pocock's public
[`prototype`](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype).

The complete upstream MIT notice is preserved in
[`references/third-party-notices.md`](references/third-party-notices.md).

The canonical shared procedure and handoff schema live in Wayfinder's
`references/prototype-handler.md`. Load that reference with `skill_view` and
follow it exactly. Keeping the protocol there gives standalone prototypes and
Wayfinder `PROTOTYPE` tickets one source of truth.

## Invocation and input

Run only when:

- the user explicitly asks to prototype one decision; or
- one existing named Wayfinder `PROTOTYPE` / `HITL` ticket invokes it.

For a Wayfinder invocation, require its map and ticket handles and return the
canonical `wayfinder-prototype-v1` handoff.

For a standalone invocation, establish the equivalent bounded input before
building:

- destination;
- exactly one decision question;
- `LOGIC` or `UI` branch;
- constraints and direct dependencies;
- artifact authority and allowed location;
- human decision owner.

Use `ticket_handle: standalone` in the handoff when no authoritative ticket
exists. Do not create a Wayfinder package or tracker item merely to supply an
ID.

## Procedure

1. Load `wayfinder`, then load
   `references/prototype-handler.md` through `skill_view`.
2. Apply its authority, placement, branch, smoke-verification, human-reaction,
   evidence-lifecycle, persistence, and no-promotion gates.
3. Build only the smallest runnable artifact needed to answer the named
   question.
4. Execute the documented command or URL path and verify the decision-bearing
   interaction or variants.
5. Deliver the artifact to the human and collect actual reaction. A runnable
   artifact without reaction remains unresolved.
6. Return the complete `wayfinder-prototype-v1` handoff.
7. Stop. Production specification, implementation, commit, publication,
   deployment, and cleanup require their own authority.

## Boundaries

- A prototype is decision evidence, not production implementation.
- A burnable visual brief may explain alternatives but cannot replace an
  interactive prototype when behavior or interaction is the question.
- Do not drive a user-mediated IDE; provide a scoped prompt and independently
  inspect/verify the resulting artifact when that policy applies.
- Do not install dependencies, mutate production data, merge prototype code,
  or delete evidence without separate approval.

## Verification

- [ ] Invocation was explicit or attached to one named prototype ticket.
- [ ] The canonical Wayfinder prototype handler was loaded.
- [ ] One LOGIC or UI question, owner, authority, and location were explicit.
- [ ] The artifact passed a real smoke check.
- [ ] Human reaction and accepted/rejected alternatives were preserved.
- [ ] Durable context and prototype evidence have resolvable handles.
- [ ] The handoff conforms to `wayfinder-prototype-v1`.
- [ ] No production promotion or unauthorized side effect occurred.
