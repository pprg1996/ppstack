# Review an existing architecture

Follow the user's named subsystem or pain point. When scope is open, use recent changes, recurring defects, and costly coordination to select useful areas to inspect. A directory count or stylistic preference alone is weak evidence for a refactor.

Trace representative caller paths and the decisions spread across them. Look for information leakage, repeated coordination, unclear ownership, fragile ordering, or test setup that exposes private implementation details. Check existing domain documentation and ADRs before judging an intentional tradeoff. Apply [Design checks](design-checks.md) to plausible candidates.

For each worthwhile candidate, identify:

- The affected files and a concrete example of current friction.
- The proposed ownership or interface change and how caller behavior would look afterward.
- The expected benefit, compatibility and migration cost, and verification needed.
- Confidence in the evidence and any existing decision the proposal would reopen.

Rank candidates by demonstrated benefit and cost. Explain the strongest recommendation, or say that the inspected scope offers no justified structural change. Separate observed friction from speculative future needs.

Use before/after diagrams when relationships are hard to communicate in prose, and produce an HTML report when requested or useful for the comparison. Match the output to the task instead of requiring a report format or an interview. For review-only requests, leave implementation as a proposal. If the user requested improvements be implemented, proceed within that scope using the main workflow.
