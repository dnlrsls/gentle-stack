---
name: verify
description: Execute checks against acceptance criteria, reproduce defects, and assess regressions. Use to establish behavioral evidence rather than perform a code review.
---

# Verify

Demonstrate behavior against requirements, established contracts, or an independent reference. Passing tests whose expectations merely repeat implementation assumptions offer weak evidence.

## Establish the target

Read the request, relevant Engram decisions, current code, and check configuration. Identify the candidate by commit and clean-worktree status, or a diff/content fingerprint covering tracked and relevant untracked files. Record relevant environment assumptions.

For a reproducible Git candidate, use the optional bundled helper: `python <skill-directory>/scripts/candidate.py --repo <project-directory> --base <review-base>`. Resolve the base once and reuse its returned full commit ID. The helper fingerprints HEAD, the index, and tracked plus non-ignored untracked working files, including deletions, modes, and symlinks. See [candidate limitations](references/candidate.md) when invoking it or choosing an alternative. It requires Python 3 and Git; another tool may implement the documented identity contract.

Map acceptance criteria and affected contracts to meaningful checks. Shared state, data, security, concurrency, and irreversible effects warrant deeper coverage. Check count is not an objective.

## Execute

- Reuse relevant observed evidence for the same candidate and environment; label prior observations accurately.
- Reproduce reported defects when feasible. For an authorized fix, demonstrate that the regression check detects the original failure and passes after the change when practical.
- Run focused checks and relevant broader regression checks. Use disposable environments for side effects and respect execution permissions.
- Distinguish product failure, infrastructure failure, skipped checks, and inconclusive results. A command that did not execute cannot pass.
- When a fresh run disagrees with the current source, inspect execution inputs such as stale bytecode, build caches, installed packages, and background processes. Use a fresh disposable build/cache where needed; a changed source fingerprint alone does not prove the runner executed that source.
- Check-only requests do not authorize production-code fixes. Change tests only within the requested scope and report those changes.

Return candidate identity, criteria checked, commands or procedures, observed results, and gaps. If the candidate changes, reassess applicability and rerun affected checks before claiming coverage.

Check candidate identity before and after execution. Map each result to an acceptance criterion and record exit status or observed outcome plus relevant environment. A failed or skipped criterion remains unresolved. If a change affects only unrelated surfaces, retain earlier evidence with an explicit applicability reason; an old fingerprint never becomes a new observed run. Pass this evidence directly to ODD or RDD without a required report file.

Discover available Engram operations and save concise evidence references and reusable findings, excluding secrets and bulk logs. Disclose failed or unavailable persistence. Verification is independent only when a separate executor actually performed it.

For composed work, reuse current memory and let the coordinating agent save the checkpoint. For standalone persistence, resolve the actual project and use a bound or successfully registered session if needed. Read back uncertain writes before retrying, follow returned conflict handling, and never enable cloud to fix local memory access.
