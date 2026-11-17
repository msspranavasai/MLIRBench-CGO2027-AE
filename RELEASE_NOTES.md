# MLIRBench CGO 2027 Artifact Evaluation Release

## Overview

This release provides the MLIRBench benchmark and its reproducibility infrastructure for CGO 2027 Artifact Evaluation.

The distribution includes published scientific data, evaluation code, compiler toolchains, validation utilities, archived experimental evidence, and a unified Docker environment.

## Scientific Dataset

The published benchmark contains:

- 1,768 MLIR program pairs: 888 Linalg and 880 Torch.
- 15,912 reasoning records from nine evaluated language models.
- 46 mutation rules: 24 Linalg and 22 Torch.
- Archived execution observations and judge evaluations.
- Downstream prediction records and compiler experiment evidence.

The unused Linalg mutation rule `L2_R2` has been removed from the live mutation catalog to match the rule IDs present in the frozen dataset.

Published program pairs, reasoning records, evaluation labels, scoring formulas, and numerical policies are preserved.

## Agent Model Configuration

The intended live-agent configuration is:

| Agent | Model |
|---|---|
| Mutation | GPT-5.5 |
| Execution | `gemini-2.5-flash` |
| LLM Reasoning | Nine benchmark models |
| Judge | `gpt-5.4-mini` |

The nine reasoning models are Claude Haiku 4.5, Claude Sonnet 4.5, GLM 5.1, GPT-4.1 Mini, GPT-OSS 120B, Kimi K2.6, Llama 4, Qwen3 Coder Next, and Gemini 3.1 Pro.

Live model configurations are distinct from the archived responses used for paper reproduction.

These intended assignments require verification against the final runtime configuration before publication.

## Docker Distribution

The artifact provides one multi-platform Docker image supporting native AMD64 and ARM64 execution.

The environment includes the compiler dependencies, evaluation tools, and agent implementations.

The default reviewer workflow:

- Requires no paid API calls or model credentials.
- Uses archived responses for model-dependent stages.
- Runs CPU compiler validation examples.
- Recomputes objective scores and paper tables.
- Replays saved downstream prediction metrics.

The complete offline distribution includes an exported Docker image.

Docker Engine 29 or newer with the containerd image store enabled is required for the supplied multi-platform image export.

## Reproducibility and Integrity

The release provides scientific-file checksums, a complete distribution manifest, source-file mapping, Docker image metadata, and validation utilities.

Intentional catalog and live-model configuration changes are documented separately from the frozen experimental dataset.

All integrity checks, Docker tests, and validation reports must be regenerated after modifying distributed scientific files.

## Known Limitations

The artifact does not claim complete reproduction of historical GPU inference, the author-excluded judging ablation, or every historical execution input.

Known semantic-label discrepancies remain documented without modifying the published labels.

Fresh provider access and model availability are not established by offline replay or intercepted API tests.

No Artifact Evaluation badge is claimed by this release document.

See `PROVENANCE.md`, `FINAL_VALIDATION_REPORT.md`, and `STATUS.md` for additional details.
