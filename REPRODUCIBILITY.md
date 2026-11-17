# Reproduction map

Use `./ae.sh quickstart` for the complete required no-cost route, or load the archive's image and use the local-mode command in README.md. Each invocation starts one container. Default experiment networking is disabled. Original scientific implementations and scoring policies are unchanged.

| What is checked | Command | Main evidence |
|---|---|---|
| Published data, tests, four-stage replay, metrics, downstream replay, compiler arithmetic, fresh CPU examples | `./ae.sh quickstart` | `START_HERE.md`, `tests.json`, `preservation.json`, `readiness.json` |
| Individual archived agents | `./ae.sh pipeline --stage mutation` (then execution/reasoning/judge/metrics using `--input`) | stage `REPORT.md`, hashes and parent records |
| Fresh Linalg execution | `./ae.sh pipeline --stage execution --mode fresh --id seed1_linalg_prog1_L1_R1` | exact inputs, repeats and current outcomes |
| Fresh Torch execution | `./ae.sh pipeline --stage execution --mode fresh --id torch_seed1_prog10_T1_R1` | exact inputs, repeats and current outcomes |
| Saved downstream predictions | `./ae.sh reproduce-downstream --output /results/downstream` | recalculated classification metrics |
| Compiler archived arithmetic | `./ae.sh compiler --output /results/compiler` | archived comparison checks |
| Fresh full compiler corpora | `./ae.sh compiler --mode fresh --dialect linalg --output /results/compiler-linalg` (or torch) | IR, commands, observed/archive comparisons |
| Fresh static RISC-V code generation | `./ae.sh compiler --mode fresh --dialect linalg --riscv --workers 4 --output /results/riscv` | assembly and instruction analysis |
| Label-disposition dossier | `./ae.sh review-labels --output /results/label-review` | 30 documented dispositions |
| Additional current-suite audit | `./ae.sh audit-provenance --all --workers 4 --output /results/audit` | current observations, not relabeled data |

See [ARTIFACT.md](ARTIFACT.md) for the full stage-by-stage commands, new-input experiments, explicit data-download consent and opt-in live models. The fresh compiler commands accept `--limit 8` for demonstrations; subsets do not certify full-corpus reproduction.

## Interpretation

Mutation pairs, historical execution observations, reasoning responses and subjective judge ratings are replayed. Objective label correctness relative to the archived labels, score totals and aggregate metrics are recomputed. Fresh CPU checks use operation-aware shared inputs and repeated processes; finite equality is scoped to the tested suite. No archived response is silently reused with changed upstream inputs.

The unchanged paper comparison contains 61 checks (45 Table 4 cells plus 16 other checks). The original author-defined Table 4 tolerance is 0.15/100 with ordering checks; it is neither an execution-output tolerance nor a badge decision. Current recorded agreement is described in validation evidence. A numerical PASS does not resolve historical labels.

GPU inference/training requires external Qwen base weights, GPU resources and original experiment dependencies; it is not validated by saved-prediction replay. Optional live calls require explicit `--allow-paid-api` and user-arranged credentials, and can incur costs. They are not prerequisites for the evaluator workflow under [Woodruff's guidance](docs/woodruff-guidance.md). No paid provider request is claimed as tested.

The [30-case review](docs/label-dispositions.md), [scope](docs/release-scope.md) and [validation report](FINAL_VALIDATION_REPORT.md) retain known scientific limitations.
