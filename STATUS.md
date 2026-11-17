# Artifact status and limitations

## Current release status

**Corrected artifact documentation and source: pending final runtime and distribution revalidation.**

The required reviewer workflow is designed to support four-stage archived replay, independently recomputed metrics, downstream saved-prediction replay, archived compiler arithmetic and fresh CPU execution. It does not require paid APIs, Nova access or an author-operated service.

Previously recorded PASS results apply to the exact source and Docker image that were tested. See [FINAL_VALIDATION_REPORT.md](FINAL_VALIDATION_REPORT.md) for historical evidence and the outstanding validation requirements for the corrected release.

## Scientific data integrity

The published benchmark contains 1,768 program pairs and 15,912 reasoning records from nine evaluated models. Its published labels, archived responses, scoring formulas and numerical policies are preserved.

The active optional Linalg mutation catalog excludes unused `L2_R2`, consistent with the published 24 Linalg and 22 Torch mutation rules. Historical documentation mentioning an excluded `L2_R2` dataset entry remains valid scientific evidence.

## Intended live-agent configuration

| Agent | Intended model |
|---|---|
| Mutation | GPT-5.5 |
| Execution | `gemini-2.5-flash` |
| Reasoning | Nine published models |
| Judge | `gpt-5.4-mini` |

The final runtime must be checked for these assignments. In particular, fresh CPU compiler execution is not evidence of Gemini inference. Provider IDs, authentication and paid live calls have not been established by archived replay.

## Outstanding validation

- Confirm the corrected scientific-file hashes and intentional modification records.
- Verify exact runtime model identifiers and optional live-agent behavior.
- Run tests, offline quickstart and preservation checks against the final source.
- Validate native AMD64/ARM64 images with matching source fingerprints.
- Recreate and independently verify the complete archive and image export.
- Update final validation evidence with actual results, not historical PASS values.

## Known scientific and build limitations

- Historical execution runtime arguments remain incompletely recovered. The [30-case disposition dossier](docs/label-dispositions.md) documents conflicts and nondeterminism without relabeling the published data.
- Portable fresh GPU checkpoint inference/training is unverified. Optional adapters do not include external Qwen base weights.
- The judge-reliability ablation is excluded from required reproduction and remains unreproduced, despite its appearance in the manuscript.
- A frozen Docker export does not guarantee identical future apt repository resolution.
- Full compiler and static RISC-V experiments have separate evidence and commands. Quickstart arithmetic and examples do not establish complete regeneration or hardware speedups.
- Optional paid-provider integrations have been tested with intercepted responses, not independently verified paid requests.

Successful software tests or metric agreement do not establish universal semantic correctness or award an Artifact Evaluation badge.

The final versioned AE snapshot should remain immutable once validated and published. Any later scientific or image changes require a new version and corresponding integrity evidence.
