# Reference map

This is the writing team's map to the vetted registry in
`references/source-registry.json`. It is a starting set, not an instruction to
treat documentation or vendor claims as universal best practice.

## Use rules

1. Start with the official specification or current framework documentation.
2. Add an independent standard or original study for cross-product claims.
3. Label vendor guidance and architecture patterns as contextual advice.
4. Cite an exact version or access date for living sources.
5. Test behavioral claims with a minimal example before publishing them.

## Coverage

| Topic | Primary anchors | Counterweight or cross-cutting anchor |
|---|---|---|
| Python middle layer | Cosmic Python service layer/unit of work; SQLAlchemy Session | PEP 249 transaction contract |
| Python functional style | Python Functional HOWTO and functional modules | React purity as a bounded comparison, not a Python authority |
| Python data layer | PEP 249; SQLAlchemy Session | PostgreSQL isolation semantics |
| SQL | PostgreSQL isolation and `EXPLAIN` | OWASP SQL injection guidance; ISO SQL listed for acquisition |
| Data architecture | OpenLineage specification; Beam model | Lakehouse paper, treated as an argument to evaluate |
| Data engineering | Beam model; Kafka design | OpenLineage specification |
| React | React purity, state structure, and Effects guides | Security standards added per article |
| Node.js | Node event-loop and security guidance | OWASP ASVS testable controls |
| Next.js | Current App Router security and production guides | React guidance and OWASP ASVS |
| Security | NIST SSDF; OWASP ASVS | NIST AI profile for AI systems |
| Prompt design | Current OpenAI model guidance | Chain-of-thought and ReAct papers, with model-era limits |
| Agent design | OpenAI practical guide | ReAct, Toolformer, and NIST AI profile |
| Agent engineering | OpenAI model/agent guidance | NIST SSDF, NIST AI profile, ReAct, and Toolformer |

## Reproducible snapshots

Three exact artifacts are retained with hashes in the registry: PEP 249, NIST
SP 800-218, and NIST AI 600-1. All other sources remain canonical links. This
avoids freezing fast-moving framework docs and redistributing material whose
reuse terms are unclear.

## Currency flags

“Living” means the author must revisit the source before making a
version-sensitive claim. This applies especially to React, Node.js, Next.js,
OpenAI, Kafka, Beam, OpenLineage, and PostgreSQL's `current` alias. Stable papers
show what was demonstrated at publication time; they do not establish current
production behavior.
