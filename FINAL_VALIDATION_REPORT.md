# Final distribution validation

**Packaging validation is in progress; this document is not yet a final release attestation.** Scientific limitations are retained independently of packaging outcomes.

## Verified so far

| Check | Status | Evidence |
|---|---|---|
| Source tag resolves to specified commit | PASS | `v0.3.0rc5` → `1cddc68073dea07b283d29c4f5171f608cabf29c` |
| Scientific and non-documentation source unchanged | PASS | 178 original files checked using `python3 release_tools/verify_distribution.py --source-only`, exit 0 |
| Runtime source fingerprint | PASS | `8fee6cdc664378040d97e74f3cad35a59dd0d6b32c63e55b8971bf339b1bf2d1` |
| Scientific record counts | PASS | 1,768 master (888 Linalg, 880 Torch), 15,912 reasoning, 15,907 judge observations; five missing judge observations remain disclosed |
| Unified Docker export integrity | PASS | One 1,314,104,320-byte export; all 66 content-addressed blobs verified; AMD64 and ARM64 included |
| Exported image load and offline native ARM64 quickstart | PASS | `docker load --input docker/mlirbench-ae-v0.3.0rc5-image.tar`; local-mode quickstart, exit 0 |
| Existing unit/integration tests | PASS | 214 run, zero failures/errors/skips |
| Preservation checks | PASS | All 64 frozen checks |
| Paper metric agreement | PASS under unchanged policy | 61/61 accepted; 40 exact and 21 within existing criteria |
| Copied optional resources | PASS | 914 manifest entries verified before copying, including 11 final adapters |
| Four agents and compiler installations | PASS | Actual implementation paths, Python/apt/tool versions in `release/image-inventory.json` |
| Credential signature scan | PASS for performed scan | No high-confidence private-key/GitHub/provider-token signatures found in readable files scanned; not a proof against all secrets |
| Native fresh-runner save/remove/load and quickstart | NOT VERIFIED YET | CI runs after initial preparation commit |
| Final archive extraction/checksums/quickstart | NOT VERIFIED YET | Must complete before release |

The local preflight uses Docker Desktop 29.9.3 on ARM64, experiment `--network none`, and no paid APIs. Per-run reports are outside the Git repository. Source builds and native platform tests from the original frozen rc5 publication are linked in PROVENANCE.md; source build is not rerun solely for documentation/packaging changes.

## Scientific limitations retained

Historical runtime inputs remain unproven; label-disposition review does not relabel the dataset or resolve every unsupported domain. Fresh portable GPU inference and base-weight pinning remain unverified. The author-excluded judge-reliability ablation is not reproduced. Future apt resolution is not fully frozen. Full corpus compiler/RISC-V evidence is separate from quickstart subsets/arithmetic. Live paid requests have not been performed; SDK integration tests use intercepted responses.

Quickstart therefore still reports `NOT_SUBMISSION_READY` for complete scientific readiness. A verified offline software distribution is a narrower conclusion; no AE badge or complete historical-label validation is claimed.
