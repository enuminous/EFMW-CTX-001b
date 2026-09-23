# EFMW-CTX-001 initial attempt

## Frozen idea

Estimate a coupling in

```text
a_t - p_C = kappa_c * J_t^(c) + e_t
```

using two interleaved contexts, a housekeeping-only residual, EWMA current `J = m/sqrt(v+epsilon)`, and a within-context permutation sham. The first version used `alpha = beta = 0.05`, `epsilon = 1e-8`, and a nominal `p = 1/2`.

## Source-reported toy attempt 1

The source described a synthetic world with true `kappa_c = 0.08`, `N = 4,000` shots per context (`8,000` total), and `p_QM = 1/2`. Reported pooled estimate: `0.063 ± 0.038` (`z ≈ 1.66`). The contexts were reported as `0.11 ± 0.05` and `0.011 ± 0.055`; the within-context sham was `0.096 ± 0.038` (`z ≈ 2.5`). A separate zero-coupling world was reported as `-0.026 ± 0.036`.

These are toy simulation summaries, not hardware data. The initial attempt was not a pass: the planned sensitivity was insufficient, the contexts did not agree, and the sham was not quiet.

## Changes leading to 001b

- Centered `J` within context before pooling.
- Added a planned-SE gate before opening outcomes.
- Added a blank arm as a first-class control.
- Required context estimates to share sign.
- Kept the regression to one coupling and prohibited post-outcome additions.

The source did not include the original 001 shot-level data or its generator. The included `data/attempt001_initial_planted.csv` and `data/attempt001_null_world.csv` are regenerated synthetic QA, not reconstructions of those original rows.
