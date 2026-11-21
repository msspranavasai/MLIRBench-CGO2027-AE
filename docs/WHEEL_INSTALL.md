# Running the standalone MLIRBench Python wheel

The wheel installs Python code and a console entrypoint. It does **not** include the archived CGO 2027 scientific datasets, experimental manifests, or pinned compiler/GPU environment. Use the separately distributed complete reviewer artifact for offline reproducibility.

For a standalone wheel, set `MLIRBENCH_ARTIFACT_ROOT` to the **absolute path** of an extracted, compatible artifact root that contains `data/bundle/manifest.json` and `experiments/claims.json`:

```bash
export MLIRBENCH_ARTIFACT_ROOT="/real/absolute/path/to/MLIRBench-artifact"
mlirbench --help
mlirbench prepare-data
mlirbench dataset-info
```

Replace the example path with the actual extracted directory. The entrypoint refuses missing resources and mismatched release metadata (when `release/release.json` is present) rather than silently treating `site-packages` as the dataset root. It never downloads data on the user's behalf without the existing explicit consent flow.

The container-first `./ae.sh quickstart` route remains the recommended reviewer workflow. The wheel's installer dependency requirements and external compiler tools are separately documented; a wheel-only install is not a complete evaluation environment.

The original `src/mlirbench/cli.py` and all scientific-reference inputs are unchanged by this adapter. `python -m mlirbench` continues to use the original source/container command path; the environment variable is implemented for the installed **`mlirbench` console script**.
