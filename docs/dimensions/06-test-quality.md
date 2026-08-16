# Testing, verification, and testability

## Purpose

Tests and analyses provide evidence about selected properties; they do not make
software correct by volume alone. Testability is the ability to observe and
control behavior without coupling tests to irrelevant implementation details.

## Criteria

- Behavior-focused unit and behavioral tests at component boundaries.
- Integration and contract evidence at real boundaries.
- Negative, regression, property, fuzz, and mutation testing where appropriate.
- Deterministic setup, meaningful assertions, and diagnostic failure output.
- Coverage of risk, not merely lines.

## Review questions

- Which claim does each test establish, and which important claim remains untested?
- Would a plausible incorrect implementation still pass?
- Are dependency contracts tested at the boundary where assumptions matter?
- Can failures be reproduced without hidden time, order, or environment dependencies?

## Warning signals and failure modes

Happy-path-only suites, excessive mocking, assertion-free tests, snapshots with
blind updates, flaky timing, and coverage targets without risk models create
false confidence, slow feedback, and undiagnosable regressions.

## Strong evidence

Requirement-to-test traceability, mutation results, boundary-value suites,
contract environments, escaped-defect regressions, and stable CI history.

## Related dimensions

[Correctness](01-correctness.md), [reliability](08-reliability.md),
[performance](09-performance.md), and [security](07-security.md).
