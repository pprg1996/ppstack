---
name: recall
description: "Reconstruct recent working context from the conversation, available history, repository state, and connected records. Use for 'recall my work on X', 'catch me up', 'where did I leave off', or before resuming earlier work."
---

# Recall

Rebuild the user's recent working context and return a tight capsule of where things stand now and what to do next.

Context can live in the current conversation, harness-provided memory or history, repository state, source-control history, issues, team discussions, documents, incidents, and observability. Treat every source as optional. Never invent a location or claim coverage of a source the environment cannot expose.

## Evidence ladder

1. **Scope.** Pin the topic, workspace, and time window. Default "recent" to the last seven days. Never read another workspace's private history unless the user asked for it.
2. **Given context.** Use a complete state capsule from the user without re-mining it.
3. **Conversation and history.** Search the current conversation, then any history or memory the harness exposes. Search for the topic before reading full records. Keep stable identifiers or links for each finding.
4. **Repository state.** Inspect the working tree, branches, commits, pull requests, and relevant files. Current state outranks old summaries.
5. **Shared record.** For a named feature, file, subsystem, or bug, search the connected issue tracker, team discussions, long-form documents, incidents, error tracking, and observability. Look for prior attempts, reversions, and unresolved user reports. The `why` skill provides deeper source guidance when installed.
6. **Gaps.** Name every unavailable evidence category that could materially change the answer. Continue with the sources that exist.

Parallelize independent searches when isolated workers are available. Otherwise search sequentially. Read only what the in-scope threads require.

## Verify the present

A transcript, ticket, or summary is history rather than current truth. Verify surfaced artifacts through the live tools available in the environment. When an answer hinges on what an earlier agent actually did, inspect the fullest available record instead of relying on a summary.

## Output contract

- **Capsule.** At most five bullets describing the work and its overall state.
- **Threads.** One line per thread with a concrete state such as merged, open PR, in flight, verified but uncommitted, reverted, or planned.
- **Problems.** At most five recurring or unresolved problems, including failed or reverted fixes.
- **Next move.** The single most useful concrete action.
- **Coverage gaps.** Only gaps that could alter the brief.

Keep adjacent work out unless it blocks the named topic. Cite findings with their stable record identifiers. Sanitize private context before public output.
