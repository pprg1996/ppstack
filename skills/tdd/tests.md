# Tests that detect behavior changes

Exercise the subject through an interface its callers use and assert an observable contract: a return value, error, state transition, persistence effect, or interaction with an external boundary. Prefer the test boundary that exposes the defect with the least unrelated setup.

## Independent expectations

Derive expected results from the requirement, a worked example, a trusted independent implementation, or a justified property. An assertion that recomputes the answer with the implementation under test cannot independently detect its error.

Concrete values are useful for examples, but literal equality is not the only valid test. Property tests, approximate numerical results, ordering constraints, expected exceptions, compile-time contracts, and the absence of a side effect can all express real requirements.

Judge a test by the plausible contract violation it would catch, rather than banning a matcher. For example, asserting no payment request is sent for a rejected order tests an external effect. When practical, pair a negative case with a contrasting positive case to distinguish correct behavior from a disconnected path. An empty result or a missing callback may be the intended behavior; evaluate whether the setup and assertions show that the subject actually ran.

## Mocks and state

Use real collaborators when they give reliable, affordable evidence. Fakes or mocks can isolate external services, nondeterminism, unavailable infrastructure, or a failure mode that is otherwise difficult to trigger. Keep the behavior being tested in the real subject.

Assert the output or effect relevant to the contract. Call counts and ordering can matter for retry limits, deduplication, or protocol behavior; they are brittle when they merely pin an internal decomposition. A mocked provider response can test the caller's handling of that response, but cannot prove the provider accepts the real request.

Check persistent state through the public interface when that expresses the requirement. Inspect stored data directly when storage behavior itself is under test or the integration boundary requires it; identify which layer the evidence covers.

## Useful failure signals

Use a concrete counterexample, contrasting input, or targeted fault when confidence in a test's sensitivity matters. A plausible broken implementation should fail the relevant assertion. Do not apply a universal requirement to replace every imported function with an empty return: some contracts are about effects, rejection, or deliberate absence.

Avoid tests that only check fixture data, repeat prompt wording, or pin a configuration constant without exercising the behavior that consumes it. Snapshots are useful when their contents represent a reviewed observable contract; unexplained bulk updates can conceal a regression.

Preserve meaningful assertions through refactoring. When the contract legitimately changes, update the expectation from the new requirement and describe the change rather than adjusting it merely to make the run pass.
