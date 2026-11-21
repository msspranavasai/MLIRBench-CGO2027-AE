# Planned complete v1.0.0 distribution (not yet assembled)

The intended canonical file is `MLIRBench-CGO2027-AE-v1.0.0.tar.gz`; once built, its only top-level directory must be `MLIRBench-CGO2027-AE-v1.0.0/`. No complete v1.0.0 archive is asserted to exist yet.

| Path | Contents |
|---|---|
| `ae.sh`, `Dockerfile`, `requirements/` | Unified launcher and digest-pinned frozen-toolchain build |
| `src/`, `optional/live_pipeline/`, `tools/`, `tests/`, `experiments/` | Maintained workflow, optional adapters, scientific policies and tests |
| `data/`, `paper/reference/` | Frozen datasets/history/downstream snapshot and accepted reference |
| `assets/nova/` | Original 914-entry supplemental inventory including 11 adapters |
| `evidence/label-review/`, `evidence/native-ci/`, other restored evidence | Historical rc5 observations, not rc6 validation |
| `evidence/rc6/` | Earlier candidate evidence only; new v1.0.0 evidence must remain separately identified |
| `docker/` | Planned newly exported v1.0.0 multi-platform image and actual inventory; original rc5 toolchain recipe retained |
| `release/`, `release_tools/` | Release identity, manifests, classified source map and strict verification/packaging |

No `.git`, Python caches, environments, AppleDouble/resource-fork files, transient build data or credentials are packaged. All regular files are covered by `MANIFEST.sha256` except that manifest itself. A SHA-256 sidecar outside the archive covers the archive bytes. Executable bits are retained; tar owners/timestamps are normalized. Reviewer results default to the sibling `MLIRBench-AE-runs/` directory and are never packaged as scientific inputs.
