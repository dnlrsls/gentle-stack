# Restacking dependent PRs

Read this when a parent layer changes or merges, or when a downstream PR must change base. Planning a stack does not require restacking it.

## Inspect before choosing a strategy

Record current branch heads, the old dependency boundary, the new destination, remote tracking state, worktree status, and open PR bases. Inspect the actual parent merge: merge commits, squash merges, and rebases can produce different ancestry. Do not infer ancestry from a closed PR or matching commit messages.

For a downstream layer, identify the exact commits owned by that layer relative to its old parent. When replaying them, exclude parent commits already integrated, including content integrated through a squash. If ownership is ambiguous, inspect diffs and history or stop with a concrete recovery question; do not replay the entire branch by guesswork.

## Preserve recoverability

Use an isolated worktree or a clean, appropriately owned branch. Preserve prior heads through a recoverable local reference before any authorized history rewrite. Do not stash, reset, clean, or overwrite unrelated user work as an incidental convenience. Creating a backup reference does not authorize a rewrite.

Choose the project's supported strategy: merging an updated parent, rebasing only the owned range, or creating a replacement branch/PR. Restacking permission is not automatically permission to rewrite a shared published branch. Use a non-rewriting alternative when suitable; otherwise obtain the missing authorization for that concrete operation.

For an authorized remote rewrite, verify the current remote head and use a lease tied to that observed head. Never use an unconditional force push. A lease rejection means remote state changed: inspect it before deciding how to proceed, rather than retrying with a new lease blindly.

## Reconcile and verify

After each successful operation, inspect the incremental diff and detect duplicated, missing, or accidentally reordered changes. Run affected layer checks and relevant combined checks. Update PR bases and dependency links through supported hosting tools, checking the actual results. Retargeting a PR alone does not remove ancestor commits from its branch.

Retain old evidence as historical. State why any check remains applicable or obtain new evidence for changed content and bases. Treat each layer separately so one failure does not erase already confirmed operations.

When a conflict prevents continuation, record branch, old/new base, operation in progress, completed layers, and pending layers. Abort only the operation started for this task when aborting is the appropriate recovery; do not reset another contributor's work. Do not claim the restack succeeded until local and remote topology agree.
