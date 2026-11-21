# Package metadata to Docker image identity

The scientific `source_fingerprint` is intentionally unchanged because it is
part of the frozen CGO 2027 reference. An additional identity binds the *exact
bytes* of `pyproject.toml` to a newly built Docker image.

To reproduce the metadata SHA-256 from a source checkout:

```bash
python3.11 -B tools/release/package_image_identity.py
```

On an Apple Silicon Mac, build and verify the new local ARM64 image:

```bash
AE_IMAGE_SOURCE=build AE_IMAGE=mlirbench-ae:round2-identity ./ae.sh quickstart
python3.11 -B tools/release/package_image_identity.py \
  --image mlirbench-ae:round2-identity --platform linux/arm64
```

The verifier checks three independent facts: image OCI metadata label, actual
`/app/pyproject.toml` bytes inside the image, and the installed Python
`mlirbench` distribution version. It refuses any missing or inconsistent input.
The native AMD64/ARM64 GitHub Actions workflow runs the same validation.

This is not a substitute for published archive checksum validation, native
execution tests, provenance review, or scientific reproducibility. The
original rc6 image predates this supplementary identity and remains unchanged.
