<!-- generated-from: a3-code-quality; do not edit -->

# Constructing knowledge governance tooling

## Implementation status

**Built baseline.** `qreview knowledge-status` reports source and specialist counts, ownership, missing licenses, and age warnings for living sources and specialist reviews. Scheduling, feedback ingestion, and release automation are planned.

## Architecture

Govern by stable knowledge ID. Each maintainable unit needs an owner, last substantive review, source currency class, license, applicable versions, evaluation coverage, publication route, and open gaps.

## Core algorithm

```text
KNOWLEDGE_STATUS(registry, catalogs, today):
  warnings ← []
  for source in registry.sources:
    if source.license is empty:
      warnings += MISSING_LICENSE(source.id)
    if source.currency = LIVING and age(source.accessed, today) > 90 days:
      warnings += STALE_SOURCE(source.id, age)

  for catalog in catalogs:
    require owner and reviewed_at
    if age(catalog.reviewed_at, today) > 180 days:
      warnings += STALE_CATALOG(catalog.id, age)

  return counts + owner + warnings
```

A feedback event should create a proposal containing the affected ID, evidence, privacy classification, and requested change. It must not directly rewrite canonical knowledge.

## Failure handling

Invalid dates, missing ownership, unknown IDs, and private-data policy violations fail intake. Link or version churn creates a review task rather than automatic prose replacement.

## Tests to build

Test freshness boundaries, living versus stable sources, ownership fallback, missing licenses, private feedback rejection, duplicate proposals, release compatibility, and deterministic reports.

## Security considerations

Feedback and rejected findings may contain source code, incidents, or personal data. Default to metadata-only records, define retention, restrict access, and require explicit approval before public promotion.

## Planned extensions

Add scheduled freshness checks, broken-link caches, reviewed proposal queues, privacy-aware usage analytics, changelogs, semantic-versioned exports, and dashboards showing coverage without ranking contributors by raw finding counts.

---

Canonical knowledge ID: `tool-governance`  
Reference IDs: _See chapter links and canonical modules._

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
