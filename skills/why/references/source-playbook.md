# Evidence-source playbook

Search only sources the environment exposes. Use read-only operations unless the user separately authorized a write.

## Source control

- Trace the exact lines with blame, then inspect the introducing commit and surrounding history.
- Read pull-request descriptions, review threads, linked issues, tests, and later reverts.
- Follow renames and file moves before concluding that history is absent.

## Issues and project tracking

- Search symbols, feature names, error text, customer language, and linked commit or PR identifiers.
- Read parent initiatives and comments for scope changes, deadlines, compliance needs, and rejected approaches.
- Compare ticket status with shipped code instead of treating either as authoritative alone.

## Long-form documents

- Search ADRs, RFCs, specifications, postmortems, meeting notes, and project pages.
- Look for problem statements, alternatives, constraints, success metrics, and follow-up decisions.
- Check dates and superseding documents.

## Team discussions

- Search symbols, feature names, incident identifiers, PR links, and author names around the implementation window.
- Prefer full threads over isolated messages.
- Treat informal discussion as context unless shipped code or a recorded decision confirms it.

## Incidents and observability

- Match error signatures, stack frames, monitor names, thresholds, and timelines to the code change.
- Distinguish the symptom that triggered the work from the constraint the final design must preserve.
- Check whether the signal changed after deployment or later regressed.

## Error tracking

- Compare first-seen, last-seen, release, stack trace, and affected-version evidence.
- Check whether defensive code corresponds to an actual error path or only a hypothetical one.

## Product analytics

- Verify the dataset, population, time window, units, and aggregation behind a threshold or product decision.
- Prefer reproducible queries and numeric summaries over dashboard screenshots alone.
- Name retention gaps, schema drift, and missing populations.

## Coverage vocabulary

- **Found:** the search returned evidence relevant to the target.
- **Empty:** the source was searched with concrete keys and returned no relevant evidence.
- **Unavailable:** the environment had no access to the source.
- **Inconclusive:** the source contained related material that did not establish intent.
