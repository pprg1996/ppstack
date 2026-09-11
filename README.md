# ppstack

Portable engineering skills adapted from [pstack](https://github.com/cursor/plugins/tree/main/pstack).

ppstack is a skill collection, not a plugin. It contains no MCP server, agent definition, automation, model configuration, or Cursor rule. Its public skills use capabilities when they are available and degrade explicitly when a harness lacks workers, history, connectors, or a known project-skill directory.

## Why ppstack exists

ppstack is the owner's maintained fork for engineering workflows, adapted for GPT-6 and portable across agent harnesses. Prefer pstack-derived replacements where they cover the task well; retain useful skills from other sources where no replacement is ready.

Adaptations preserve domain knowledge and evidence while letting the agent choose an approach appropriate to the task. They remove hard-coded models, mandatory orchestration, unnecessary approval gates, and automatic publication. Overlapping skills are replaced deliberately, one capability at a time.

See [the migration plan](docs/gpt6-migration.md) for replacement candidates, coverage gaps, and rollout criteria. The first replacements are `debug` for Matt Pocock's `diagnosing-bugs` and a pstack-derived `tdd` for test-first features and bug fixes.

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

| Skill | Job | Portability adaptation |
| --- | --- | --- |
| `blast-radius` | Find downstream breakage and prove the safety fact a change depends on. | Parallel review falls back to sequential risk angles. |
| `debug` | Diagnose bugs from reproductions, live signals, or captured evidence; repair when requested. | Chooses the available evidence path without requiring a perfect reproduction, fixed models, or delegation. |
| `create-verification-skill` | Generate a project-local skill that drives the real app and captures evidence. | Discovers the active project-skill directory instead of assuming a Cursor path. |
| `how` | Explain subsystem ownership, runtime flow, state, boundaries, and placement. | Explains narrow questions directly and uses optional workers for independent slices. Architectural critique belongs to a dedicated design or review workflow. |
| `maintain-verification-skill` | Audit a verification skill and feature map against source and live behavior. | Discovers skill locations and works sequentially when workers are unavailable. |
| `no-comments` | Remove narration and encode real constraints in types, tests, checks, or structure. | Replaces the Cursor-specific reviewer agent with a portable review contract. |
| `recall` | Reconstruct recent work and verify it against current state. | Climbs an evidence ladder and reports missing history or connectors as gaps. |
| `show-me-your-work` | Keep a reviewable TSV decision trail for long or unattended work. | Uses any available run evidence and makes isolated review capability-dependent. |
| `tdd` | Build requested features test-first and lock down bugs with focused regression tests. | Infers test boundaries, supports red-green-refactor, and preserves useful assertion and test types. |
| `technical-writing` | Apply a layered technical-writing standard to docs and engineering prose. | Removes harness invocation metadata. |
| `typescript-best-practices` | Apply disciplined TypeScript modeling and boundary validation. | Embeds required type guidance instead of depending on pstack principle skills. |
| `unslop` | Remove generic AI patterns while preserving voice and meaning. | Becomes an explicit edit rather than a mandatory global mode. |
| `why` | Reconstruct design motivation from source history and shared records. | Searches available evidence categories and reports unavailable ones. |

All 13 public skills are adapted rather than verbatim copies.

## What ppstack leaves out

Every upstream skill is classified in [`selection.json`](selection.json). The fork can extract a focused workflow from a larger upstream skill: `poteto-mode`'s debugging playbooks and two diagnostic principles are adapted into the single public `debug` skill; the global mode is not imported.

Some former exclusions were based on overlap with Matt's skills. Those are now migration candidates, not a permanent boundary. They remain excluded from the current package until their replacements are ready. The [migration plan](docs/gpt6-migration.md) maps the installed collection and distinguishes likely replacements from partial overlap.

Platform-specific integrations, personal modes, and blanket operating rules remain out unless a requested workflow gives them a portable, well-scoped role. `selection.json` records the reason for each upstream skill and is validated against the pinned inventory.

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
