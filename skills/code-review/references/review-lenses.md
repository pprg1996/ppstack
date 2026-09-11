# Review lenses

Use the lenses relevant to the change. They guide investigation rather than prescribe a finding quota or a redesign.

## Requirements and repository standards

Map available acceptance criteria to implementation and evidence. Look for missing or partial behavior, unintended scope changes, and code that appears to satisfy a requirement but fails on a relevant path. Keep inferred intent distinct from a documented requirement.

Cite the applicable rule for a repository-standard violation and respect documented exceptions. Existing patterns provide context but do not excuse a reachable defect. Avoid duplicating passing automated checks with cosmetic manual comments; report actual tool failures when relevant. Naming, duplication, and coupling become useful findings when their consequences are concrete, not merely because they match a smell label.

## Correctness and security

Trace inputs, conditions, state, and effects. Check relevant failure paths, boundaries, retries, partial completion, and concurrency. Distinguish guards that enforce a valid contract from fallbacks that hide its violation. For bug fixes, inspect whether the repaired layer owns the failing invariant and whether the reported symptom can still occur.

For a security finding, establish the trust boundary, attacker-controlled input or access, the missing control, and the reachable consequence. For type or validation concerns, check the actual guarantees: runtime data, mutation, concurrency, and untyped callers can invalidate static assumptions. For shared state, evaluate whether the chosen ownership, isolation, transactions, or synchronization meets the required consistency; no single mechanism fits every design.

## Integration and verification

Follow changed contracts through callers, persisted data, external consumers, and operational configuration where affected. Consider compatibility and staged migrations before proposing removal of legacy paths. Inspect whether tests protect meaningful outcomes and whether they would detect the suspected failure.

A mock can verify local decisions without proving the remote contract. A dispatch acknowledgment can succeed before the intended effect completes. Distinguish static reasoning, local execution, integration evidence, and production observations. Missing coverage should be tied to a material risk or requirement rather than treated as an automatic defect.

## Maintainability and structure

Look for policy duplicated across callers, leaked internal decisions, fragile ordering, unclear ownership, or complexity introduced without a task-relevant benefit. A strong finding explains a concrete change or failure the structure makes harder, with a practical improvement proportionate to the scope.

File length, adapter count, casts, forwarding methods, and repeated syntax are clues to inspect. Their presence alone does not establish a blocker. Preserve useful abstraction, compatibility, and operational boundaries. Evaluate simplifications against behavior and migration costs rather than favoring rewrites or smaller code automatically.
