# rc6 validation status

This file accompanies a local candidate, not an already published release. Current results and exact source/image/archive identities are recorded in `evidence/rc6/` and the external `FINAL_RELEASE_VALIDATION.md` delivered with the candidate.

Required expected baseline: 214 tests without failures/errors/skips; 64 preservation checks; 61 accepted paper comparisons (40 exact, 21 within the unchanged 0.15 criterion); 76 matching downstream comparisons; successful fresh Linalg/Torch pairs. The baseline is not evidence of a new run.

Native ARM64 and packaged-byte offline runs must be observed for this exact source. Native AMD64 and matching public online testing are NOT TESTED until they actually run; the source/image must first be published with explicit approval. Historical rc5 results are not reused as rc6 results. See `PROVENANCE.md` for restored historical evidence and `release/release.json` for the local publication state.
