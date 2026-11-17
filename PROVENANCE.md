# Source and distribution provenance

Original repository: https://github.com/msspranavasai/MLIRBench_temp

Original release: **MLIRBench-AE 0.3.0rc5**; tag `v0.3.0rc5`; commit `1cddc68073dea07b283d29c4f5171f608cabf29c`. The source tag was resolved and verified before copying. The original repository is unchanged.

Destination: https://github.com/msspranavasai/MLIRBench-CGO2027-AE ; destination tag `v0.3.0rc5` identifies the cleaned packaging commit, not the original commit. The exact destination commit is recorded by the tag and `release/destination-commit.txt` in the standalone archive. A Git-tracked document cannot embed its own final commit hash without changing that hash. The archive adds no scientific modifications.

## Integrity and organization

`release/original-files.sha256` inventories every original tracked file before cleanup. `release/scientific-files.sha256` freezes all original non-Markdown/non-CI files, including code, data, experiment configuration, prompts, tests, launcher, Dockerfile, dependency pins and citation metadata. `release/source-file-map.tsv` maps every original path to the identical final path and original hash. No scientific source files are moved, deleted or edited. Only documentation, CI and external packaging tools are added/updated. No experimental development Git history is imported.

`release_tools/verify_distribution.py` checks preserved scientific hashes and, in the complete archive, every file in `MANIFEST.sha256`. The manifest excludes itself and `.git`; the outer archive checksum is separate. Data bundle manifests retain original compressed/raw SHA-256 identities. The master raw SHA-256 is `84718efccae10e5bbd66fd7c4455ca9f22a8957c968151465b830855335a0541`. The original runtime source fingerprint is `8fee6cdc664378040d97e74f3cad35a59dd0d6b32c63e55b8971bf339b1bf2d1`. Packaging tools live outside fingerprinted runtime directories.

## Unified image

One image tag: `ghcr.io/msspranavasai/mlirbench-ae:0.3.0rc5`.

Immutable index: `sha256:9238290317c4e6a0b70cd20781fc30169efa87c6fcbc663debdcccd3275eeec8`. The image's original OCI source/revision labels correctly refer to the original repository and source commit. This release does not replace the registry image. The archive's `docker/image-inventory.json` records export SHA-256, image/platform identities, toolchain versions and export command.

The original [native build/publication](https://github.com/msspranavasai/MLIRBench_temp/actions/runs/44052904293) and [anonymous pull verification](https://github.com/msspranavasai/MLIRBench_temp/actions/runs/44053955096) establish both native variants. This repository's CI verifies downloads and execution without registry publication.

## Evidence and resource scope

`data/`, `experiments/`, `paper/reference/`, original scientific snapshots and published records are preserved. The standalone archive additionally includes the 914-file Nova asset copy (including 11 final adapters), raw label-review evidence and native CI verification records. These resources are distribution inputs, not new results. Large optional assets are not Git blobs and are not required for the CPU replay route. Qwen base weights and validated portable GPU inference are not bundled. See [external resource inventory](release/EXTERNAL_ASSETS.md).
