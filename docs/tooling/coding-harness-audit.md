<!-- generated-from: a3-code-quality; do not edit -->

# Constructing a coding-harness readiness audit

## Implementation status

**Built structural audit.** `qreview harness-audit` detects repository-scoped Codex, Claude Code, and portable agent surfaces, normalizes them into capabilities, and renders prioritized remediation. Behavioral live-agent evaluation, instruction contradiction analysis, trace capture, and adapter generation are planned.

## Architecture

```text
repository paths/config metadata
              ↓
        safe structural scanner
              ↓
portable capabilities + vendor evidence + findings
              ↓
     JSON contract or Markdown remediation plan
              ↓
 fixture behavioral evals → isolated live harness evals → reviewed promotion
```

The scanner never executes target commands, hooks, MCP servers, imports, or validation. It emits paths, counts, event names, and bounded metadata—not secret values or complete command bodies.

## Core algorithm

```text
AUDIT_HARNESS(root):
  files ← WALK(root) excluding VCS, dependencies, builds, caches, and symlinks
  instructions ← FIND AGENTS.md and CLAUDE.md; record scope/size/validation language
  skills ← FIND SKILL.md; validate activation metadata
  agents ← FIND Codex/Claude agent definitions; detect explicit tool boundaries
  hooks ← PARSE event names and handler counts; locate scripts/tests
  policy ← COUNT Codex rule decisions and Claude permission classes
  mcp ← COUNT configured servers; find governance registry; never emit credentials
  validation ← FIND standard checks, CI, behavioral evals, and trace contracts
  findings ← APPLY stable evidence-backed checks
  return SORTED versioned contract + limitations

RENDER(audit):
  ASSERT supported schema
  print capability matrix
  print detected surfaces
  order findings by consequence then stable ID
  include evidence paths, remediation, and structural limitations
```

## Failure handling

Malformed optional configuration becomes absent/unknown evidence rather than executable input. Unsupported audit schemas fail closed. Missing scripts, oversized instructions, broad permissions, and ungoverned MCP become explicit findings. A future strict mode should distinguish parse failure from absence and support policy-defined severity.

## Tests to build

Create synthetic empty, Codex-only, Claude-only, dual-harness, nested-instruction, malformed-config, missing-hook, wildcard-permission, secret-bearing MCP, oversized-guidance, invalid-skill, and subagent fixtures. Assert deterministic bytes, stable IDs, severity ordering, no secret leakage, and no execution.

Behavioral evaluation should run identical tasks through each harness in disposable worktrees. Score task success, instruction compliance, prohibited actions, approval quality, validation selection, citations, diff scope, recovery, human correction, time, tokens, and cost.

## Security considerations

Harness configuration is executable supply chain. Avoid following symlinks, importing target code, expanding variables, resolving credentials, or executing handlers. Treat configuration text as untrusted. Report capability and risk without reproducing secrets or enabling instructions. Live evaluation requires explicit consent, isolation, budgets, redaction, and cleanup.

## Planned extensions

Add strict parse diagnostics, nested instruction precedence, contradiction detection, token budgets, canonical policy/adapter rendering, hook contract test generation, MCP governance schema, trace/event schema, worktree checks, CI integration, versioned vendor capability adapters, and live cross-harness evaluation runners.

---

Canonical knowledge ID: `tool-harness-audit`  
Reference IDs: _See chapter links and canonical modules._

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
