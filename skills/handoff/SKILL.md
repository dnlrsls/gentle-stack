---
name: handoff
description: Prepare or execute a bounded transfer to another agent or session with faithful requirements, clear ownership, dependencies, and a return contract.
---

# Handoff

Transfer responsibility without making the receiver reconstruct requirements. Preparing a handoff does not require launching an agent.

Retrieve relevant Engram decisions and inspect current task state. Identify the transfer reason: requested delegation, independent parallel work, expertise, continuation, or context limits. When transfer was not requested and direct execution is simpler, keep work local.

Include:

- Outcome, acceptance requirements, and ticket/spec references. Preserve exact strings and constraints; avoid lossy requirement summaries.
- Repository, branch/candidate, current state, allowed edit surfaces, and exclusions.
- Decisions, evidence, dependencies, and Engram references. Include essential facts directly if the receiver cannot access referenced sources.
- Available capabilities and permissions, expected verification, and a return contract covering changes, evidence, blockers, and reusable learning.

Use the host's delegation mechanism only when supported and authorized. Check receiver access; tools, permissions, memory access, and worktrees do not automatically transfer. Parallel writers need disjoint edit surfaces or actual isolation. Keep dependent units ordered. If execution is unavailable, return the prepared handoff and capability gap without claiming launch.

The initiating agent owns integration. On return, inspect changes and evidence and check combined behavior as needed. Worker completion does not itself establish acceptance.

Discover Engram operations and save ownership, transfer references, decisions, and integration outcome. Mark pending transfers as pending. If persistence is unavailable, return an explicitly unsaved continuation record. Never claim independence without an actual separate executor.
