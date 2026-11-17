# Release history and provenance

This repository maintains a dedicated versioned history for the MLIRBench CGO 2027 Artifact Evaluation distribution.

The artifact contains the published benchmark records, scientific implementation, archived evaluation evidence, reproducibility infrastructure and Docker-based reviewer environment.

The published program pairs, reasoning records, labels and scoring policies are preserved. An unused Linalg mutation-catalog entry, `L2_R2`, was excluded to align the active catalog with the 24 Linalg and 22 Torch rules represented in the published dataset.

The intended optional live-agent assignments are GPT-5.5 for Mutation, `gemini-2.5-flash` for Execution, nine published reasoning models and `gpt-5.4-mini` for Judge. These assignments require matching runtime verification before final publication.

Historical and final file identities are recorded in `release/original-files.sha256`, `release/scientific-files.sha256` and `release/source-file-map.tsv`. These manifests distinguish preserved source content from intentional changes. Historical source identity must remain auditable even though this public-facing document does not reference another repository.

Local build caches, transient logs and old run directories are excluded from the source distribution. Scientific records and diagnostic evidence required for reproducibility remain part of the artifact or its complete archive.

Changes to scientific source, live-agent defaults or distributed image bytes require an updated release record and validation evidence. Existing immutable release tags and checksums must not be silently rewritten.

See [PROVENANCE.md](PROVENANCE.md), [RELEASE_NOTES.md](RELEASE_NOTES.md) and [FINAL_VALIDATION_REPORT.md](FINAL_VALIDATION_REPORT.md).
