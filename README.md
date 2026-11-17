# MLIRBench: CGO 2027 Artifact Evaluation

### CGO 2027 Artifact Evaluation Release

This repository contains the MLIRBench artifact prepared for evaluation alongside the paper *MLIRBench: A Benchmark and Dataset for Compiler and Hardware-Aware Reasoning*, accepted at CGO 2027.

The artifact provides the published datasets, scientific implementation, experimental configurations, validation utilities, and a unified Docker-based reproducibility environment.

It is organized for artifact evaluation, public research use, and long-term archival.

## Overview

MLIRBench evaluates compiler and hardware-aware reasoning using MLIR Linalg and Torch program pairs.

The published benchmark contains:

- **1,768 program pairs:** 888 Linalg and 880 Torch.
- **15,912 reasoning records:** Nine evaluated language models.
- **46 mutation rules:** 24 Linalg and 22 Torch.
- Archived execution and judging observations.
- Downstream classification data, evaluation scripts, and compiler experiments.

Read the [accepted paper](https://arxiv.org/abs/2611.14881) for the benchmark methodology and experimental results.

## Agent Architecture

MLIRBench uses four agents:

| Agent | Model | Purpose |
|---|---|---|
| Mutation Agent | GPT-5.5 | Generates rule-guided MLIR mutations |
| Execution Agent | Gemini 2.5 Flash (`gemini-2.5-flash`) | Assists execution-stage analysis and validation |
| LLM Reasoning Agent | Nine evaluated models | Produces compiler-aware reasoning responses |
| Judge Agent | GPT-5.4-mini | Evaluates model-generated reasoning |

The model assignments above describe the intended live-agent configuration. The archived benchmark responses and judge observations remain unchanged.

The nine reasoning models are Claude Haiku 4.5, Claude Sonnet 4.5, GLM 5.1, GPT-4.1 Mini, GPT-OSS 120B, Kimi K2.6, Llama 4, Qwen3 Coder Next, and Gemini 3.1 Pro.

The default evaluation workflow uses archived responses and does not require external model inference.

## Start Here

### Prerequisites

- Docker Engine 29 or newer with the containerd image store enabled, including a compatible Docker Desktop installation.
- Python 3.10 or newer on the host.
- Approximately 20 GB of available disk space for extraction, image loading, and generated results.

The image supports native Linux AMD64 and ARM64. macOS users can run it through Docker Desktop.

See [offline Docker compatibility](docs/container-publication.md#offline-image-store-compatibility).

### Quickstart

```bash
git clone --branch v0.3.0rc5 https://github.com/msspranavasai/MLIRBench-CGO2027-AE.git
cd MLIRBench-CGO2027-AE
./ae.sh quickstart
```

The launcher uses one versioned Docker image and starts one evaluation container containing the compiler toolchains and MLIRBench evaluation environment.

The default workflow requires no API keys, paid model calls, Nova access, GPU hardware, or external database.

Experiment networking is disabled by default.

Generated results are written outside the repository to:

`../MLIRBench-AE-runs/`

Open the generated `START_HERE.md` for the results and stage reports.

## Reproducibility Workflow

The no-cost workflow replays the four benchmark stages:

1. Mutation
2. Execution
3. LLM Reasoning
4. Judge

It also recomputes objective scores and paper tables, replays downstream saved-prediction metrics, and performs fresh CPU compiler demonstrations.

Archived model responses and historical execution observations are explicitly identified as archived data. Replay does not constitute fresh LLM inference.

Optional live model calls and GPU experiments are separate from the required evaluator workflow.

## Offline Archive

The [complete distribution](GITHUB_DOWNLOAD.md) contains the scientific artifact, supporting evidence, optional adapter assets, and an exported multi-platform Docker image.

After extracting the verified distribution:

```bash
python3 release_tools/verify_distribution.py
docker load -i docker/mlirbench-ae-v0.3.0rc5-image.tar
AE_IMAGE_SOURCE=local AE_IMAGE=ghcr.io/msspranavasai/mlirbench-ae:0.3.0rc5 ./ae.sh quickstart
```

Local mode uses the supplied image without pulling or rebuilding it.

The image inventory records the included architectures, image identities, and export checksum.

## Scientific Integrity

The published benchmark uses 24 Linalg and 22 Torch mutation rules.

The unused Linalg catalog entry `L2_R2` was removed because it does not occur in the frozen dataset's mutation provenance.

The published program pairs, reasoning records, labels, scoring formulas, and numerical policies are preserved.

This catalog correction and any live-agent configuration updates are documented separately from the published experimental results.

See [PROVENANCE.md](PROVENANCE.md) for integrity verification and release provenance.

## Documentation

- [ARTIFACT.md](ARTIFACT.md): Evaluator instructions, individual stages, fresh execution, and optional live experiments.
- [REPRODUCIBILITY.md](REPRODUCIBILITY.md): Result-to-command mapping and expected outputs.
- [STRUCTURE.md](STRUCTURE.md): Repository and archive organization.
- [PROVENANCE.md](PROVENANCE.md): Scientific integrity, model configuration, checksums, and release identity.
- [FINAL_VALIDATION_REPORT.md](FINAL_VALIDATION_REPORT.md): Executed validation checks and known limitations.
- [ZENODO.md](ZENODO.md): Archival upload and integrity verification.
- [RELEASE_NOTES.md](RELEASE_NOTES.md): Release changes and compatibility.
- [STATUS.md](STATUS.md): Scientific readiness and limitations.
- [docs/live-configuration.md](docs/live-configuration.md): Optional model credentials and exact runtime model identifiers.

## Known Limitations

Historical execution-input provenance and semantic-label conflicts remain documented in the [30-case disposition review](docs/label-dispositions.md).

Full GPU inference, the author-excluded judging ablation, and permanently frozen future package-manager rebuilds are not claimed as reproduced.

Successful software execution and metric reproduction do not establish universal semantic correctness or automatically award an Artifact Evaluation badge.

## Licensing and Citation

The software is distributed under Apache-2.0, and the MLIRBench dataset is distributed under CC BY 4.0.

See [LICENSE](LICENSE), [DATA_LICENSE.md](DATA_LICENSE.md), and [CITATION.cff](CITATION.cff).

Third-party components retain their respective licenses.

This repository is intended to remain the permanent, versioned CGO 2027 artifact reference. Changes affecting scientific files, model configurations, or release integrity require a documented release update.
