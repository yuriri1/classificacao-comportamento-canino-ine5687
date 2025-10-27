import sys
from pathlib import Path

repo_root = str(Path(__file__).resolve().parents[2])
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

notebooks_root = str(Path(__file__).resolve().parents[1])
if notebooks_root not in sys.path:
    sys.path.append(notebooks_root)