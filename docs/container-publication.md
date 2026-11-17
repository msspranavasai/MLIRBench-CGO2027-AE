# One image, one reviewer container

Frozen public image reference for this release:

```text
ghcr.io/msspranavasai/mlirbench-ae:0.3.0rc5
```

The single root Dockerfile packages the four agents, local validation tools, both IREE toolchains, archived observations and metric computation. The registry index has two native variants of that same environment: linux/amd64 and linux/arm64. Docker chooses the CPU-compatible variant; the reviewer runs one container per invocation. There is no supporting database, remote compiler server, Compose stack or per-agent image.

## Reviewer command

From the matching source checkout:

```bash
./ae.sh quickstart
```

The launcher downloads the versioned image for the Docker daemon's CPU and checks its source-fingerprint label against this checkout. The experiment container runs with networking disabled unless the user explicitly requests an optional paid API experiment. No provider API credentials, credits or Nova access are needed for the default archived route. Image downloading is separate from experiment networking.

The existing rc5 image is public. Reviewers can pull without registry credentials. This dedicated repository’s CI only verifies the frozen image; it does not publish a replacement.

Use `AE_IMAGE_SOURCE=build ./ae.sh quickstart` to build the same Dockerfile locally. Use `AE_IMAGE_SOURCE=local AE_IMAGE=mlirbench-ae:reviewer ./ae.sh quickstart` for an already loaded local image without registry access. An explicit AE_PLATFORM selects a platform; choosing another CPU architecture requires emulation and is identified in the output. AE_IMAGE may be set to the published index digest for a binary-immutable reference.

## Publication verification

The original source repository’s versioned publication workflow:

1. Builds AMD64 and ARM64 on native GitHub-hosted runners.
2. Runs the full offline workflow, tests, numerical agreement and preservation checks on each.
3. Checks private-repository visibility before pushing any source-bearing layers.
4. Pushes each tested platform by digest, with no public architecture-specific tags. The pushed configuration must match the tested one.
5. Assembles exactly those two manifests under one version tag. A conflicting existing version tag is not overwritten.
6. Pulls that one tag on new native AMD64 and ARM64 runners and repeats the complete reviewer workflow.

The OCI source/revision/version labels and per-platform CI evidence identify the build. The workflow publishes an index digest in the `published-image` artifact. A successful container publication validates this packaged software workflow; it does not resolve the separately disclosed historical label, GPU or incomplete RISC-V scientific checks.

## Public download verification

The GHCR package is public independently of this repository's preparation visibility. The verification CI uses fresh native runners and a fresh Docker configuration with no registry login. Passing on both platforms establishes anonymous reviewer access to the one versioned image. No image rebuild is required for documentation-only changes.

For offline use, verify and load the single export as documented in README.md. The image inventory records the platforms actually exported. The complete reviewer workflow uses one container; no Docker service dependencies are introduced.

References:

- https://docs.docker.com/build/building/multi-platform/
- https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
- https://docs.github.com/en/packages/learn-github-packages/configuring-a-packages-access-control-and-visibility
