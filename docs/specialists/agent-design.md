<!-- generated-from: a3-code-quality; do not edit -->

# Agent design

Agent design decides whether nondeterministic model reasoning and tools are justified, then defines goals, state, tools, permissions, stopping conditions, and human control. Use deterministic software when rules and inputs are sufficiently structured.

## Failure mechanisms

- An agent acts beyond the user’s intent or without meaningful approval.
- Tool descriptions, results, or retrieved documents inject control instructions.
- Multi-agent decomposition multiplies context loss, cost, and inconsistent authority.
- Memory retains sensitive, stale, or incorrect information.
- The loop lacks budgets, termination, or a recoverable state machine.

## Review questions and evidence

Ask why an agent is needed, what each tool can read/write, where authority changes, how state is validated, and when the system stops or escalates. Test ambiguous intent, denied tools, injection, partial failure, and human handoff.

## Counterexample

A deterministic workflow with one classification step may be safer and easier to evaluate than a general autonomous agent.

## Worked case

A refund workflow lets the model gather evidence and propose an amount, but a deterministic policy validates eligibility and a human approves high-value refunds. Tool simulations test prompt injection, duplicate submission, denial, and handoff.

## Tool-assisted review

Model the workflow and permissions as data, simulate tools, and retain traces. AI can propose decompositions, but only policy and explicit user authorization grant action authority.

## References

- `openai-agent-guide`
- `react-paper`
- `toolformer-paper`
- `nist-ai-rmf-gai`

---

Canonical knowledge ID: `agent-design`  
Reference IDs: `openai-agent-guide`, `react-paper`, `toolformer-paper`, `nist-ai-rmf-gai`

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
