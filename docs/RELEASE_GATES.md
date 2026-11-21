# MLIRBench v1.0.0 release acceptance gates

This is a pre-release engineering checklist, not proof that a gate has passed. A Git checkout does not include the full offline distribution. The original `v0.3.0rc6` container/archive is a separate immutable tested candidate; changing source or package metadata in this branch requires rebuilding before calling a new version verified.

| Gate | Required evidence | Release condition |
| --- | --- | --- |
| Source identity | Immutable commit SHA, source fingerprint, release/tag/metadata agreement | Every published entrypoint points to the *same* audited source and version |
| Dataset preservation | All manifest/checksum checks, exact published pairs/records, distinct data/software licenses | Original 1,768 program pairs and 15,912 reasoning records unchanged unless an explicitly new dataset is released |
| Python package | Reproducible installation on declared Python versions, dependencies match `requirements/core.txt` and `requirements/live.txt` | Clean-environment installation and import/CLI checks pass |
| Compiler environment | Exact pinned tools, fresh Linalg and Torch compiler/runtime checks | Demonstrated on native supported platforms, no emulation described as native |
| Tests | Full suite and failures/skip accounting | Zero unexpected failures/errors/skips; number is recorded from actual run |
| Scientific reproduction | Archived replay, 61 paper comparison checks, 76 downstream comparisons and preservation | All comparisons pass under disclosed author-defined criteria; historical provenance limitations remain stated |
| Extended experiments | Full compiler corpus/RISC-V records, GPU checkpoints/inference when claimed | Gaps clearly reported, no fake pass, no replay mislabeled as full fresh experiment |
| Image integrity | Native AMD64/ARM64 clean build, packaged-byte load, matching source fingerprint and manifest digests | Exact image distribution verified in the selected runtime; Docker and Apptainer test scopes distinguished |
| Distribution | Full tarball including external assets, SHA sidecar, every internal manifest, independent download/re-extraction | Remote bytes match archived hashes and unpacked verifier passes |
| Public access | Anonymous repository/Zenodo/download and container pull checks | No maintainer credentials, institutional network, remote lab path or paid model key required for documented offline route |
| Security and licensing | Secret/history scan, third-party asset license review, license/citation/DOI consistency | No known exposed credentials or incompatible distribution rights |
| Documentation | Fresh contributor installation, evaluator quickstart, citations, reproducibility claim map, known limitations and versions | Commands tested literally on clean target machines |
| Provenance and organization | CGO 2027 release linked to original repair history; lab ownership and governance | `swapp-lab/MLIRBench` one-commit snapshot created only after all prior gates pass |

## Source / binary separation

The `repair/v0.3.0rc6` branch and the original rc6 tarball are not overwritten by v1 work. `MANIFEST.sha256`, `release/scientific-files.sha256`, OCI manifests and the outer archive `.sha256` refer to specific bytes. Documentation, packaging, Python metadata, Docker labels or runtime source changes all demand a deliberate release audit and typically a newly packaged distribution. A successful earlier CI run does not establish new package bytes passed.

## AE scientific scope

Archived reasoning and judge records are preserved inputs. Recomputing scores from them is useful independent arithmetic reproduction, but is not fresh paid model inference. Fresh CPU demonstrations sample the stated input suite and do not prove universal program equivalence. Runtime histories, semantic-label conflicts, compiler full-corpus claims, GPU checkpoint evaluations, and numerical agreement criteria must each be reported at their real evidence level.

## Target release organization

Only once the **source repository** is audit-ready should the permanent `swapp-lab/MLIRBench` repository receive an independent one-root-commit snapshot and an immutable `v1.0.0` tag. The old development repository remains available for provenance. Future dialects belong in subsequent separately reviewed versions; no architecture change is required for the CGO 2027 scientific baseline.
