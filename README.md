# MLIRBench — CGO 2027 Artifact Evaluation

### CGO 2027 Artifact Evaluation Release

This repository contains the final MLIRBench artifact prepared for evaluation alongside the paper *MLIRBench: A Benchmark and Dataset for Compiler and Hardware-Aware Reasoning*, accepted at CGO 2027.

The release preserves the scientific implementation, datasets, experimental configurations, and unified Docker-based reproducibility infrastructure associated with the submitted artifact.

The repository has been organized for artifact evaluation, public research use, and long-term archival.

This version is intended to remain a stable, versioned reference to the submitted artifact.

## Start here

MLIRBench evaluates compiler and hardware-aware reasoning on MLIR Linalg and Torch program pairs. This artifact bundles 1,768 published pairs, 15,912 reasoning records for nine models, archived execution/judge observations, tests, metric computation and both compiler toolchains. See the [accepted paper](https://arxiv.org/abs/2611.14881).

Prerequisites: Docker Engine/Desktop and Python 3.10+ on the host. Native Linux AMD64 and ARM64 image variants are verified; macOS uses Docker Desktop. Allow at least 20 GB free space for extraction, image loading and generated results, more for full experiments.

```bash
git clone --branch v0.3.0rc5 https://github.com/msspranavasai/MLIRBench-CGO2027-AE.git
cd MLIRBench-CGO2027-AE
./ae.sh quickstart
```

The launcher pulls **one image**, `ghcr.io/msspranavasai/mlirbench-ae:0.3.0rc5`, for the Docker host's CPU and starts **one container** containing all four agents and compiler tools. It requires no model credentials, paid API calls, Nova access, database or supporting service. Experiment networking is disabled by default. Results go outside the checkout to `../MLIRBench-AE-runs/`; open the printed `START_HERE.md`.

The no-cost route replays mutation → execution → reasoning → judge, recomputes objective scores and paper tables, replays saved downstream prediction metrics, and runs fresh CPU compiler examples. Archived responses are explicitly identified; replay is not fresh LLM inference. Optional live model calls and GPU experiments remain separate and may produce different results.

## Offline archive

The complete Zenodo distribution additionally contains the actual exported image and optional adapter assets. After extraction:

```bash
python3 release_tools/verify_distribution.py
docker load -i docker/mlirbench-ae-v0.3.0rc5-image.tar
AE_IMAGE_SOURCE=local AE_IMAGE=ghcr.io/msspranavasai/mlirbench-ae:0.3.0rc5 ./ae.sh quickstart
```

The final image inventory records the architectures included in the single export. Local mode never pulls or rebuilds. No host checkout or institutional files are required.

## Documentation and scope

- [ARTIFACT.md](ARTIFACT.md): detailed evaluator commands, individual stages, fresh execution and optional live calls.
- [REPRODUCIBILITY.md](REPRODUCIBILITY.md): result-to-command map and expected outputs.
- [STRUCTURE.md](STRUCTURE.md): source and archive layout.
- [PROVENANCE.md](PROVENANCE.md): frozen source, hashes, unchanged-file mapping and image identity.
- [FINAL_VALIDATION_REPORT.md](FINAL_VALIDATION_REPORT.md): actual validation results and limitations.
- [ZENODO.md](ZENODO.md): manual upload, metadata and integrity verification.
- [RELEASE_NOTES.md](RELEASE_NOTES.md): packaging changes and compatibility.

Historical execution-input provenance and label conflicts remain disclosed in the [30-case disposition review](docs/label-dispositions.md). Full GPU inference, the author-excluded judging ablation and permanently frozen apt rebuilds are not claimed as reproduced. Software/metric success does not establish every historical semantic label or award an AE badge. See [STATUS.md](STATUS.md).

Scientific code, labels, source records, scoring and numerical policies are byte-for-byte preserved from the original rc5 release. The Apache-2.0 software and CC BY 4.0 dataset licenses are distinct; see [LICENSE](LICENSE), [DATA_LICENSE.md](DATA_LICENSE.md) and [CITATION.cff](CITATION.cff). Third-party components retain their own licenses.

This Docker-inclusive AE repository remains the permanent review reference. Any future source-only distribution will be maintained separately without replacing this versioned artifact.
