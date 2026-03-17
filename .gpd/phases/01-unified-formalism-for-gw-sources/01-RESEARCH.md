# Phase 01: Unified Formalism for GW Sources - Research

**Researched:** 2026-03-17
**Domain:** Early Universe Cosmology / Gravitational Waves
**Confidence:** HIGH

## Summary
This research establishes the theoretical foundation for a unified GW spectrum from first-order phase transitions. The primary discovery is that for transitions occurring in a thermal plasma (like the Electroweak PT), sound waves (acoustic phase) dominate the signal over the initial bubble collisions. The Sound Shell Model (SSM) provides the necessary semi-analytic framework to model this, characterized by a double-broken power law spectrum.

**Primary recommendation:** Use the Hindmarsh-Hijazi (2019) SSM spectral function as the base, integrating bubble collision and turbulence contributions as additive components with appropriate transition timescales.

## User Constraints
- Active anchor: Hindmarsh 2015 (arXiv:1504.03291).
- Conventions: Metric (-+++), Physics Fourier, Natural Units.

## Active Anchor References
| Anchor / Artifact | Type | Why It Matters Here | Required Action |
| ----------------- | ---- | ------------------- | --------------- |
| Hindmarsh 2015 | Benchmark | Proves acoustic dominance and efficiency | Compare results |
| Hindmarsh 2019 | Method | Provides the SSM fitting formula | Implement formula |

## Conventions
- Metric: $(-+++)$
- Fourier: $\tilde{f}(\mathbf{k}) = \int d^3x e^{-i\mathbf{k}\cdot\mathbf{x}} f(\mathbf{x})$
- Units: $\hbar = c = G = 1$

## Mathematical Framework
- **Key Equations:** $\Omega_{\text{GW}}(k) \approx \tilde{\Omega}_{\text{GW}} \cdot (H_* L_f) \cdot \frac{K^2}{(1+w)^2} \cdot \frac{\tau_{sw}}{H_*^{-1}}$.
- **Spectral Shape:** $\tilde{\Omega}_{\text{GW}}(k) \approx \frac{\Omega_0}{\left[ (k/k_1)^{-5} + (k/k_1)^{-1} \right] + (k_2/k_1)^{-1} (k/k_2)^{3}}$.

## Standard Approaches
1. **Sound Shell Model (SSM):** Recommended for acoustic phase.
2. **Envelope Approximation:** Fallback for vacuum/runaway cases.
3. **Kolmogorov/Kraichnan:** For the late-stage turbulent decay.

## Existing Results to Leverage
- $8\pi\tilde{\Omega}_{\text{GW}} \simeq 0.8$ (efficiency parameter).
- $k^{-3}$ UV power law for deflagrations.

## Validation Strategies
- **Causality Limit:** Verify $k^3$ IR scaling for $\rho_{GW}$ (or $k^5$ in specific SSM formulations).
- **Energy Conservation:** Ensure kinetic energy fraction $\kappa$ matches fluid simulations.
