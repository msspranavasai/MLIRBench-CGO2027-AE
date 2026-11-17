# MLIRBench CGO 2027 AE — v0.3.0rc5

A stable artifact-evaluation distribution of the original rc5 scientific release. The destination tag identifies a packaging commit; original software identity is preserved in PROVENANCE.md. No scientific code, records, labels, formulas, prompts, dependency pins or compiler flags are changed.

Packaging adds consolidated evaluator documentation, original-to-final hash manifests, archive verification tools, external-asset inventory and a single Docker-inclusive offline distribution. The destination repository starts with a clean packaging history. CI validates the existing public image without rebuilding or replacing it.

The core workflow runs without API keys, Nova or GPU hardware. One versioned image supports native AMD64 and ARM64; each invocation runs one container. The offline export inventory identifies included architectures. Optional adapter assets are distributed separately from the core image inside the complete archive. Qwen base weights remain external.

Known limitations remain: historical runtime-input provenance and semantic-label conflicts, fresh portable GPU inference, author-excluded/unreproduced judge-reliability ablation, and future apt repository reproducibility. Full compiler/RISC-V evidence is distinguished from quickstart subsets and archived arithmetic. No AE badge is claimed. See FINAL_VALIDATION_REPORT.md and STATUS.md.
