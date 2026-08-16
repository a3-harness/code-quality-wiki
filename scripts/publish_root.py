from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / ".build-site"
PUBLISHED_PATHS = (
    "404.html",
    "assets",
    "dimensions",
    "index.html",
    "process",
    "search",
    "sitemap.xml",
    "sitemap.xml.gz",
    "stylesheets",
)


subprocess.run([sys.executable, "-m", "mkdocs", "build", "--strict"], cwd=ROOT, check=True)
for relative in PUBLISHED_PATHS:
    target = ROOT / relative
    if target.is_dir():
        shutil.rmtree(target)
    elif target.exists():
        target.unlink()
    source = BUILD / relative
    if source.is_dir():
        shutil.copytree(source, target)
    elif source.exists():
        shutil.copy2(source, target)
(ROOT / ".nojekyll").touch()
print("Published MkDocs output to the repository root.")
