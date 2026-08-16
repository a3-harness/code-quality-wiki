<!-- generated-from: a3-code-quality; do not edit -->

# SQL quality

SQL quality combines correct relational semantics, durable integrity, safe parameterization, comprehensible queries, and measured execution behavior. A query can be syntactically valid and still be wrong under duplicates, `NULL`, concurrency, skew, or production cardinalities.

## Prefer

- Express invariants with keys, foreign keys, checks, and appropriate uniqueness.
- Bind values as parameters; allowlist identifiers when dynamic structure is unavoidable.
- State expected cardinality and duplicate behavior at joins and aggregations.
- Treat `NULL`, time zones, collation, precision, and empty sets deliberately.
- Use `EXPLAIN`/runtime evidence with representative statistics before performance claims.

## Failure mechanisms

- A join multiplies rows and silently inflates totals.
- `NOT IN` with a `NULL` produces unexpected three-valued logic.
- Application-side uniqueness races under concurrency.
- String construction crosses the code/data boundary and enables injection.
- An index improves one read while making writes, storage, or another plan worse.

## Review questions and evidence

Ask for input/output cardinalities, enforced constraints, isolation assumptions, parameter binding, representative data distribution, and before/after plans. A plan without actual workload context is diagnostic evidence, not proof of production improvement.

## Counterexample

Replacing a clear query with a clever single statement can worsen reviewability and recovery. Multiple statements inside a correct transaction may be the safer design.

## Worked case

A report total doubles after joining orders to multiple payments. A fixture with two payments exposes the cardinality error; pre-aggregating payments restores the invariant. The reviewer retains before/after result sets and plans rather than accepting a visually plausible query.

## Tool-assisted review

Deterministic tooling should parse migration/query artifacts, confirm parameter APIs, and retain plans and timings. AI can explain likely mechanisms and generate test cases, but it must not fabricate schema facts, plan behavior, or benchmark results.

## References

- `postgres-transactions`
- `postgres-explain`
- `owasp-sql-injection`

---

Canonical knowledge ID: `sql`  
Reference IDs: `postgres-transactions`, `postgres-explain`, `owasp-sql-injection`

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
