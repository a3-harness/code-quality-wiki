# Concurrency and parallelism

## Purpose

Concurrency governs overlapping work and the ordering of effects. Parallelism
uses multiple execution resources. Correct concurrent behavior requires explicit
ownership, synchronization, cancellation, and progress guarantees.

## Criteria

- Shared mutable state and ownership.
- Atomicity, races, and memory visibility.
- Deadlock, livelock, starvation, and fairness.
- Async ordering, cancellation, backpressure, and reentrancy.

## Review questions

- Which state can be observed or mutated concurrently, and under what protocol?
- What must be atomic from the user's perspective?
- Can cancellation arrive between an effect and its bookkeeping?
- Is lock ordering stable, and can callbacks re-enter protected code?

## Warning signals and failure modes

Check-then-act sequences, unsynchronized caches, inconsistent lock order,
fire-and-forget tasks, blocking work on event loops, and lost cancellation can
produce corruption, duplicate effects, deadlocks, leaks, and shutdown hangs.

## Strong evidence

Happens-before reasoning, race detectors, stress and schedule exploration,
linearizability models, bounded queues, cancellation tests, and production traces.

## Related dimensions

[Correctness](01-correctness.md), [reliability](08-reliability.md),
[performance](09-performance.md), and [data integrity](11-data-integrity.md).
