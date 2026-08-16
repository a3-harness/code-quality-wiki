# Wiki 03 demo: first specialist publication wave

Status: complete

- Thirteen pages were generated from canonical A3 knowledge IDs.
- The publication manifest records routes, source paths, and content hashes.
- A second generation check reported no drift.
- MkDocs strict build completed and root output contains all thirteen routes.
- Site smoke validation reports 194 searchable documents.

Every page includes a worked case, counterexample, evidence questions, reference
IDs, tooling boundaries, and a preserved publication-specific editorial region.

## Full publication rerun — 2026-08-16

### Setup

- Canonical repository: sibling `a3-code-quality` checkout at `86bba227`.
- Publication repository: this checkout on `main`.
- MkDocs runtime: existing `.venv` executed inside the project development
  container; no dependencies were installed.

### Commands

```bash
cd ../a3-code-quality
python3 -m unittest discover -s tests -v
python3 scripts/publish_wiki.py --write
python3 scripts/publish_wiki.py --check

cd ../code-quality-wiki
.venv/bin/python scripts/publish_root.py
.venv/bin/python scripts/check_references.py
.venv/bin/python scripts/check_site.py --site-dir .
python3 ../a3-code-quality/scripts/publish_wiki.py --check
```

### Expected and observed behavior

- Expected: all 13 canonical pages regenerate, the manifest points to the
  current source commit, the root site builds strictly, and a second generation
  reports no drift.
- Observed: 38 canonical tests passed; 13 pages regenerated; the manifest now
  points to `86bba2272dc24e5a714efecd0c15b9833d15914c`; the registry reported 28
  sources covering 13 topics; the smoke check reported 15 dimensions and 283
  searchable documents; the final drift check passed.
- Generated artifact: `publication-manifest.json` plus the committed root-site
  directories listed in `scripts/publish_root.py`.
- Known gaps: the local commit is intentionally not pushed by this workflow;
  remote publication remains an explicit maintainer action.
- Video: not applicable because this is a deterministic non-UI publication
  pipeline; the command-output evidence above exercises every acceptance gate.

### Requirement mapping

- Canonical ownership and traceability: manifest source commit and hashes.
- Reproducibility: write followed by two successful check-mode runs.
- Publication: strict MkDocs root build and root-site smoke validation.
- Source integrity: reference registry hash and topic-coverage validation.
