"""
lib/assignment_loader.py
========================
Dynamically imports a student's solution file and verifies it by running the
unit tests that live alongside it in the assignment folder.

Usage (called by the Next.js API route):
    python3 lib/assignment_loader.py <assignment_folder_name>

Exit codes:
    0  — all tests passed
    1  — one or more tests failed, or the solution / test file could not be loaded

The script writes human-readable output to stdout/stderr, which the API route
captures and forwards to the dashboard UI.
"""

from __future__ import annotations

import importlib.util
import os
import sys
import unittest


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_module_from_file(module_name: str, file_path: str):
    """Import a Python source file as a module, regardless of its location."""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot create module spec for {file_path!r}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module  # register so relative imports work
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


# ---------------------------------------------------------------------------
# Core loader
# ---------------------------------------------------------------------------

def check_assignment(assignment_id: str) -> bool:
    """
    Load the student solution and run the associated test suite.

    Parameters
    ----------
    assignment_id : str
        The name of the assignment folder (e.g. ``"assignment1"`` or
        ``"review4"``). The folder is expected to live at
        ``assignments/<assignment_id>/`` relative to the repository root.

    Returns
    -------
    bool
        ``True`` if every test in ``test_solution.py`` passed, ``False``
        otherwise.
    """
    # Resolve paths relative to this file's grandparent (repo root).
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assignment_dir = os.path.join(repo_root, "assignments", assignment_id)

    solution_path = os.path.join(assignment_dir, "solution.py")
    test_path = os.path.join(assignment_dir, "test_solution.py")

    # Validate that both files exist.
    for path, label in [(solution_path, "solution.py"), (test_path, "test_solution.py")]:
        if not os.path.isfile(path):
            print(f"[ERROR] {label} not found at: {path}", file=sys.stderr)
            return False

    # Make the assignment directory importable so that ``test_solution.py``
    # can do ``import solution`` or ``from solution import ...``.
    if assignment_dir not in sys.path:
        sys.path.insert(0, assignment_dir)

    # Load the student's solution module.
    try:
        _load_module_from_file("solution", solution_path)
    except Exception as exc:  # noqa: BLE001
        print(f"[ERROR] Could not load solution.py: {exc}", file=sys.stderr)
        return False

    # Load the test module (this *also* imports solution via normal imports).
    try:
        test_module = _load_module_from_file("test_solution", test_path)
    except Exception as exc:  # noqa: BLE001
        print(f"[ERROR] Could not load test_solution.py: {exc}", file=sys.stderr)
        return False

    # Discover and run all TestCase subclasses defined in the test module.
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_module)

    runner = unittest.TextTestRunner(
        stream=sys.stdout,
        verbosity=2,
        failfast=False,
    )
    result = runner.run(suite)

    return result.wasSuccessful()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 lib/assignment_loader.py <assignment_id>", file=sys.stderr)
        sys.exit(1)

    assignment_id = sys.argv[1]

    # Basic sanity-check: only allow alphanumeric characters and hyphens/underscores.
    import re
    if not re.fullmatch(r"[\w-]+", assignment_id):
        print(f"[ERROR] Invalid assignment id: {assignment_id!r}", file=sys.stderr)
        sys.exit(1)

    passed = check_assignment(assignment_id)
    sys.exit(0 if passed else 1)
