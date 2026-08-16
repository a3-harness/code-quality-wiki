# Correctness and functional suitability

## Purpose

Correct software implements the intended behavior for valid inputs, defines
what happens for invalid inputs, and preserves its invariants through every
state transition. Correctness is contextual: code can match its implementation
specification while solving the wrong user problem.

## Criteria

- Behavioral correctness against explicit intent and acceptance examples.
- Preconditions, validation, invariants, and postconditions.
- Boundary, edge, exceptional cases, and empty-state behavior.
- State-machine transitions, including illegal and repeated transitions.
- Error semantics: detection, propagation, translation, and recovery.

## Review questions

- What observable promise does this change make, and where is that promise defined?
- Which inputs, states, timing conditions, or dependency responses violate its assumptions?
- Are partial success, retries, duplicate requests, and repeated operations well defined?
- Can an error be mistaken for success or leave externally visible partial state?

## Warning signals and failure modes

Implicit requirements, unchecked conversions, off-by-one boundaries, default
branches that hide new states, swallowed exceptions, and tests that mirror the
implementation all deserve investigation. Failures include incorrect results,
state corruption, lost work, double application, misleading success, and
regressions outside the happy path.

## Strong evidence

Executable examples, contract tests, property tests, state-transition models,
typed invariants, production counterexamples, and domain-expert confirmation.
Line inspection alone rarely establishes end-to-end correctness.

## Related dimensions

[Test quality](06-test-quality.md), [data integrity](11-data-integrity.md),
[reliability](08-reliability.md), and [compatibility](13-compatibility.md).
