<!-- generated-from: a3-code-quality; do not edit -->

# Data engineering

Data engineering delivers repeatable, observable transformations whose time, delivery, quality, and recovery semantics are explicit. Batch and streaming are execution modes; correctness depends on event time, state, replay, and side-effect boundaries.

## Failure mechanisms

- Late or out-of-order events are silently dropped or double-counted.
- “Exactly once” covers broker state but not an external side effect.
- Replay changes results because transformations, reference data, or code are not versioned.
- Backfills overwhelm production or violate retention and deletion policies.
- Lineage records movement but not semantic transformations or ownership.

## Review questions and evidence

Ask which clock matters, how watermarks and lateness work, what is idempotent, where state lives, and how replay/backfill is verified. Require fixture streams, late-data cases, recovery drills, reconciliation, and lineage events.

## Counterexample

A scheduled bounded batch may be simpler, cheaper, and more reliable than streaming when freshness requirements allow it.

## Worked case

An hourly revenue window receives a payment event two hours late. A fixture advances the watermark, injects late data, and verifies the chosen correction output. Replay repeats the same result because the sink key is idempotent and reference-data versions are pinned.

## Tool-assisted review

Tools can validate schemas, contracts, lineage, freshness, reconciliation, and replay fixtures. AI can reason about missing cases only while stating the guarantee boundary and observed facts.

## References

- `beam-model`
- `kafka-design`
- `openlineage-spec`

---

Canonical knowledge ID: `data-engineering`  
Reference IDs: `beam-model`, `kafka-design`, `openlineage-spec`

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
