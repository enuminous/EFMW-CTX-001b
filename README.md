# EFMW-CTX-001b — Apparatus-current coupling in two measurement contexts

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/EFMW-CTX-001b) · This repository is linked through its source; GitHub Pages is not enabled.

<details>
<summary>Recent repositories (9)</summary>

- [Oroboros](https://github.com/enuminous/Oroboros) · [README](https://github.com/enuminous/Oroboros/blob/main/README.md) · [Page](https://enuminous.github.io/Oroboros/)
- [P-NP](https://github.com/enuminous/P-NP) · [README](https://github.com/enuminous/P-NP/blob/main/README.md) · [Page](https://enuminous.github.io/P-NP/)
- [Research-Program](https://github.com/enuminous/Research-Program) · [README](https://github.com/enuminous/Research-Program/blob/main/README.md) · [Page](https://enuminous.github.io/Research-Program/)
- [I-Have-Guts](https://github.com/enuminous/I-Have-Guts) · [README](https://github.com/enuminous/I-Have-Guts/blob/main/README.md) · [Page](https://enuminous.github.io/I-Have-Guts/)
- [Wrights-Law](https://github.com/enuminous/Wrights-Law) · [README](https://github.com/enuminous/Wrights-Law/blob/main/README.md) · [Page](https://enuminous.github.io/Wrights-Law/)
- [Aristotle-eNuminous](https://github.com/enuminous/Aristotle-eNuminous) · [README](https://github.com/enuminous/Aristotle-eNuminous/blob/main/README.md) · [Page](https://enuminous.github.io/Aristotle-eNuminous/)
- [Multiverse-Simulator](https://github.com/enuminous/Multiverse-Simulator) · [README](https://github.com/enuminous/Multiverse-Simulator/blob/main/README.md) · [Page](https://enuminous.github.io/Multiverse-Simulator/)
- [accelerando-8192](https://github.com/enuminous/accelerando-8192) · [README](https://github.com/enuminous/accelerando-8192/blob/main/README.md) · [Page source](https://github.com/enuminous/accelerando-8192/blob/main/docs/index.html)
- [Codex-888](https://github.com/enuminous/Codex-888) · [README](https://github.com/enuminous/Codex-888/blob/main/README.md) · [Page](https://enuminous.github.io/Codex-888/)

</details>
<!-- ENUMINOUS-NETWORK:END -->

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
