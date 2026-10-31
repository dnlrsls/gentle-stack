---
name: rdd
description: Review an identified code candidate with risk-proportionate lenses and bind findings to that version. Use for receipt-driven review rather than execution testing or implementation.
---

# Receipt-Driven Review

Adapt Receipt-Driven Development into an on-demand review with an evidence receipt. This skill does not reproduce Gentle AI's native state engine, enforce immutability, or grant delivery authority.

## Identify the candidate

Read requirements, relevant Engram decisions, and verification evidence. Record repository, base and head commits, and review scope. For dirty work, capture a diff/content fingerprint including relevant untracked files and baseline; HEAD alone cannot identify uncommitted changes.

Use an available read-only snapshot or isolated view when practical. Otherwise compare candidate identity before and after review. If identity cannot be established, disclose that the review is not version-bound.

## Review

Choose relevant lenses based on concrete risks and the requested scope:

- **Risk:** security, privacy, data integrity, compatibility, and side effects.
- **Resilience:** failures, recovery, retries, concurrency, and partial completion.
- **Readability:** unclear contracts or structure that creates maintenance defects.
- **Reliability:** behavior, invariants, test relevance, and operational assumptions.

Do not require every lens for every change. Cite actionable findings with location, triggering scenario, consequence, and severity. Separate defects from uncertainties and preferences. Passing tests do not prove every reviewed claim.

Keep review read-only unless corrections are authorized. If they are, bound them to findings, identify the new candidate, rerun affected checks, and review changed surfaces. Stop at resolved findings, documented remaining issues, or a needed decision; avoid unbounded correction cycles.

## Receipt

Return candidate identity, scope and lenses, evidence, findings, gaps, and reviewer provenance. Distinguish self-review from actual independent review. Recheck candidate identity; mark affected conclusions stale and reassess if it changed. No findings means none found within the stated scope, not guaranteed correctness.

Discover Engram operations and save the receipt summary and references without requiring a repository file. Disclose unavailable persistence and return the unsaved receipt. The receipt does not authorize commit, merge, release, or deployment.
