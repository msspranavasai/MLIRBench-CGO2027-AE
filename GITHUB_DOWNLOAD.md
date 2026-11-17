# Download the complete artifact from GitHub

The canonical distribution is `MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz`. It includes one exported Docker image with both native CPU variants, source, datasets, evidence and optional adapters. The archive exceeds GitHub's [2 GiB per-file release limit](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases). Zenodo receives the single intact archive; GitHub release assets carry three transport parts of those exact bytes. These are not separate environments or independently maintained archives.

From the [v0.3.0rc5 release](https://github.com/msspranavasai/MLIRBench-CGO2027-AE/releases/tag/v0.3.0rc5), download:

- `MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz.part01`
- `MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz.part02`
- `MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz.part03`
- `MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz.parts.sha256`
- `MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz.sha256`

In a new directory containing those files:

```bash
# macOS; Linux can use sha256sum -c instead.
shasum -a 256 -c MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz.parts.sha256
cat MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz.part01 \
    MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz.part02 \
    MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz.part03 \
    > MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz
shasum -a 256 -c MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz.sha256
tar -xzf MLIRBench-CGO2027-AE-v0.3.0rc5.tar.gz
cd MLIRBench-CGO2027-AE-v0.3.0rc5
python3 release_tools/verify_distribution.py
docker load -i docker/mlirbench-ae-v0.3.0rc5-image.tar
AE_IMAGE_SOURCE=local AE_IMAGE=ghcr.io/msspranavasai/mlirbench-ae:0.3.0rc5 ./ae.sh quickstart
```

Allow disk space for parts, reconstructed archive, extracted files, loaded image and new reports (at least 20 GB free; more for full experiments). If the canonical archive is obtained directly from Zenodo, skip the part reconstruction and check the outer SHA-256 before extraction. The plain GitHub source ZIP/tarball omits the actual image and large supplemental assets; use the complete distribution for offline archival reproduction.
