<!-- generated-from: a3-code-quality; do not edit -->

# AI software engineering for coding harnesses

AI software engineering treats a coding agent and its harness as a production development system: instructions, context, models, tools, permissions, hooks, external connectors, delegated agents, workspaces, validation, traces, and human decisions all affect the result. A capable model does not compensate for missing repository context, ambiguous authority, unsafe tools, or absent evaluation.

## Failure mechanisms

- Durable rules live only in chat prompts, so they disappear across sessions, users, or compaction.
- Instruction files grow into conflicting manuals that consume context and reduce compliance.
- The harness can edit or execute broadly while safety exists only as prose rather than sandbox, permission, rule, or hook enforcement.
- Vendor-specific files encode the only copy of project intent, making another harness incomplete or divergent.
- MCP servers expose live data or side effects without ownership, data classification, authorization, and approval contracts.
- Subagents receive excessive tools, insufficient context, or overlapping file ownership and return conclusions that the parent cannot verify.
- Hooks are trusted as controls without tests for event matching, input, output, timeout, failure, and bypass behavior.
- Agents optimize for “task completed” while tests, review, security, latency, token use, and human correction are not measured.
- Repository content injects instructions into prompts or tool output and is treated as authority.
- Long conversations accumulate stale decisions; compaction or delegation drops critical constraints.

## Review questions and evidence

Ask which intent belongs in a prompt, repository instruction, skill, mechanical policy, hook, MCP server, specialist agent, or scheduled workflow. Verify the actual precedence and scope supported by the selected harness rather than assuming names are portable.

Inspect:

- concise root and nested instruction files;
- deterministic build, test, lint, type, security, and end-to-end commands;
- sandbox, network, approval, and destructive-action policies;
- hook definitions plus contract tests;
- skill descriptions, triggers, inputs, outputs, and fixtures;
- subagent tool/permission boundaries and file ownership;
- MCP purpose, owner, data class, actions, authentication, and failure behavior;
- prompt/model/tool versions and privacy-aware traces;
- labeled task, safety, recovery, and regression evaluations;
- evidence that human corrections feed new tests or reviewed guidance.

The strongest evidence is behavior under representative and adversarial tasks, not file presence. Run offline fixtures first, then controlled live harness evaluations in isolated worktrees with bounded permissions.

## Counterexample

A repository without Claude-specific settings is not necessarily unsuitable for Claude Code if its canonical engineering policy, build commands, and safety controls are accessible through a maintained adapter. Conversely, the presence of both `AGENTS.md` and `CLAUDE.md` is not maturity if the files disagree or contain unenforced aspirations.

Likewise, a broad tool set is not automatically unsafe for every task. The defect is authority that exceeds the task’s need without isolation, approval, observability, and recovery.

## Worked case

A repository has `AGENTS.md`, reusable skills, Codex hooks, command rules, specialist roles, and validation scripts. A structural audit finds strong Codex coverage but no Claude adapter, no dedicated hook tests, no portable trace schema, and no explicit tool restrictions on specialist agents.

The team keeps `AGENTS.md` as the canonical shared policy, generates a concise `CLAUDE.md` adapter that imports or points to the same rules where supported, adds fixture tests for hooks and agent constraints, defines a vendor-neutral trace/event contract, and evaluates the same tasks through both harnesses. Differences remain explicit in adapter files; shared intent is not duplicated.

## Tool-assisted review

Run `qreview harness-audit PATH --format json` to collect structural evidence and `--format markdown` for a remediation brief. The audit does not execute hooks, servers, or target code and does not prove instruction following.

Use deterministic fixtures to simulate hook inputs, permission decisions, malformed tool results, injection, missing context, validation failure, and subagent conflicts. Optional live evaluations should use disposable worktrees, fixed task suites, bounded tokens/time, least privilege, trace redaction, and human scoring.

## References

- `openai-codex-best-practices`
- `openai-codex-agents-md`
- `openai-codex-security`
- `openai-codex-hooks`
- `anthropic-claude-memory`
- `anthropic-claude-hooks`
- `anthropic-claude-settings`
- `anthropic-claude-subagents`
- `anthropic-claude-mcp`
- `nist-ssdf`
- `nist-ai-rmf-gai`

---

Canonical knowledge ID: `ai-software-engineering`  
Reference IDs: `openai-codex-best-practices`, `openai-codex-agents-md`, `openai-codex-security`, `openai-codex-hooks`, `anthropic-claude-memory`, `anthropic-claude-hooks`, `anthropic-claude-settings`, `anthropic-claude-subagents`, `anthropic-claude-mcp`, `nist-ssdf`, `nist-ai-rmf-gai`

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
