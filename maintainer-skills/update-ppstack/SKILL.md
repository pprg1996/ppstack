---
name: update-ppstack
description: "Synchronize a ppstack checkout with the upstream pstack skill collection while preserving ppstack's portability and companion scope. For ppstack maintainers only."
metadata:
  internal: true
---

# Update ppstack

Update the ppstack source repository from `cursor/plugins/pstack`. This is a maintainer workflow. Consumers update installed skills with their skill manager.

## Contract

- Work only in a clean ppstack checkout, or preserve and report unrelated changes.
- Treat `selection.json` as the classification source of truth. Every upstream skill appears exactly once as `included`, `adapted`, `excluded`, or `pending`.
- Keep public skills independent of Cursor paths, plugin manifests, named worker APIs, hard-coded model slugs, and guaranteed access to history or connectors.
- Describe optional capabilities and provide a sequential or reduced-evidence fallback.
- Preserve attribution and the upstream MIT license.
- Keep the companion boundary: Matt's skills organize project work; ppstack supplies tactical workflows. Exclude duplicate names, equivalent objectives, personal modes, and global orchestrators.
- Produce a reviewable diff. Do not commit or push unless the user separately authorizes publication.

## Check

Run:

```bash
python3 scripts/upstream_sync.py check
```

Exit code 0 means the lock matches upstream `main`. Exit code 1 means an update is available.

## Update

1. Record the working-tree state and the old commit from `upstream.lock.json`.
2. Obtain a current `cursor/plugins` checkout. Use sparse checkout for `pstack` when cloning a new copy.
3. Run `python3 scripts/upstream_sync.py audit --source <checkout>`. Account for every added, removed, and changed upstream skill.
4. Read the upstream diff from the locked commit to the current commit. For selected skills, reapply the upstream change semantically instead of overwriting ppstack's portability adaptations. For excluded or pending skills, update the reason if the upstream objective changed.
5. Update `selection.json` until its keys exactly match the upstream inventory. A new skill starts as `pending` only while its overlap and portability are being evaluated; resolve it before publishing a release.
6. Run `python3 scripts/validate_repo.py` and the available skill-package validation. Fix every portability or inventory error.
7. After the public files reflect the inspected upstream revision, run `python3 scripts/upstream_sync.py record --source <checkout>`.
8. Rerun `audit`, repository validation, and public skill discovery. Review the full diff, especially deletions and changed reasons.

## Handoff

Report the old and new upstream commits, added/removed/changed skills, adaptations made, exclusions reconsidered, validation results, and unresolved gaps. The lock advances only after every upstream skill is classified and every selected change has been reviewed.
