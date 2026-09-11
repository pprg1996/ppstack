# Design checks

Apply the checks relevant to the proposed boundary. These are diagnostic questions, not a scorecard or mandatory architecture style.

## Information and ownership

A deep module hides useful complexity behind an interface that callers can understand without learning its internals. Depth is about capability and caller obligations, not line counts or call-chain length. Look for callers coordinating internal stages, options that expose implementation choices, and the same invariant maintained in several places.

Group related knowledge and policy under a clear owner. Stages such as load, validate, and save may belong together when they share invariants; separate them when deployment, streaming, lifecycle, or reuse gives the boundary a concrete role.

Use the deletion test: if removing a layer eliminates complexity, it may be unnecessary; if it spreads policy across callers, the layer is doing useful work. Forwarding can still earn its place through compatibility, instrumentation, adaptation, or ownership. Judge an abstraction by its current obligations and credible change pressures rather than the number of adapters it has.

## Contracts and data

Locate validation at trust boundaries and state transitions where an invariant can actually fail. Internal types can remove redundant checks when they establish the required guarantees; mutable state, concurrency, deserialization, and untyped callers can invalidate those guarantees. Keep necessary runtime validation where that risk exists.

Prefer domain concepts at application interfaces when transport or storage representations would couple callers to private decisions. Protocol and integration libraries may intentionally expose those representations. Document the ownership and compatibility obligation either way.

Choose data structures against actual reads, writes, lifetimes, and scale requirements. Identify who can mutate shared state and how concurrent operations preserve invariants. Isolation, transactions, synchronization, or conflict resolution should follow the consistency requirement. For retried operations, account for duplicates and partial completion where applicable.

## Dependencies and verification

Separate deterministic policy from effects when that improves understanding and verification; the production contract may legitimately be an effect. Keep dependency injection focused on actual lifecycle, isolation, or substitution needs.

Test through a stable behavioral boundary without exposing private controls solely for tests. Pure computation can be checked directly. Local dependencies may support realistic integration tests; remote services may require fakes or mocks plus contract or integration evidence for behavior those doubles cannot prove. Distinguish what each check establishes.

When restructuring, map existing tests to the behavior they protect. Retain valuable internal algorithm or invariant coverage, move tests whose boundary changed, and remove obsolete tests only once their useful guarantees are accounted for. An interface-level test does not automatically supersede all tests underneath it.

## Migration cost

Include caller changes, persisted representations, external compatibility, operational constraints, and rollback needs where affected. Favor a coherent change that reduces total coordination cost. Preserve a justified boundary even when merging code would look locally simpler; avoid adding speculative infrastructure or unrelated cleanup as a prerequisite.
