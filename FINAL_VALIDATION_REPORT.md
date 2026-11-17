# Artifact Validation Report

## Release validation status

**Corrected release: PENDING REVALIDATION.**

This report separates previously recorded validation evidence from checks that must be repeated after the Linalg mutation-catalog correction and intended live-agent model updates. No previously reported PASS is represented as a PASS for modified source or a rebuilt image.

The published dataset and archived paper results remain the reference for scientific comparisons. The optional Linalg mutation catalog excludes the unused `L2_R2` entry, and the intended live-agent assignments are Mutation GPT-5.5, Execution `gemini-2.5-flash`, nine reasoning models, and Judge `gpt-5.4-mini`. Exact runtime implementation, provider IDs, and fresh API behavior must be verified.

## Historical validation evidence

The following results were recorded for the earlier tested artifact and are **historical evidence only**, not validation of the corrected release.

| Historical check | Previously recorded result |
|---|---|
| Scientific source inventory | 178 non-documentation/non-CI files matched the then-current inventory |
| Published records | 1,768 pairs: 888 Linalg and 880 Torch |
| Reasoning and judging records | 15,912 reasoning records, nine model keys, 15,907 judge observations |
| Bundled input integrity | 21 published manifest entries and 288 downstream files |
| Historical execution export | 1,804 rows; 1,768 published rows |
| Optional assets | 914 entries, including 11 final adapters |
| Unit/integration tests | 214 tests passed |
| Preservation checks | 64 passed |
| Paper comparison | 61/61 within the existing criteria: 40 exact, 21 within criteria |
| Archived compiler arithmetic | 1,369 comparisons |
| CPU demonstrations | Fresh Linalg and Torch examples passed |
| Native CI | AMD64, ARM64 and macOS launcher checks recorded |

The five missing Gemini judge observations remain missing. No missing observation is synthesized.

The historical image reference was `ghcr.io/msspranavasai/mlirbench-ae:0.3.0rc5`, with recorded index digest `sha256:9238290317c4e6a0b70cd20781fc30169efa87c6fcbc663debdcccd3275eeec8`. The historical exported image was 1,314,104,320 bytes with SHA-256 `ece02c64a3fc675b45912ad09c3b68f7c0b564e37693e9b1632efe139cb31697`. **These values must not be assigned to a rebuilt or modified image without independent verification.**

The historical native verification records are available in the repository's CI history and, where packaged, under `evidence/review-ci/` and `evidence/review-multiplatform-ci/`. They do not establish that a subsequently modified image was tested.

## Scientific data and configuration scope

The published benchmark comprises 1,768 pairs and 15,912 reasoning records. The published program pairs, archived responses, labels, scoring formulas and numerical policies are intended to remain unchanged.

The Linalg catalog correction removes `L2_R2` from the optional mutation-rule catalog. The published rule count is 24 Linalg plus 22 Torch. Historical references to an excluded `L2_R2` program in label-provenance documentation must remain intact.

The intended live-agent configuration is:

| Stage | Intended model |
|---|---|
| Mutation | GPT-5.5 |
| Execution | `gemini-2.5-flash` |
| Reasoning | Nine published benchmark models |
| Judge | `gpt-5.4-mini` |

Fresh CPU compiler execution does not itself establish that Gemini is called. A live Execution Agent integration must be verified separately. The exact GPT-5.5 provider request identifier must also be confirmed. None of these intended settings changes historical archived inference records.

## Required validation of the corrected release

Before marking this release PASS, record actual commands, exit codes, timestamps, tested commit, image digests and resulting evidence for:

1. The corrected scientific-file manifest, original-to-final source map and intentional modification classification.
2. The 24 Linalg and 22 Torch rule counts and absence of `L2_R2` from the active Linalg catalog.
3. Actual runtime defaults and request payloads for Mutation, Execution (if model-assisted), Reasoning and Judge.
4. Unit/integration tests, archived replay, preservation checks, scoring and downstream metric recomputation.
5. Fresh CPU Linalg and Torch execution demonstrations.
6. Native AMD64 and ARM64 image build/test, or explicitly scoped verification of a matching published image.
7. A complete multi-platform image export, checksum, clean load and offline quickstart.
8. The final `MANIFEST.sha256`, outer archive SHA-256 and clean extraction verification.
9. The exact tested source fingerprint, Docker labels and image identities.
10. Validation of all documentation links, secret scanning and absence of unintentional artifacts.

The source-only integrity check is:

```bash
python3 release_tools/verify_distribution.py --source-only
```

The required reviewer workflow is:

```bash
./ae.sh quickstart
```

For a completed standalone archive:

```bash
python3 release_tools/verify_distribution.py
docker load -i docker/mlirbench-ae-v0.3.0rc5-image.tar
AE_IMAGE_SOURCE=local AE_IMAGE=ghcr.io/msspranavasai/mlirbench-ae:0.3.0rc5 ./ae.sh quickstart
```

The archive and image names above describe the existing rc5 convention. If a corrected release receives a new version, update the commands, file names and references consistently. Do not overwrite an immutable published tag with different bytes.

## Scientific limitations

- Historical execution runtime inputs remain incompletely proven. The 30-case disposition dossier records structural conflicts, unsafe metadata, counterexamples and nondeterminism without changing published labels.
- Portable fresh GPU checkpoint inference/training remains unverified. Optional adapters are bundled, but external Qwen base weights and a fully validated portable inference path are not.
- The author-excluded judge-reliability ablation is not reproduced, despite its presence in the manuscript.
- A frozen exported image does not guarantee identical future apt repository resolution during source rebuilds.
- Live paid-provider requests have not been established as successful by intercepted SDK tests.
- Archived arithmetic and small CPU demonstrations are not substitutes for full 857-program Linalg, 845-program Torch and 693-program RISC-V regeneration.
- Static RISC-V instruction analysis does not demonstrate hardware speedups.

The author-defined Table 4 comparison criterion remains 0.15 points on a 0–100 scale, with all 45 cells and model/level orderings required. This is neither an execution-output tolerance nor an AE badge decision.

## Release conclusion

The earlier distribution has recorded successful software and offline-replay evidence. **The corrected distribution has not yet earned an updated validation PASS in this document.**

Once final tests are performed, replace this pending status with the measured outcomes and reference the exact final archive, image digests, test evidence and `FINAL_ARCHIVE_VALIDATION.json`. No AE badge or universal semantic-label correctness is claimed.
