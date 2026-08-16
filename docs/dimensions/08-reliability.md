# Reliability and resilience

## Purpose

Reliable systems deliver acceptable service despite expected faults, load, and
partial failure. Resilience is not “never fail”; it is controlled failure,
recovery, and prevention of disproportionate impact.

## Criteria

- Failure containment and bounded blast radius.
- Deadlines, retries, idempotency, and retry budgets.
- Recovery, redundancy, and graceful degradation.
- Overload control, queues, admission, and backpressure.
- Distributed consistency and partial-failure semantics.

## Review questions

- What happens when each dependency is slow, unavailable, stale, or inconsistent?
- Can retry multiply load or repeat a non-idempotent effect?
- Which resources are bounded, and what is shed first under overload?
- How is recovery detected, rehearsed, and prevented from causing a second incident?

## Warning signals and failure modes

Missing timeouts, synchronized retries, unbounded queues, shared fate, optimistic
health checks, and unclear idempotency can produce cascading latency, retry
storms, duplicate effects, data loss, and prolonged recovery.

## Strong evidence

SLOs, failure budgets, chaos or fault-injection tests, recovery drills, queue and
capacity models, dependency telemetry, and incident history.

## Related dimensions

[Operability](12-operability.md), [performance](09-performance.md),
[data integrity](11-data-integrity.md), and [architecture](04-architecture.md).
