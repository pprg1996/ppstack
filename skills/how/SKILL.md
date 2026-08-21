---
name: how
description: "Explain how a codebase subsystem works: ownership, runtime flow, state, boundaries, and placement. Use for code walkthroughs, onboarding explanations, or 'where should this live?' questions. Use why for historical motivation."
---

# How

Explore the codebase and produce the smallest explanation that gives a senior engineer a working mental model. Explain behavior and ownership rather than annotating source files.

## Choose the mode

- **Explain** is the default.
- **Critique** applies only when the user asks whether the architecture is sound, where something should live, or what should change. Explain the current design before judging it.

## Build the model

1. Restate the target and identify the user action, request, event, or public call that starts the flow.
2. Read repository guidance, architecture records, and the nearest tests before tracing implementation.
3. Find entry points, follow the runtime path, and identify state ownership, persistence, external boundaries, errors, and cleanup.
4. Read representative implementations rather than every sibling. Widen only when the behavior differs or an invariant crosses the boundary.
5. Check every important claim against a concrete file, test, runtime observation, or authoritative dependency source.

For a subsystem with independent slices, use isolated workers when available. Assign non-overlapping angles such as entry points, state, persistence, and failure handling. If workers are unavailable, inspect those angles sequentially. The final explanation must reconcile their findings into one flow.

## Explain

Lead with a plain definition and why the subsystem exists. Then cover:

- the main runtime flow from entry to observable result;
- the modules that own policy, state, and boundary adaptation;
- the data transformations and persistence points;
- the failure and cleanup paths;
- the best starting points for someone about to modify it.

Cite paths and line numbers for claims that are not obvious. Use a compact diagram only when three or more moving parts are easier to understand visually.

## Critique

After explaining, read [`references/critique-rubric.md`](references/critique-rubric.md). Judge only problems supported by the traced behavior. Separate structural problems from taste, and state the cost of leaving each issue unchanged. If independent reviewers are available, let them review the same explanation and evidence separately; otherwise perform a distinct second pass.

## Confidence

Label meaningful uncertainty. Distinguish behavior proven by tests or execution, behavior supported by source, and inference. State any important surface you could not inspect.
