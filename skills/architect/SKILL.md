---
name: architect
description: "Design software interfaces and system structure, or review an existing codebase for architectural improvements. Use when deciding ownership, data flow, or a refactor's shape."
---

# Architect

Make the important structural decisions visible: what each part owns, what callers need to know, and how the design preserves required behavior. Match the work to the request: advice produces a recommendation or sketch; an implementation request includes building and verifying the chosen design. Honor an explicit design checkpoint, while resolving routine choices from available evidence.

## Ground the decision

Trace the relevant callers, data flow, state ownership, dependencies, and tests. Read existing domain terminology and architectural decisions where available. Inspect history when the reason for a boundary affects the decision. Distinguish observed constraints from assumptions; investigate uncertainties that could change the design.

For an open-ended architecture review, use [Review an existing architecture](references/review.md). For a specific change, focus on the affected contracts instead of surveying the entire repository.

## Shape the design

Start from realistic caller usage and required outcomes, including failure behavior. Derive the types, signatures, ownership, and data structures from those examples and the dominant access patterns. Use the project's terminology. An interface includes ordering constraints, errors, configuration, and other obligations callers must understand, beyond its type signature.

Use [Design checks](references/design-checks.md) when choosing or assessing a structural change. Show what complexity the proposed interface hides and what remains with callers. A short sketch may suffice; use a module map or diagram when relationships need explanation. Keep provisional sketches separate from executable source unless scaffolding is part of the requested work.

Compare genuinely different shapes when uncertainty or migration cost makes the comparison useful. Evaluate them against the same requirements and explain the recommendation and accepted tradeoffs. Choose the depth of exploration according to the decision; multiple models or a fixed candidate count are not prerequisites. Any delegation must be available and authorized by the active environment.

## Carry the decision through

For design advice, finish with enough detail to assess the proposal: affected contracts, rationale, consequential unknowns, and a practical implementation and verification path. Choose prose, code sketches, or a visual report to suit the request. Clarify only unresolved decisions that materially affect the outcome.

When implementation is requested, carry the design through callers, compatibility, and verification. Sequence migrations so each stage has a clear behavior to check. Repeated workarounds or leaking invariants are evidence to reconsider the shape; revise the affected design using what implementation revealed. A single edge case does not by itself justify a rewrite.

Complete the requested scope and report what the evidence establishes. Preserve valuable regression coverage while changing test boundaries. Record durable rationale in the project's existing documentation when that belongs to the task; distinguish accepted decisions from proposals.
