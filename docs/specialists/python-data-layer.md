<!-- generated-from: a3-code-quality; do not edit -->

# Python data layer

The data layer translates between application concepts and persistence while preserving database constraints and transaction semantics. Abstraction should clarify ownership and testing without pretending that every database behaves alike.

## Prefer

- Make session/connection lifetime and commit/rollback ownership explicit.
- Enforce durable invariants with database constraints, not application checks alone.
- Use parameter binding through the driver or query builder.
- Translate persistence exceptions only when the application can act on the distinction.
- Keep migrations, serialization, timezone, numeric precision, and deletion semantics reviewable.

## Failure mechanisms

- Check-then-write validation races with concurrent transactions.
- A shared session crosses threads or asynchronous tasks.
- Lazy loading turns serialization into unbounded queries or fails after session close.
- Broad retry repeats external effects or hides deterministic constraint failures.
- Tests against fakes pass while real isolation and constraint behavior fails.

## Review questions and evidence

Ask what invariant the database enforces, which isolation anomaly matters, where rollback occurs, and whether a retry is safe. Require integration tests against the supported database for constraints, concurrency, rollback, and migrations.

## Counterexample

A repository interface is not automatically useful. When the application needs database-specific queries and guarantees, a generic repository can hide essential semantics and obstruct plan analysis.

## Worked case

Two concurrent requests reserve the last seat. An application-side count check fails under concurrency; a database uniqueness/availability constraint makes one transaction fail, and the service translates that specific failure while rolling back the unit of work.

## Tool-assisted review

Tools can inventory transaction calls, migration changes, query counts, and schema constraints. AI may relate them to failure mechanisms, but database documentation, executed concurrency tests, and observed plans outrank its inference.

## References

- `pep-249`
- `sqlalchemy-session`
- `postgres-transactions`

---

Canonical knowledge ID: `python-data-layer`  
Reference IDs: `pep-249`, `sqlalchemy-session`, `postgres-transactions`

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
