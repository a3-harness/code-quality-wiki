<!-- generated-from: a3-code-quality; do not edit -->

# Constructing structured knowledge contracts

## Implementation status

**Built.** QReview normalizes the vetted reference registry, joins `llm_wiki` records by canonical ID and SHA-256, stores specialist metadata, and exposes knowledge queries. Rich claim-level promotion remains a future extension.

## Architecture

Use stable IDs to join references, topics, quality dimensions, chapters, evidence, evaluations, and public routes. JSON carries identity and relationships; Markdown carries explanation. Never attempt to derive canonical identity from a title alone.

## Core algorithm

```text
IMPORT(registry, ingestion_export):
  assert supported registry version
  sources ← empty map

  for source in registry ordered by source.id:
    require HTTPS URL, topics, authority, currency, license
    reject duplicate source.id
    sources[source.id] ← normalized source metadata

  for extracted in ingestion_export:
    canonical ← sources[extracted.external_id]
    fail if canonical is missing
    fail if canonical.sha256 ≠ extracted.sha256
    canonical.ingestion ← extraction status, warnings, lifecycle, cache path

  return stable_sorted_catalog(sources)
```

For every specialist pack, validate that its reference IDs exist and that its canonical Markdown contains the declared citations and required evidence sections.

## Failure handling

Unknown IDs, duplicate IDs, hash mismatches, unsupported schema versions, missing licenses, and invalid URLs fail before output is written. A `--check` mode compares expected bytes with checked-in output and makes drift visible in CI.

## Tests to build

Use valid and invalid fixtures for every required field and foreign key. Test deterministic ordering, duplicate rejection, hash mismatches, schema migrations, missing pages, and catalog queries that join the correct source records.

## Security considerations

A citation is not an endorsement. Store source authority, currency, applicability, and license so retrieval can expose limitations. Do not embed restricted source text merely because metadata is public.

## Planned extensions

Introduce first-class claim, practice, question, example, and contradiction records with reviewed promotion events. Until implemented, explanatory Markdown remains the approved claim surface.

---

Canonical knowledge ID: `tool-knowledge-contracts`  
Reference IDs: _See chapter links and canonical modules._

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
