# Manual Zenodo deposit

No Zenodo record is created by this repository. The author uploads the verified software archive manually. The separately published dataset must not be replaced or assigned an invented DOI. Its exact DOI could not be confirmed from the source or public search during preparation; add a related identifier only after verifying the actual dataset record.

## Files to upload

- `MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz`: complete source, scientific bundles, copied optional adapters, evidence and one actual multi-platform Docker export.
- `MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz.sha256`: outer SHA-256.

The archive extracts to one directory of the same name without `.tar.gz`. Its `MANIFEST.sha256` covers every distributed file except itself. The source repository excludes the image and large optional assets from Git blobs; the complete archive includes them. See `STRUCTURE.md`, `release/EXTERNAL_ASSETS.md` and `docker/image-inventory.json`.

Zenodo currently documents a 50,000,000,000-byte total and up to 100 files per record; see [official file limits](https://help.zenodo.org/docs/deposit/manage-files/). Check the final measured size and current quota before uploading. The compressed archive plus checksum must fit that total. Do not split deposits merely to evade quota.

GitHub’s per-file limit is smaller than the complete archive. Its release provides checksum-verified transport parts; [GITHUB_DOWNLOAD.md](GITHUB_DOWNLOAD.md) reassembles the exact canonical archive. Upload the single intact `.tar.gz` to Zenodo, not the transport parts.

## Metadata

- Title: **MLIRBench: CGO 2027 Artifact Evaluation Release (v0.3.0rc5)**
- Resource type: Software
- Version: 0.3.0rc5
- Authors in publication order: Pranava Sai Maganti; Meghasyam Peddireddy; Muzakker Hossain; Kaining Gao; Farhan Ahmed; Ali Jannesari.
- Conference: 2027 IEEE/ACM International Symposium on Code Generation and Optimization (CGO 2027).
- Associated paper: *MLIRBench: A Benchmark and Dataset for Compiler and Hardware-Aware Reasoning*, https://arxiv.org/abs/2611.14881 .
- Software license: Apache-2.0. The bundled MLIRBench dataset is CC BY 4.0, and third-party components retain separate original licenses; explain this in the description and refer to DATA_LICENSE.md. A record-level software license does not relicense the entire image or model assets.
- Keywords: MLIR; Compiler Optimization; Large Language Models; Semantic Reasoning; Artifact Evaluation; Compiler Benchmarks; Program Analysis; Reproducibility.
- Related software URL: https://github.com/msspranavasai/MLIRBench-CGO2027-AE/releases/tag/v0.3.0rc5 .

Suggested description:

> MLIRBench is a benchmark and dataset for compiler and hardware-aware reasoning on MLIR Linalg and Torch program pairs. This frozen CGO 2027 artifact preserves the rc5 scientific implementation, 1,768 published pairs and 15,912 reasoning records for nine models, archived execution and judging observations, scientific configurations, tests, and reproducibility scripts. A single unified Docker image includes all four agents and compiler toolchains. The default offline, no-cost workflow replays historical agent records, independently recalculates objective scores and aggregate metrics, reproduces saved downstream prediction metrics, and demonstrates fresh CPU compiler execution. The archive includes the actual Docker image export and copied optional adapter assets. Fresh live-model and GPU experiments are optional and require external resources. Known historical label/provenance issues and unverified experiments are explicitly documented; no AE badge or universal semantic-label validation is claimed. Software is Apache-2.0, MLIRBench data CC BY 4.0, and third-party components retain their licenses.

A machine-readable metadata aid is in `release/zenodo-metadata.json`. It is not an API publication request and contains no invented DOI.

## Upload and verify

1. Verify the outer checksum locally: on macOS `shasum -a 256 -c MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz.sha256`; on Linux use `sha256sum -c` instead. Read FINAL_VALIDATION_REPORT.md and retain its limitations.
2. Sign in to Zenodo and choose **New upload**. Use a new software deposit, not the existing dataset DOI. Do not enable GitHub automation for this manual deposit.
3. Upload the archive and checksum. Wait for both transfers to complete; check the displayed filenames and byte sizes against the local files.
4. Enter the metadata above. Add the arXiv URL as the associated paper, the versioned GitHub release as related software, and the confirmed existing dataset DOI only if available. Do not reuse the paper/dataset DOI as the software record DOI.
5. Review authors, version, licenses and description. Read the preview, then publish only after the archive integrity and applicable packaging validation pass. Zenodo assigns the software DOI; no DOI is assumed here.
6. Download the uploaded archive to an independent location and verify the outer SHA-256. Extract it and run `python3 release_tools/verify_distribution.py`, then the README's `docker load` and local-mode quickstart commands. Preserve the checksum and generated reports.
7. Cite the assigned version DOI in the submission and future metadata. Preserve the frozen Git tag and archive; later changes require a new version rather than silently replacing this artifact.
