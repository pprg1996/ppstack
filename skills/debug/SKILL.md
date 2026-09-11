---
name: debug
description: "Investigate a reported bug or performance regression, or diagnose a captured trace. Fix and verify it when the request includes repair."
---

# Debug

Choose the investigation that can distinguish causes with the evidence available. Keep the observed symptom, proposed mechanism, and proof separate. A request for diagnosis ends with findings; a request for repair includes the fix and appropriate verification.

## Choose the evidence path

Start with the reported behavior, expected behavior, affected environment, and any existing evidence. Inspect code or history when it helps locate the cause or build a reproduction. Use the matching reference only when its situation applies:

- **A runnable failure or an intermittent trigger:** [reproduce and repair](references/reproduce-and-repair.md).
- **A live process with a leak, CPU spike, latency, or visual glitch:** [live investigation](references/live-investigation.md).
- **An existing profile, trace, heap snapshot, log, or crash report:** [captured evidence](references/captured-evidence.md).

Paths can combine. If the target cannot be run, continue with available source and artifacts, state the evidence gap, and identify the next discriminating check. Ask for missing access or an artifact only when it blocks further useful work. A production-only failure does not make source-based investigation worthless or establish permission to change production.

## Follow the evidence

Select the next observation or experiment for how well it separates plausible causes. Narrow an existing harness before building a new one. Refine or minimize the reproduction when it will make the investigation more reliable or cheaper; a perfectly minimal case is not an entry condition.

When repeated attempts fail, revisit what those attempts assumed. Seek evidence that could refute the shared premise. Measure per-actor imbalance only when uneven ownership or work distribution is a plausible mechanism. A balanced measurement can rule out that mechanism without settling the whole diagnosis.

For failures after a restart, inspect persisted state, configuration, caches, and compatibility with the running version. Preserve evidence before testing a reset. A reset that helps is a clue; it does not by itself prove the cause or justify deleting user state.

## Finish within the request

For authorized repairs, fix the demonstrated mechanism and verify the original behavior at the closest available surface. Check related occurrences when the same mechanism could affect them; keep repairs within the requested scope. If a production incident needs a mitigation before the cause is known, identify it as a mitigation and report the remaining uncertainty.

Preserve useful artifacts while removing temporary instrumentation and resources created by the investigation. Redact secrets from shared evidence. Existing authorization controls browser access, live instrumentation, external writes, and publication; this skill supplies none of those permissions.

Report what failed, the best-supported cause and its confidence, what changed if anything, the checks actually run, and the remaining gap. Distinguish a local test, live reproduction, and production verification. A plausible patch or a passing check on a different symptom is not a verified fix.
