---
name: odd
description: Implement authorized features, fixes, and refactors using Organic Driven Development, adapting exploration, tracking, and checks to uncertainty and resumability.
---

# Organic Driven Development

Keep intent, implementation, and observed evidence connected as work evolves. This skill guides development without installing an orchestrator or requiring a pipeline.

## Compose without restarting

Carry a compact work context between capabilities: task/ticket, acceptance criteria, candidate, evidence (criterion, procedure, result, candidate/environment), unresolved findings, next action, and Engram references. Reuse existing conversation and tickets; no new file or skill invocation is required. Omit fields that do not apply.

The coordinating agent owns memory for the task. Reuse relevant memory already retrieved, and consolidate significant updates at a checkpoint or completion rather than reading and saving once per skill. Resolve the actual workspace/project; use an existing bound session, or register one through supported operations if needed. Never pass an unregistered session ID or enable cloud to repair local memory. After an uncertain write, read back before retrying. Follow returned conflict handling and disclose incomplete persistence or conflict detection.

## Understand and size

Establish the outcome and existing authorization. Explanation and proposal requests remain read-only. Retrieve relevant Engram context and inspect current code and repository policy. Preserve exact strings and examples when they are acceptance requirements.

Resolve technical uncertainties through evidence. Ask about real unresolved product decisions; reuse decisions already made.

Keep understood work lightweight when risk is contained and the request and diff provide enough context to resume. Use recoverable tracking when requirements, dependencies, external waits, or multiple sessions would otherwise lose intent. Reuse tickets and Engram; do not automatically create task folders or duplicate plans.

## Implement and check

- Work in coherent behavior units with their tests and necessary documentation. Adapt to new evidence within the authorized outcome.
- Prefer a failing behavior test first when a runnable test and an independently grounded expected result exist. Otherwise use applicable functional checks and explain their limits.
- Delegate only for a concrete benefit such as independent parallel work or a context boundary, when supported and authorized. Small work stays with the current executor.
- Reuse existing evidence while its candidate and assumptions remain valid. Exploration, verification, handoff, and RDD skills can help when needed; they are not mandatory stages.

Before review, identify the candidate and pass the acceptance criteria and existing evidence instead of re-explaining the task. After a review finding, correct the affected unit within scope, identify the revised candidate, and rerun affected checks and review surfaces. Retain unaffected evidence with a reason for its applicability; do not restart the entire workflow. A blocked criterion is not a completed criterion.

## Close or checkpoint

Compare results with acceptance criteria. Report the change, observed checks, failures, unverified claims, and remaining work. Commit or publish only within existing authorization.

For ticketed work, keep the ticket reference and report criteria met, failed, or unverified. Follow tracker conventions for in-progress and review states. Leave the ticket open when integration is pending unless the project's completion policy says otherwise; delivery records the final integration result.

Discover the available Engram integration and save significant decisions, candidate and evidence references, and the next action. Keep ticket updates consistent with actual completion. Exclude secrets and raw transcripts. If memory is unavailable, disclose it and return an unsaved continuation record.
