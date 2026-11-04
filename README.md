# Gentle Stack

Eleven agent-agnostic, on-demand skills for a software factory, with Engram as its persistent memory.

## Vision

Adapt the main capabilities of Gentle AI and Gentle Shell into focused, composable skills. The agent owns execution and coordination, skills provide methods, and Engram preserves knowledge. There is no mandatory pipeline or custom agent runtime.

Each skill should have a clear responsibility, explicit instructions, and the supporting resources needed to perform its task. The goal is to let developers adopt individual capabilities and combine them to suit their projects.

## Approach

- Identify the core capabilities and workflows in Gentle AI and Gentle Shell.
- Map each capability to a focused skill, documenting dependencies where needed.
- Write actionable instructions with clear inputs, expected outcomes, and validation steps.
- Include scripts, templates, or references when they help execute the workflow.
- Validate skills on real development tasks and improve them through community feedback.

## Project status

Eleven instruction-based skills are available, including skill improvement, technical documentation, and stacked delivery. They share compact work context, consolidated memory ownership, and ticket completion rules, with optional reproducible candidate helpers for review and verification. They are adapted workflows, not a drop-in replacement for Gentle AI's native RDD engine. The [v0.2 evaluation record](evaluations/v0.2.md) covers the original eight skills and helper checks; behavioral evaluation of the three additions and cross-agent evaluation remain pending. Iteration labels do not imply packaged releases.

## Skills

| Skill | Purpose |
| --- | --- |
| [explore](skills/explore/SKILL.md) | Understand code and resolve technical uncertainties. |
| [work-breakdown](skills/work-breakdown/SKILL.md) | Turn objectives into actionable work-unit tickets. |
| [odd](skills/odd/SKILL.md) | Implement changes through Organic Driven Development. |
| [verify](skills/verify/SKILL.md) | Check behavior and gather execution evidence. |
| [rdd](skills/rdd/SKILL.md) | Review an identified candidate and bind findings to that version. |
| [handoff](skills/handoff/SKILL.md) | Transfer bounded work with faithful requirements. |
| [continuity](skills/continuity/SKILL.md) | Save, recover, and reconcile context through Engram. |
| [deliver](skills/deliver/SKILL.md) | Prepare commits, pull requests, and delivery evidence. |
| [skill-improve](skills/skill-improve/SKILL.md) | Evaluate existing skills and improve them from observed failures. |
| [technical-docs](skills/technical-docs/SKILL.md) | Write and validate documentation for a defined reader and task. |
| [stacked-delivery](skills/stacked-delivery/SKILL.md) | Plan and maintain dependent PRs with per-layer evidence. |

## Installation and prerequisites

Clone this repository and register the desired folders under `skills/` using your agent's supported skill discovery mechanism. Each folder contains a standalone `SKILL.md`. Installation paths and invocation syntax depend on the host agent; there is no universal slash command.

If native discovery is unavailable, ask the agent to read the relevant `SKILL.md` directly and follow it for the task. These are instructions, not runtime enforcement.

Connect your existing Engram installation through your agent's supported integration. Skills discover available memory operations without assuming MCP tool names or CLI commands. They also need repository access and whatever tools the task requires. Ticket publication requires an authenticated tracker; actual delegation requires a supported executor. Skills do not install these dependencies or grant permissions.

If Engram is unavailable, skills disclose that limitation and return an unsaved checkpoint. They never silently replace Engram or claim persistence.

## Usage examples

Use these natural-language prompts when skills are discoverable. Otherwise include the corresponding `skills/<name>/SKILL.md` path. Ticket numbers below are illustrative.

### Create refactor tickets

> Use work-breakdown to plan a refactor of the payments module. Preserve its public API and existing behavior. Consult Engram and inspect the code. Create work-unit tickets in this repository's GitHub Issues, including acceptance checks and dependencies. Save decisions and ticket references in Engram. Do not implement the refactor yet.

Expected output: ticket URLs, execution order, dependencies, and an Engram reference. Ticket creation does not start implementation.

### Implement a unit

> Use odd to implement issue #12. Recover the relevant context from Engram, verify the acceptance criteria, and keep unrelated changes out of scope. Use other skills only when useful. Save the outcome and remaining work in Engram.

Expected output: an implemented change, observed checks, and explicit remaining work. Small changes require no task document or subagent.

### Review and deliver

> Use rdd to review the current change against main. Identify the exact candidate and focus on payment correctness and compatibility. Report findings and evidence. Keep this request read-only.

> Use deliver to prepare and publish a draft PR for the reviewed change. Confirm the evidence still matches the candidate, include validation results, and link the issue. Do not merge it.

### Resume work

> Use continuity to recover the payments refactor from Engram. Reconcile memory with Git and the tickets. Report the next actionable unit without changing code yet.

### Improve a skill

> Use skill-improve to audit work-breakdown. In this failed run, it split tests from implementation and produced tickets that could not be completed independently. Propose focused improvements and evaluation cases. Keep this request audit-only.

Expected output: evidence-backed findings and proposed changes, distinguishing a walkthrough from an executed evaluation. Editing, installing, and publishing remain separate actions unless authorized.

### Document a module

> Use technical-docs to update the payments guide for developers integrating this module. Inspect the current implementation, explain its contracts and rounding behavior, and validate safe examples. Reuse the existing documentation structure and save significant decisions in Engram.

### Prepare a PR stack

> Use stacked-delivery to plan two dependent PRs for the payments refactor: extract the fee helper, then migrate refund_fee. Identify each branch base, acceptance checks, and integration order. Return the plan without creating branches or publishing PRs.

For actual publication, explicitly request the desired actions, for example:

> Create the planned local branches and publish both as draft PRs. Link their dependencies and validate each layer. Do not merge or rewrite existing published history.

## Composition and sources of truth

Share task identity, requirements, candidate identity, evidence, and next actions as needed. Reuse existing context rather than creating a document at every boundary. Engram stores decisions, learning, and references; the tracker owns ticket status; Git owns code versions; executed checks establish observed results. Reconcile memory with these sources before relying on it.

ODD can explore and verify directly. RDD evaluates a specific candidate and its evidence; it does not replace behavioral checks. Changed candidates require reassessing affected evidence. Actual reviewer independence and immutable snapshots require tools that provide those properties.

Pass only the relevant work context: task/ticket, acceptance criteria, candidate, observed evidence and environment, unresolved findings, next action, and Engram references. Keep it in existing conversation, tickets, or memory; no new file is required. One coordinating agent consolidates durable memory updates. A skill switch alone does not trigger another memory read or write.

Local Engram is sufficient. Resolve project and session through supported integration operations, register a session only when necessary, and confirm writes. Uncertain saves are read back before retry; saved observations with incomplete conflict detection are not saved again. Do not enable cloud to repair local memory access.

Verification and review each bundle an optional, standalone [candidate helper](skills/rdd/scripts/candidate.py):

```text
python <skill-directory>/scripts/candidate.py --repo <project-directory> --base <review-base>
```

It needs Python 3 and Git. Reuse the returned resolved base commit and compare fingerprints before and after checks. It captures the index and tracked/non-ignored untracked working files, but not ignored inputs or execution environments. It refuses submodules instead of returning incomplete identity. See [coverage and limitations](skills/rdd/references/candidate.md). Neither the helper nor another skill is required to read or use these instructions.

For ticketed work, acceptance, review, and integration follow the project's existing completion policy. Opening a PR does not automatically close its ticket.

## Validation

```text
python -m unittest discover -s tests -v
```

These disposable-repository tests validate candidate-helper behavior. The [evaluation record](evaluations/v0.2.md) separately describes the refactor, evidence invalidation, and local Engram recovery exercises; they were author-directed, not independent agent trials.

## Initial roadmap

- Evaluate the skills on real development tasks and multiple agents.
- Exercise a complete ticket-to-delivery workflow with Engram.
- Improve instructions based on observed failures and coordination costs.

## Contributing

Contributions and ideas are welcome. Open an issue to suggest a feature, report a problem, or discuss the project's direction. For substantial changes, please start a discussion in an issue before submitting a pull request.

## Inspiration

[Gentle AI](https://github.com/Gentleman-Programming/gentle-ai) and [Gentle Shell](https://github.com/Gentleman-Programming/gentle-shell) are the inspiration for this project. These are original instruction-based adaptations of documented ideas. Gentle Stack is an independent initiative and does not imply affiliation with or endorsement by those projects.

## License

Gentle Stack is released under the [MIT License](LICENSE).
