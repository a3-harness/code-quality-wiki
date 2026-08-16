# Research gaps and conflicts

The reference pass supports drafting, but not timeless claims. These are the
research gates to resolve in each piece.

- **Python “middle layer” has no standard definition.** Define it as the
  application/service boundary and compare transaction-script and domain-model
  shapes instead of prescribing one pattern.
- **Functional Python is hybrid.** Separate referential transparency,
  immutability, and composition from imitation of purely functional languages.
- **ORM advice cannot replace database semantics.** Verify isolation, locking,
  retries, and constraints against the chosen database and driver.
- **SQL portability is bounded.** Mark standard versus PostgreSQL-specific
  claims; examples need execution plans and fixture data.
- **Data architecture labels are contested.** Lakehouse, mesh, warehouse, and
  event-driven forms are choices with organizational and operational costs.
- **Exactly-once needs a boundary.** State whether it covers the broker, pipeline
  state, external side effects, or the end-to-end outcome.
- **React purity means render purity.** It is not whole-application purity.
- **Next.js caching is version-sensitive.** Pin the major version and distinguish
  Cache Components from the previous model.
- **Security checklists are baselines.** Threat context determines applicable
  ASVS controls and rigor.
- **Prompt tactics age quickly.** Require representative evals and distinguish
  stable prompt structure from model-specific advice.
- **Agent design and engineering overlap.** Design covers decomposition, tools,
  memory, and human control; engineering covers contracts, execution,
  observability, evaluation, recovery, cost, and operations.
- **Research prototypes are not production proof.** ReAct and Toolformer establish
  techniques under specific experiments; system claims require current evals.

Every article also needs a reproducible example, a failure case, a review
checklist, and one challenged claim. Agent pieces need fixtures for task success,
unsafe-action prevention, tool errors, and recovery—not merely fluent output.
