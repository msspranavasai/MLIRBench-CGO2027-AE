# Artifact release scope

## Required reviewer route

The required reviewer workflow is:

```bash
./ae.sh quickstart
```

It replays archived mutation, execution, reasoning and judge observations; independently recalculates scores and paper tables; replays saved downstream prediction metrics; checks archived compiler arithmetic; and performs fresh repeated CPU execution demonstrations.

No model API credentials, paid provider credits, or GPU are required. Individual stages can also be replayed separately. Fresh model inference is optional and produces new observations that may differ from the published benchmark.

## Published dataset and intentional corrections

The published dataset contains 1,768 MLIR program pairs, 15,912 reasoning records and nine evaluated reasoning models. The published mutation-rule count is 24 Linalg plus 22 Torch.

Published pairs, reasoning records, labels, scoring formulas and numerical policies are preserved. The optional Linalg mutation catalog excludes the unused `L2_R2` entry. Historical label-provenance documentation mentioning an excluded `L2_R2` program remains part of the evidence.

The intended optional live-agent models are GPT-5.5 for Mutation, `gemini-2.5-flash` for Execution, nine published reasoning models, and `gpt-5.4-mini` for Judge. These are configuration targets until confirmed against the final runtime and request payloads. Archived results are not retroactively regenerated.

The dataset has a separately published archival identity. This software release does not replace or silently relabel the dataset deposit. Link the verified dataset DOI when available; do not invent one.

## Excluded or unresolved reproduction

The author excluded the reviewer-requested judge-reliability ablation from required reproduction on November 16, 2026. The archived manuscript still includes Appendix E.14/Table 24, but that does not establish independent reproduction. Report the ablation as `EXCLUDED_FROM_REQUIRED_SCOPE`, not PASS.

Other limitations include historical execution input/toolchain provenance and label conflicts, portable fresh GPU checkpoint inference, full compiler/backend regeneration on additional environments, and permanently frozen future apt dependency resolution.

A passing software workflow does not validate every historical semantic label or award an AE badge.

## Optional assets and dependencies

The complete distribution includes optional reviewer assets under `assets/nova/`, including the previously inventoried 914 files and 11 final adapter directories, subject to verification against the actual final archive. The adapters are not Qwen base-model weights. Portable GPU inference remains an optional, separately validated workflow.

Python runtime dependencies are pinned in `requirements/runtime-lock.txt`, and the base image is digest-pinned. An exported image freezes its installed environment; future apt resolution for a new build is a different guarantee.

## Final-release integrity

Scientific-file checksums, source mappings, the Docker image inventory and the archive manifest must describe the actual final files. Intentional catalog or live-configuration modifications must be classified accurately. Historical validation reports must not be presented as new PASS results.

Each final image version requires native AMD64/ARM64 verification, matching source fingerprint and image labels, an exported image round-trip, and a complete archive checksum check. See [FINAL_VALIDATION_REPORT.md](../FINAL_VALIDATION_REPORT.md), [PROVENANCE.md](../PROVENANCE.md), and [STATUS.md](../STATUS.md).
