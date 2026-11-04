---
name: skill-improve
description: Evaluate and improve existing agent skills using observed failures and realistic task scenarios. Use for auditing skill behavior and instructions rather than creating a new skill from scratch.
---

# Skill Improve

Improve a skill's decisions and observable outcomes while preserving its intended scope. More instructions are useful only when they solve a demonstrated problem.

## Establish the problem

Identify the target skill, its intended consumers, the requested mode (audit or edit), and the relevant version. Read its entrypoint and only the supporting resources used by the workflow. Retrieve relevant Engram findings if they are not already in the current context.

Use reported runs, artifacts, and user expectations to distinguish an instruction defect from a missing tool, host limitation, or ambiguous product decision. Do not promise that prose can enforce isolation, permissions, persistence, or reviewer independence.

Inspect discovery and routing as well as execution: a vague description can select the skill for unrelated work, while a narrow one can miss its actual task. Preserve agent portability unless the skill explicitly targets a particular host.

## Evaluate

- Choose representative cases, including the reported failure and an adjacent case where the proposed restriction should not apply. Define observable acceptance conditions before changing instructions.
- Reproduce the failure in a disposable workspace when practical. Use drafts or a sandbox for external mutations; evaluation does not authorize publishing tickets, spending on additional agents, or changing real project configuration.
- Separate structural validation, manual instruction walkthroughs, actual task execution, and independent evaluation. Do not claim a scenario passed because the text mentions the expected rule.
- Use a separate evaluator only when supported and authorized. Give it the request, skill version, and necessary raw artifacts without supplying the intended answer. If independence is unavailable, label the evaluation author-directed.

## Improve and check

For an audit-only request, return findings and proposed edits. For authorized changes, make the smallest change supported by evidence. Prefer removing duplication, clarifying a decision boundary, or adding a focused reference over introducing universal gates and new files.

Keep skill names, descriptions, and resource paths consistent. Preserve standalone installation: a sibling skill can be an optional collaborator, never an undeclared required file. Check affected links and frontmatter with available validators; execute changed scripts. Repeat behavioral checks relevant to the change, retaining unaffected evidence with its original scope. Avoid wording-matching tests that merely echo the instructions.

Stop when the requested defect is addressed, remaining findings are documented, or a concrete blocker prevents evaluation. Do not automatically modify unrelated skills, installed copies, or host configuration.

## Result and memory

Return the original problem, changes or audit findings, evidence before and after, the skill version examined, and untested cases. Publishing or installing changes follows the user's existing authorization.

Save durable failure patterns, decisions, and evaluation references in local Engram. In composed work, return them to the coordinating memory owner rather than saving a duplicate checkpoint. Resolve the actual project and use only a bound or successfully registered session if required. Read back uncertain saves before retrying, handle returned conflicts through supported operations, and disclose unavailable persistence. Never enable cloud to repair local memory.
