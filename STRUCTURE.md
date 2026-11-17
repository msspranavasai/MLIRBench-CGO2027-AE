# Artifact structure

The repository keeps runtime and scientific paths stable wherever required by imports, manifests, and reproducibility tools. The optional mutation catalog contains an intentional correction excluding the unused Linalg `L2_R2` entry. Published data and historical observations remain distinct from optional live-agent configuration.

| Path | Purpose |
|---|---|
| `ae.sh`, `Dockerfile`, `requirements/` | Single-container launcher, image definition and dependency pins |
| `src/mlirbench/` | Pipeline, checkpoint verification, execution, scoring and reports |
| `optional/live_pipeline/` | Four-agent implementations and optional live-model adapters |
| `data/` | Published scientific records, downstream predictions and provenance |
| `experiments/` | Manuscript expectations, experiment configurations and numerical policy |
| `paper/reference/` | Accepted manuscript and reference materials |
| `tests/` | Unit, integration and compiler tests |
| `tools/` | Runtime and release verification utilities |
| `docs/` | Detailed workflows, known limitations and release guidance |
| `release/` | Historical and final checksums, source-file mapping and resource inventory |
| `release_tools/` | Distribution verification and packaging utilities |
| `.github/workflows/` | Native-platform and launcher verification; publication behavior depends on the versioned workflow |
| `docker/` (complete archive only) | Exported multi-platform image and inventory |
| `assets/nova/` (complete archive only) | Optional adapters, compiler records and datasets |
| `evidence/` (complete archive only) | Archived scientific and release-validation evidence |

Generated reviewer outputs are written outside the checkout by default, under `../MLIRBench-AE-runs/`. Build caches, transient logs and unrelated development artifacts are not part of the scientific distribution.

The complete archive excludes `.git/`. Release identity and file integrity are documented in [PROVENANCE.md](PROVENANCE.md) and the manifests under `release/`.

The final source map must classify intentionally modified files accurately rather than treating all paths as byte-for-byte unchanged.
