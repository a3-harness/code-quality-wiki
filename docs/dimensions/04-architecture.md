# Software architecture and system structure

## Purpose

Architecture governs system-scale boundaries, communication, data ownership,
deployment units, and the tradeoffs that constrain future evolution. A locally
clean change may still create system-wide coupling or an unsafe failure path.

## Criteria

- Component boundaries, layering, and dependency rules.
- Fitness for required quality attributes and operating constraints.
- Explicit architectural tradeoffs and irreversible decisions.
- Integration topology, protocols, and data ownership.
- Evolution, migration, and decommissioning paths.

## Review questions

- Which quality attributes drove this structure, and what was traded away?
- What new remote call, shared state, trust boundary, or deployment dependency appears?
- Can components evolve and fail independently?
- How is the decision reversed, migrated, or retired?

## Warning signals and failure modes

Shared databases without ownership, cyclic service dependencies, synchronous
critical-path fan-out, undocumented protocols, and permanent transitional
layers can create distributed monoliths, cascading failure, lockstep releases,
and irreversible platform dependence.

## Strong evidence

Architecture decision records, context/container diagrams, fitness functions,
failure-mode analysis, load models, migration rehearsals, and operational history.

## Related dimensions

[Design](03-design.md), [reliability](08-reliability.md),
[operability](12-operability.md), and [compatibility](13-compatibility.md).
