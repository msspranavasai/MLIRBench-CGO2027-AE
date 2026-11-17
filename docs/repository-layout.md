# Repository layout

The MLIRBench CGO 2027 AE repository organizes published scientific inputs, offline reproducibility tools, optional live agents and release verification resources. See [STRUCTURE.md](../STRUCTURE.md) for the complete source and archive layout.

| Location | Purpose |
|---|---|
| `src/mlirbench/pipeline.py` | Archived replay and fresh-stage orchestration |
| `src/mlirbench/stage_artifacts.py` | Checkpoint hashes, parent validation and resume |
| `src/mlirbench/dataset.py` | Local-first data resolution and consented downloads |
| `src/mlirbench/live.py` | Lazy adapters to optional live-model agents |
| `src/mlirbench/execution/` | Compiler/runtime validation, input domains and diagnostics |
| `src/mlirbench/evaluation/` | Score aggregation and downstream metrics |
| `optional/live_pipeline/agents/` | Mutation, execution, reasoning and judge implementations |
| `data/` | Published scientific inputs, archived observations and provenance |
| `experiments/` | Manuscript expectations, numerical policy and claim map |
| `tests/` | Boundary, consent, scoring and execution tests |
| `requirements/` | Runtime, compiler and optional agent dependencies |
| `docs/` | Evaluator instructions and scientific limitations |
| `paper/reference/` | Accepted manuscript and reference materials |
| `release/` | Source mapping, historical and final checksums, external assets |
| `release_tools/` | Packaging and distribution integrity utilities |

The Docker image contains offline evaluation and optional live-agent code. Archived replay does not initialize model clients. Expected paper values are loaded only after metric computation.

The intended live-agent models are GPT-5.5 for Mutation, `gemini-2.5-flash` for Execution, nine reasoning models and `gpt-5.4-mini` for Judge. Exact provider identifiers and runtime behavior must be checked against the final implementation. CPU compiler execution alone does not prove a Gemini API call.

The published benchmark has 24 Linalg and 22 Torch mutation rules. The optional Linalg catalog excludes unused `L2_R2`; historical references in scientific evidence remain preserved.

New reviewer results go to `../MLIRBench-AE-runs/` by default. Published input records remain under `data/`; they are not disposable logs.

`experiments/release_invariants.json` records baseline identities for frozen inputs and archived results. `src/mlirbench/preservation.py` checks these invariants during quickstart. A preservation PASS means the specified comparisons passed; it does not prove the correctness of all historical labels.

The repository's CI and publication workflows must be interpreted per version. A previously tested image does not validate a modified runtime source. Any corrected image must have matching source fingerprint, versioned image identity, native-platform tests and release evidence.
