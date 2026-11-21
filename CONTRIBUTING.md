# Contributing to MLIRBench

MLIRBench is a compiler-reasoning benchmark and dataset, with its CGO 2027 scientific baseline preserved independently of later code improvements. Read [ARTIFACT.md](ARTIFACT.md), [REPRODUCIBILITY.md](REPRODUCIBILITY.md), and [docs/known-limitations.md](docs/known-limitations.md) before changing execution or evaluation behavior.

## Which workflow should I use?

- **AE evaluator:** Download the complete versioned release archive, including the exported container image and its checksum sidecar, and follow `README.md`. A Git checkout is *not* the complete offline distribution. The core replay does not use paid APIs.
- **CPU/code contributor:** Use the supported container when you need the pinned IREE and Torch-MLIR toolchains. Python 3.11 is the reference interpreter (`.python-version`). On a supported machine with preinstalled toolchains, `python3.11 -m pip install -e '.[live,dev]'` installs Python dependencies. The separately pinned paper compiler backend, scientific data bundles and GPU models require their documented setup; the Python package alone is not the full research environment.
- **Dataset contributor:** Preserve the existing scientific reference and published record IDs. New datasets and dialects must use new versioned schemas or releases, not overwrite the CGO 2027 baseline.

## Before opening a pull request

1. Make the change on a feature branch; do not force-push an archival tag.
2. Run `python3.11 -B scripts/check_repo_consistency.py` and `python3.11 -B release_tools/verify_distribution.py --source-only`.
3. From the pinned reviewer container run the 214-test suite and the complete `quickstart` workflow, preserving reports and source/image fingerprints. When relevant, also run fresh compiler tests on both AMD64 and ARM64.
4. If the change affects any file included in the release's fingerprint or distribution manifest, rebuild the image and complete archive. Recompute manifests and outer SHA-256 checksums. Never relabel old binary bytes as a new build.
5. Document the scientific and reproducibility implications, including whether the result uses archived predictions or fresh computation. Provide exact input identities and CLI commands.
6. Confirm no credentials, private environment files, personal paths requiring access, caches, or unintended generated files are committed. Public historical provenance can contain source-host path metadata; do not interpret those paths as current runtime prerequisites.

## Code conventions

Keep offline replay separate from paid/live model inference; future model requests require explicit user authorization and credential checks. Validate outputs and return structured errors instead of silently substituting labels or scores. Use stable per-run output directories, retained source hashes and deterministic random seeds. Test both ordinary paths and failure paths.

Current v1 dialect support is Linalg and Torch. New dialect support is intentionally postponed until a separate versioned implementation. Do not modify or relabel archived Linalg/Torch records as part of extension work.

## Version and evidence policy

The current development branch inherits the verified `v0.3.0rc6` scientific baseline. Its Python metadata may be hardened before the later `v1.0.0` freeze. Do **not** claim a new public release or badge before the corresponding code, container, archive, DOI and independent validation exist. Review [docs/RELEASE_GATES.md](docs/RELEASE_GATES.md).
