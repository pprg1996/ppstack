---
name: tdd
description: "Build features or fix bugs test-first when requested, or add a focused regression test where a practical test boundary exists."
---

# Test-driven development

Make the intended behavior executable before implementing it. For a feature, work from acceptance criteria; for a bug, capture the reported failure. This skill governs the test-first work the task needs, rather than expanding every edit into a testing project.

## Choose the boundary

Use the closest existing public interface and test harness that can observe the behavior meaningfully. Infer established boundaries from the code, tests, and request. Choose an ordinary new interface when needed; ask about unresolved behavior or design choices only when they materially affect the outcome or scope.

When assertion quality, mocks, or test type need attention, consult [tests.md](tests.md). Prefer existing fixtures and infrastructure. Test setup should serve the behavior under development rather than force unrelated architectural changes.

## Red, green, refactor

Choose a useful increment of observable behavior. Add a focused test and run it before implementation. Confirm that the failure demonstrates the missing or incorrect behavior; distinguish it from unrelated syntax, import, or environment failures. A test that already passes may capture an existing requirement, but it is not evidence that the reported defect was reproduced.

Implement that increment and rerun the test. Preserve nearby contracts and expected behavior. Refactor when it improves the implementation, keeping affected tests passing. Continue with the remaining acceptance criteria; choose the size of each increment from the behavior, without a fixed number of tests or assertions.

Run adjacent tests, type checks, or scenario checks when the change affects their contracts. Repeat checks after relevant changes or unresolved failures. A passing local test proves only the behavior and environment it exercised.

## When test-first work is constrained

For a requested TDD workflow, a new feature may need a small amount of test scaffolding. Build what is justified by the request. If the required test depends on unavailable access, uncertain requirements, or substantial unrelated infrastructure, explain the concrete limitation and resolve it with the user rather than silently substituting implementation-first work.

For an incidental bug fix without a test-first requirement, use the closest reliable executable check when a durable regression test is impractical. Report the reason and the coverage gap. Preserve failing-before evidence when available; never infer it from a passing-after run.

For intermittent bugs, control relevant time, randomness, concurrency, or state where possible without removing the failure mechanism. Report the number of attempts and observed failures when verification remains probabilistic.

## Completion

Complete the requested behavior and relevant checks. Change existing expectations only when the intended contract changes, and explain why. Report the failing-before and passing-after evidence, relevant additional validation, and anything that could not be exercised. Commit, publish, or access external systems only within the user's authorization.
