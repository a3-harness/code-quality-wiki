<!-- generated-from: a3-code-quality; do not edit -->

# Constructing an AI-assisted review tool

## Implementation status

**Built contract and safe paths.** QReview provides a deterministic mock and an opt-in OpenAI Responses API adapter. Remote execution requires an explicit provider flag, `--allow-remote`, credentials, and an evaluated model name. No autonomous action tool is exposed.

## Architecture

Keep deterministic observations distinct from model inference. The model receives a bounded review bundle and returns a schema-validated advisory report with cited knowledge IDs, confidence, missing context, proposed severity, usage, and `human_judgment_required`.

## Core algorithm

```text
AI_REVIEW(bundle, provider, policy):
  assert bundle.human_judgment_required
  assert bundle has retrieved knowledge IDs
  redact secrets according to policy
  mark diff, evidence, and retrieved text as UNTRUSTED_DATA

  request ← {
    instructions: fixed review contract,
    input: bounded bundle,
    output_schema: advisory_review_schema,
    token_budget: configured_limit,
    tools: none
  }

  response ← provider.generate(request)
  validate response against schema
  validate every cited ID exists in bundle
  force external_actions_allowed = false
  append provider/model/usage/audit metadata
  return response
```

## Failure handling

Missing credentials, absent evaluated model, timeout, refusal, malformed JSON, unknown citations, and budget exhaustion become explicit safe failures. The caller retains the deterministic bundle and can continue reviewing offline.

## Tests to build

Mock normal, refusal, malformed, timeout, and retry cases. Test prompt injection in diffs, citation validity, redaction, empty retrieval, output budgets, zero external actions, and stable audit linkage. Run live smoke tests separately and never make them the reproducible acceptance path.

## Security considerations

The model has no authority merely because it can describe an action. Tool permissions, user authorization, and approval state belong to deterministic policy. Minimize remote data and log metadata rather than sensitive content.

## Planned extensions

Add more provider adapters, cancellation, rate/cost limits, trace storage, and structured abstention graders. Action tools remain out of scope until separate authorization and idempotency designs pass adversarial evaluation.

---

Canonical knowledge ID: `tool-ai-review`  
Reference IDs: _See chapter links and canonical modules._

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
