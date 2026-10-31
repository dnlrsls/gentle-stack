---
name: work-breakdown
description: Convert a feature, refactor, or migration objective into work-unit tickets with acceptance checks and dependencies. Use for backlog preparation or ticket creation rather than implementation.
---

# Work Breakdown

Produce coherent units another executor can complete without reconstructing the original discussion.

## Define the work

Retrieve relevant Engram context; inspect current code and existing tickets. Establish the outcome, exclusions, constraints, and acceptance conditions. For refactors, explicitly identify behavior and public contracts that must remain unchanged. Ask only about unresolved decisions that materially change the breakdown.

Split by independently verifiable outcomes or migration boundaries. Keep code, tests, and necessary documentation for one behavior together. A dependent unit is not parallel work. Note shared edit surfaces and prerequisites. Keep small objectives as a single ticket when splitting adds no value.

Each ticket includes title, outcome, scope and exclusions, relevant references, acceptance criteria, verification approach, and dependencies. Distinguish evidence from assumptions.

## Publish and remember

Use the established tracker. Publish when ticket creation is requested or already authorized; proposal-only requests produce drafts. If the target tracker is ambiguous, prepare drafts before asking the necessary targeted question.

Check for equivalent tickets before creation. Retain returned IDs and URLs after every successful write. On partial failure, reconcile remote state and retry only missing units. Link dependencies with supported tracker features or explicit URLs, updating earlier tickets once later URLs exist. Never invent issue numbers.

Return ticket URLs or drafts, execution order, parallel opportunities, and blockers. Save rationale, dependencies, and ticket references in Engram; the tracker owns status. Discover available tools rather than assuming a provider. Disclose unavailable tracker or memory operations and return unpublished or unsaved material explicitly. Ticket creation does not start implementation.
