# Live investigation

Match the signal to the symptom: a CPU profile for unexpected work, allocation or heap evidence for retention, timings and query plans for latency, or a UI trace for a visual glitch. Prefer observation through an existing authorized control surface. Use source to interpret captures and choose instrumentation.

Reduce the evidence to a mechanism: the hot path, retaining reference, repeated scheduler, blocked resource, or expensive query. Compare against expected activity, request volume, and the capture interval. A busy function may be serving legitimate work; a retained object may still have a valid owner.

Test the mechanism with the least intrusive discriminating probe. Runtime evaluation, hot patches, traffic generation, and additional instrumentation can change state or expose data; use them only within the existing task authorization. If mutation is unavailable, continue with captures and source and label the inference.

Capture enough context to compare before and after: workload, duration, environment, and the relevant baseline. Map observations to source where symbols permit. Missing symbols or access limit confidence; report what is established and what remains unresolved.

For a diagnosis request, return the supported mechanism and evidence. For a repair request, continue through the applicable fix and verification path. Preserve captures and restore temporary diagnostic changes made by this investigation.
