# ppstack migration for GPT-6

## Direction

On September 11, 2026, the owner changed ppstack's role: prefer suitable pstack workflows over Matt Pocock's equivalents, maintain adaptations in this fork, and adjust instructions for GPT-6. The former rule that Matt must remain the project orchestrator no longer applies.

Proceed one capability at a time. Keep useful pstack knowledge and execution evidence while removing fixed model choices, mandatory delegation, unnecessary approval gates, universal phase sequences, and automatic publication. Preserve user authorization and repository-specific invariants. Select replacements by actual task coverage, not by matching names.

## Completed first increment: debugging

`debug` adapts the bug-fix, live-forensics, and trace-forensics playbooks from the upstream `poteto-mode` directory plus root-cause and premise-checking principles. Attribution and the upstream revision are recorded through `NOTICE.md`, `selection.json`, and `upstream.lock.json`.

It replaces Matt's `diagnosing-bugs` for diagnosis and requested repairs. The key changes are evidence-based routing, useful progress before a reproduction exists, explicit confidence, proportional testing, and continued repair when authorized. Broadly applicable principles are embedded rather than installed as additional global skills.

The source does not require Matt's other skills or the upstream global mode. A profile can be investigated without recreating the process. Local proof remains distinct from production proof. Mitigations remain distinct from root-cause fixes.

## Candidate map

The initial September 11 local installation lock recorded 25 Matt skills. The table covers all of them, including explicit-only entries. These are replacement candidates, not claims that every pstack alternative already provides equivalent coverage.

| Installed Matt skill(s) | pstack starting point | Next decision |
| --- | --- | --- |
| `diagnosing-bugs` | Bug-fix and forensic playbooks; root-cause and premise principles | Replaced by `debug`; published and installed from the fork. The Matt skill was removed. |
| `tdd` | `tdd`; behavior-testing principle | Adapted as `tdd`, extending pstack's regression workflow to requested test-first features and preserving valid assertion types. |
| `codebase-design`, `improve-codebase-architecture` | `architect`; boundary and foundational-design principles | Replaced together by `architect`; preserves design and survey coverage with task-scoped implementation and optional exploration formats. |
| `code-review` | `interrogate` | Preserve specification/standards coverage and working-tree review; support useful review without multi-model availability. |
| `prototype` | Prototype playbook; `arena` | Compare experiment design and disposable artifacts; avoid mandatory competing implementations. |
| `implement` | Feature playbook; `figure-it-out` | Extract focused implementation with completion criteria; avoid importing global mode machinery. |
| `domain-modeling` | Domain-modeling and boundary principles | Check glossary and ADR ownership; a principle alone may not replace the full workflow. |
| `grilling`, `grill-me`, `grill-with-docs` | `architect`, `interrogate` | Partial overlap only. Preserve interactive elicitation and document creation if replaced. |
| `teach` | `teach` | Compare ongoing learning/project behavior against upstream's code-explanation focus. |
| `research` | Investigation playbook; `why` | Partial overlap: historical explanation does not cover all primary-source research. |
| `handoff` | Session-pickup and pause-safely playbooks; `recall` | Compare outgoing handoff artifacts and incoming reconstruction. |
| `resolving-merge-conflicts` | Babysit playbook | Inspect Git safety and conflict verification before adopting a subset. |
| `wayfinder` | Multi-phase-plan and orchestration playbooks | Preserve multi-session state and decision tracking without requiring specific tools. |
| `triage`, `to-spec`, `to-tickets` | No established equivalent yet | Inspect upstream workflow coverage; keep until a replacement covers tracker semantics and authorization. |
| `ask-matt`, `setup-matt-pocock-skills` | No direct replacement needed yet | Reconsider routing/setup once the capabilities they reference have migrated. |
| `to-questionnaire`, `wait-what`, `wizard` | No established equivalent | Keep; do not create a replacement merely to remove the source dependency. |
| `writing-for-agents` | Authoring-a-skill playbook; reader-load and structure principles | Evaluate separately; current skill-authoring guidance also comes from the active harness. |

## Rollout contract

For each replacement, inspect upstream sources, document coverage and intentional differences, validate package discovery and references, then exercise representative tasks where practical. Retire only the replaced Matt entry after the replacement is validated. For a distinct name, disable or remove the old entry. For a same-name replacement, replace the installed directory and update its source record; do not disable the shared name. Keep a reversible copy of configuration and avoid modifying vendor source in place.

Publication is a separate action. A local install from this working tree is not an update published to the GitHub repository; report that distinction and keep its source available until replaced with a published installation.

## Validation scenarios for debug

1. An existing executable failure: confirm a relevant failing check, repair, and verify the original symptom.
2. A production-only intermittent failure with logs and source but no live access: make useful progress, identify a discriminating experiment, and avoid claiming verified production repair.
3. A captured profile without a before/after pair: explain what the artifact establishes and whether the causal interpretation remains a hypothesis.
4. A diagnosis-only request: preserve product code while producing findings.
5. Repeated failed patches: revisit the shared premise without assuming every problem is a per-actor imbalance.

Package validation proves structure and portability, not model behavior or superiority over Matt's skill. Record actual scenario runs and their limits before claiming a behavioral improvement.

## Initial September 11 qualification (before publication)

- Added and locally installed `debug`; Codex's reloaded skill listing confirms it enabled and `diagnosing-bugs` disabled. The old Matt files remain available for rollback.
- The installed debug files match this fork's source byte for byte. This is an unpublished local install; the skill manager did not add a remote update entry for it. After publication, reinstall from the fork's GitHub source to establish the normal consumer update path.
- Repository validation, skill frontmatter validation, all debug reference links, and public discovery pass. Discovery exposes 12 public skills and excludes the internal maintenance skill.
- Upstream is pinned at `f5bdd6826fd0a0d9cbc4347134c3a74a200b9d9d`; all 47 skill hashes match the inspected checkout. The only upstream skill changed since the previous pin was the global mode; the diff concerned other playbooks and wording, not the extracted debugging files.
- No comparative model runs or real bug investigations were performed with the new skill. The five scenarios above remain behavioral validation work, not completed evidence.
- Matt's explicit `ask-matt` router still points to its original diagnosis skill. Use `debug` directly or the existing inventory-based Skill Advisor; reassess that legacy router as migration progresses rather than editing its vendor copy.
- Other Matt skills remain unchanged. The next proposed replacement is TDD, subject to its feature-development coverage check.

## Second increment: TDD

The owner approved replacing Matt's `tdd` with a pstack-derived `tdd`, maintained in this fork. The replacement extends upstream's bug-fix workflow to explicitly requested test-first feature development. It infers established interfaces, permits red-green-refactor, chooses testing effort according to the task, and preserves meaningful property, error, and absence assertions. It does not require the user to confirm every test boundary.

`selection.json` maps both upstream `tdd` and `principle-test-behavior-not-implementation` to the public `tdd` directory. The latter is adapted into `tests.md` rather than installed as a separate global principle. The pinned upstream snapshot already contains both sources; this increment does not advance the lock.

Same-name installation preserves existing `/tdd` references. Matt's retained `implement` skill separately requires pre-agreed seams; replacing `tdd` does not remove that caller's rule. Review it when adapting the implementation workflow.

Representative behavioral checks remain: a new feature built test-first; a reproducible bug; an unavailable test environment with an explicit TDD requirement; a meaningful property test; a negative side-effect assertion; and a refactor that preserves behavior. Package validation and discovery do not establish model performance on these scenarios.

## Third increment: architecture

The owner approved replacing Matt's `codebase-design` and `improve-codebase-architecture` with `architect`, using the upstream name. It adapts upstream `architect`, its design references, and the boundary-discipline and foundational-thinking principles. The pinned upstream revision is unchanged.

Coverage includes specific interface design, open-ended architecture surveys, caller usage, data and ownership decisions, dependency and testing strategy, existing ADRs, alternative shapes, migration planning, and implementation when requested. Review guidance lives in a conditional reference; design checks retain useful interface-depth and information-hiding concepts without enforcing a vocabulary.

Intentional differences include no prescribed models, worker counts, alternative counts, full-system exploration, mandatory HTML report, or grilling loop. Design advice does not authorize implementation. Validation follows actual trust and state guarantees instead of unconditional internal trust. Test coverage is evaluated by the guarantees it protects rather than deleted wholesale when modules are combined. Scaffolding and cleanup must serve the requested change.

`selection.json` maps all three upstream sources to the public `architect` directory. Retire only the two replaced Matt installations after package and discovery validation. The remaining Matt `ask-matt` router still names the retired architecture commands, and its setup documentation mentions them; those files are unchanged pending their own migration. Use `architect` directly or inventory-based discovery.

Qualification: repository and skill validators, conditional-reference resolution, upstream inventory audit, public discovery, installation equality, and fresh Codex discovery are required for this increment. These structural checks do not establish behavioral superiority. Representative behavioral scenarios remain unexecuted: a review with no justified refactor; a narrow design-only request; an authorized refactor preserving regression coverage; a compatibility boundary that should remain; and a runtime invariant that static types cannot guarantee.
