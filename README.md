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

## Publishing from `main` / repository root

Generate and commit the static HTML at the repository root:

```bash
.venv/bin/python scripts/publish_root.py
git add -A
git commit -m "update published wiki"
git push
```

GitHub Pages serves those committed files from `main` / `(root)` at:

<https://a3-harness.github.io/code-quality-wiki/>

The repository's Pages source must be **Deploy from a branch**, branch `main`,
folder `/(root)`. The validation workflow rebuilds the site and fails if the
committed HTML is stale.

## Content ownership

The wiki is an independently publishable reader experience. The source
knowledge currently originates in `a3-code-quality/knowledge`; future edits
should be reconciled deliberately rather than copied in both directions without review.
