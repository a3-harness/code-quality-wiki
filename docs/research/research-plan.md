# Specialized knowledge research plan

## Goal

Establish a trustworthy reference base for specialized software-quality pieces
covering Python application layers and functional style, SQL and data systems,
JavaScript web stacks, security, prompt design, and agent engineering. Research
precedes article drafting so claims can be scoped, cited, and kept current.

## Topics and boundaries

| Topic | Intended focus | Boundary questions |
| --- | --- | --- |
| Python middle layer | Service/application/domain coordination, transaction boundaries, dependency direction, framework isolation | What belongs between transport and persistence? |
| Python functional style | Pure transformations, iterators, higher-order functions, immutability, effects, typing, and Pythonic limits | When does functional style clarify or obscure Python? |
| Python data layer | DB-API, ORM/session lifecycle, repositories, transactions, loading, migrations, and test seams | Where are identity, consistency, and resource ownership enforced? |
| SQL | Relational semantics, constraints, joins, nulls, transactions, isolation, query plans, injection, and migrations | Which claims are standard SQL versus engine-specific? |
| Data architecture | Ownership, operational/analytical boundaries, warehouse/lake/lakehouse, mesh, contracts, lineage, governance | Which topology fits which quality attributes? |
| Data engineering | Batch/stream processing, event time, delivery semantics, orchestration, testing, observability, and cost | What does the platform guarantee versus the pipeline implement? |
| React | Rendering model, state/effects, composition, accessibility, performance, testing, and security boundaries | What belongs in React versus browser/platform code? |
| Node.js | Event loop, async lifecycle, streams, errors, shutdown, packages, security, and diagnostics | Which work blocks progress or escapes lifecycle control? |
| Next.js | Server/client boundaries, routing, caching, rendering, data access, security, deployment, and upgrades | Which behavior depends on version, router, or hosting platform? |
| Security | Secure design/review, threat modeling, verification, supply chain, secrets, authn/authz, and operational response | Which controls are normative, contextual, or tool-specific? |
| Prompt design | Instruction hierarchy, task/context/output contracts, examples, structured output, injection resistance, iteration, and evals | Which advice is model-specific and empirically measured? |
| Agent design | Goals, state, tools, delegation, planning, human control, failure containment, and when not to use agents | What autonomy is necessary for the outcome? |
| Agent engineering | Runtime loops, tool contracts, persistence, tracing, evals, security, cost, concurrency, deployment, and incident response | How is behavior tested and operated as a system? |

## Research questions for every topic

1. What concepts and terms need precise definitions?
2. What quality attributes and failure modes dominate?
3. Which design choices are stable principles versus version-specific behavior?
4. What evidence can verify a claim in review, testing, and production?
5. What common advice has important counterexamples or tradeoffs?
6. Which primary sources support the guidance, and what is their authority?
7. What should a practitioner be able to decide after reading the piece?

## Source hierarchy

1. Normative specifications, standards, PEPs, and official framework/runtime docs.
2. Public-sector and nonprofit security/architecture guidance.
3. Original peer-reviewed papers and author-hosted technical reports.
4. Maintainer engineering articles and official vendor architecture guidance,
   explicitly labeled where product-specific.
5. Practitioner books and courses as identified reading only unless their
   licenses permit local redistribution.

Secondary tutorials, SEO articles, unsourced checklists, and generated summaries
may help discover vocabulary but will not support final claims.

## Version and citation policy

- Record publisher, title, canonical URL, source type, topic, access date,
  version/date, license/access status, and applicability notes.
- Prefer versioned/permalink URLs. Flag living documentation as time-sensitive.
- Separate Python language guidance from framework patterns and SQL standards
  from PostgreSQL/SQLite-specific behavior.
- Cite claims near the relevant passage in future articles, not only in a bibliography.
- Recheck framework and model-platform documentation immediately before drafting.
- Do not treat one vendor's documentation as universal architecture guidance.

## Download policy

- Download only resources with clear public-domain or redistribution terms.
- Store downloads under `references/downloads/` with a SHA-256 manifest.
- Do not copy paywalled books, standards, or restricted training material.
- For restricted but valuable works, record exactly what the user can buy or
  download from the rights holder.
- Prefer links for living documentation so readers reach maintained content.

## Execution passes

### Pass 1 — Authoritative map

Identify primary sources for all 13 topics and record why each source matters.

### Pass 2 — Standards and seminal work

Add cross-cutting sources for architecture, security, distributed data,
prompting, agents, evaluation, and human oversight.

### Pass 3 — Acquisition and integrity

Download clearly redistributable anchor documents, record hashes/licenses, and
list restricted resources the user may obtain separately.

### Pass 4 — Gap and conflict analysis

Identify terminology conflicts, version-sensitive claims, weakly sourced areas,
and questions requiring hands-on experiments rather than citations.

### Pass 5 — Article backlog

Turn the evidence map into a drafting order, required sections, reference sets,
and acceptance tests for each specialized piece.

## Deliverables

- This research plan.
- A machine-readable source registry and human-readable reference map.
- Download manifest with origin, license note, and SHA-256 checksum.
- A user-acquisition list for valuable restricted resources.
- Gap/conflict notes and an evidence-backed article backlog.

## Completion criteria

- Every topic has at least two primary/official anchors and one independent or
  cross-cutting source where appropriate.
- Every registry entry has authority, currency, access, and applicability notes.
- Downloaded files match recorded hashes and redistribution rationale.
- Restricted works are identified without unauthorized copying.
- Drafting order follows dependency and evidence strength, not topic popularity.
