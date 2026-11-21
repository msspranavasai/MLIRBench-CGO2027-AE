# v1.0.0 source preparation status

This branch is an **unpublished release candidate under development**. The version identifiers are being prepared; the complete v1.0.0 offline archive, matching two-platform image export, immutable archive checksum and public-download checks are not yet available or validated. No release/tag, new historical runtime inputs, paid inference, fresh full GPU reproduction, or AE badge is claimed.

The prior rc6 hardening commit `a1f1f04bc4a8357bbf473060ca59fed670686f3a` was tested in native AMD64 and ARM64 CI. That success **does not certify the new v1.0.0 bytes**. See `FINAL_VALIDATION_REPORT.md` for the historical rc6 local-candidate validation record, and `docs/RELEASE_GATES.md` for the gates that must be checked anew for v1.

Required before publication: native source and image validation on both CPUs; immutable packaged-byte offline export/load tests; 61 paper and 76 downstream comparisons; frozen input and original scientific-reference verification; complete archive and asset manifest validation; anonymous registry pull and remote checksum checks; third-party licensing and credential scanning; and explicit review of outstanding historical provenance, compiler/RISC-V and GPU limitations.

The required reviewer workflow remains offline and does not require paid model calls. `NOT_SUBMISSION_READY` must not be silently reclassified based on engineering test success alone.
