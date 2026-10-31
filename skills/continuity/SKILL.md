---
name: continuity
description: Save, recover, or reconcile project and task context through Engram across sessions, interruptions, and agents. Use for explicit checkpoints and resumption.
---

# Continuity

Engram is the factory's persistent memory. Discover its available integration and supported operations without inventing tool names or assuming a filesystem location.

## Save

Use stable project and task identities, such as the repository and ticket URL. Search for an existing record before creating competing state. Preserve:

- Outcome, constraints, and acceptance requirements not recoverable elsewhere.
- Decisions and rationale, distinguishing facts from assumptions.
- Git/candidate references, ticket URLs, completed and pending work.
- Evidence references, blockers, and the next actionable step.

Store durable facts rather than transcripts. Exclude credentials, sensitive payloads, and bulk logs. Use supported update/link operations to supersede stale decisions while retaining useful rationale. Confirm writes through returned identifiers or readback before claiming persistence.

## Recover

Retrieve relevant project/task memories and reconcile them with current Git state, tracker status, and evidence. Engram explains intent and history; Git owns code versions, the tracker owns ticket status, and executed checks establish observed results.

Identify contradictions and stale evidence. Resolve from authoritative sources where possible and correct memory. Ask only when a consequential decision cannot be recovered. Do not restart completed work merely because the session changed.

Return recovered state, material discrepancies, and the next action. Resume-only requests do not authorize code changes.

## Missing memory

If Engram is unavailable or a write fails, disclose the limitation and return a portable checkpoint in the response. Do not silently substitute another persistence system, create task folders, or claim cross-session storage. Continue independent work; pause only decisions that depend on missing context and cannot safely be resolved.
