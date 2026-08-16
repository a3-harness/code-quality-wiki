<!-- generated-from: a3-code-quality; do not edit -->

# Constructing evaluation and promotion gates

## Implementation status

**Built baseline.** QReview evaluates deterministic rules and knowledge retrieval with explicit denominators, dispositions, mode comparisons, and a promotion threshold. Corpus diversity, blind review, and live-model regression matrices remain ongoing work.

## Architecture

Version the corpus, expected outcomes, reviewer dispositions, prompt/model configuration, and metrics separately. Do not count unknown or context-required cases as convenient failures or successes.

## Core algorithms

```text
EVALUATE_RETRIEVAL(cases, k):
  hits ← 0
  expected_total ← 0
  for case in cases:
    actual ← retrieve(case.profile, case.findings, k)
    hits += size(intersection(actual, case.expected_ids))
    expected_total += size(case.expected_ids)
  recall_at_k ← hits / expected_total
  pass ← recall_at_k ≥ configured_threshold

EVALUATE_FINDINGS(observed, dispositions):
  precision_denominator ← accepted + rejected
  precision ← accepted / precision_denominator
  consequential_recall ← surfaced_ground_truth / ground_truth_total
  report unknown, context, and duplicate counts separately
```

Compare deterministic-only, profile-only, and combined retrieval on identical cases. For model reviews also track citation validity, grounded claims, abstention, unsafe-action rate, latency, tokens, and cost.

## Failure handling

Zero denominators produce `null`, not a misleading 0% or 100%. Orphaned labels and duplicate IDs fail. Model/provider upgrades do not inherit an earlier version’s promotion decision.

## Tests to build

Test metric arithmetic, exclusions, threshold boundaries, corpus schema, holdout separation, deterministic ordering, adversarial cases, and regression failure messages.

## Security considerations

Evaluation data may contain proprietary code or personal data. Record provenance and redistribution policy, minimize stored content, and prevent private samples from entering public reports or provider calls.

## Planned extensions

Grow licensed specialist cases, introduce blinded multi-reviewer agreement, create per-model promotion records, and add cost/latency budgets and incident-derived regression suites.

---

Canonical knowledge ID: `tool-evaluation`  
Reference IDs: _See chapter links and canonical modules._

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
