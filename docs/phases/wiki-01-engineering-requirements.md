# Wiki 01 engineering requirements

## Active user goal

Create and publish a MkDocs wiki from the knowledge in `a3-code-quality`.

## Source of truth

This document governs Wiki 01. The source content is
`a3-code-quality/knowledge`; `mkdocs.yml` governs the published information architecture.

## Why this phase advances the goal

It turns the Markdown knowledge collection into a searchable, navigable,
publicly deployable site without changing the source project's optional tooling.

## Phase goal

Deliver a production-valid MkDocs Material site and GitHub Pages workflow.

## Requirements

- Publish all 15 quality dimensions and five process guides.
- Provide clear home navigation, site search, responsive theme, light/dark modes,
  edit links, and accessible semantic Markdown.
- Build with `mkdocs build --strict` using pinned dependencies.
- Publish committed static HTML from `main` / repository root.
- Validate generated output in CI with least privilege and immutable action pins.

## Non-goals

Custom domain, analytics, comments, authentication, server-side search, or an
automatic cross-repository synchronization system.

## Assumptions

The repository is public or has an organization plan supporting Pages, and the
repository Pages source can be configured for GitHub Actions.

## Affected layers and modules

Wiki Markdown, MkDocs configuration/theme, dependency manifest, workflow, and delivery docs.

## Dependency/library choices

MkDocs 1.6.1 and Material for MkDocs 9.7.7, project-locally installed and pinned.

## Architecture notes

Markdown and `mkdocs.yml` are canonical; MkDocs output is generated into a
temporary directory and synchronized into the repository root for branch-based Pages.

## Data, API, and configuration changes

No APIs or user data. The public URL is
`https://a3-harness.github.io/code-quality-wiki/`.

## Demo requirements

Strict local build, HTML/link smoke checks, workflow syntax inspection, and live Pages verification.

## Test requirements

Validate strict build, expected page count, generated search index, internal
links, required HTML titles, and absence of committed build output.

## Security and sandbox considerations

Workflow permissions are read-only. Actions are pinned to immutable SHAs.
No secrets or analytics are required. Published content must contain no private data.

## Risks

Pages may not be enabled, organization policy may block Actions, or copied
knowledge may drift. Record publication state and make synchronization explicit.

## Acceptance criteria

Local strict build passes, generated root content is current and searchable, CI
is valid, main is pushed, branch-root Pages deployment succeeds, and the URL responds.

## Rollback plan

Disable the Pages workflow or revert its commit. The repository remains a valid
Markdown collection even without deployment.
