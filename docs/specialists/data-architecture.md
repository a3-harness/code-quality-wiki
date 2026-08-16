<!-- generated-from: a3-code-quality; do not edit -->

# Data architecture

Data architecture assigns durable responsibilities for data products, storage, movement, contracts, lineage, access, and lifecycle under specific workloads. Labels such as warehouse, lakehouse, mesh, or event-driven describe options—not maturity rankings.

## Failure mechanisms

- Ownership and semantic contracts are unclear across producers and consumers.
- One platform promises incompatible latency, consistency, governance, and cost goals.
- Copies proliferate without lineage, retention, or deletion propagation.
- Architecture claims depend on vendor features or research assumptions not present in operation.

## Review questions and evidence

Ask who owns meaning and quality, which workload and guarantees matter, how lineage and access are represented, and how recovery or migration works. Use decision records, workload measurements, ownership maps, lineage events, and recovery exercises.

## Counterexample

Centralization can be appropriate for a small organization with shared semantics; decentralization without capable owners merely distributes inconsistency.

## Worked case

A customer metric has three conflicting definitions across dashboards. The decision record assigns a semantic owner, contract, lineage facets, freshness objective, and migration path; architecture selection follows those constraints rather than beginning with a platform label.

## Tool-assisted review

Catalog and lineage tools automate inventory and relationships. AI may compare options and locate contradictions, but must label source authority and cannot invent ownership or operational guarantees.

## References

- `openlineage-spec`
- `beam-model`
- `lakehouse-paper`

---

Canonical knowledge ID: `data-architecture`  
Reference IDs: `openlineage-spec`, `beam-model`, `lakehouse-paper`

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
