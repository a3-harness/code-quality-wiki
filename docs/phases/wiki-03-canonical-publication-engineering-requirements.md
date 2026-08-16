# Wiki 03 engineering requirements: canonical specialist publication

## Active user goal

Publish the specialist software-quality knowledge developed from vetted
references and AI-assisted tooling, without turning this repository into a
second manually maintained source of truth.

## Source of truth and repository roles

- `llm_wiki` ingests immutable reference files and maintains a proposed research
  graph. Its extracted cache and staging pages are not public knowledge.
- `a3-code-quality` owns approved structured knowledge, canonical explanatory
  Markdown, review tooling, and promotion decisions.
- This repository owns MkDocs presentation, navigation, editorial framing, and
  root/main GitHub Pages output.

The Phase 05 requirements in `a3-code-quality` govern the cross-repository flow.

## Phase goal

Generate, review, and publish 13 cited specialist sections from canonical IDs,
with stable routes, source-version warnings, tool examples, and reproducible
publication manifests.

## Requirements

- Accept only approved canonical knowledge, never raw `llm_wiki` staging output.
- Convert canonical relationships to normal MkDocs links; Obsidian staging links
  must not leak into published pages.
- Separate generated zones from publication-specific editorial content.
- Record source commit, generator version, content hashes, routes, and freshness
  warnings in a publication manifest.
- Pair each knowledge article with relevant deterministic and optional AI-tooling
  usage while preserving human-judgment boundaries.
- Support `--check` without writes and reproducible `--write` generation.

## Non-goals

Reference extraction, live model calls, canonical claim approval, direct
publication from `llm_wiki`, or manual duplication of canonical articles.

## Assumptions

GitHub Pages continues to serve root-generated MkDocs HTML from `main`.

## Affected layers and modules

`docs/`, `mkdocs.yml`, generator/check scripts, publication manifest, root HTML,
search index, sitemap, and site tests.

## Dependency choices and architecture

Use the existing MkDocs environment and a small deterministic importer/renderer.
The pipeline is approved A3 data/Markdown → wiki source pages → MkDocs root
output. A source adapter may read `llm_wiki` export metadata for provenance
checks, but it cannot bypass A3 promotion.

## Data and configuration changes

Add a publication-manifest schema, canonical-ID frontmatter, generated-zone
markers, route mappings, and freshness display conventions.

## Demo and test requirements

Generate one specialist wave, demonstrate preserved editorial content, fail on
staging/unapproved input, run a no-drift second generation, build MkDocs strictly,
and smoke-test every route, citation link, navigation entry, and search record.

## Security considerations

Treat imported Markdown and model-derived text as untrusted. Escape unsafe HTML,
exclude raw/private source content, avoid secrets in manifests, and require
explicit human action for commit or push.

## Risks

Canonical drift, accidental publication of restricted material, broken link
conversion, stale framework advice, and generated overwrites. Mitigate with
promotion state, licenses, hashes, freshness warnings, protected regions, and
check mode.

## Acceptance criteria

All 13 specialist routes are reproducibly generated from approved canonical IDs,
cited, searchable, linked to tooling guidance, and publishable from root/main
without manual reconciliation.

## Rollback plan

Remove the generated specialist routes and restore the prior publication
manifest. Existing dimension and process pages remain intact; canonical and
staging knowledge stay in their owning repositories.
