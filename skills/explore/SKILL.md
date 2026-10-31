---
name: explore
description: Investigate a codebase or technical uncertainty and return evidence-backed findings, dependencies, and change points. Use for understanding rather than implementation.
---

# Explore

Resolve the question relevant to the requested outcome. Keep investigation read-only unless changes are also authorized.

1. Retrieve relevant Engram decisions for the project and task. Verify remembered claims against current code and documentation.
2. Follow relevant entry points, callers, contracts, shared state, and tests. Investigate enough to answer the question rather than inventorying the repository.
3. Separate observed facts, hypotheses, and unresolved product decisions. Cite code locations or primary documentation for material claims and identify freshness constraints.
4. Stop when the question is resolved or a concrete evidence gap prevents further progress. Return the answer, evidence, likely change surfaces, constraints, and consequential unknowns.

Save durable discoveries and source references in Engram. Use the available memory integration without assuming tool names. Exclude secrets and bulk logs. If memory is unavailable, return an explicitly unsaved summary; never claim persistence. No graph service or subagent is required.
