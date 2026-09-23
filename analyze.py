#!/usr/bin/env python3
"""Analyze one synthetic or live-formatted CSV using the frozen OLS fit."""
import argparse, csv, math
from pathlib import Path
import numpy as np

def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit("No rows found")
    return rows

def fit(x, y):
    x = np.asarray(x, dtype=float); y = np.asarray(y, dtype=float)
    x = x - x.mean()
    sxx = float(x @ x)
    if sxx <= 0: raise ValueError("No variation in J")
    slope = float(x @ (y-y.mean()) / sxx)
    resid = y - (y.mean() + slope*x)
    # Source protocol requests analytic SE; use Bernoulli/model-based SE.
    p_hat = min(max(float(y.mean() + 0.5), 0.0), 1.0)
    se = math.sqrt(max(p_hat * (1-p_hat), 1e-15) / sxx)
    return slope, se, slope/se

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csv", type=Path)
    ap.add_argument("--sham-seed", type=int, default=20260923)
    ap.add_argument("--permutations", type=int, default=1, help="Number of within-context permutation shams")
    args=ap.parse_args()
    rows=read_csv(args.csv)
    ctx=np.array([int(r["context"]) for r in rows])
    j=np.array([float(r["J_centered"]) for r in rows])
    a=np.array([int(r["outcome_a"]) for r in rows])
    y=a-0.5
    print(f"file={args.csv} N={len(rows)}"); print("WARNING: synthetic QA CSV; not live hardware evidence unless replaced by verified live data.")
    pooled=fit(j,y); print(f"pooled: kappa={pooled[0]:.6f} SE={pooled[1]:.6f} z={pooled[2]:.3f}")
    for c in (0,1):
        f=fit(j[ctx==c],y[ctx==c]); print(f"C{c}: kappa={f[0]:.6f} SE={f[1]:.6f} z={f[2]:.3f}")
    rng=np.random.default_rng(args.sham_seed)
    zs=[]
    for _ in range(args.permutations):
        jp=j.copy()
        for c in (0,1):
            ids=np.where(ctx==c)[0]; jp[ids]=rng.permutation(jp[ids])
        zs.append(fit(jp,y)[2])
    print(f"within-context sham: mean_z={np.mean(zs):.3f} max_abs_z={np.max(np.abs(zs)):.3f} permutations={len(zs)}")
    var=float(np.var(j,ddof=1)); seplan=math.sqrt(0.25/(len(rows)*var))
    print(f"Var(J_centered)={var:.6f} SE_plan={seplan:.6f}")

if __name__ == "__main__": main()
