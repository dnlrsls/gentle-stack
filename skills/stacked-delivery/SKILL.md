---
name: stacked-delivery
description: Plan, create, or maintain dependent pull requests with explicit branch bases and per-layer evidence. Use when one delivery needs multiple ordered PRs rather than a single PR or independent tickets.
---

# Stacked Delivery

Make dependent changes reviewable without losing the relationship between layers. Use one PR when a stack adds no review or integration value. This capability specializes delivery; it does not introduce a mandatory workflow or require a particular hosting service.

## Establish the stack

Determine whether the request authorizes planning, local branch creation, publication, restacking, or merging. Reuse authorization already given. Inspect repository policy, worktree state, local and remote branches, existing PRs, and applicable Engram context. Preserve unrelated user work. If remote inspection is unavailable, label the topology unconfirmed and provide a plan rather than guessing remote state.

Split by coherent, testable outcomes that can be reviewed against their immediate parent. A layer contains its behavior, tests, and necessary documentation. Define a stack map in the existing response, tracker, or PR descriptions with:

- Layer identity and outcome, linked ticket if present, and dependencies.
- Head branch and immediate base branch, plus observed commit IDs.
- Local or published state and PR URL when one exists.
- Acceptance criteria, validation/review evidence, and next action.

For a linear stack, the first PR targets the integration branch and each later PR targets the preceding layer's branch. Independent changes target the integration branch separately. Branch topology is not proof of semantic independence or acceptance.

## Build and publish

Create layers in dependency order. Inspect each diff against its declared base so downstream reviews show the incremental change. Verify each layer in its dependency context; final combined checks do not automatically prove every intermediate layer works. RDD may review a layer's exact base/head candidate when requested or required by policy.

Before publication, check for existing branches and PRs to avoid duplicates. Publish only within scope, retaining returned URLs after each successful operation. If an operation fails or times out, inspect remote state before retrying; report completed and pending layers separately.

Explain the stack order and prerequisites in each PR using real links once available. Do not use automatic issue-closing keywords on a partial layer. Do not merge layers merely because the stack was published.

## Maintain and integrate

Before restacking after a parent edit or merge, read [restacking guidance](references/restacking.md). Check actual integration strategy and current topology; never assume a merged parent kept its commit identities. Changed bases or content require reassessing affected verification and review evidence, preserving historical identities.

Follow the project's integration order and completion rules. Close a ticket only when its full acceptance and required integration are satisfied. Confirm each result remotely before treating it as complete. Stop at an unresolved conflict, missing required authority, or ambiguous topology that evidence cannot resolve; retain the stack map and exact next action for recovery.

## Result and memory

Return the stack map or published URLs, incremental scope per layer, evidence, unresolved findings, and pending operations. No extra repository planning folder is required.

Save topology references, consequential integration decisions, and the next action in local Engram. Reuse current context and one coordinating memory owner. Use supported project/session resolution with only bound or registered IDs, read back uncertain saves, handle returned conflicts, and disclose unavailable memory. Engram records context; Git and the hosting service determine actual branch and PR state. Never enable cloud to repair local memory.
