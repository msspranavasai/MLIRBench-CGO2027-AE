# rc6 image and publication gates

One unified reviewer image reference, `ghcr.io/msspranavasai/mlirbench-ae:0.3.0rc6`, contains native-platform AMD64 and ARM64 configurations. The local candidate is not published. Each reviewer invocation starts one container; no extra services or credentials are required for replay. Use the complete offline route in [README.md](../README.md).

The root Dockerfile builds corrected source on the immutable two-platform rc5 toolchain index, preserving compiler/runtime packages and scientific flags. `docker/Dockerfile.rc5` is the original full dependency recipe. Rebuilding the rc6 source requires that frozen base; loading the supplied final export does not require any registry.

Source fingerprint verification is unchanged. Version/package fixtures were updated for rc6, not weakened. Image/source disagreement remains an error. Local mode also checks the source fingerprint and requires an explicitly loaded matching export; the complete distribution verifier also compares image labels with actual source before execution.

Docker 29+ with the containerd image store is required for multi-platform load. Check `docker info -f '{{ .DriverStatus }}'` for `io.containerd.snapshotter.v1`. Preserve unrelated daemon settings and images.

Before publication, run native source-build/local-image CI on both architectures. `.github/workflows/ci.yml` is prepared for that purpose but cannot validate this unpublished source until its branch is approved for upload. After explicit approval, publish the new source/image identities without replacing rc5 and run `.github/workflows/verify-public-image.yml` with anonymous credentials. Inspect actual results; do not call an emulated AMD64 build/run native validation. Export the actual final two-platform image, verify every blob and matching labels, then clean-load/run on both native runners. These checks remain separately reported; historical rc5 CI does not pass them for rc6.
