<!-- generated-from: a3-code-quality; do not edit -->

# Functional-style Python

Functional style in Python means using pure transformations, immutable values, explicit inputs, and composable functions where those properties simplify reasoning. Python remains multi-paradigm: controlled mutation, iteration, objects, and context managers are often the clearest expression of effects and resource lifetimes.

## Prefer

- Separate calculation from I/O, time, randomness, and mutation.
- Use iterators for composable, bounded-memory pipelines.
- Pass dependencies explicitly instead of reading hidden global state.
- Return new values when shared mutation would create aliasing or concurrency risk.
- Choose comprehensions or ordinary loops when they communicate intent better than nested combinators.

## Failure mechanisms

- A function that appears pure reads environment, clock, database, or mutable globals.
- Lazy iterators defer exceptions and resource use beyond the expected boundary.
- Dense `map`/`filter`/lambda chains conceal domain names and error handling.
- Copying large structures for ideological immutability creates avoidable cost.

## Review questions and evidence

Ask which effects occur, whether evaluation is eager or lazy, who owns consumed resources, and whether identical inputs truly yield identical results. Property tests and repeatability tests are stronger than stylistic assertions.

## Counterexample

An explicit loop that validates records, records indexed failures, and stops on a budget can be clearer and safer than a point-free pipeline.

## Worked case

Split invoice processing into `parse`, `validate`, and `total` pure functions, then keep database writes in one outer function. Property tests exercise totals independently; a repeatability test fixes clock and exchange-rate inputs instead of hiding them in globals.

## Tool-assisted review

Static tooling can locate global writes, mutable defaults, and I/O calls but cannot prove semantic purity. AI can propose an effect map or refactoring, subject to tests for behavior, memory, exceptions, and readability.

## References

- `py-functional-howto`
- `py-functional-modules`

---

Canonical knowledge ID: `python-functional`  
Reference IDs: `py-functional-howto`, `py-functional-modules`

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
