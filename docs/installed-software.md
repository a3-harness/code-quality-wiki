# Installed software

## MkDocs 1.6.1 and Material for MkDocs 9.7.7

- **Install command:** `.venv/bin/python -m pip install --requirement requirements.txt`
- **Reason:** build and validate the static knowledge wiki.
- **Scope:** project-local development, test, and documentation build tooling.
- **Reproducibility:** direct dependencies are pinned in `requirements.txt`;
  CI installs the same file. The `.venv/` and generated `site/` directories are ignored.
- **Cleanup:** remove `.venv/` and `site/`; no global package installation is performed.
