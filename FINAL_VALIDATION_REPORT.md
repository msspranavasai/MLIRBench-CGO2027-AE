# Final artifact validation

**Core software and offline distribution rehearsal: PASS. Scientific limitations remain disclosed.** This report records performed tests, not a guarantee that every paper experiment or historical label is validated. The final archive is checked again after freezing; the release sidecar `FINAL_ARCHIVE_VALIDATION.json` identifies the exact final archive bytes and destination commit without a circular self-checksum.

## Frozen source and data

| Check / command | Outcome |
|---|---|
| Resolve original `v0.3.0rc5^{commit}` | PASS, exit 0: `1cddc68073dea07b283d29c4f5171f608cabf29c` |
| `python3 release_tools/verify_distribution.py --source-only` | PASS, exit 0: 178 original non-documentation/non-CI files unchanged, no original files removed |
| `python3 tools/release/source_identity.py` | PASS, exit 0: `8fee6cdc664378040d97e74f3cad35a59dd0d6b32c63e55b8971bf339b1bf2d1` |
| Original-to-final mapping | Every original path retained; original/final SHA-256 and packaging-edit classification in `release/source-file-map.tsv` |
| Published bundled records | PASS: 1,768 master pairs (888 Linalg, 880 Torch), 15,912 reasoning records, nine model keys, 15,907 judge observations |
| Quickstart integrity checks | PASS: 21 published manifest entries, 288 downstream files, original 1,804-row execution export and all 1,768 published rows |
| Optional asset integrity | PASS: all 914 source-manifest entries verified, including 11 final adapters |

The five missing Gemini judge observations remain missing; none is synthesized. Scientific implementations, published records/labels, prompts, experiment configurations, score formulas, compiler flags and numerical tolerances are unchanged.

## Unified image and clean-extraction rehearsal

One image: `ghcr.io/msspranavasai/mlirbench-ae:0.3.0rc5`. Immutable index: `sha256:9238290317c4e6a0b70cd20781fc30169efa87c6fcbc663debdcccd3275eeec8`. Export: `docker/mlirbench-ae-v0.3.0rc5-image.tar`, 1,314,104,320 bytes, SHA-256 `ece02c64a3fc675b45912ad09c3b68f7c0b564e37693e9b1632efe139cb31697`. The single Docker/OCI-compatible export contains both AMD64 and ARM64 and requires Docker 29+ with the containerd image store (see docs/container-publication.md); all 66 content-addressed blobs were hashed and checked. Exact platform manifests, config IDs, source labels, packages, apt inventory and tool versions are in `docker/image-inventory.json`.

The archive rehearsal was built from preparation commit `2e574d10622afa4b07c745247d2db1e4c2808a96`; its outer SHA-256 was `235dd962408f2f56212b66fe787df9570916d1f9bf6deac3ef1e3dbea58ac1be`. Final packaging documents differ from that rehearsal; scientific/image/data bytes do not. The exact final distribution is independently attested by the release sidecar after its own extraction/load/run test.

Performed locally on Docker Desktop 29.9.3, Linux ARM64 container on native ARM64:

```bash
python3 release_tools/verify_distribution.py
docker load --input docker/mlirbench-ae-v0.3.0rc5-image.tar
AE_IMAGE_SOURCE=local AE_IMAGE=ghcr.io/msspranavasai/mlirbench-ae:0.3.0rc5 ./ae.sh quickstart
```

All exited 0 from a newly extracted archive outside the source workspace. All distribution checksums passed. Exactly one evaluation container was observed; its network mode was `none`. No rebuild, registry pull, paid API, Nova login or external database was used. The local Docker daemon already contained layers; fresh-runner removal/reload checks below establish an independent round trip. The final sidecar records the final run commands, exact archive identity and observed container count.

| Evaluator result | Outcome |
|---|---|
| Existing unit and integration tests | PASS: 214 tests, zero failures/errors/skips |
| Frozen input and recomputed-output preservation | PASS: all 64 checks |
| Paper comparison | PASS under unchanged policy: 61/61 accepted, 40 exact and 21 within criteria |
| Downstream saved-prediction replay | PASS; independent recalculation and split checks, not fresh inference |
| Archived compiler arithmetic | PASS, 1,369 comparisons; not a fresh full-corpus run |
| Fresh CPU Linalg and Torch examples | PASS, real compiler/runtime with valid shared inputs and process repeats |
| Individual archived stages | Mutation, execution, reasoning, judge and metrics each EXIT_0, separately invoked |
| Label-disposition dossier verification | EXIT_0; historical label provenance remains REVIEW_REQUIRED |
| Local Markdown targets | PASS, no missing relative file targets in maintained documentation |
| Secret/cache inspection | No high-confidence token/private-key signatures in scanned readable source/asset files; downstream snapshot has no `.env`, `.git` or cache members. This is a scoped scan, not proof against all secrets |

## Native platform and dependency verification

[Destination CI run 44063676902](https://github.com/msspranavasai/MLIRBench-CGO2027-AE/actions/runs/44063676902) passed on native AMD64 and ARM64. Each fresh runner pulled anonymously, saved the actual image, removed its rc5 image reference, confirmed that reference absent, loaded the export, checked the image identity and completed offline quickstart. Each passed 214 tests and 64 preservation checks. The macOS system-Bash launcher tests also passed. The archive retains these reports under `evidence/review-ci/`. The subsequent [dual-platform native CI run 44065285212](https://github.com/msspranavasai/MLIRBench-CGO2027-AE/actions/runs/44065285212) also passed AMD64, ARM64 and macOS launcher checks. Each native runner enabled the containerd image store, pulled both variants, verified that one export contained both architectures, removed the image reference, reloaded that export and passed the offline workflow. Its reports and successful step identities are retained in `evidence/review-multiplatform-ci/`. The actual final export is separately content-verified and loaded during the local archive test.

The original [rc5 native source builds/publication](https://github.com/msspranavasai/MLIRBench_temp/actions/runs/44052904293) and [anonymous pulls](https://github.com/msspranavasai/MLIRBench_temp/actions/runs/44053955096) establish successful dependency installation and native execution for this unchanged scientific/runtime fingerprint. Fresh source builds were NOT RERUN during this documentation/packaging operation. Existing source-build evidence is credited as historical evidence rather than a newly executed build.

Full 857-program Linalg, 845-program Torch and 693-program RISC-V regeneration is NOT RERUN in this packaging pass. The original independent evidence and portable commands remain distinct from the 1,369 archived arithmetic checks and small fresh tests. Static instruction counts do not establish hardware speedups.

## Limits on the release conclusion

- Historical execution runtime inputs remain unproven. The 30-case dossier preserves counterexamples, unsafe metadata, structural conflicts and nondeterminism without relabeling the dataset. Unsupported-domain cases remain unresolved.
- Fresh portable GPU checkpoint inference/training is NOT VERIFIED. Copied adapters are bundled; external Qwen base weights, an immutable base revision and suitable GPU resources are not supplied as a validated inference path.
- The author-excluded judge-reliability ablation is NOT REPRODUCED despite the archived manuscript’s Appendix E.14/Table 24.
- Future apt repository resolution is NOT FULLY FROZEN. The exported binary is frozen and inventoried; a future rebuild is a different guarantee.
- No billed live-provider requests were run. Optional API integration tests use intercepted responses; provider access/model availability and fresh result equality are NOT VERIFIED.
- The existing dataset Zenodo DOI could not be confirmed from available source/public search; no DOI is invented and no Zenodo deposit is created.

Quickstart retains `NOT_SUBMISSION_READY` for complete scientific readiness. The release conclusion is a verified, usable core software distribution with explicit scientific limitations, not full validation of every accepted-paper claim, universal label correctness, an awarded AE badge or a guarantee of all four badges. The existing author-defined Table 4 tolerance remains 0.15/100 with ordering checks; no criteria were weakened for this release.

## Archival delivery

The final `.tar.gz` includes source, scientific bundles, all copied adapters, verification evidence and one actual multi-platform image export. Stable file ordering, ownership, timestamps and executable permissions are normalized by `release_tools/package_distribution.py`. The Docker export and scientific bytes are preserved exactly. `MANIFEST.sha256` excludes itself; the outer checksum and final archive validation are separate.

The archive fits Zenodo’s documented 50 GB quota. It exceeds GitHub’s 2 GiB per-asset limit, so GitHub carries three checksum-verified transport parts of the same canonical archive; ZENODO.md instructs uploading the single intact archive manually. No Zenodo record or DOI is created automatically.
