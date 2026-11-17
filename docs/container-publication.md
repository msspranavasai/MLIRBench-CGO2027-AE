# One image, one reviewer container

MLIRBench uses a single versioned multi-platform Docker image, with native `linux/amd64` and `linux/arm64` variants. The root `Dockerfile` packages the four-agent code, compiler toolchains, archived observations and metric utilities. Each evaluator command runs one disposable container, without a database, Compose stack or per-agent images.

## Reviewer workflow

```bash
./ae.sh quickstart
```

The default route replays archived agent observations, recomputes scores and performs CPU compiler checks. It does not require paid API credentials, GPU hardware, Nova access or an external compiler service. The experiment container uses networking disabled by default. Pulling an image is separate from experiment networking.

The previously published image reference is:

```text
ghcr.io/msspranavasai/mlirbench-ae:0.3.0rc5
```

**Release identity matters:** a source checkout with modified mutation catalogs or runtime model configuration must not be described as validated by an older image. The launcher checks the image's source-fingerprint label. If that fingerprint differs, build and validate a matching image or publish a new immutable version. Do not silently replace an existing immutable tag.

## Image acquisition

```bash
# Default: pull the versioned image for the Docker host CPU.
./ae.sh quickstart

# Explicit local build using the current checkout.
AE_IMAGE_SOURCE=build ./ae.sh quickstart

# Use an already loaded matching image without pulling.
AE_IMAGE_SOURCE=local AE_IMAGE=mlirbench-ae:reviewer ./ae.sh quickstart
```

An explicit `AE_PLATFORM` can select `linux/amd64` or `linux/arm64`. Running a non-native platform can require emulation.

## Versioned publication and verification

For every image version intended for reviewers:

1. Freeze the scientific source and documented configuration.
2. Build AMD64 and ARM64 on native runners.
3. Run unit/integration tests, offline quickstart, preservation checks and metric comparisons on both.
4. Verify OCI source, revision, version and source-fingerprint labels.
5. Publish the two tested platform images and assemble one multi-platform index.
6. Refuse to overwrite an existing version tag with conflicting platform digests.
7. Pull the published index anonymously on fresh native runners and repeat the reviewer workflow.
8. Export the multi-platform image, record the actual index/export digests and test a clean offline load.
9. Regenerate the distribution inventory and archive integrity evidence.

Historical CI success is evidence only for the source and image versions actually tested. Documentation-only edits generally do not require a new image if the runtime source fingerprint and image contents remain identical. Scientific source or runtime configuration changes do require renewed matching validation.

Useful references:

- https://docs.docker.com/build/building/multi-platform/
- https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
- https://docs.github.com/en/packages/learn-github-packages/configuring-a-packages-access-control-and-visibility

## Offline image-store compatibility

The complete distribution includes one exported image with both native CPU variants. Loading this multi-platform export requires Docker Engine 29 or newer with the containerd image store enabled, including a compatible Docker Desktop installation.

Check the active image store:

```bash
docker info -f '{{ .DriverStatus }}'
```

The output should include `io.containerd.snapshotter.v1`. On Docker Desktop, enable **Use containerd for pulling and storing images** in Settings > General if needed. For Docker Engine, follow the [containerd image-store documentation](https://docs.docker.com/engine/storage/containerd/) and preserve unrelated daemon settings.

Switching image stores can temporarily hide images and containers from the other store. The launcher does not modify the user's Docker daemon.

For a complete archive whose image has been validated:

```bash
python3 release_tools/verify_distribution.py
docker load -i docker/mlirbench-ae-v0.3.0rc5-image.tar
AE_IMAGE_SOURCE=local AE_IMAGE=ghcr.io/msspranavasai/mlirbench-ae:0.3.0rc5 ./ae.sh quickstart
```

Use the actual final release's image name and version if different. Loading the archive should not require a registry pull, and the evaluator workflow should still run one container.
