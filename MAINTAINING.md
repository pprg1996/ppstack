# Maintaining ppstack

This document is for repository maintainers. Installed-skill consumers should use `npx skills update` instead.

## Run the maintainer skill

From a ppstack checkout, install the internal skill deliberately:

```bash
INSTALL_INTERNAL_SKILLS=1 \
  npx skills add ./maintainer-skills/update-ppstack \
  --skill update-ppstack
```

You can also give `maintainer-skills/update-ppstack/SKILL.md` directly to a harness that supports local skills. The workflow itself is harness-neutral.

## Scope and replacements

Use `docs/gpt6-migration.md` for the owner's current migration direction. ppstack may replace overlapping third-party skills; the earlier companion-only restriction is retired. Document each replacement's coverage, provenance, and validation before changing the active installation.

## Check upstream

```bash
python3 scripts/upstream_sync.py check
```

The command compares `upstream.lock.json` with the current `main` revision of `cursor/plugins`. It exits with status 1 when an update exists.

## Audit a checkout

Use an existing checkout or make a sparse one outside this repository, then run:

```bash
python3 scripts/upstream_sync.py audit --source /path/to/cursor-plugins
```

The audit reports added, removed, changed, and unchanged upstream skills. It also fails when `selection.json` no longer classifies the exact upstream inventory.

## Apply an update

Read the upstream diff between the locked and current commits. Apply selected-skill changes semantically. Do not overwrite ppstack's portability adaptations with upstream harness assumptions.

Classify every new upstream skill. `pending` is acceptable while evaluating a change locally, but a published revision should resolve pending entries to `included`, `adapted`, or `excluded`.

Validate before advancing the lock:

```bash
python3 scripts/validate_repo.py
```

After the adaptations and classifications reflect the inspected upstream revision, record it:

```bash
python3 scripts/upstream_sync.py record --source /path/to/cursor-plugins
```

Rerun the audit and validation, then test normal `npx skills` discovery. Review the full diff before committing. Publication remains a separate, explicitly authorized action.
