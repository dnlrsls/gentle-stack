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

Preserve the compact work context on return: task/ticket, criteria addressed, candidate, checks with their environment and result, unresolved findings, and next action. Reuse valid received evidence rather than rerunning exploration or tests simply because ownership changed. Explain applicability if the integrated candidate differs.

Discover Engram operations and save ownership, transfer references, decisions, and integration outcome. Mark pending transfers as pending. If persistence is unavailable, return an explicitly unsaved continuation record. Never claim independence without an actual separate executor.

The initiating agent normally owns memory consolidation. Workers return durable learning and any memory IDs already written; do not make both sides save the same handoff. Resolve project and session through supported operations, use only bound or registered session IDs, and read back uncertain writes before retrying. Handle returned conflicts and disclose unresolved detection. Do not enable cloud for local memory.
