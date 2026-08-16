# Software design and modularity

## Purpose

Design assigns responsibilities, knowledge, and change boundaries within a
codebase. Good modularity keeps related decisions together, exposes deliberate
interfaces, and prevents one change from propagating through unrelated modules.

## Criteria

- Responsibility and cohesion.
- Coupling, dependency direction, and stable boundaries.
- Useful abstraction without speculative indirection.
- Encapsulation, state ownership, and lifecycle ownership.
- API contracts and domain-model fidelity.

## Review questions

- Which module owns this decision and the state it changes?
- What future change is this boundary designed to localize?
- Does the interface expose domain intent or implementation machinery?
- Can callers violate invariants or observe partially initialized state?

## Warning signals and failure modes

God modules, bidirectional dependencies, feature envy, leaky abstractions,
anemic models, shared mutable state, and interfaces shaped around one caller can
produce shotgun changes, fragile tests, inconsistent policy, and unsafe reuse.

## Strong evidence

Dependency diagrams, change-history analysis, API contract tests, ownership
maps, representative extension exercises, and architecture fitness checks.

## Related dimensions

[Architecture](04-architecture.md), [maintainability](05-maintainability.md),
[correctness](01-correctness.md), and [test quality](06-test-quality.md).
