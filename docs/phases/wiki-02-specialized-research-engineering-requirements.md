# Wiki 02 engineering requirements: specialized research

## Active user goal

Prepare and execute rigorous research for 13 specialized knowledge areas before
writing the corresponding wiki pieces.

## Source of truth

`docs/research/research-plan.md` governs research method; the source registry is
the evidence inventory.

## Why this phase advances the goal

Specialized guidance becomes misleading when framework versions, vendor advice,
or architecture fashions are presented as universal facts. This phase creates
traceable evidence and explicit boundaries first.

## Phase goal

Deliver a verified primary-source map, lawful offline anchors, gap analysis, and
article backlog for all requested topics.

## Requirements

- Cover all 13 named topics.
- Prioritize primary and official sources; label vendor and version scope.
- Record access, license, currency, applicability, and download status.
- Download only clearly permitted resources and hash them.
- Identify restricted resources for user acquisition.
- Validate registry structure, URLs, topics, and local download hashes.

## Non-goals

Drafting the full specialized articles, copying books/standards, or asserting
that cited guidance is universally applicable.

## Assumptions

Living web documentation will remain external; a small set of stable standards
can be retained offline. Internet access is authorized for this research phase.

## Affected layers and modules

`docs/research/`, `references/`, validation scripts, MkDocs navigation, and phase evidence.

## Dependency/library choices

Standard-library validation and command-line download tools only; no new package installation.

## Architecture notes

The JSON registry is the structured citation inventory; Markdown maps explain
selection and gaps. Specialized articles will cite canonical URLs directly.

## Data, API, and configuration changes

Add reference-registry schema conventions and exclude binary research downloads
from the published MkDocs navigation while retaining them in Git history when licensed.

## Demo requirements

Validate all topics, URLs, required metadata, download hashes, and strict site build.

## Test requirements

Registry parsing, topic coverage, unique IDs, HTTPS canonical URLs, required
fields, existing local copies, matching SHA-256 hashes, and MkDocs strict build.

## Security and sandbox considerations

Treat downloaded content as untrusted data; do not execute it. Avoid secrets,
authenticated scraping, license circumvention, or unpublished/private sources.

## Risks

Documentation drift, vendor bias, citation laundering, licensing ambiguity, and
topic overlap. Mitigate through source labels, dates, independent anchors, and gaps.

## Acceptance criteria

The research plan completion criteria are met and validation is reproducible.

## Rollback plan

Remove the additive research registry, downloads, and navigation entries; the
published first-edition knowledge remains intact.
