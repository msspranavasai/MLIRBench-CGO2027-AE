# v1.0.0 archival publication procedure (not yet authorized)

**Nothing in this preparation branch is a newly published v1.0.0 archive or DOI.** Preserve [the previous Zenodo record](https://zenodo.org/records/24309675), its files and DOI. Preserve the independently published [dataset record](https://zenodo.org/records/24237192); a software release does not replace it.

The planned archive and sidecar are `MLIRBench-CGO2027-AE-v1.0.0.tar.gz` and `MLIRBench-CGO2027-AE-v1.0.0.tar.gz.sha256`. Upload only bytes actually produced, verified and approved, with a single archive root `MLIRBench-CGO2027-AE-v1.0.0/`. Never reuse the hashes or images of rc5 or rc6 as v1.0.0 artifacts.

Complete local native AMD64/ARM64 CI, immutable multi-platform export/load, package and frozen scientific-input checks, offline evaluator reproduction, full asset/manifest auditing and secret/license review first. Following explicit publication approval, publish the exact tested source/image identities, independently execute anonymous public-image checks, and then distribute the archive and actual SHA-256 sidecar. Re-download published bytes without maintainer credentials and independently re-extract and rerun the documented offline reviewer route before reporting completion.

`release/zenodo-metadata.json` is only a proposal. Do not assert that a v1.0.0 DOI has been assigned.
