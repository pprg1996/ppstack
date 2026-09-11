---
name: code-review
description: "Review code changes for defects, requirement gaps, and repository-standard violations. Use for PRs, branches, specified revisions, or uncommitted work."
---

# Code review

Produce evidence-backed findings that help the user decide what to fix. This workflow adapts pstack's `interrogate`; its public name preserves existing `code-review` callers. A review request authorizes inspection and appropriate local verification, not applying fixes or publishing review comments. Carry out fixes or publication only when the request includes them.

## Establish scope and intent

Use the user's requested files, revisions, PR, or working-tree scope. Read [Git review scope](references/git-scope.md) to select and record the exact comparison, including relevant untracked files. Infer a base only when the branch, PR, or conversation establishes it; ask when materially different interpretations remain. An empty comparison means no changes in that scope, not proof that all current work was reviewed.

Use explicit requirements and supplied specifications first, then relevant issue or PR descriptions, repository documents, and conversation context. Commit messages and code can suggest intent but cannot establish missing acceptance criteria. Fetch connected records through available tools when authorized. If requirements remain unavailable, review what can be established and report the specification gap; ask only when the uncertainty blocks a meaningful conclusion.

Read applicable repository standards and architectural constraints. State the intended behavior and the scope briefly so the user can assess the review's basis.

## Investigate

Apply [Review lenses](references/review-lenses.md) to relevant risks, preserving both requirement coverage and repository-standard checks. Follow callers, dependencies, state transitions, and tests beyond the diff where needed to establish impact. For a suspected defect, trace a reachable trigger and consequence. Run a focused check when it can resolve the uncertainty, using disposable local resources within the task's permissions. Report unavailable evidence without implying the check passed.

Review directly by default. Independent reviewers can help on complex changes when available and authorized; give them the same scope and intent plus the context needed to evaluate their assigned areas. Honor an explicit multi-reviewer request where supported and disclose any unavailable capability. There is no dependency on a particular model or worker API.

## Judge and report

Validate candidate findings against the actual source and constraints. Resolve contradictory claims through evidence; model agreement is a lead to investigate, not proof. A lone finding can establish a serious defect. Merge duplicates without hiding distinct consequences, and separate newly introduced problems from pre-existing issues outside the requested scope.

Lead with actionable findings ranked by impact and urgency, retaining requirement or standard citations where relevant. Each finding should identify its location, triggering condition, consequence, and supporting evidence. Distinguish demonstrated defects, documented-standard violations, and justified maintainability concerns from optional preferences. Keep genuine findings even when there are many; a fixed count is not a quality criterion.

Finish with scope, meaningful verification results, and material coverage gaps. If no actionable findings remain, say so without claiming the absence of all bugs. Include rejected findings or reviewer disagreements only when they explain a consequential judgment or the user requested an audit trail. For a review-and-fix request, verify the corrections against the reported defects and summarize the final state.
