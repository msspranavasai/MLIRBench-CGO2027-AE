# MLIRBench: CGO 2027 Artifact Evaluation — v0.3.0rc6

This local release candidate repairs packaging and optional live-configuration consistency after the [v1 Zenodo release](https://zenodo.org/records/24309675). It has **not been published**. Publication, final anonymous online testing and native AMD64 validation remain separate gates; see `FINAL_VALIDATION_REPORT.md`. No AE badge is claimed.

## Start here: complete offline distribution

Prerequisites: Docker Engine 29+ with the containerd image store (Docker Desktop is supported), Python 3.10+ for host verification, Bash, and at least 20 GB free disk space. The container has Python 3.11 and all required tools; no host MLIR or Python package installation is required.

Obtain these **two files together** from the approved release location when published, or use the delivered local candidate:

- `MLIRBench-CGO2027-AE-v0.3.0rc6.tar.gz`
- `MLIRBench-CGO2027-AE-v0.3.0rc6.tar.gz.sha256`

```bash
# In the directory containing both delivered files (macOS):
shasum -a 256 -c MLIRBench-CGO2027-AE-v0.3.0rc6.tar.gz.sha256
# Linux alternative: sha256sum -c MLIRBench-CGO2027-AE-v0.3.0rc6.tar.gz.sha256

tar -xzf MLIRBench-CGO2027-AE-v0.3.0rc6.tar.gz
cd MLIRBench-CGO2027-AE-v0.3.0rc6
python3 -B release_tools/verify_distribution.py
docker load -i docker/mlirbench-ae-v0.3.0rc6-image.tar
AE_IMAGE_SOURCE=local AE_IMAGE=ghcr.io/msspranavasai/mlirbench-ae:0.3.0rc6 ./ae.sh quickstart
```

This is a plain gzip-compressed tar, with exactly the top-level directory shown. Do not rename it to ZIP or add another archive wrapper. The earlier Zenodo upload was a ZIP around an unversioned tar and is not this candidate. The SHA-256 sidecar delivered with this candidate verifies these actual bytes; no claim is made that it was already published on Zenodo.

The experiment container runs with networking disabled. No model keys, paid inference, GPU, institutional services, GitHub access or registry pull is needed after the complete archive is acquired. Each command starts one disposable reviewer container; no Compose stack or companion database is used.

Output is written outside the artifact, under `../MLIRBench-AE-runs/quickstart-<timestamp>-<pid>/`. Open its `START_HERE.md`. To choose a different host folder, set `AE_OUTPUT_ROOT=/absolute/path/to/results`. Each run uses a new subdirectory and refuses to overwrite completed outputs. Repeat the same command for an independent second run.

## Public online route — requires approved publication

The intended immutable image is `ghcr.io/msspranavasai/mlirbench-ae:0.3.0rc6`. It is not asserted to be public yet. After source and image publication are approved and completed, run from the matching versioned source:

```bash
./ae.sh quickstart
```

The launcher pulls the native variant and checks the real runtime source fingerprint. Do not bypass a mismatch. The source and binary use a new rc6 identity; rc5 public bytes/tags are preserved.

## Scientific scope

Frozen inputs remain 1,768 program pairs (888 Linalg, 880 Torch), 15,912 saved reasoning records from nine models, and 15,907 judged records. The required quickstart verifies inputs, runs the supplied tests, replays all four archived stages, recomputes objective correctness and scores, compares paper tables, replays downstream saved-prediction metrics, checks archived compiler arithmetic and compiles/executes representative Linalg/Torch pairs.

Expected baseline: 214 passing tests, 64 preservation checks, 61 accepted benchmark checks (40 exact; 21 within the unchanged 0.15/100 Table 4 policy), 76 matching downstream comparisons, and successful repeated CPU pair checks. These are expectations, not substitutes for the actual generated reports.

Archived replay is not new LLM inference. Fresh CPU equality covers the tested shared-input suite, not universal semantic equivalence. Historical input provenance, semantic-label conflicts, GPU training/inference and the explicitly excluded judging ablation remain documented limitations.

The corrected optional catalog excludes unused Linalg `L2_R2`; frozen records retain their original provenance. Optional mutation preflight and actual request defaults now both use `gpt-5.5`; judge defaults remain `gpt-5.4-mini`. Network-intercepted SDK tests can verify configuration, not paid provider access or availability. Gemini execution assistance is not implemented by the deterministic CPU stage. No new model observations were generated.

## Contents and verification

The complete archive includes source, scientific bundles, the actual two-platform image, 914 verified Nova asset entries including 11 adapter models, and historical label/native CI evidence. Historical rc5 evidence is explicitly historical and does not validate rc6. Current candidate evidence is kept under `evidence/rc6/`.

`MANIFEST.sha256` covers every regular file except itself, including the image. `release/scientific-reference.sha256` pins protected scientific source/data; `release/scientific-files.sha256` covers distributed source implementation. `docker/image-inventory.json` records actual image identities. No `.git`, caches, AppleDouble metadata, virtual environments or credential files belong in the package.

- [ARTIFACT.md](ARTIFACT.md): stages, compiler checks and optional live experiments.
- [REPRODUCIBILITY.md](REPRODUCIBILITY.md): result-to-command mapping and scope.
- [PROVENANCE.md](PROVENANCE.md): repair decisions and preservation.
- [FINAL_VALIDATION_REPORT.md](FINAL_VALIDATION_REPORT.md): actual candidate validation status.
- [STRUCTURE.md](STRUCTURE.md): package layout.
- [GITHUB_DOWNLOAD.md](GITHUB_DOWNLOAD.md), [ZENODO.md](ZENODO.md): transport/publication instructions.
- [docs/live-configuration.md](docs/live-configuration.md): optional live configuration.

Software: Apache-2.0. Dataset: CC BY 4.0. Third-party assets retain their terms; Qwen base weights and credentials are not included. See `LICENSE`, `DATA_LICENSE.md`, and `CITATION.cff`.
