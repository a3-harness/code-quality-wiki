<!-- generated-from: a3-code-quality; do not edit -->

# Operate coding agents as an engineering system

A coding harness is the control plane around a model. It selects and scopes instructions, exposes tools, mediates permissions, connects external systems, delegates work, preserves state, and decides what evidence reaches a human. Manage that control plane with the same rigor as build and deployment infrastructure.

## Capability model

| Capability | Purpose | Preferred evidence |
| --- | --- | --- |
| Task contract | Goal, context, constraints, done condition | Issue/plan and acceptance checks |
| Durable instructions | Repository layout, commands, conventions, boundaries | Concise versioned guidance |
| Skills | Reusable, on-demand workflow | Trigger fixtures and output contracts |
| Mechanical policy | Enforce action authority | Sandbox, permissions, command rules |
| Hooks | Enforce or observe lifecycle events | Contract tests and trusted definitions |
| External tools | Live data and controlled actions | MCP registry and authorization tests |
| Delegation | Isolate specialist work/context | Role, ownership, tool limits, aggregation tests |
| Workspace isolation | Separate concurrent changes | Worktrees/sandboxes and conflict checks |
| Validation | Establish behavior | Unit/integration/e2e/security checks |
| Observability | Explain what happened | Redacted versioned trace events |
| Evaluation | Decide whether to promote | Labeled tasks, safety cases, denominators |
| Feedback | Improve repeat failures | Reviewed policy/skill/eval changes |

## Put policy on the right surface

Use the task prompt for one outcome; repository instructions for durable local facts; skills for repeated methods; deterministic configuration, rules, permissions, and hooks for enforcement; MCP for authorized external capabilities; and specialist agents for bounded delegation. Do not place a mandatory safety control only in prose.

Maintain one canonical statement of shared engineering intent. Harness adapters should be thin and explicit about vendor differences. Never assume similarly named hooks, permissions, memories, or agents have identical precedence or failure semantics.

## Context engineering

Context is a budget and a trust boundary. Load the smallest authoritative material that supports the task. Keep root instructions concise; retrieve specialist guidance and detailed workflows on demand. Quote untrusted repository, issue, log, and tool content as data. Preserve task goal, constraints, decisions, outstanding work, and validation evidence across compaction or delegation.

Measure instruction bytes/tokens, retrieved units, repeated content, contradictions, tool-output volume, and handoff loss. More context can reduce quality when it hides the operative rule.

## Action security

Grant the least capability needed for the current task. Separate what the model may propose from what policy permits. Sandbox file and network access, require approval for consequential external state, validate targets before destructive operations, and prefer recoverable actions. Treat project-local hooks, MCP servers, plugins, and scripts as executable supply chain that requires trust and review.

## Delegation and concurrency

Delegate bounded, independently verifiable work. Give each agent clear ownership, inputs, outputs, tool restrictions, and stopping conditions. Use isolated worktrees for overlapping write tasks. The parent remains accountable for integration, conflicts, test evidence, and final decisions. Parallel activity is valuable only when correctness and coordination cost are measured.

## Evaluation loop

Evaluate layers separately:

1. Retrieval: did the harness select the right instructions and knowledge?
2. Planning: did it identify constraints, risks, and tests?
3. Action: did it use allowed tools and respect approvals?
4. Implementation: did the change satisfy behavior and architecture?
5. Verification: did it run the strongest available evaluators?
6. Communication: did it report uncertainty, changes, and remaining risk accurately?
7. Operations: were latency, cost, failure, recovery, and human effort acceptable?

Use representative, adversarial, absence-of-evidence, and recovery cases. Record denominators and versions. A model or harness upgrade is a new configuration requiring regression evaluation.

## Improvement loop

When an agent fails repeatedly, classify the cause before adding prose:

```text
missing project fact       → repository instruction or project inventory
repeated workflow          → skill
mechanically decidable     → formatter, validator, rule, permission, or hook
missing external context   → governed MCP/resource
specialist noisy task      → bounded subagent
model behavior variance    → prompt/model/tool change plus eval
ambiguous ownership        → human decision and architecture record
```

Promote a correction only after evidence shows it is general enough. Remove stale rules and skills; harness configuration is production code, not an append-only prompt.

## Adoption sequence

1. Audit current surfaces and authority.
2. Establish concise canonical instructions and deterministic validation.
3. Add least-privilege policy for high-impact actions.
4. Convert repeated workflows into tested skills.
5. Add tested hooks only for clear enforcement or observation needs.
6. Govern external tools before connecting them.
7. Introduce bounded subagents and workspace isolation.
8. Establish trace and evaluation contracts.
9. Compare harnesses on identical tasks before claiming portability.
10. Feed failures into reviewed policy, skills, and evals.

---

Canonical knowledge ID: `process-ai-software-engineering`  
Reference IDs: `openai-codex-best-practices`, `openai-codex-security`, `anthropic-claude-settings`, `anthropic-claude-subagents`, `nist-ai-rmf-gai`

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
