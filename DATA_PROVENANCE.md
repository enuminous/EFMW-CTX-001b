# Data provenance

## What the source supplied

The pasted source contains summary statistics for two toy attempts and the complete refined protocol. It explicitly says the second attempt was a toy world with a planted `kappa_c = 0.05`, and later clarifies that the apparent pass was method validation, not physics. The source does not contain original shot-level CSVs or the code that generated them.

## What this repository supplies

The CSVs in `data/` are deterministic, newly generated synthetic QA data. `generate_qa.py` computes an EWMA current from simulated housekeeping residuals and then generates Bernoulli outcomes for planted or null cases. Seeds and rules are in the script. These datasets are included to make the repository runnable and to exercise the analyzer.

They are **not** the original data from the two source simulations, and they are **not** live hardware results. The source's reported summary statistics are preserved separately in `SOURCE_SUMMARIES.json`; regenerated fits will differ because the original random streams and generator implementation were not supplied.

## Files

- `attempt001_initial_planted.csv`: synthetic 8,000-shot planted QA set, `kappa = 0.08`.
- `attempt001_null_world.csv`: synthetic 8,000-shot zero-coupling QA control.
- `attempt001b_planted_live.csv`: synthetic 160,000-shot planted QA set, `kappa = 0.05`; despite the filename's protocol-arm terminology, this is simulation only, not live.
- `attempt001b_blank.csv`: synthetic 160,000-shot null blank QA set.

The refined source narrative also reports a planted sham summary. The analyzer computes a fresh within-context permutation sham when run; its value is not a source-reported original result.
