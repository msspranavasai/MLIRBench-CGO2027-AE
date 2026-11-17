# rc6 release repair. The rc5 binary toolchain is an immutable, two-platform base.
# docker/Dockerfile.rc5 preserves its original dependency-building recipe.
FROM ghcr.io/msspranavasai/mlirbench-ae@sha256:9238290317c4e6a0b70cd20781fc30169efa87c6fcbc663debdcccd3275eeec8
ARG TARGETARCH
ENV MLIRBENCH_IMAGE_ARCH=${TARGETARCH}
WORKDIR /app
COPY Dockerfile ae.sh pyproject.toml README.md ARTIFACT.md STATUS.md LICENSE DATA_LICENSE.md CITATION.cff run.py .gitignore /app/
COPY requirements /app/requirements
COPY optional/live_pipeline /app/optional/live_pipeline
COPY src /app/src
COPY tools /app/tools
COPY tests /app/tests
COPY experiments /app/experiments
COPY docs /app/docs
# Source installation has no dependency resolution and no network access.
RUN --network=none python -m pip install --no-cache-dir --no-deps --no-build-isolation . && \
    python -c "import importlib.metadata,mlirbench; assert importlib.metadata.version('mlirbench') == mlirbench.__version__ == '0.3.0rc6'" && \
    command -v mlir-opt && command -v torch-mlir-opt && command -v iree-compile && \
    python -c "import iree.compiler,iree.runtime,numpy" && test ! -f /app/.env
ENTRYPOINT ["python", "-m", "mlirbench"]
CMD ["--help"]
