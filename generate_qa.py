#!/usr/bin/env python3
"""Generate deterministic synthetic QA data. These are not live or original source rows."""
import csv
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
ALPHA = BETA = 0.05
EPS = 1e-8
P = 0.5

def make_rows(n, kappa, seed, attempt, arm):
    rng = np.random.default_rng(seed)
    contexts = np.resize(np.array([0, 1], dtype=int), n)
    rng.shuffle(contexts)
    # Housekeeping residuals are independent of outcome generation.
    residual = rng.normal(0.0, 1.0, n)
    m = 0.0
    v = 1.0
    current = np.empty(n)
    for i, r in enumerate(residual):
        m = (1 - ALPHA) * m + ALPHA * r
        v = (1 - BETA) * v + BETA * (r * r)
        current[i] = m / np.sqrt(v + EPS)
    centered = current.copy()
    for c in (0, 1):
        mask = contexts == c
        centered[mask] -= centered[mask].mean()
    probs = np.clip(P + kappa * centered, 0.0, 1.0)
    outcomes = rng.binomial(1, probs)
    return zip(range(n), contexts, residual, current, centered, probs, outcomes)

def write(path, n, kappa, seed, attempt, arm):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["attempt", "arm", "shot", "context", "r_housekeeping", "J", "J_centered", "p_generated", "outcome_a", "planted_kappa", "synthetic_only"])
        for shot, c, r, j, jc, p, a in make_rows(n, kappa, seed, attempt, arm):
            w.writerow([attempt, arm, shot, int(c), f"{r:.10g}", f"{j:.10g}", f"{jc:.10g}", f"{p:.10g}", int(a), kappa, "true"])

if __name__ == "__main__":
    DATA.mkdir(exist_ok=True)
    write(DATA / "attempt001_initial_planted.csv", 8000, 0.08, 20260923, "001", "planted")
    write(DATA / "attempt001_null_world.csv", 8000, 0.0, 20260924, "001", "null")
    write(DATA / "attempt001b_planted_live.csv", 160000, 0.05, 7, "001b", "planted_synthetic_not_live")
    write(DATA / "attempt001b_blank.csv", 160000, 0.0, 11, "001b", "blank_synthetic")
    print("Wrote deterministic synthetic QA CSVs under data/. No hardware data were generated.")
