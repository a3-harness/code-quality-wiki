<!-- generated-from: a3-code-quality; do not edit -->

# Constructing credential-safe live LLM validation

## Implementation status

**Built as a bounded validation path.** QReview keeps its normal unit suite offline and supplies an explicitly authorized runner for two synthetic OpenAI Responses API checks: a transport/schema smoke test and an adversarial end-to-end review. The runner retains outcomes and usage, not secrets or model prose.

## Architecture

Use three rings of evidence rather than asking live calls to prove everything:

1. Pure tests validate prompts, policies, parsers, citation rules, and application behavior without a model.
2. A mocked transport test validates the exact provider request and response boundary without network cost or variability.
3. A small live suite validates authentication, endpoint compatibility, structured output, and representative behavior using sanitized fixtures.

The live ring is supplemental evidence. It is never the sole acceptance path because provider availability, latency, and model output vary. Credentials enter only through an allowlisted loader, model choice must be explicit, and the test adapter exposes no tools.

## Core algorithm

```text
LIVE_LLM_VALIDATE(env_file, remote_consent, cases, limits):
  require remote_consent = true
  assert count(cases) <= limits.max_requests

  environment ← parse_assignments_as_data(env_file)
  credentials ← select_allowlisted_names(environment)
  require credentials.api_key
  require credentials.explicit_model

  for case in cases:
    assert case.content_is_synthetic
    request ← build_strict_structured_request(case, tools = none)
    response ← call_provider(request, output_budget = limits.output_tokens)
    validate response.schema
    validate response.citations ⊆ case.retrieved_knowledge_ids
    validate response.human_judgment_required = true
    force response.external_actions_allowed = false
    record counts, timing, usage, and pass/fail only

  assert logs contain no credential values, prompts, completions, or response IDs
  return redacted_summary
```

## Failure handling

Fail before network access when consent, credentials, or the evaluated model is missing. Convert provider and parsing failures into domain errors without echoing authorization headers. Reject malformed structured output and citations outside the supplied bundle. Keep live failures distinct from deterministic regressions so transient provider incidents do not masquerade as product defects.

Set request and output limits before execution. A live suite should stop after its declared cases and should not retry silently; retries change both cost and the meaning of the evidence. If operational retry is later added, cap attempts, add jitter, and record the attempt count in protected telemetry.

## Tests to build

- Unit-test the allowlist parser with placeholder values; never copy real credentials into fixtures.
- Mock the HTTP boundary and assert endpoint, model, output budget, strict schema, and authorization-header presence without snapshotting the header.
- Test missing consent, missing key, missing model, timeouts, refusal, malformed JSON, and unknown citations.
- Use a synthetic normal case to verify transport and structured output.
- Use a synthetic prompt-injection case to verify that untrusted content cannot grant authority.
- Assert the persisted summary contains only test names, booleans, counts, latency, and token usage.
- Run the deterministic suite before and after live checks; never make ordinary CI depend on paid network calls.

For model comparison or promotion, replace a two-case smoke suite with a versioned corpus, blinded grading where appropriate, repeated trials for unstable metrics, and declared thresholds for quality, safety, latency, and cost.

## Security considerations

Treat `.env` as data, not executable shell. Load only named variables, avoid printing inherited environment state, and restrict the file to its owner. Do not send real repository content until a separate data-classification and retention review authorizes it. Store raw traces only in an access-controlled telemetry system with retention limits; public demos should contain redacted aggregates.

An API response remains advice. Schema success does not authorize file writes, messages, deployment, or other actions. Tool access and approvals require a separate deterministic policy boundary. Rotate a credential immediately if its value appears in output, history, artifacts, or a committed file.

## Planned extensions

Build a versioned behavioral corpus and quality/cost promotion gates; introduce protected request tracing and explicit retry policy; integrate an approved secret manager; add provider-specific conformance adapters; measure drift on scheduled, budgeted runs; and define incident handling for leaked data or unexpected model behavior. Preserve the offline suite as the fast, reproducible foundation throughout.

---

Canonical knowledge ID: `tool-live-llm-validation`  
Reference IDs: _See chapter links and canonical modules._

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
