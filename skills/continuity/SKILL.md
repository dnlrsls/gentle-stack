---
name: continuity
description: Save, recover, or reconcile project and task context through Engram across sessions, interruptions, and agents. Use for explicit checkpoints and resumption.
---

# Continuity

Engram is the factory's persistent memory. Discover its available integration and supported operations without inventing tool names or assuming a filesystem location.

## Establish memory access

Resolve project identity from the actual workspace and the integration's project resolver. Prefer an existing authoritative runtime session. Do not reuse a session from another project or pick the most recent of several ambiguous sessions. If the integration requires registration, register a fresh session for the current directory and use its ID only after successful registration. A detected project name alone is not proof that a write will accept that project.

On a project/session error, reconcile identity using supported operations and retry only a write known not to have persisted. If a timeout leaves the result unknown, search/read back before retrying. Local storage is sufficient; never enable cloud, enroll projects, or change synchronization settings to make memory work.

Use one memory owner for a composed task, normally the coordinating agent. Reuse context already retrieved in this session while still current. Contributors return memory-worthy facts to that owner, who consolidates significant decisions and checkpoints; switching skills alone does not require another read or write.

## Save

Use stable project and task identities, such as the repository and ticket URL. Search for an existing record before creating competing state. Preserve:

- Outcome, constraints, and acceptance requirements not recoverable elsewhere.
- Decisions and rationale, distinguishing facts from assumptions.
- Git/candidate references, ticket URLs, completed and pending work.
- Evidence references, blockers, and the next actionable step.

Store durable facts rather than transcripts. Exclude credentials, sensitive payloads, and bulk logs. Use supported update/link operations to supersede stale decisions while retaining useful rationale. Confirm writes through returned identifiers or readback before claiming persistence.

Use a stable topic key when supported, scoped to project and task, and preserve the returned memory ID. Retrieve a record before replacing it so an update does not discard unresolved requirements. If a save returns conflict candidates, inspect them and use supported judgment operations with their returned candidate IDs. A confirmed save with incomplete conflict detection is still saved: report the unresolved detection and do not duplicate the write. Current explicit user decisions resolve known choices; ask only for a consequential conflict the available evidence cannot settle, following the integration's requirements.

## Recover

Retrieve relevant project/task memories and reconcile them with current Git state, tracker status, and evidence. Engram explains intent and history; Git owns code versions, the tracker owns ticket status, and executed checks establish observed results.

Identify contradictions and stale evidence. Resolve from authoritative sources where possible and correct memory. Ask only when a consequential decision cannot be recovered. Do not restart completed work merely because the session changed.

Return recovered state, material discrepancies, and the next action. Resume-only requests do not authorize code changes.

For transfers, carry a compact work context: task/ticket reference, outcome and acceptance criteria, current candidate, evidence with its candidate and environment, unresolved findings, next action, and memory references. Omit irrelevant fields and reuse the conversation or ticket; this is an information contract, not a required file. Historical checks on an older candidate remain historical until applicability is established.

## Missing memory

If Engram is unavailable or a write fails, disclose the limitation and return a portable checkpoint in the response. Do not silently substitute another persistence system, create task folders, or claim cross-session storage. Continue independent work; pause only decisions that depend on missing context and cannot safely be resolved.
