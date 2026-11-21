# v1.0.0 image and publication gates

**Unpublished preparation.** The planned reviewer image reference is `ghcr.io/msspranavasai/mlirbench-ae:1.0.0`. No public v1.0.0 image is asserted to exist yet. The existing rc5 and rc6 images, evidence and metadata retain their original identities.

The Dockerfile is based on the immutable two-platform rc5 toolchain index. It installs the current versioned source with no dependency network access. The frozen scientific `source_fingerprint` implementation remains unchanged, while the separate package-metadata identity verifier binds the exact `pyproject.toml` bytes, image label and installed distribution version. See [package identity](PACKAGE_IMAGE_IDENTITY.md).

Before publication, build and run the exact v1.0.0 source on **native** AMD64 and ARM64 runners. The CI workflow must verify image metadata, complete tests, published data/preservation checks, archived paper and downstream metrics, and actual image export/load/re-execution. No earlier rc6 build is v1.0.0 evidence.

The complete offline distribution must include the *newly exported v1.0.0 multi-platform image*, its actual image inventory, every required scientific bundle, supplemental asset and evidence item, a complete `MANIFEST.sha256`, a plain canonical `.tar.gz` and its independently verified `.sha256` sidecar. The complete verifier will reject absent image/archive members in this development checkout.

Only after approved publication should [the anonymous public-image workflow](../.github/workflows/verify-public-image.yml) pull the v1.0.0 image on both native CPU platforms using a clean unauthenticated Docker configuration. Record actual results rather than pre-marking publication gates as PASS. The reviewer workflow does not require APIs or extra services.
