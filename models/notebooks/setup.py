import sys
import os
from pathlib import Path

# Ensure repository root is on sys.path (two levels up from this file)
repo_root = str(Path(__file__).resolve().parents[2])
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

# Also include the notebooks folder (one level up) for any local utilities
notebooks_root = str(Path(__file__).resolve().parents[1])
if notebooks_root not in sys.path:
    sys.path.append(notebooks_root)