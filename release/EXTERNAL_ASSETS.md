# Bundled and external scientific resources

| Resource | Availability | Identity / limitation |
|---|---|---|
| Published program pairs and nine-model reasoning/evaluation | Source and unified image | `data/bundle/manifest.json`, raw/compressed SHA-256; 1,768 pairs and 15,912 reasoning records |
| Downstream saved predictions/splits | Source bundle and image | `data/downstream/manifest.json` and preserved snapshot |
| Historical execution records | Source and image | `data/historical/source_manifest.json`; historical runtime arguments remain unproven |
| Accepted paper/reference | Source | `paper/reference/`; https://arxiv.org/abs/2611.14881 |
| Copied Nova resources and 11 adapters | Complete archive `assets/nova/`, not Git/image | Original 914-file `ASSET_MANIFEST.json`; checkpoint hashes also in `data/provenance/checkpoint_source_hashes.json` |
| Label-review diagnostics | Complete archive `evidence/label-review/` | Copied original rc5 raw evidence and checksums; 30 cases, no relabeling |
| Native platform build/pull evidence | Complete archive `evidence/native-ci/` | Original rc5 GitHub CI records; original source identity retained |
| Qwen/Qwen2.5-Coder-14B-Instruct base weights | External, optional GPU only | Not bundled; original experiment checkpoint metadata has no pinned base revision. This prevents claiming fully frozen GPU inference; model is not required for CPU replay |
| Optional live LLM providers | External, optional only | Explicit opt-in and user-arranged credentials; provider availability and fresh outputs may differ |
| Future source build apt resources | External for rebuild only | Base digest/Python versions pinned; apt repository snapshot not frozen. Offline image use avoids this dependency |
| Published dataset recovery | External only if local/bundled records absent | Hugging Face `mlirbench/MLIRBench`, revision `1af6c3c7a29946a7cd0e2aafd9386686d7fec9d1`, explicit consent and original hashes required |
| Existing dataset Zenodo deposit | Author reports already public | Exact DOI not confirmed from available source. No DOI is invented or replacement dataset deposit created |

Software Apache-2.0 and dataset CC BY 4.0 are separate. Third-party dependencies/model assets retain their original license terms. Adapter distribution does not grant rights to unbundled base weights. Historical cluster/absolute paths in immutable provenance are source metadata, not default runtime dependencies. The core image is self-contained for the documented no-cost CPU workflow; optional GPU/live experiments are not claimed self-contained.
