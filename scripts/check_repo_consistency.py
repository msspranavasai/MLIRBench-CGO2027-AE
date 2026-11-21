#!/usr/bin/env python3
"""Fast, stdlib-only source-repository consistency check (Python 3.11+).

This does NOT substitute for complete-distribution verification, tests or a fresh
container experiment. Historical rc5 references are intentionally not banned.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import tomllib

CORE = "requirements/core.txt"
LIVE = "requirements/live.txt"
REQUIRED = (
    "README.md", "ARTIFACT.md", "REPRODUCIBILITY.md", "PROVENANCE.md",
    "CITATION.cff", "LICENSE", "DATA_LICENSE.md", "Dockerfile", "ae.sh",
    "CONTRIBUTING.md", "docs/RELEASE_GATES.md", "release/release.json",
    "release/scientific-reference.sha256", "release/scientific-files.sha256",
    "experiments/release_invariants.json", ".github/workflows/ci.yml",
    ".github/workflows/repository-integrity.yml", ".python-version",
)


def requirement_lines(text: str) -> set[str]:
    return {line.strip() for line in text.splitlines()
            if line.strip() and not line.lstrip().startswith("#")}


def check(root: Path) -> list[str]:
    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    for path in REQUIRED:
        require((root / path).is_file(), f"Missing required file: {path}")
    if errors:
        return errors

    metadata = tomllib.loads((root / "pyproject.toml").read_text())
    project = metadata["project"]
    version = project["version"]
    require(project["name"] == "mlirbench", "Project name must be mlirbench")
    require(project["requires-python"] == ">=3.11,<3.13",
            "Supported Python range must match tested Python 3.11/3.12 dependency set")
    require((root / ".python-version").read_text().strip() == "3.11",
            ".python-version must identify the tested reference interpreter")
    require(set(project["dependencies"]) == requirement_lines((root / CORE).read_text()),
            "pyproject dependencies differ from requirements/core.txt")
    require(set(project.get("optional-dependencies", {}).get("live", [])) ==
            requirement_lines((root / LIVE).read_text()),
            "pyproject live extra differs from requirements/live.txt")

    package_init = (root / "src/mlirbench/__init__.py").read_text()
    require(re.search(r'__version__\s*=\s*[\"\']' + re.escape(version) + r'[\"\']',
                      package_init) is not None,
            "Python package version differs from pyproject.toml")
    citation = (root / "CITATION.cff").read_text()
    require(re.search(r"(?m)^version:\s*['\"]?" + re.escape(version) +
                      r"['\"]?\s*$", citation) is not None,
            "CITATION.cff version differs from pyproject.toml")

    release = json.loads((root / "release/release.json").read_text())
    require(release.get("version") == version,
            "Release metadata version differs from pyproject.toml")
    image = release.get("image")
    require(isinstance(image, str) and bool(image) and image.endswith(":" + version),
            "Release image must end with the package version (without a v prefix)")
    require(f"v{version}" in release.get("archive", ""),
            "Release archive filename must identify this version")
    require(f"v{version}" in release.get("root_directory", ""),
            "Distribution root directory must identify this version")
    if isinstance(image, str) and image:
        require(image in (root / "ae.sh").read_text(),
                "Default reviewer launcher image differs from release metadata")
        require(image in (root / ".github/workflows/ci.yml").read_text(),
                "Native CI image differs from release metadata")
    readme = (root / "README.md").read_text()
    require(f"v{version}" in readme.splitlines()[0],
            "README title version differs from release version")

    for path in ("README.md", "ARTIFACT.md", "REPRODUCIBILITY.md", "CONTRIBUTING.md",
                 "docs/RELEASE_GATES.md"):
        body = (root / path).read_text()
        for match in re.finditer(r"(?<!!)\[[^]]+\]\(([^)]+)\)", body):
            target = match.group(1).split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "/")):
                continue
            require((root / path).parent.joinpath(target).exists(),
                    f"Broken local Markdown link in {path}: {target}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    failures = check(root)
    if failures:
        for failure in failures:
            print("FAIL:", failure, file=sys.stderr)
        return 1
    print("PASS: Python versions, dependencies, current release metadata, image references,"
          " citation, required source files and checked Markdown links")
    print("NOTE: complete archive, container runtime, scientific experiments and secrets"
          " scan require separate validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
