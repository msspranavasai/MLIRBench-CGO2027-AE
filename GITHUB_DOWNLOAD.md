# Canonical v1.0.0 artifact download (planned, not published)

The complete v1.0.0 distribution has **not** been produced or published. The intended files are `MLIRBench-CGO2027-AE-v1.0.0.tar.gz` and `MLIRBench-CGO2027-AE-v1.0.0.tar.gz.sha256`. Do not download an automatic GitHub source ZIP and mistake it for the complete offline artifact: it omits large supplemental resources and the exported multi-platform image.

After final packaging and approval, the archive must be a plain `.tar.gz` containing exactly one root `MLIRBench-CGO2027-AE-v1.0.0/`. Check its actual SHA-256 before extraction, run `release_tools/verify_distribution.py` on the extracted full distribution, load the included image, and execute the documented local reviewer quickstart on supported native CPUs.

The original rc5 public upload and rc6 development evidence retain their historical names and hashes. Do not overwrite them, rename their bytes to v1.0.0, or publish the planned paths as though they already exist. The full offline reviewer download is a separate publication gate.
