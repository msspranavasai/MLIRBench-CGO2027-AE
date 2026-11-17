# Reproduction map

Use `./ae.sh quickstart` for the required no-cost reviewer workflow. Alternatively, verify and load the complete archive's Docker image and use the local-mode command in [README.md](README.md). Each invocation starts one container; experiment networking is disabled by default.

Published benchmark data, archived reasoning records, labels, scoring formulas and numerical policies are preserved. The optional mutation catalog excludes unused Linalg `L2_R2`. Optional live changes are separate from archived reproduction; no paid provider availability is established.

| What is checked | Command | Main evidence |
|---|---|---|
| Published data, tests, four-stage replay, metrics, downstream replay, compiler arithmetic and fresh CPU examples | `./ae.sh quickstart` | `START_HERE.md`, `tests.json`, `preservation.json`, `readiness.json` |
| Individual archived agents | `./ae.sh pipeline --stage mutation` (then execution/reasoning/judge/metrics with `--input`) | Stage `REPORT.md`, hashes and parent records |
| Fresh Linalg execution | `./ae.sh pipeline --stage execution --mode fresh --id seed1_linalg_prog1_L1_R1` | Inputs, repeats and observed outcomes |
| Fresh Torch execution | `./ae.sh pipeline --stage execution --mode fresh --id torch_seed1_prog10_T1_R1` | Inputs, repeats and observed outcomes |
| Saved downstream predictions | `./ae.sh reproduce-downstream --output /results/downstream` | Recomputed classification metrics |
| Archived compiler arithmetic | `./ae.sh compiler --output /results/compiler` | Archived comparison checks |
| Fresh Linalg compiler corpus | `./ae.sh compiler --mode fresh --dialect linalg --output /results/compiler-linalg` | IR, commands and comparisons |
| Fresh Torch compiler corpus | `./ae.sh compiler --mode fresh --dialect torch --output /results/compiler-torch` | IR, commands and comparisons |
| Fresh static RISC-V generation | `./ae.sh compiler --mode fresh --dialect linalg --riscv --workers 4 --output /results/riscv` | Assembly and instruction analysis |
| Label-disposition dossier | `./ae.sh review-labels --output /results/label-review` | 30 documented dispositions |
| Current-suite audit | `./ae.sh audit-provenance --all --workers 4 --output /results/audit` | Current observations, not relabeled data |

See [ARTIFACT.md](ARTIFACT.md) for stage-by-stage commands, new-input experiments, data-download consent, and optional live inference. Fresh compiler commands accept `--limit 8` for demonstrations; subsets do not establish full-corpus reproduction.

## Interpretation

Mutation replay restores published pairs and metadata. Execution replay restores historical observations. Reasoning replay restores saved model responses. Judge replay retains archived subjective observations while recomputing objective correctness and weighting.

Fresh CPU checks use shared inputs and repeated processes. Observed equality is scoped to the tested input suite, not universal equivalence. Archived responses must not be silently reused when upstream inputs change.

The paper comparison comprises 61 checks: 45 Table 4 cells and 16 other checks. The author-defined Table 4 tolerance is 0.15/100 with ordering checks. This is not an execution-output tolerance or an AE badge decision. Historical validation evidence must not be attributed to an untested corrected release.

## Optional live-agent configuration

The intended assignments are:

| Stage | Model |
|---|---|
| Mutation | GPT-5.5 |
| Execution | `gemini-2.5-flash` |
| Reasoning | Nine published benchmark models |
| Judge | `gpt-5.4-mini` |

These are configuration targets, not proof of live provider access or implementation. The default CPU execution workflow does not require Gemini credentials. Optional live calls require explicit `--allow-paid-api` and independently arranged credentials; they may incur costs. See [docs/live-configuration.md](docs/live-configuration.md).

GPU inference/training requires external Qwen base weights, GPU resources and suitable dependencies. Saved-prediction replay is not fresh GPU inference. The author-excluded judge-reliability ablation is not reproduced.

The [30-case review](docs/label-dispositions.md), [release scope](docs/release-scope.md) and [validation report](FINAL_VALIDATION_REPORT.md) document remaining limitations.
