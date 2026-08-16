<!-- generated-from: a3-code-quality; do not edit -->

# React

React quality depends on pure rendering, deliberate state ownership, and Effects limited to synchronization with external systems. Components should make data flow and user events easier to reason about, not conceal them behind derived state and lifecycle choreography.

## Failure mechanisms

- Render mutates inputs or external state, so retries and concurrent rendering change behavior.
- Duplicated or contradictory state drifts apart.
- Effects derive local render data, producing extra renders and stale synchronization.
- Unstable identities reset state or invalidate memoization unexpectedly.
- Raw HTML or client-trusted authorization crosses a security boundary.

## Review questions and evidence

Ask who owns each state value, whether it can be derived during render, which external system an Effect synchronizes, and what happens under repeated render and cleanup. Prefer interaction tests, Strict Mode evidence, profiler traces, and accessibility checks over snapshot volume.

## Counterexample

Memoization and abstraction are not automatic improvements. A small calculation or one-use component may be clearer and cheaper without either.

## Worked case

A filtered list stores both `items` and `visibleItems`, then updates the latter in an Effect. Removing the duplicate state and deriving the filter during render eliminates a stale frame; interaction tests prove selection behavior and the profiler checks whether memoization is actually needed.

## Tool-assisted review

Linters can surface hook and dependency violations; profilers establish actual render cost. AI can map state and suggest tests, but must not infer performance or correctness from component shape alone.

## References

- `react-purity`
- `react-effects`
- `react-state`

---

Canonical knowledge ID: `react`  
Reference IDs: `react-purity`, `react-effects`, `react-state`

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
