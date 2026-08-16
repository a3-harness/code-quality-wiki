# Performance and scalability

## Purpose

Performance concerns whether work meets latency, throughput, and resource
objectives. Scalability concerns how those properties change with data, traffic,
tenancy, and parallelism. Optimization without a workload and budget is guesswork.

## Criteria

- Algorithmic complexity and data-shape sensitivity.
- Latency budgets and critical-path composition.
- CPU, memory, network, storage, and energy efficiency.
- Capacity limits, contention, and scaling behavior.

## Review questions

- What workload distribution and percentile objective matter?
- Which operation grows with users, records, fan-out, or payload size?
- Is work repeated, serialized, copied, or retained unnecessarily?
- Where is the capacity ceiling, and how will approaching it be observed?

## Warning signals and failure modes

Unbounded scans, N+1 calls, synchronous fan-out, large allocations, missing
pagination, cache stampedes, and averages without tail percentiles can cause
latency breaches, memory exhaustion, cost spikes, and collapse under load.

## Strong evidence

Representative benchmarks, profilers, load and soak tests, complexity analysis,
production percentiles, capacity models, and cost-per-operation measurements.

## Related dimensions

[Reliability](08-reliability.md), [concurrency](10-concurrency.md), and
[operability](12-operability.md).
