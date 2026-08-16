<!-- generated-from: a3-code-quality; do not edit -->

# Agent engineering

Agent engineering turns an agent design into a bounded, observable, recoverable system. It treats prompts, models, retrieval, memory, tools, approvals, traces, and evals as versioned production components.

## Failure mechanisms

- Tool inputs or outputs violate contracts and corrupt later decisions.
- Retries duplicate external actions or amplify cost.
- Context compaction removes goals, evidence, or approval state.
- Traces omit the evidence needed to reproduce a failure.
- Model upgrades change tool use or safety behavior without regression gates.

## Review questions and evidence

Ask how calls are correlated, which operations are idempotent, what budgets apply, how secrets are redacted, and how a run resumes safely. Evaluate task success, citations, unsafe-action prevention, abstention, recovery, latency, tokens, and cost.

## Counterexample

A successful demo is not evidence of reliability. If representative failures, tool errors, and denied actions are absent, the system is not ready for autonomous operation.

## Worked case

A ticket agent times out after creating an external record but before receiving confirmation. An idempotency key and reconciliation tool allow safe resume; the trace retains tool input, result, approval state, model version, cost, and recovery outcome for regression replay.

## Tool-assisted review

Use typed tool schemas, allowlists, mocks, trace graders, replayable fixtures, and deployment gates. AI-generated judgments remain advisory until grounded evidence and explicit approval satisfy the action policy.

## References

- `openai-model-guidance`
- `openai-agent-guide`
- `nist-ssdf`
- `nist-ai-rmf-gai`

---

Canonical knowledge ID: `agent-engineering`  
Reference IDs: `openai-model-guidance`, `openai-agent-guide`, `nist-ssdf`, `nist-ai-rmf-gai`

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
