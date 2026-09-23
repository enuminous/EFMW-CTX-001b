# Wiring and data-flow notes

This is a proposal sketch, not a completed apparatus diagram.

```text
independent context randomizer ──> setting switch ──> binary outcome channel ──> outcome log a_t
                                                            │
                                                            └── no connection to J inputs

housekeeping sensors ──> frozen predictor ──> residual r_t ──> EWMA m_t, v_t ──> J_t ──> context centering
                                                                                         │
                                                                                         └── frozen OLS after outcome lock

shutter/classical RNG ──> blank outcome log ─────────────────────────────────────────────┘
```

The isolation requirement is central: `J` must be computable with the quantum outcome channel disabled and must not use clicks, no-clicks, or labels derived from them. Preserve raw sensor and outcome streams, timestamps, setting bits, packet hash, and hardware IDs. The drawing does not identify a specific instrument; channel names and synchronization/aggregation rules must be frozen for the selected device.
