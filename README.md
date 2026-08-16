# Software Quality Knowledge Base Wiki

The publishable MkDocs edition of the software-quality knowledge developed in
[`a3-code-quality`](https://github.com/a3-harness/a3-code-quality).

## Local preview

```bash
python -m venv .venv
.venv/bin/python -m pip install --requirement requirements.txt
.venv/bin/mkdocs serve
```

Open <http://127.0.0.1:8000/>. Validate a production build with:

```bash
.venv/bin/mkdocs build --strict
```

## Publishing

Pushing `main` runs `.github/workflows/pages.yml`. The workflow builds the site,
uploads a GitHub Pages artifact, and deploys it to:

<https://a3-harness.github.io/code-quality-wiki/>

The repository's Pages source must be set to **GitHub Actions**. The workflow
uses only `contents: read`, `pages: write`, and `id-token: write`, with every
third-party action pinned to a commit SHA.

## Content ownership

The wiki is an independently publishable reader experience. The source
knowledge currently originates in `a3-code-quality/knowledge`; future edits
should be reconciled deliberately rather than copied in both directions without review.
