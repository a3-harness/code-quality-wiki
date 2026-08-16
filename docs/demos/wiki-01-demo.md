# Wiki 01 demo

## Local commands

```bash
.venv/bin/mkdocs build --strict
python scripts/check_site.py
```

## Publication checks

```bash
gh run list --workflow pages.yml --limit 1
curl --fail --location https://a3-harness.github.io/code-quality-wiki/
```

Final observed results are recorded in the delivery status.
