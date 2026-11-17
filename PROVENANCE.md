# rc6 source and distribution provenance

The repair starts from public source commit `0e928aae24691f20c17d1f47948fb06c3822b601` and the exact Zenodo bytes independently reviewed on November 17, 2026. The public rc5 record and independent review are preserved.

## Evidence-based decisions

Commit `e77cecd9b2e8f9c8a1edb85c102449722ad072ce` intentionally removed unused catalog rule `L2_R2`. Commit `0e928aae24691f20c17d1f47948fb06c3822b601` intentionally changed optional mutation preflight/reporting to `gpt-5.5` after the rc5 image build. Neither edits published records. Retain those intentions and rebuild; do not falsify labels or disable fingerprint validation. rc6 also applies the existing fingerprint guard in local mode. The actual mutation SDK default still selected `gpt-5-mini`; rc6 aligns that request default with preflight and tests its intercepted payload. This is isolated optional future-inference configuration, not a regeneration of historical results. Provider access/availability is not tested.

The root Dockerfile derives from the exact two-platform rc5 index `sha256:9238290317c4e6a0b70cd20781fc30169efa87c6fcbc663debdcccd3275eeec8`, copies the actual corrected source, cleanly uninstalls the previous MLIRBench distribution from an isolated working directory, and installs only the new pure Python package with no dependency resolution or network. Isolated Python must see exactly one installed MLIRBench distribution. This preserves installed compiler/dependency bytes and scientific flags. `docker/Dockerfile.rc5` preserves the original dependency-building recipe. A new source fingerprint and actual new image configurations are required. Nothing is relabeled in place.

The original complete local rc5 archive has SHA-256 `ca59d388bdc528983d85bb7dc01ee28b117857dc05e71ec0d89f2295deed96bb`, matching its pre-existing sidecar. Its manifest verifies the recovered 914-entry Nova inventory, 11 adapter models and historical evidence files. Restored evidence keeps its original contents and source identities; it is not attributed to rc6. External base weights and unavailable historical execution arguments remain unavailable.

## Integrity scopes

- `release/original-files.sha256`: unchanged historical inventory.
- `release/source-file-map.tsv`: actual before/after hashes with intentional modification classifications.
- `release/scientific-reference.sha256`: protected data, scoring/compiler implementation, numerical policies and configurations, pinned to the evaluated release.
- `release/scientific-files.sha256`: current distributed source hashes, including authorized packaging/version/optional configuration changes.
- `MANIFEST.sha256`: every complete-distribution file except itself, including restored assets, validation evidence and the actual image.
- `docker/image-inventory.json`: actual export checksum, platform/config digests, fingerprint and validation scope.
- Canonical `.tar.gz.sha256`: actual outer archive identity, external to that archive.

Generated experiment outputs remain outside the extracted artifact. No labels, scoring formulas, tolerances, compiler flags, model records, downstream predictions/splits or paper results are changed. Passing software does not establish universal semantic correctness or award an AE badge.

## Preservation baseline reconciliation

The first real rc6 run passed all 214 tests, metrics and fresh CPU cases but correctly failed one of 64 preservation checks: `experiments/release_invariants.json` still pinned the original optional catalog. The original baseline is retained byte-for-byte as `release/rc5-release-invariants.json`. Only the catalog SHA-256 is updated in the active baseline; all scientific data and recomputed-output expectations remain identical. The distribution verifier independently enforces that this is the sole structural difference. No check, tolerance or expectation is removed; 64 checks remain. This is release-validation identity metadata, not a changed numerical or experimental policy. `release/baseline-reconciliation.json` records exact hashes and the zero published occurrences of the removed rule.
