# Wiki 03 backlog: specialized articles

Each article must cite registry IDs, pin tested versions, include one minimal
example, one failure case, a review checklist, and explicit trade-offs.

## Publication contract

Articles are approved and canonical in `a3-code-quality`, then generated into
this repository under the Wiki 03 engineering requirements. `llm_wiki` supplies
immutable-source extraction and proposed research relationships, but its staging
pages are never published directly. Every item below therefore requires:

- canonical knowledge IDs and an approved promotion record;
- a publication route and generated-content hash;
- conversion of relationships to valid MkDocs links;
- a paired deterministic or AI-assisted tool workflow;
- a no-drift regeneration test and preserved editorial regions.

| ID | Article | Required reference IDs | Required evidence | Status |
|---|---|---|---|---|
| ART-301 | Python middle layer | `cosmic-service-layer`, `cosmic-uow`, `sqlalchemy-session`, `pep-249` | Transaction boundary tests and thin-handler comparison | complete |
| ART-302 | Functional-style Python | `py-functional-howto`, `py-functional-modules` | Pure/impure boundary example and readability counterexample | complete |
| ART-303 | Python data layer | `pep-249`, `sqlalchemy-session`, `postgres-transactions` | Constraint, rollback, retry, and concurrent-session tests | complete |
| ART-304 | SQL quality | `postgres-transactions`, `postgres-explain`, `owasp-sql-injection` | Fixture, parameterization test, and before/after plan | complete |
| ART-305 | Data architecture | `openlineage-spec`, `beam-model`, `lakehouse-paper` | Decision matrix with workload and ownership constraints | complete |
| ART-306 | Data engineering | `beam-model`, `kafka-design`, `openlineage-spec` | Late-data, replay, idempotency, and lineage scenarios | complete |
| ART-307 | React | `react-purity`, `react-effects`, `react-state` | Render/effect tests and state-shape refactor | complete |
| ART-308 | Node.js | `node-event-loop`, `node-security`, `owasp-asvs` | Event-loop delay and hostile-input tests | complete |
| ART-309 | Next.js | `next-production`, `next-security`, `react-purity` | Major-version pin, server/client exposure and cache tests | complete |
| ART-310 | Security | `nist-ssdf`, `owasp-asvs`, `owasp-sql-injection` | Threat model plus mapped verification evidence | complete |
| ART-311 | Prompt design | `openai-model-guidance`, `cot-paper`, `react-paper` | Versioned eval set with prompt variants, quality, cost, latency | complete |
| ART-312 | Agent design | `openai-agent-guide`, `react-paper`, `toolformer-paper`, `nist-ai-rmf-gai` | Deterministic-vs-agent decision and unsafe-action cases | complete |
| ART-313 | Agent engineering | `openai-model-guidance`, `openai-agent-guide`, `nist-ssdf`, `nist-ai-rmf-gai` | Tool-contract, trace, recovery, approval, and regression evals | complete |

Recommended sequence: 301–304 establish application/data boundaries; 307–310
cover runtime and security; 305–306 cover distributed data; 311–313 finish with
evaluation-led AI system guidance. Articles may proceed independently after
their required evidence fixture is defined.
