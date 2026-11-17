# Manual Zenodo deposit

The MLIRBench CGO 2027 Artifact Evaluation software distribution is intended for a separate Zenodo software record. This process does not create or replace the existing dataset deposit. Do not invent or reuse the dataset DOI as the software DOI.

**Publication gate:** upload only after the corrected scientific-file checksums, runtime configuration, Docker image and complete archive have been rebuilt or reconciled, and the final validation report identifies the exact tested release.

## Files to upload

For the existing rc5 naming convention:

- `MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz`: complete source, published scientific bundles, optional adapters, evidence and one actual multi-platform Docker image export.
- `MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz.sha256`: SHA-256 checksum of the complete archive.

If the corrected artifact is assigned a new version, use that version consistently in the archive, image, Git tag, metadata and checksum filename. Do not overwrite a previously published immutable release with different bytes.

The archive's `MANIFEST.sha256` covers its distributed files except the manifest itself. The outer archive checksum is separate. See [STRUCTURE.md](STRUCTURE.md) and [release/EXTERNAL_ASSETS.md](release/EXTERNAL_ASSETS.md).

Zenodo file-size and quota limits can change. Check the [official deposit file limits](https://help.zenodo.org/docs/deposit/manage-files/) and the measured archive size before uploading. GitHub transport parts, if used, must reconstruct the identical canonical archive; upload the single complete `.tar.gz` to Zenodo.

## Suggested metadata

- **Title:** MLIRBench: CGO 2027 Artifact Evaluation Release
- **Resource type:** Software
- **Version:** The exact validated Git/release version
- **Authors:** Pranava Sai Maganti; Meghasyam Peddireddy; Muzakker Hossain; Kaining Gao; Farhan Ahmed; Ali Jannesari
- **Conference:** 2027 IEEE/ACM International Symposium on Code Generation and Optimization (CGO 2027)
- **Associated paper:** *MLIRBench: A Benchmark and Dataset for Compiler and Hardware-Aware Reasoning*, https://arxiv.org/abs/2611.14881
- **Software repository:** https://github.com/msspranavasai/MLIRBench-CGO2027-AE
- **Software license:** Apache-2.0
- **Dataset license:** CC BY 4.0
- **Keywords:** MLIR; Compiler Optimization; Large Language Models; Semantic Reasoning; Artifact Evaluation; Compiler Benchmarks; Program Analysis; Reproducibility

The record-level software license does not relicense bundled data, model assets or third-party dependencies. Consult `DATA_LICENSE.md` and third-party license information.

### Suggested description

> MLIRBench is a benchmark and dataset for compiler and hardware-aware reasoning using MLIR Linalg and Torch program pairs. This CGO 2027 Artifact Evaluation software distribution includes 1,768 published program pairs, 15,912 reasoning records from nine evaluated language models, archived execution and judge observations, scientific configurations, reproducibility tools and a unified Docker environment. The published benchmark uses 24 Linalg and 22 Torch mutation rules; the optional mutation catalog excludes an unused Linalg rule absent from the frozen dataset. The intended live-agent configuration is GPT-5.5 for Mutation, Gemini 2.5 Flash for Execution, nine reasoning models and GPT-5.4-mini for Judge, subject to runtime verification. The required offline reviewer route replays archived observations, independently recomputes scores and metrics, and demonstrates fresh CPU compiler execution without paid API access. Optional live inference and GPU experiments are outside the required route. Known scientific limitations are documented, and no Artifact Evaluation badge is claimed.

A machine-readable metadata aid is available in `release/zenodo-metadata.json`. Verify its version, links and description against the actual final archive before uploading.

## Upload and independent verification

1. Confirm that `FINAL_VALIDATION_REPORT.md` records passing validation for the exact final source, Docker image and archive.
2. Verify the outer archive checksum. On macOS:

   ```bash
   shasum -a 256 -c MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz.sha256
   ```

   On Linux, use `sha256sum -c` with the corresponding checksum file. Substitute the actual final version if different.
3. Create a new **Software** upload in Zenodo, separate from the existing dataset.
4. Upload the intact archive and its checksum. Check filenames and byte sizes.
5. Enter the validated version, publication-order authors, licenses, associated paper and related repository. Add the dataset DOI only after confirming it.
6. Review the record before publishing. Zenodo assigns the software DOI; do not assume one in advance.
7. Download the deposited archive independently, verify its outer SHA-256, extract it and run:

   ```bash
   python3 release_tools/verify_distribution.py
   ```

8. Load the exported image and run the documented local-mode quickstart from the extracted archive. Preserve the resulting verification evidence.
9. Keep the versioned Git tag, archive and checksum immutable. Later corrections require a separately versioned release.
