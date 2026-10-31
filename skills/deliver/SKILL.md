---
name: deliver
description: Prepare coherent commits, pull requests, and delivery summaries, checking that validation and review evidence match the delivered candidate.
---

# Deliver

Determine the requested step: preparation, commit, push, PR publication, merge, release, or deployment. Act within existing authorization and repository policy without requesting permissions already granted.

## Prepare

- Retrieve relevant Engram decisions and ticket references. Inspect status, actual diff, base branch, and existing PRs. Preserve unrelated user work and stage only intended changes.
- Compare results with acceptance criteria. Confirm that verification and any review receipt match the intended candidate; reassess affected evidence after changes.
- Use coherent reviewable units when useful. Do not rewrite published history or split changes arbitrarily. No new task document is required.
- Describe the concrete problem, resulting behavior, observed validation, and material limitations. Use repository templates and link relevant tickets. Distinguish checks not run.

## Publish and close

Use available Git and tracker tools. Preparation-only requests produce drafts. Before retrying remote mutations, inspect remote state to avoid duplicate PRs or releases. Stop after the requested action or a concrete blocker; PR publication does not imply merge or deployment.

Confirm resulting commits, branches, and URLs. Update ticket state only when actual completion and project conventions support it; a PR need not close an issue immediately.

Discover Engram operations and save delivery and evidence references, decisions, and remaining work. Disclose unavailable persistence. If remote operations are unavailable, return prepared material and the blocker without claiming publication.
