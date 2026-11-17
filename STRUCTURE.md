# Artifact structure

Scientific paths are preserved to protect imports, manifests and runtime behavior. No empty organizational directories are created.

| Path | Purpose |
|---|---|
| `ae.sh`, `Dockerfile`, `requirements/` | One-container launcher, unified image and pinned dependencies |
| `src/mlirbench/` | Pipeline, checkpoint verification, execution, scoring and report implementation |
| `optional/live_pipeline/` | Original agents and optional live-model implementation |
| `data/` | Frozen compressed published records, downstream predictions and provenance |
| `experiments/` | Manuscript expectations, configurations, numerical policy and invariants |
| `paper/reference/` | Accepted manuscript and source identification |
| `tests/` | Existing unit/integration and compiler tests |
| `tools/` | Preserved runtime/release verification tools |
| `docs/` | Scientific limitations and detailed workflow references |
| `release/` | Original file inventory, source mapping and resource provenance |
| `release_tools/` | Non-scientific distribution verification/packaging |
| `.github/workflows/` | Native anonymous-pull and macOS launcher verification; no image publication |
| `docker/` (complete archive only) | One exported image and its inventory |
| `assets/nova/` (complete archive only) | Copied optional adapters, compiler records and datasets; no Nova login needed |
| `evidence/` (complete archive only) | Frozen diagnostic and native CI verification evidence |

Generated reviewer outputs remain outside the checkout by default in `../MLIRBench-AE-runs/`. Historical scientific observations within frozen inputs remain intact; transient caches and development logs are not distributed. The complete archive excludes `.git/`; source history is available through the original repository referenced in PROVENANCE.md.
