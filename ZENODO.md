# rc6 archival publication procedure

**Approval required. Nothing in this local candidate has been uploaded.** Preserve [the existing Zenodo release](https://zenodo.org/records/24309675), its files and DOI. Create an approved new version related to that release; do not overwrite or relabel public rc5 bytes. The standalone dataset remains [record 24237192](https://zenodo.org/records/24237192).

Upload exactly the candidate files `MLIRBench-CGO2027-AE-v0.3.0rc6.tar.gz` and `MLIRBench-CGO2027-AE-v0.3.0rc6.tar.gz.sha256`. Use the actually generated hash/byte size, not a placeholder. Upload the archive directly, without ZIP wrapping. Its sole root is `MLIRBench-CGO2027-AE-v0.3.0rc6/`.

Before requesting publication approval, complete local source/distribution checks and packaged-byte offline runs. Native AMD64 and public online validation remain unmet until actually executed. Review `FINAL_VALIDATION_REPORT.md`; historical rc5 CI files cannot satisfy rc6 gates.

After approval: publish the matching source revision and immutable rc6 two-platform image; run the anonymous online quickstart on native AMD64 and ARM64, capture source/platform identities and logs; then archive the exact tested distribution and sidecar. Do not claim public online success before these runs. Read back Zenodo metadata and downloaded bytes, compare its checksum/size and the delivered SHA-256, extract in a new directory and repeat the documented offline workflow. If the service presents another wrapper, document its observed structure and checksum independently; do not assume it happened.

Reviewer checksum/extraction commands are in [README.md](README.md). `release/zenodo-metadata.json` is a local metadata proposal, not evidence of publication or a newly assigned DOI.
