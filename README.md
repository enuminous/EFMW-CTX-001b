# EFMW-CTX-001b — Apparatus-current coupling in two measurement contexts

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/EFMW-CTX-001b) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#core-efmw-and-review)

<details open>
<summary><strong>On this page</strong></summary>

- [Status and evidence boundary](#status-and-evidence-boundary)
- [Repository contents](#repository-contents)
- [Quick start](#quick-start)
- [Frozen primary model](#frozen-primary-model)
- [What a pass could support](#what-a-pass-could-support)


</details>

**Related repositories:** [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian) · [efmw-equation-review](https://github.com/enuminous/efmw-equation-review) · [EFMW-Axioms](https://github.com/enuminous/EFMW-Axioms) · [EFMW_Post156_Zoo_Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit) · [EFMW](https://github.com/enuminous/EFMW) · [papers](https://github.com/enuminous/papers)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


A flat, GitHub-ready research packet extracted from the supplied conversation. It contains the refined live-hardware proposal, the earlier 001 attempt, source-reported toy summaries, and reproducible synthetic QA datasets.

## Status and evidence boundary

**No live hardware experiment is reported here.** The two attempts in the source are toy simulations with a planted coupling. They demonstrate packet/estimator behavior only; they are not measurements of quantum systems, contextuality, or nature.

The supplied source contained summary statistics but did **not** contain the original shot-level files or generator code. The CSV files in `data/` are freshly regenerated, deterministic synthetic QA datasets based on the stated design. They are not the original simulation output and are not live measurements. See `SOURCE_SUMMARIES.json` for the values reported in the source and `DATA_PROVENANCE.md` for details.

## Repository contents

- `PROTOCOL.md` — extracted refined EFMW-CTX-001b hardware protocol and decision rules.
- `ATTEMPT_001.md` — initial packet, reported toy outcome, and reasons it did not pass.
- `SOURCE_SUMMARIES.json` — source-reported summaries for attempts 001 and 001b, preserved as reported (including awkward/ambiguous source values).
- `DATA_PROVENANCE.md` — evidence and reconstruction boundary for included CSVs.
- `PACKET.json` — machine-readable frozen design parameters and evidence status.
- `WIRING.md` — minimal apparatus, data-flow, and isolation notes.
- `generate_qa.py` — deterministic regeneration of synthetic QA CSVs.
- `analyze.py` — OLS estimator, analytic standard errors, within-context permutation sham, and planning gate.
- `data/` — synthetic shot-level CSVs for initial attempt, null control, refined planted arm, and refined blank.
- `SHA256SUMS` — file integrity hashes, excluding itself and the ZIP archive.
- `LICENSE_STATUS.md` — license status.

## Quick start

```bash
python3 -m pip install numpy
python3 generate_qa.py
python3 analyze.py data/attempt001_initial_planted.csv
python3 analyze.py data/attempt001_null_world.csv
python3 analyze.py data/attempt001b_planted_live.csv
python3 analyze.py data/attempt001b_blank.csv
```

The script's inferred fit is a QA calculation over synthetic data. Do not describe it as a live result. The source-reported summary numbers are kept separately in `SOURCE_SUMMARIES.json` and are not expected to match the regenerated CSVs exactly.

## Frozen primary model

For interleaved contexts `C ∈ {0,1}`, with frozen target probability `p_C = 1/2`:

```text
E[a_t | C_t, J_t] = p_C + kappa_c * J_t^(c)
```

`J_t` is computed solely from housekeeping residuals, then centered within context. The primary estimate is OLS of `a_t - p_C` on `J_t^(c)`, with analytic standard error. The primary null is `kappa_c = 0`; the design alternative is `|kappa_c| >= 0.05`.

## What a pass could support

A pass under the frozen rule would support a device-level coupling for the tested apparatus and packet. A second apparatus replication is required for a stronger claim. It would not establish that information is a spacetime tensor, explain contextuality, or show that conventional physics has failed.
