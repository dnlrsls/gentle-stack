---
name: technical-docs
description: Create or revise technical documentation for a defined audience and task, grounding explanations and examples in current implementation. Use for guides, architecture explanations, and operational documentation rather than delivery summaries.
---

# Technical Docs

Help the intended reader complete a task or understand a system with the minimum necessary context. Favor accurate, navigable documentation over exhaustive descriptions of the code.

## Establish audience and evidence

Identify who will read the document, what they need to do or decide, where the document belongs, and the requested language. Follow existing project conventions and explicit user preferences; do not create a parallel documentation tree without a reason.

Inspect relevant implementation, configuration, tests, and current documentation. Reuse applicable Engram decisions already retrieved, verifying them against current sources. Separate shipped behavior, planned behavior, assumptions, and recommendations. If sources disagree, resolve the discrepancy or make it visible rather than documenting a desired behavior as implemented.

## Shape the document

- Lead with the reader's goal and the information needed to act. Put prerequisites before the step that needs them and explain expected outcomes.
- Separate a runnable quick path from conditional detail. Link deeper explanations rather than forcing every reader through architecture and background first.
- Document public contracts, invariants, ownership boundaries, and consequential failure modes. Include rationale when it prevents a likely mistake, without narrating every internal function.
- Use examples from supported behavior, with explicit placeholders for unavailable credentials and environment-specific values. Avoid universal installation paths, tool names, or commands that only work on one host unless the scope says so.
- Use diagrams only when they clarify structure or behavior. Keep labels consistent with the implementation and explain what an arrow means.
- Update existing canonical information and its references rather than copying facts into multiple documents. Preserve working links and anchors where practical; inspect inbound references before relocating content.

## Validate and deliver

Check local links, referenced paths, command syntax, and examples against the current version. Run safe examples or available documentation checks when they meaningfully validate the content. Do not run destructive examples or publish changes to external systems solely to validate prose. Label unexecuted examples and remaining gaps; a successful Markdown build alone does not establish correctness.

For operational guidance, distinguish observation, diagnosis, and repair, including how to confirm the result. For architecture guidance, make current boundaries and tradeoffs explicit; do not turn documentation work into an unrequested redesign.

Return the changed documents, intended reader outcome, validation performed, and material uncertainties. A documentation request does not itself authorize implementation changes or external publication. The deliver capability may prepare a requested PR without becoming a required stage.

## Memory

Save significant terminology, documentation decisions, source references, and unresolved gaps in local Engram. Keep canonical documentation in the repository; memory holds context and references rather than a second manual. In composed work, let the coordinating agent consolidate the checkpoint. Resolve project/session through supported operations, use only bound or registered sessions, read back uncertain saves, handle returned conflicts, and disclose unavailable persistence. Do not enable cloud for local memory.
