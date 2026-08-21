# ppstack

Portable tactical skills adapted from [pstack](https://github.com/cursor/plugins/tree/main/pstack).

ppstack is a skill collection, not a plugin. It contains no MCP server, agent definition, automation, model configuration, or Cursor rule. Its public skills use capabilities when they are available and degrade explicitly when a harness lacks workers, history, connectors, or a known project-skill directory.

## Why ppstack exists

[Matt Pocock's skills](https://github.com/mattpocock/skills) provide the project spine: planning, implementation, debugging, architecture, testing, review, and handoff. ppstack adds tactical lenses used inside that work. It does not replace or orchestrate Matt's collection.

The boundary is intentional:

- Matt's skills decide how a project-sized effort moves forward.
- ppstack skills answer narrower questions such as how a subsystem works, why a decision exists, what a change could break, or how to prove an app still behaves correctly.
- Exact-name conflicts, equivalent objectives, personal modes, and global orchestrators stay out.

## Install

List the available skills:

```bash
npx skills add pprg1996/ppstack --list
```

Install interactively:

```bash
npx skills add pprg1996/ppstack
```

Install selected skills:

```bash
npx skills add pprg1996/ppstack \
  --skill blast-radius \
  --skill how \
  --skill why \
  --skill recall
```

Update installed copies from this repository:

```bash
npx skills update
```

## Public skills

| Skill | Tactical job | Portability adaptation |
| --- | --- | --- |
| `blast-radius` | Find downstream breakage and prove the safety fact a change depends on. | Parallel review falls back to sequential risk angles. |
| `create-verification-skill` | Generate a project-local skill that drives the real app and captures evidence. | Discovers the active project-skill directory instead of assuming a Cursor path. |
| `how` | Explain subsystem ownership, runtime flow, state, boundaries, and placement. | Uses optional isolated workers without named worker types or models. |
| `maintain-verification-skill` | Audit a verification skill and feature map against source and live behavior. | Discovers skill locations and works sequentially when workers are unavailable. |
| `no-comments` | Remove narration and encode real constraints in types, tests, checks, or structure. | Replaces the Cursor-specific reviewer agent with a portable review contract. |
| `recall` | Reconstruct recent work and verify it against current state. | Climbs an evidence ladder and reports missing history or connectors as gaps. |
| `show-me-your-work` | Keep a reviewable TSV decision trail for long or unattended work. | Uses any available run evidence and makes isolated review capability-dependent. |
| `technical-writing` | Apply a layered technical-writing standard to docs and engineering prose. | Removes harness invocation metadata. |
| `typescript-best-practices` | Apply disciplined TypeScript modeling and boundary validation. | Embeds required type guidance instead of depending on pstack principle skills. |
| `unslop` | Remove generic AI patterns while preserving voice and meaning. | Becomes an explicit edit rather than a mandatory global mode. |
| `why` | Reconstruct design motivation from source history and shared records. | Searches available evidence categories and reports unavailable ones. |

All 11 public skills are adapted rather than verbatim copies.

## What ppstack leaves out

Every upstream skill is classified in [`selection.json`](selection.json). The current exclusions fall into these groups:

| Reason | Excluded upstream skills |
| --- | --- |
| Project orchestration or substantial overlap with Matt's skills | `architect`, `figure-it-out`, `interrogate`, `tdd`, `teach`, `principle-boundary-discipline`, `principle-encode-lessons-in-structure`, `principle-exhaust-the-design-space`, `principle-fix-root-causes`, `principle-foundational-thinking`, `principle-minimize-reader-load`, `principle-model-the-domain`, `principle-outcome-oriented-execution`, `principle-redesign-from-first-principles`, `principle-sequence-verifiable-units`, `principle-subtract-before-you-add` |
| Harness-specific orchestration, history, configuration, or personal mode | `arena`, `automate-me`, `poteto-mode`, `reflect`, `setup-pstack`, `swarm`, `principle-guard-the-context-window`, `principle-never-block-on-the-human` |
| Too small, too broad, or too specialized for the default companion set | `bro`, `principle-build-the-lever`, `principle-experience-first`, `principle-laziness-protocol`, `principle-make-operations-idempotent`, `principle-migrate-callers-then-delete-legacy-apis`, `principle-prove-it-works`, `principle-separate-before-serializing-shared-state` |
| Folded into an adapted public skill | `principle-type-system-discipline` is incorporated into `typescript-best-practices`. |

An exclusion is not a judgment that the upstream skill is poor. It means the skill does not fit ppstack's portable companion boundary. `selection.json` records the specific reason for every skill and is validated against the pinned upstream inventory.

## Two update paths

Consumers update ppstack from this repository with `npx skills update`.

Maintainers update this repository from upstream pstack with the internal `update-ppstack` workflow:

```text
cursor/plugins/pstack -> update-ppstack -> pprg1996/ppstack -> npx skills update -> installed skills
```

The maintainer skill lives outside `skills/`, declares `metadata.internal: true`, and is absent from normal public discovery. It detects upstream changes, requires every upstream skill to remain classified, preserves the portability contract, validates the public package, and advances `upstream.lock.json` only after semantic review. It does not commit or push automatically. See [`MAINTAINING.md`](MAINTAINING.md).

## Provenance

ppstack is derived from pstack at the revision recorded in [`upstream.lock.json`](upstream.lock.json). The upstream inventory and per-skill content hashes make additions, removals, and changes auditable.

See [`NOTICE.md`](NOTICE.md) for attribution. ppstack is an independent project and is not affiliated with or endorsed by Cursor, pstack, Lauren Tan, or Matt Pocock.

## License

MIT. See [`LICENSE`](LICENSE).
