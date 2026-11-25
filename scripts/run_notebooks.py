"""Execute all notebooks of the workshop and report failures.

Usage (notebooks are searched relative to the current working directory):
    pip install -r requirements.txt nbclient
    python scripts/run_notebooks.py                 # all notebooks below cwd
    python scripts/run_notebooks.py exercises       # all notebooks in a folder
    python scripts/run_notebooks.py 1_1_matplotlib.ipynb exercises/CRISPRi/figure_2a.ipynb

Notebooks are executed in their own directory (like in Jupyter); they are
not modified on disk.
"""

import sys
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

ROOT = Path.cwd()
SKIP_DIRS = {"_build", "jupyter_execute", ".ipynb_checkpoints"}


def find_notebooks(base: Path = ROOT) -> list[Path]:
    return sorted(
        p
        for p in base.rglob("*.ipynb")
        if not SKIP_DIRS.intersection(p.relative_to(base).parts)
    )


def collect(args: list[str]) -> list[Path]:
    if not args:
        return find_notebooks()
    notebooks = []
    for arg in args:
        path = Path(arg).resolve()
        notebooks.extend(find_notebooks(path) if path.is_dir() else [path])
    return notebooks


def display(path: Path) -> Path:
    try:
        return path.relative_to(ROOT)
    except ValueError:
        return path


def run(path: Path, timeout: int = 600) -> None:
    nb = nbformat.read(path, as_version=4)
    client = NotebookClient(
        nb,
        timeout=timeout,
        kernel_name="python3",
        resources={"metadata": {"path": str(path.parent)}},
    )
    client.execute()


def main() -> int:
    notebooks = collect(sys.argv[1:])
    failed = []
    for path in notebooks:
        rel = display(path)
        print(f"Running {rel} ...", end=" ", flush=True)
        start = time.perf_counter()
        try:
            run(path)
        except CellExecutionError as e:
            print("FAILED")
            print(str(e)[-2000:])
            failed.append(rel)
            continue
        print(f"ok ({time.perf_counter() - start:.1f}s)")

    print(
        f"\n{len(notebooks) - len(failed)}/{len(notebooks)} notebooks ran successfully."
    )
    for rel in failed:
        print(f"  failed: {rel}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
