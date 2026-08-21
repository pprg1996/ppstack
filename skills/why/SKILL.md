---
name: why
description: "Investigate why code or a product decision has its current shape using source history and whatever shared records are available. Use for design rationale, regressions, postmortems, rejected alternatives, or data-backed thresholds. Use how for runtime behavior."
---

# Why

Reconstruct motivation from evidence. Do not turn plausible intent into fact.

Historical context may exist in source control, issues, long-form documents, team discussions, incidents, observability, error tracking, or product analytics. Every category is optional. Search the sources the environment exposes, record missing categories as coverage gaps, and continue without inventing harness-specific tools.

## Investigation

1. **Anchor the target.** Identify the exact symbol, behavior, threshold, decision, or regression. Read enough current code to know what needs explaining.
2. **Build search keys.** Collect symbol names, file paths, commit or PR identifiers, ticket IDs, authors, dates, error text, feature flags, metric names, and old names from renames.
3. **Search source control first.** Use blame as an index, then read the relevant commits, pull requests, review discussion, tests, and linked issues. Follow renames and moved files.
4. **Search connected records.** Inspect every available evidence category that could contain the decision. Read [`references/source-playbook.md`](references/source-playbook.md) for the category-specific questions.
5. **Verify leads.** Read the full relevant record, not only its title or search snippet. Cross-check dates, authors, shipped code, and later reversions.
6. **Synthesize.** Apply the confidence rules in [`references/epistemics.md`](references/epistemics.md). Preserve conflicting evidence instead of forcing agreement.

Use independent workers for separate evidence categories when the environment supports them. Otherwise search categories sequentially. A null result from a searched source is a finding; an unavailable source is a gap.

## Output

- **Answer.** The best-supported reason in plain language.
- **Evidence.** The records that directly support it, with stable links or identifiers.
- **Alternatives and constraints.** What was rejected, preserved, or forced, when evidence exists.
- **Confidence.** High, medium, or low, with the reason for that calibration.
- **Sources consulted.** Each searched category, including empty results.
- **Coverage gaps.** Unavailable categories that could materially change the conclusion.

If the investigation precedes a change, finish with a compact `Preserve / Change / Avoid / Risk` constraint set. Keep inference visibly separate from recorded intent.
