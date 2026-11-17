# Optional live-agent developer reference

Archived replay needs no credentials and never constructs model clients. Fresh CPU execution also needs no model credentials. Fresh model stages require `--allow-paid-api`. Before data preparation or any agent runs, the maintained runner resolves selected model keys, checks credentials needed by requested fresh stages, validates request budgets, and constructs SDK clients without making requests. An invalid model, missing credential, invalid budget, or SDK setup error stops the run before an earlier stage can incur charges.

This local preflight does not authenticate with providers or establish model availability, quota, endpoint access, or output quality. A syntactically valid model ID may still be rejected by the provider. There is no automatic substitute model. Fresh results can differ from archived paper results.

## Agent architecture and model identities

The following table distinguishes the **intended agent assignments** from the model calls actually documented in the current optional live runner. The intended assignments must be implemented and tested before they can be described as verified runtime defaults.

| Agent | Intended model | Runtime status and scope |
|---|---|---|
| Mutation | OpenAI `gpt-5.5` | Selected through `MLIRBENCH_MUTATION_MODEL`; confirm the installed runtime default and provider availability |
| Execution | Google `gemini-2.5-flash` | Intended model-assisted execution analysis; the documented fresh CPU execution stage is deterministic and does **not** require Gemini credentials or make a model call |
| LLM Reasoning | Nine published benchmark models | Chosen using `--model MODEL_KEY`; the nine published model keys are listed below |
| Judge | OpenAI `gpt-5.4-mini` | Selected through `OPENAI_MODEL`; confirm the installed runtime default and provider availability |

**Do not conflate execution-stage model assistance with compiler execution.** The default execution stage compiles and runs programs using the bundled toolchains. Listing `gemini-2.5-flash` here does not establish that a Gemini-powered execution adapter has been implemented or integrated into the runner.

The published dataset includes 1,768 program pairs (888 Linalg, 880 Torch), 15,912 reasoning records across nine models, and 46 mutation rules (24 Linalg, 22 Torch). The unused Linalg catalog entry `L2_R2` was removed because it has no occurrences in the frozen mutation provenance. The archived program pairs, reasoning records, labels, and scoring policies remain unchanged.

## Optional local configuration

The required AE route uses archived responses and needs none of these settings. API credentials, credits, and an author-operated API service are not provided or promised. Evaluators are not expected to purchase access. Users who independently choose live inference may set environment variables or use `AE_ENV_FILE` pointing to a private Docker environment file **outside** the repository. Never commit credentials. The launcher forwards named provider settings only when `--allow-paid-api` is present.

| Live stage | Provider/model | Credential | Selection or override |
|---|---|---|---|
| Mutation | OpenAI, intended `gpt-5.5` | `OPENAI_API_KEY` | `MLIRBENCH_MUTATION_MODEL` (exact provider model ID) |
| Reasoning | Selected registry entry below | Provider credential from registry | `--model MODEL_KEY` |
| Judge | OpenAI, intended `gpt-5.4-mini` | `OPENAI_API_KEY` | `OPENAI_MODEL` (exact provider model ID) |
| Optional model-assisted execution | Google, intended `gemini-2.5-flash` | `GOOGLE_API_KEY` if implemented | **No verified execution-agent selector or model-call integration is documented here** |

A judge-only fresh run needs the judge credential, not the evaluated reasoning model's credential. A reasoning-only fresh run needs only the selected reasoning provider's credential. A full live run needs credentials for the stages that actually make provider requests. The deterministic fresh execution stage does not require `GOOGLE_API_KEY` solely because Gemini is an intended model-assisted execution component.

### Reasoning-model registry

The nine **published** reasoning models are the first nine rows. The last three entries are additional available registry choices, **not** additional published benchmark models.

| Reasoning key | Provider | Configured request model ID | Credential | Published benchmark |
|---|---|---|---|---|
| `gemini-3.1-pro-preview` | Google | `gemini-3.1-pro-preview` | `GOOGLE_API_KEY` | Yes |
| `gpt-4.1-mini` | OpenAI | `gpt-4.1-mini` | `OPENAI_API_KEY` | Yes |
| `claude-sonnet-4-5` | Anthropic | `claude-sonnet-4-5` | `ANTHROPIC_API_KEY` | Yes |
| `claude-haiku-4-5` | Anthropic | `claude-haiku-4-5` | `ANTHROPIC_API_KEY` | Yes |
| `qwen3-coder-next` | OpenRouter | `qwen/qwen3-next-80b-a3b-instruct` | `OPENROUTER_API_KEY` | Yes |
| `llama-4` | OpenRouter | `meta-llama/llama-4-maverick` | `OPENROUTER_API_KEY` | Yes |
| `glm-5.1` | OpenRouter | `z-ai/glm-5.1` | `OPENROUTER_API_KEY` | Yes |
| `kimi-k2.6` | OpenRouter | `moonshotai/kimi-k2.6` | `OPENROUTER_API_KEY` | Yes |
| `gpt-oss-120b` | OpenRouter | `openai/gpt-oss-120b` | `OPENROUTER_API_KEY` | Yes |
| `gemini-3-flash` | Google | `gemini-3-flash-preview` | `GOOGLE_API_KEY` | No |
| `gemini-2.5-flash` | Google | `gemini-2.5-flash` | `GOOGLE_API_KEY` | No |
| `gemini-2.5-pro` | Google | `gemini-2.5-pro` | `GOOGLE_API_KEY` | No |

OpenRouter entries use `https://openrouter.ai/api/v1`. These are the currently documented registry mappings, not independent proof of historical provider identities. In particular, `qwen3-coder-next` maps to a Qwen3-Next Instruct request ID; confirm its historical identity before making exact-reproduction claims. Provider availability and account access must be checked before a large live experiment.

Legacy aliases remain `openai` → `gpt-4.1-mini`, `claude` → `claude-sonnet-4-5`, and `gemini` → `gemini-3-flash`. For the paper's Gemini model, explicitly select `--model gemini-3.1-pro-preview`; the generic `gemini` alias selects another model. `GEMINI_API_KEY` alone does not satisfy this registry's `GOOGLE_API_KEY` requirement.

**Model ID verification:** `gpt-5.5` and `gpt-5.4-mini` are the requested identifiers. Before releasing a rebuilt image, confirm that these are the exact identifiers accepted by the configured OpenAI API and that the code actually uses them. Do not silently substitute a different model. A failed or unavailable provider model should remain an explicit failure.

## Request limits

These are finite request budgets for new runs, not historical generation settings or monetary caps. Provider reasoning tokens may count toward output budgets. Truncated or failed responses remain failures and are never replaced with archived scores.

| Environment variable | Documented default | Allowed range |
|---|---:|---|
| `MLIRBENCH_API_TIMEOUT_SECONDS` | 180 | finite, greater than 0, at most 3600 |
| `MLIRBENCH_API_MAX_RETRIES` | 0 | integer 0–5, SDK retries per request |
| `MLIRBENCH_MUTATION_MAX_OUTPUT_TOKENS` | 8192 | integer 1–131072 |
| `MLIRBENCH_REASONING_MAX_OUTPUT_TOKENS` | registry default | integer 1–131072 |
| `MLIRBENCH_JUDGE_MAX_OUTPUT_TOKENS` | 4096 | integer 1–131072 |
| `MLIRBENCH_MUTATION_MAX_ATTEMPTS` | 3 | integer 1–10 |

Registry reasoning defaults remain 4096 tokens except `llama-4` at 2048. SDK retries default to zero; reasoning and judging each make one agent attempt. Mutation retains a maximum of three generation/validation attempts. Maximum request attempts for one mutation case are `mutation_max_attempts × (sdk_retries + 1)`; for one reasoning or judge case, `sdk_retries + 1`. Timeout applies to each SDK request, not the entire experiment. Workload size increases with `--all`.

Each fresh run saves `live_configuration` in its `manifest.json`: resolved model IDs, provider names, credential-variable names, and budgets, without credential values. Archived replay's records and metric calculations are unchanged. Tests construct registered provider SDKs and intercept request payloads with dummy credentials and networking disabled. Such tests do not verify real authentication or paid inference.

For durable case recovery, see [continuing a stopped fresh run](../ARTIFACT.md#continue-a-stopped-fresh-run). Continuation requires the same resolved settings and source fingerprint and explicit `--resume-incomplete`; changing model identities or budgets starts a separate experiment.

Self-contained fresh checkpoints can continue without published dataset views at runtime. If host bundles are missing and a matching local image already exists, `AE_SKIP_BUILD=1` reuses it without building or pulling; see the reviewer instructions. Historical replay retains frozen-source checks.

## Live judging and provenance safeguards

Optional live judging validates raw responses before computing a score. Required fields are a scores object containing `result_accuracy` in [0,10] and integer-valued `explanation_rating` in [0,4], an evidence object, and nonempty reasoning text. Booleans, strings, NaN/infinities, duplicate JSON keys, malformed/truncated responses, and out-of-range ratings are rejected. Supplied component maxima must match the mutation rubric. The failed case journal retains raw response text, its SHA-256, and schema errors, without assigning a successful score. No API headers or credential values are captured. Valid ratings retain the existing scoring formula; archived observations are not passed through the new live-response validator.

The live adapter passes the recorded mutation rule and inspection metadata to the judge. Archived pairs resolve their explicit rule ID from the packaged catalog and retain `pipeline_metadata`; provenance identifies this lookup without claiming that the current catalog proves the historical prompt. Missing metadata is identified as not recorded. Unknown or conflicting rule identities fail before the judge call. This affects future optional judging, not published ratings.

## Fresh failure handling versus the historical paper protocol

The accepted paper describes fallback zero subjective scores after judge request/parse failure (Appendix E, archived text lines 1189–1193), and clamping parsed judge scores (lines 1287–1292). New optional live judging instead rejects invalid responses and records an **unscored failed attempt**. This is an intentional validation change for new experiments, not an exact rerun of the historical failure protocol. A fresh experiment must report attempted, completed, failed, and unscored counts; an average over successful cases alone cannot be presented as the paper's full-dataset score. Frozen historical judge observations, including any recorded fallback values, are replayed unchanged. No new fallback scores are invented.

New mutation generation uses ordinary compiler verification, without `--verify-diagnostics`: expected-error comments must not turn a failing program into successful validation. Levels 1–4 require compiler acceptance; failed attempts are retained and the pipeline stops if none passes. Level 5 requires an explicit catalog rule, a compiler-valid original, a different complete module envelope, and a positive compiler error return code with a recognized verification diagnostic. Dependency-breaking R4 rules also accept recognized undefined-SSA diagnostics. Other parser/unknown-operation failures are conservatively rejected; a balanced module alone is insufficient. Accepted Level 5 candidates carry `EXPECTED_INVALID`; this validates the declared error-test shape, not full semantic compliance with every rule. Review the saved candidate and diagnostics for rule adherence. Compiler infrastructure failures stop immediately.

Fresh failed reasoning attempts retain returned text, its pre-redaction SHA-256, parse/schema status, and error details in the case journal, without fabricating a downstream label or score. Credentials and authorization headers are redacted from new diagnostic records; a completed result containing a configured credential is rejected before persistence. A hash of original text may therefore differ from a redacted displayed response. Never share environment files or provider credentials. These protections do not rewrite frozen historical records.

OpenRouter-compatible clients use Chat Completions and send registry controls via `extra_body`. OpenRouter's `reasoning.exclude` hides returned reasoning; it does not disable computation or guarantee reduced tokens, latency, or charges. Its Responses API does not honor that setting. Model availability/authentication remains unverified without independently arranged access; no automatic substitute model is selected.

## Release consistency

Changing the mutation catalog or live-agent configuration requires updating the applicable source manifests, source-file map, Docker image, distribution inventory, and validation evidence. The default offline workflow must continue to reproduce the frozen dataset and paper metrics. A previously published image or release tag must not be described as containing new source changes unless it was actually rebuilt and verified.
