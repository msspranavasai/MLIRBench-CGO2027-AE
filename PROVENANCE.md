# Source and Distribution Provenance

## Release Identity

**Artifact:** MLIRBench CGO 2027 Artifact Evaluation  
**Repository:** https://github.com/msspranavasai/MLIRBench-CGO2027-AE  
**Version:** v0.3.0rc5  
**Conference:** CGO 2027

This repository contains the versioned MLIRBench artifact prepared for evaluation alongside the accepted paper *MLIRBench: A Benchmark and Dataset for Compiler and Hardware-Aware Reasoning*.

The release consolidates the scientific implementation, published datasets, experimental configurations, validation utilities, reproducibility workflows, and Docker-based execution environment into a single artifact-evaluation distribution.

The repository is intended to provide a stable, independently accessible reference for artifact evaluation and subsequent research use.

## Scientific Integrity and Dataset Preservation

The artifact preserves the published scientific dataset and associated experimental evidence:

- **1,768 MLIR program pairs:** 888 Linalg and 880 Torch.
- **15,912 reasoning records:** Nine evaluated language models.
- **46 mutation rules:** 24 Linalg and 22 Torch.
- Archived execution results, judge observations, downstream evaluation data, and experimental configurations.

The Linalg mutation catalog excludes `L2_R2`, which is absent from the frozen dataset's mutation provenance. This aligns the catalog with the 24 Linalg mutation rules used in the published experiments.

The published program pairs, reasoning records, evaluation labels, scoring formulas, and numerical policies are not modified by this catalog correction.

## Agent Architecture and Model Configuration

MLIRBench uses four agents to generate, validate, evaluate, and judge compiler-aware reasoning tasks.

| Agent | Model configuration | Responsibility |
|---|---|---|
| Mutation Agent | GPT-5.5 | Generates MLIR program mutations using the defined mutation rules and inspection metadata. |
| Execution Agent | `gemini-2.5-flash` | Supports execution-stage analysis and validation. |
| LLM Reasoning Agent | Nine evaluated models | Produces compiler-aware reasoning responses for the published benchmark. |
| Judge Agent | GPT-based judge | Evaluates model-generated reasoning against the benchmark's evaluation criteria. |

The nine-model reasoning dataset is preserved as published. Agent model configurations and model-generated reasoning records are separate components of the artifact.

The offline reproducibility workflow uses archived model responses and execution observations. It does not require fresh inference, external API credentials, or paid model access.

Optional live agent execution may require external model access and may produce results that differ from archived observations.

## Integrity Verification

The artifact includes checksums and integrity metadata to support independent verification.

- `release/scientific-files.sha256` records the checksums of the scientific files included in the finalized distribution.
- `release/original-files.sha256` retains the historical source-file checksum inventory.
- `release/source-file-map.tsv` records file mappings and identifies intentional modifications.
- `MANIFEST.sha256` verifies the contents of the complete standalone distribution.
- `release_tools/verify_distribution.py` checks file integrity against the applicable manifests.

The master raw dataset SHA-256 is:

`84718efccae10e5bbd66fd7c4455ca9f22a8957c968151465b830855335a0541`

The release records any intentional catalog or configuration corrections separately from the frozen experimental dataset. Checksums must be regenerated and verified after changes to the distributed files.

## Unified Docker Environment

The artifact provides a unified Docker-based environment containing the MLIRBench agents, runtime dependencies, compiler toolchains, and evaluation utilities.

The distribution is designed around:

- One versioned Docker image.
- One container per evaluation run.
- Native Linux AMD64 and ARM64 image variants.
- Offline replay without external model API credentials.
- A complete downloadable archive containing the exported Docker image.

The container environment supports the artifact's reproducibility workflows while keeping optional live inference and GPU experiments separate from the default offline evaluation.

Docker image identities, platform information, and export checksums are recorded in `docker/image-inventory.json`.

The offline multi-platform image export requires Docker Engine 29 or newer with the containerd image store enabled, including a compatible Docker Desktop installation.

## Evidence and Resource Scope

The artifact includes the published benchmark data, experimental configurations, evaluation scripts, validation tests, and archived execution evidence.

The complete standalone distribution additionally includes optional Nova execution assets, downstream model adapters, label-review evidence, and supporting validation records.

These resources provide scientific provenance and evaluation support. They do not represent newly generated benchmark results.

External model weights and credentials are not bundled unless explicitly identified in the distribution inventory.

The default offline workflow does not require institutional infrastructure, Nova cluster access, or GPU hardware.

## Reproducibility Scope

The artifact supports independent inspection, integrity verification, offline experiment replay, metric recomputation, and CPU-based compiler validation.

Archived inference and judging results are distinguished from fresh model execution.

The distribution does not claim complete reproduction of every historical GPU experiment, unavailable model response, or previously documented semantic-label discrepancy.

Known limitations and validation outcomes are documented in `FINAL_VALIDATION_REPORT.md`, `REPRODUCIBILITY.md`, and `STATUS.md`.

## Archival Commitment

This repository is intended to serve as the permanent, versioned reference for the CGO 2027 MLIRBench artifact.

The finalized distribution will be archived with its scientific data, source files, integrity manifests, reproducibility documentation, and exported Docker image.

Any subsequent corrections affecting scientific files, model configurations, or distribution checksums must be documented and released under an appropriately updated version.
