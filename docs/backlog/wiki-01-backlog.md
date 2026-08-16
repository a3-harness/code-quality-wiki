# Wiki 01 backlog

## WIKI-101 — Establish the MkDocs site

- **Rationale:** The empty repository needs a reproducible static-site foundation.
- **Affected files/modules:** `mkdocs.yml`, dependencies, theme assets.
- **Implementation steps:** Configure Material, search, navigation, theme, and pins.
- **Unit test expectations:** Strict configuration build.
- **E2E test expectations:** Generated site smoke test.
- **Demo relevance:** Site foundation.
- **Acceptance criteria:** Clean environment builds without warnings.
- **Status:** complete

## WIKI-102 — Curate the knowledge collection

- **Rationale:** Source pages need a coherent web navigation model.
- **Affected files/modules:** `docs/index.md`, dimensions, process pages.
- **Implementation steps:** Migrate all pages and create reader-first navigation.
- **Unit test expectations:** Expected source/page/link checks.
- **E2E test expectations:** Search and navigation artifacts exist.
- **Demo relevance:** Primary user experience.
- **Acceptance criteria:** 15 dimensions and 5 processes are reachable.
- **Status:** complete

## WIKI-103 — Publish GitHub Pages from the repository root

- **Rationale:** The user requested a live wiki, not only local files.
- **Affected files/modules:** generated root HTML, `.nojekyll`, validation workflow.
- **Implementation steps:** Build with MkDocs, synchronize root output, validate drift in CI.
- **Unit test expectations:** Workflow and dependency inspection.
- **E2E test expectations:** Successful Actions run and public URL response.
- **Demo relevance:** Publication evidence.
- **Acceptance criteria:** Main/root Pages serves the current strict build.
- **Status:** complete

## WIKI-104 — Record demo and delivery evidence

- **Rationale:** Publication should be reproducible and supportable.
- **Affected files/modules:** demo/status docs and README.
- **Implementation steps:** Record build, smoke, deployment, URL, and limitations.
- **Unit test expectations:** All local validation.
- **E2E test expectations:** Live response.
- **Demo relevance:** Phase closeout.
- **Acceptance criteria:** Another maintainer can preview, build, and publish.
- **Status:** pending
