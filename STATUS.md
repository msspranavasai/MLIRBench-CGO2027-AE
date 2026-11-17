# Artifact status and limitations

The frozen core reviewer workflow supports four-stage archived replay, independently computed metrics, downstream saved-prediction replay, compiler arithmetic and fresh CPU execution. It requires no paid APIs, Nova or author-operated service. Individual agents and optional fresh model experiments remain available.

Use [FINAL_VALIDATION_REPORT.md](FINAL_VALIDATION_REPORT.md) for actual packaging and test results. Reports retain separate software, metrics and scientific statuses; successful execution is not universal scientific validation.

Unresolved scientific/build matters preserved from the source release:

- Original historical runtime arguments are not recovered. The [30-case disposition dossier](docs/label-dispositions.md) documents flagged witnesses and nondeterminism without relabeling the published dataset. Unsupported-domain backlog remains.
- Portable fresh GPU checkpoint inference/training is not validated; the archive includes copied adapters but not Qwen base weights.
- The judge-reliability ablation was excluded from required reproduction by the author and is not reproduced, even though the archived manuscript includes Appendix E.14/Table 24.
- A frozen exported image is provided, but fresh future apt resolution is not guaranteed by version-constrained Python dependencies or a pinned base alone.
- Full compiler/static RISC-V experiments have separate independent evidence and commands. Quickstart's arithmetic and example checks do not establish full experiment reproduction or hardware speedups.
- Optional paid provider calls were tested with intercepted responses, not actual billed requests; endpoint/model availability is not guaranteed.

Published records, labels, paper expectations, score formulas and tolerances remain byte-for-byte unchanged. The image is publicly downloadable for both native CPU architectures. This AE snapshot will remain available; future source-only organization is separate.
