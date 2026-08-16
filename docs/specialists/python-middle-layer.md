<!-- generated-from: a3-code-quality; do not edit -->

# Python middle layer

The middle layer coordinates a use case between delivery mechanisms and domain/data services. It is a boundary, not a required class named “service.” Its value is making authorization, transaction scope, orchestration, and failure semantics visible without coupling them to HTTP, queues, or an ORM.

## Prefer

- Accept explicit use-case inputs and return domain/application results.
- Keep transport parsing and response rendering at the edge.
- Define one deliberate transaction boundary per business operation.
- Put business invariants in the domain model when they must hold outside one workflow.
- Inject repositories, clocks, message publishers, and gateways behind narrow contracts.

## Failure mechanisms

- A pass-through layer adds indirection but no policy.
- A “god service” absorbs domain rules and couples unrelated workflows.
- Committing inside repositories prevents atomic multi-repository operations.
- Returning live ORM objects leaks session lifetime and lazy-loading behavior.
- Retrying a non-idempotent operation duplicates externally visible effects.

## Review questions and evidence

Ask where the use case begins and ends, who owns commit/rollback, whether invariants survive another delivery path, and how partial failure is recovered. Strong evidence includes use-case tests against fakes plus integration tests for real transaction behavior. Mock call counts alone are weak evidence.

## Counterexample

A small CRUD endpoint may be clearer as a transaction script. Adding domain objects, repositories, and a unit of work solely to satisfy a pattern can reduce change locality.

## Worked case

A transfer handler parses an account ID and amount, then calls `transfer(account_id, amount)`. The service loads both accounts, invokes the domain transfer, and commits once. Unit tests cover insufficient funds without HTTP; an integration test proves both balances roll back when the second write fails.

## Tool-assisted review

Deterministic tooling can inventory handlers, commits, repository calls, and exception paths. An AI reviewer can connect those observations to the questions above, but must cite the observed code and may not infer a missing invariant or transaction guarantee without repository/database evidence.

## References

- `cosmic-service-layer`
- `cosmic-uow`
- `sqlalchemy-session`
- `pep-249`

---

Canonical knowledge ID: `python-middle-layer`  
Reference IDs: `cosmic-service-layer`, `cosmic-uow`, `sqlalchemy-session`, `pep-249`

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
