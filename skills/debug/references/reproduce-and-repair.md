# Reproduce and repair

Use an existing test, command, request, or app control surface that exercises the reported behavior. Verify that a failure is the user's symptom rather than an unrelated setup problem. Preserve the initial evidence so later results can be compared.

For intermittent failures, vary or stress the suspected trigger within a disposable environment and record attempts and outcomes. A lower failure rate supports improvement; a few clean runs do not establish absence. When the failure is expensive or inaccessible, use a smaller discriminating experiment and state what it leaves untested.

Connect each proposed cause to an observable prediction. Source inspection and regression history can generate hypotheses before a reproduction exists. Prefer the experiment that removes the most uncertainty at reasonable cost; choose the number of hypotheses from the ambiguity rather than filling a quota.

If repair is requested, use a focused regression test when an existing test boundary can exercise the bug meaningfully. Run it before changing implementation and confirm the failure is relevant. Where a new test would require unrelated infrastructure or brittle simulation, use the closest reliable check and describe the coverage gap. Preserve an explicit user request for test-first work; resolve a material limitation rather than silently dropping it.

Apply the change justified by the evidence. Reconsider changes motivated by a refuted hypothesis. Verify the original scenario after the fix, rerun affected checks after meaningful changes, and inspect relevant side effects. Passing tests permit local refactoring needed by the repair; they do not automatically establish behavior on an inaccessible deployment.
