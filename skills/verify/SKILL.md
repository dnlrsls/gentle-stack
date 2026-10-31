---
name: verify
description: Execute checks against acceptance criteria, reproduce defects, and assess regressions. Use to establish behavioral evidence rather than perform a code review.
---

# Verify

Demonstrate behavior against requirements, established contracts, or an independent reference. Passing tests whose expectations merely repeat implementation assumptions offer weak evidence.

## Establish the target

Read the request, relevant Engram decisions, current code, and check configuration. Identify the candidate by commit and clean-worktree status, or a diff/content fingerprint covering tracked and relevant untracked files. Record relevant environment assumptions.

Map acceptance criteria and affected contracts to meaningful checks. Shared state, data, security, concurrency, and irreversible effects warrant deeper coverage. Check count is not an objective.

## Execute

- Reuse relevant observed evidence for the same candidate and environment; label prior observations accurately.
- Reproduce reported defects when feasible. For an authorized fix, demonstrate that the regression check detects the original failure and passes after the change when practical.
- Run focused checks and relevant broader regression checks. Use disposable environments for side effects and respect execution permissions.
- Distinguish product failure, infrastructure failure, skipped checks, and inconclusive results. A command that did not execute cannot pass.
- Check-only requests do not authorize production-code fixes. Change tests only within the requested scope and report those changes.

Return candidate identity, criteria checked, commands or procedures, observed results, and gaps. If the candidate changes, reassess applicability and rerun affected checks before claiming coverage.

Discover available Engram operations and save concise evidence references and reusable findings, excluding secrets and bulk logs. Disclose failed or unavailable persistence. Verification is independent only when a separate executor actually performed it.
