# Captured evidence

Treat the capture as a dataset. Identify its format, capture conditions, time range, and symbol information. Use an available parser or query tool suited to its size and structure. Convert to a database only if repeated querying makes that worthwhile.

Follow the evidence appropriate to the artifact: time and call stacks for CPU samples; retainers and ownership for heap snapshots; thread state for crash or hang reports; chronology and correlation identifiers for logs. Correlation narrows candidates but does not itself establish causality.

Map the finding to source when possible. Distinguish the most expensive sampled function or suspicious retained object from the mechanism responsible for the reported symptom. Without source mapping, report the supported artifact-level finding and the unresolved attribution.

Compare a paired capture when available, accounting for differences in workload and environment. Without a discriminating comparison or experiment, describe the strongest hypothesis the artifact supports and the next check that could confirm or refute it. Further evidence is unnecessary when the artifact itself directly establishes the mechanism; explain why in that case.

A captured artifact can support useful diagnosis without access to the live system. Return cited findings and confidence. If the user requested repair, use them to guide the change and test what is locally testable, while preserving any production verification gap.
