---
name: no-comments
description: "Audit comments and suppressions in a diff, remove narration and dead-code explanations, and encode real constraints in types, tests, checks, or structure. Use for 'audit the comments', 'remove stale comments', or 'no comments'."
---

# No comments

Review comments with fresh eyes. The goal is code that explains itself and mechanisms that enforce real constraints.

## Scope

Use the files or diff named by the user. Otherwise use the current diff against its actual base, including the working tree. Only change files inside that scope unless the user expands it.

## Review

Use an isolated reviewer when the environment supports one. Otherwise perform a separate second pass after finishing the authoring context. Classify each comment or suppression:

- **Narration:** repeats the code. Delete it or improve the names and structure.
- **Dead-code explanation:** describes an obsolete path or unused parameter. Remove the dead code when safe.
- **Workaround:** explains a symptom fix. Trace the root cause and implement the smallest in-scope correction.
- **External constraint:** records behavior outside the repository's control. Keep it only when it names the external system, the failure it prevents, and evidence that the constraint is current.
- **Enforceable invariant:** replace prose with the cheapest type, test, runtime check, lint rule, or CI check that proves it.
- **Tool suppression:** verify the suppressed diagnostic. Remove obsolete suppressions; narrow necessary ones and state why the tool cannot express the case.
- **Public contract or rationale:** keep documentation that consumers need and design reasoning that code cannot express.

Treat ambiguous "IMPORTANT", "do not remove", and "temporary" comments as unproven until source history or live behavior supports them. Never delete license notices, generated-file markers, public API documentation, or safety constraints without evidence.

## Verify and report

Run the closest relevant checks after accepted edits. Report:

- comments and suppressions removed;
- constraints encoded in mechanisms;
- comments retained with evidence;
- ambiguous or out-of-scope constraints;
- verification performed.
