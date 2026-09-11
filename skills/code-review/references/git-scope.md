# Git review scope

Resolve the user's intent before choosing a diff. Record resolved revisions and working-tree status so the review can be reproduced. Quote paths and validate refs; do not switch branches, reset files, or discard changes to obtain a comparison.

- **A branch or PR's changes:** compare its head against the merge-base with the established target. `git diff BASE...HEAD` does this for the current head. Confirm the target from the PR or repository context instead of assuming `main`. This comparison excludes all uncommitted work.
- **Exact endpoint comparison:** `git diff OLD NEW` compares those snapshots. A request to compare two revisions may need this rather than their merge-base; preserve an explicit choice.
- **All tracked uncommitted changes:** `git diff HEAD` compares the current tracked working tree with HEAD, including staged and unstaged edits in their combined final state. Inspect `git diff --cached` and `git diff` separately when the user wants the index or unstaged changes, or when that distinction matters.
- **Branch plus work in progress:** resolve the intended branch base with `git merge-base BASE HEAD`, then compare that resolved commit with the working tree using `git diff RESOLVED_BASE`. This shows the combined tracked state, not just committed changes.
- **Untracked files:** Git diffs above omit them. Discover them with `git ls-files --others --exclude-standard` and inspect relevant files separately when the requested review includes them. Use NUL-delimited output for programmatic filename handling.

Inspect status and file names before loading content, including deleted, renamed, binary, or generated files where their effects matter. For a PR head different from the checkout, obtain that revision or its diff without overwriting local work; inspect surrounding source at the matching revision. For stacked PRs, use the actual parent as the comparison base when reviewing only the current layer.

If conflicts or concurrent edits prevent a stable view, identify that limitation and review a recorded snapshot or reconcile the changed files before finalizing. If the comparison is empty, check whether the intended work is staged, unstaged, untracked, or on another head before concluding there is nothing to review.
