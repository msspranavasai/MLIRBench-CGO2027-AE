"""Installed-wheel entry point for an external, version-matched AE artifact.

The historical source-checkout entry point (mlirbench.cli) is unchanged.
This adapter only relocates the paths used by the CLI. It does not change
execution, label semantics, or archived scientific data.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import sys

from . import __version__

ARTIFACT_ENV = "MLIRBENCH_ARTIFACT_ROOT"
REQUIRED_FILES = (
    "data/bundle/manifest.json",
    "experiments/claims.json",
)


def locate_artifact_root(default_root: Path | None = None) -> Path:
    """Resolve the complete artifact directory, never a site-packages guess."""
    if default_root is None:
        from . import cli
        default_root = cli.ROOT
    configured = os.environ.get(ARTIFACT_ENV, "").strip()
    if configured:
        candidate = Path(configured).expanduser()
        if not candidate.is_absolute():
            raise SystemExit(f"{ARTIFACT_ENV} must be an absolute path: {configured}")
        root = candidate.resolve()
    else:
        root = Path(default_root).resolve()

    missing = [name for name in REQUIRED_FILES if not (root / name).is_file()]
    if missing:
        message = (f"No complete MLIRBench artifact at {root}. Missing: "
                   + ", ".join(missing) + ". ")
        if configured:
            message += f"Correct {ARTIFACT_ENV} to point to the extracted artifact directory."
        else:
            message += (f"The standalone wheel does not bundle paper datasets; "
                        f"set {ARTIFACT_ENV} to an absolute extracted-artifact path.")
        raise SystemExit(message)

    metadata_path = root / "release/release.json"
    if metadata_path.is_file():
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            raise SystemExit(f"Invalid release metadata in {metadata_path}: {exc}") from exc
        if metadata.get("version") != __version__:
            raise SystemExit(
                f"Artifact version {metadata.get('version')!r} does not match "
                f"installed MLIRBench version {__version__!r}"
            )
    return root


def main(argv: list[str] | None = None) -> int:
    """Run original reviewer commands with validated artifact paths."""
    from . import cli

    if argv is None:
        argv = sys.argv[1:]
    # Documentation/help must remain available even without an artifact.
    if "-h" in argv or "--help" in argv:
        return cli.main(argv)

    root = locate_artifact_root(cli.ROOT)
    # Restore globals on exit, for embedders and tests in one Python process.
    original = (cli.ROOT, cli.DATASET, cli.HISTORICAL)
    try:
        cli.ROOT = root
        cli.DATASET = root / "data/processed/MLIRBench/master/master.jsonl"
        cli.HISTORICAL = root / "data/historical/historical_execution.jsonl"
        return cli.main(argv)
    finally:
        cli.ROOT, cli.DATASET, cli.HISTORICAL = original
