<!-- generated-from: a3-code-quality; do not edit -->

# Constructing knowledge retrieval

## Implementation status

**Built baseline.** QReview supports catalog substring queries and deterministic metadata ranking from repository languages, frameworks, and finding dimensions. Embeddings, hybrid ranking, and learned reranking are planned only after baseline measurement.

## Architecture

Retrieve small knowledge units by stable ID. Return why each unit matched and its source IDs. Retrieval narrows context; it does not decide which guidance is correct for the repository.

## Core algorithm

```text
RETRIEVE(profile, findings, catalog, k):
  terms ← profile.languages ∪ profile.frameworks
  terms ← terms ∪ dimensions(findings)
  terms ← terms ∪ normalize_aliases(terms)

  candidates ← []
  for pack in catalog:
    searchable ← pack.id + pack.title + pack.dimensions
    score ← count(term in searchable for term in terms)
    if score > 0:
      candidates.append({pack.id, score, matched_terms})

  return stable_sort(candidates, by=-score_then_id)[0:k]
```

Stable tie-breaking matters: identical inputs should produce identical bundles and evaluation results.

## Failure handling

If no knowledge matches, return an explicit empty result and require broader human selection; never fabricate a topic. Missing foreign keys fail catalog validation. Retrieval should degrade without network or embedding services.

## Tests to build

Maintain a corpus with expected IDs and explicit K. Measure recall and precision, alias behavior, irrelevant-profile cases, ties, new-pack regressions, and queries containing adversarial instructions.

## Security considerations

Retrieved text is untrusted even when local. Keep control instructions outside retrieved content, enforce context budgets, retain canonical IDs, and prevent private units from crossing an unauthorized provider boundary.

## Planned extensions

Compare lexical BM25, metadata filters, embeddings, and hybrid reranking on the same holdout corpus. Adopt complexity only if it improves measured retrieval without unacceptable latency, cost, or privacy impact.

---

Canonical knowledge ID: `tool-knowledge-retrieval`  
Reference IDs: _See chapter links and canonical modules._

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
