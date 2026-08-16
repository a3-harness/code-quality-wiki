<!-- generated-from: a3-code-quality; do not edit -->

# Prompt design

Prompt design specifies an observable behavior contract for a particular model and task distribution. Good prompts state goals, context, constraints, boundaries, evidence, and output shape; their value is established by evaluation rather than eloquence.

## Failure mechanisms

- Repeated or conflicting instructions obscure priorities.
- Examples overfit a narrow test set or encode stale model tactics.
- Untrusted retrieved content is treated as higher-priority instruction.
- Output looks fluent while omitting required evidence or fields.
- Prompt changes improve one metric while increasing cost, latency, or unsafe behavior.

## Review questions and evidence

Ask what success means, which ambiguities require abstention, what authority is granted, and which model/version was evaluated. Compare controlled variants on representative and adversarial cases with quality, citation, safety, token, latency, and cost measures.

## Counterexample

More instructions and examples can reduce performance. A lean prompt with a precise schema and strong evals may outperform a detailed tutorial.

## Worked case

Two prompt variants review the same fixed 40-case set. The shorter prompt preserves required citations, raises task success, and lowers tokens, but loses one abstention case; it is not promoted until that safety regression is corrected and rerun.

## Tool-assisted review

Version prompts, datasets, results, and model settings. AI may generate candidates or critique failures, but promotion requires fixed evals and human review of consequential behavior.

## References

- `openai-model-guidance`
- `cot-paper`
- `react-paper`

---

Canonical knowledge ID: `prompt-design`  
Reference IDs: `openai-model-guidance`, `cot-paper`, `react-paper`

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
