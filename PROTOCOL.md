# EFMW-CTX-001b experimental protocol

**Title:** Apparatus-current coupling in two measurement contexts  
**Status:** Proposal for live-hardware testing. Simulations are packet QA only.  
**Primary parameter:** `kappa_c`  
**Primary null:** `kappa_c = 0`  
**Design alternative:** `|kappa_c| >= 0.05` (design value, not a prior about nature)

## 1. Claim

For randomly interleaved contexts `C ∈ {0,1}` on one apparatus, estimate whether

```text
E[a_t | C_t, J_t] = p_C + kappa_c J_t^(c)
```

where `a_t` is a binary outcome, `p_C` is frozen from the prepared state before outcomes are opened, and `J_t^(c)` is a centered apparatus current computed only from housekeeping channels.

## 2. Scope

This packet tests one device-level association. It does not test spacetime curvature, a Unity field, CEWs, AGI, ethics, Millennium problems, or any term absent from the frozen regression. Passing does not establish EFMW as new physics. A failed criterion is recorded as a miss.

## 3. Minimum apparatus

- Binary-outcome channel with two switchable settings (for example, photon polarization with two mutually unbiased bases, or a calibrated weak coherent pulse, PBS, and waveplate).
- Random interleaving of `C0` and `C1`, driven independently of housekeeping sensors.
- Timestamped click/no-click (or 0/1) outcomes with setting labels.
- Housekeeping stream that cannot see the quantum click: candidate channels include temperature, bias voltage, clock residual, pump monitor, or witness-detector dark-count proxy.
- Shuttered or classical-RNG blank arm using the same `J` pipeline but no quantum outcome channel.
- Clock synchronization sufficient to pair shots with housekeeping samples. If housekeeping is slower, use the last housekeeping sample before the shot; freeze this rule before collection.
- Preserve raw traces without overwriting them.

## 4. Frozen analysis objects

Freeze and hash this protocol, code, wiring diagram, channel list, predictor, and `p_C` before examining live outcomes.

| Object | Frozen rule |
|---|---|
| Contexts | `C0`, `C1`, and the switch-driving method |
| Target probability | Example: `p_C = 1/2` for both contexts from the stated preparation; no post-hoc state fit in primary analysis |
| Housekeeping residual | `r_t = y_t^app - yhat_t^app` on named housekeeping channels only |
| Predictor | Name the formula/model for `yhat^app` and freeze it |
| EWMA memory | `m_t = (1-alpha)m_(t-1) + alpha*r_t`; `v_t = (1-beta)v_(t-1) + beta*r_t^2` |
| Constants | `alpha = beta = 0.05`; `epsilon = 1e-8` |
| Apparatus current | `J_t = m_t / sqrt(v_t + epsilon)` |
| Centering | Subtract mean `J` within each context before pooling to form `J_t^(c)` |
| Primary estimator | OLS of `a_t - p_C` on `J_t^(c)`; report analytic SE |
| Sham | Permute `J_t^(c)` within context and rerun the same OLS |
| Blank | Same pipeline on shuttered/classical-RNG outcomes |
| Retuning | Do not retune memory or other parameters after seeing a z statistic |

A logistic MLE with the same linear predictor may be preregistered as secondary; it cannot replace OLS as primary.

## 5. Run order and sample-size gate

1. Hash the frozen packet.
2. Collect housekeeping only and estimate `Var(J^(c))`.
3. Do not open quantum outcomes until the planned standard error meets

   `SE_plan = sqrt(p(1-p) / (N * Var(J^(c)))) <= 0.017`,

   for `p = 1/2` and a nominal 3-sigma design at `|kappa_c| = 0.05`.
4. Run the blank arm to at least the same `N`; analyze blank and blank-sham.
5. Collect live, randomly interleaved contexts to the same `N`.
6. Analyze live pooled, per-context, and within-context sham results.
7. Stop. Add no unregistered terms.

Use measured `Var(J^(c))` to plan `N`. The source's packet-QA example used `Var(J^(c)) ≈ 0.025`, implying roughly `1.6e5` total shots for `SE ≈ 0.008`. Recalculate on the actual apparatus. A tiny current variance that requires impractical `N` is a design failure, not evidence for the hypothesis.

## 6. Decision rule

**Pass on this device only if all conditions hold:**

- `|z_live pooled| >= 3`;
- the `C0` and `C1` estimates have the same sign;
- `|z_live sham| < 2`;
- `|z_blank| < 2`.

Any failure is a miss. Also file a miss if `J` used click-stream data or if `p_C` was fitted after examining residuals. A pass is device-level only; replication on a second apparatus is needed before a broader claim.

## 7. Required report

Report these rows without selectively omitting failed checks:

| Arm | kappa estimate | SE | z |
|---|---:|---:|---:|
| Live pooled | | | |
| Live C0 | | | |
| Live C1 | | | |
| Live sham | | | |
| Blank pooled | | | |
| Blank sham | | | |

Also report `N`, `Var(J^(c))`, `SE_plan`, packet hash, hardware identifiers, channel list, exclusions, and deviations.

## 8. Prelisted systematics

Treat these as ordinary apparatus/systematic effects, not as information terms:

- setting-dependent detection efficiency;
- dead time, pile-up, accidental coincidences;
- pointing or waveplate hysteresis correlated with setting changes;
- thermal drift that also drives switch electronics;
- outcome leakage into housekeeping (fatal to the isolation claim).

If a systematic can mimic `kappa_c`, veto that housekeeping channel before freezing or preregister a covariate before unblinding. No post-unblinding covariates in the primary analysis.

## 9. Personnel split

The person writing EFMW interpretation does not unblind the live file. A second person runs the frozen script and returns the table. This is the independent veto.

## 10. Permitted conclusion

If all criteria pass, a permitted statement is: “On apparatus X, with packet hash H and `p_C` frozen as specified, we estimate `kappa_c = …`; the sham and blank checks were quiet.”

This does not establish that information is a natural tensor of spacetime, explain contextuality, or show conventional physics has failed.

## 11. Recommended first physical milestone

Before photons, run the packet on a classical Bernoulli box: two button-selected coin devices plus a thermistor-derived housekeeping current. If this blank-like system passes, the packet remains contaminated; resolve isolation before a quantum-channel test.
