# Wiki 02 backlog: specialized research

## RES-201 — Define method and topic boundaries

- **Rationale:** Prevent source collection from becoming an unscoped link dump.
- **Affected files/modules:** Research plan and phase requirements.
- **Implementation steps:** Define questions, source hierarchy, currency, license, and completion rules.
- **Unit test expectations:** All requested topic IDs represented.
- **E2E test expectations:** Plan is linked from research index.
- **Demo relevance:** Explains evidence quality.
- **Acceptance criteria:** Plan resolves overlaps and separates stable/versioned guidance.
- **Status:** complete

## RES-202 — Build authoritative source registry

- **Rationale:** Articles need traceable, queryable evidence.
- **Affected files/modules:** `references/source-registry.json`, reference map.
- **Implementation steps:** Research official/primary sources, record metadata and applicability.
- **Unit test expectations:** Schema, unique IDs, topic coverage, URLs.
- **E2E test expectations:** Published reference map builds.
- **Demo relevance:** Primary research output.
- **Acceptance criteria:** Every topic meets anchor-source criteria.
- **Status:** complete

## RES-203 — Acquire permitted offline anchors

- **Rationale:** Stable standards improve reproducibility and resilience to link drift.
- **Affected files/modules:** `references/downloads/`, download manifest.
- **Implementation steps:** Verify rights, download, hash, and record provenance.
- **Unit test expectations:** File/hash agreement.
- **E2E test expectations:** No downloaded file is executed or required to build.
- **Demo relevance:** Demonstrates reference integrity.
- **Acceptance criteria:** Every local copy has clear redistribution rationale.
- **Status:** complete

## RES-204 — Analyze gaps and restricted reading

- **Rationale:** Missing or inaccessible evidence must remain visible.
- **Affected files/modules:** Gap analysis and user-acquisition list.
- **Implementation steps:** Record conflicts, version risks, experiment needs, and rights-holder links.
- **Unit test expectations:** All topics receive a readiness state.
- **E2E test expectations:** Links build and registry remains primary-source weighted.
- **Demo relevance:** Prevents overclaiming.
- **Acceptance criteria:** Weak areas and restricted works are explicit.
- **Status:** complete

## RES-205 — Produce specialized article backlog

- **Rationale:** Research must convert into an executable writing sequence.
- **Affected files/modules:** Article backlog, demo, delivery status.
- **Implementation steps:** Order pieces, assign reference sets, sections, experiments, and acceptance tests.
- **Unit test expectations:** Every requested piece has a stable ID and sources.
- **E2E test expectations:** Strict site build and research validation.
- **Demo relevance:** Phase exit.
- **Acceptance criteria:** Drafting can begin without new scoping decisions.
- **Status:** complete
