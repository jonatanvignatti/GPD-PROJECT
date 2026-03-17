# Phase 02: Numerical Implementation and Benchmark Validation - Research

**Researched:** 2026-03-17
**Domain:** Computational Cosmology / Gravitational Waves
**Confidence:** HIGH

## Summary
This research defines the numerical strategy for implementing the unified GW spectral density formula derived in Phase 1. The focus is on the **Sound Shell Model (SSM)**, which requires numerical integration of the plasma velocity correlation functions. Validation will rely on direct comparison with the fitting formulas and numerical results provided by **Hindmarsh et al. (2015, 2017)**.

## Computational Strategy
- **Implementation Language:** Python (NumPy/SciPy) is recommended for its robust integration and interpolation routines.
- **Integration Method:** 
  - Use `scipy.integrate.quad` for 1D spectral integrals.
  - For the combined spectrum $\Omega_{GW}(k)$, a logarithmic grid in $k$ (typically $10^{-3} H_*$ to $10^{3} H_*$) is necessary to capture both the IR causality ($k^3$) and UV decay ($k^{-3}$ to $k^{-4}$).
- **Source Kernels:**
  - **Bubbles:** Implement the analytic fitting formula for the envelope approximation (Huber & Konstandin 2008).
  - **Sound Waves:** Implement the SSM spectral function $C(k, \tau)$ or its semi-analytic fit $\tilde{\Omega}_{sw}(k)$.
  - **Turbulence:** Implement the Kolmogorov-type spectrum with late-time decay.

## Benchmark Targets: Hindmarsh (2015)
- **Primary Anchor:** Fig. 7 and Eq. (34) of Hindmarsh et al. (2015) [arXiv:1504.03291].
- **Key Parameters for Validation:** 
  - $v_w = 0.5, 0.92$ (benchmark wall velocities).
  - $\alpha = 0.01, 0.1$ (transition strength).
  - Agreement within 5% for the acoustic peak amplitude and frequency is the target.

## Redshifting to Present Day
The source-frame spectrum $\Omega_{GW}^*(k)$ must be redshifted to the observer frame $(f, \Omega_{GW})$:
- **Frequency:** $f = f_* \cdot \frac{a_*}{a_0} \approx 1.65 \times 10^{-5} \text{Hz} \cdot \left( \frac{f_*}{H_*} \right) \left( \frac{T_*}{100 \text{ GeV}} \right) \left( \frac{g_*}{100} \right)^{1/6}$.
- **Energy Density:** $\Omega_{GW} h^2 \approx 1.67 \times 10^{-5} \cdot \Omega_{GW}^* \left( \frac{g_*}{100} \right)^{-1/3}$.

## Validation Checklist
- [ ] Convergence test: Verify that increasing the integration resolution does not change the result by > 1%.
- [ ] Limit test: Set $\kappa_{sw}, \kappa_{turb} \to 0$ and recover the bubble-only spectrum.
- [ ] Peak shift: Verify that peak frequency scales as $1/R_*$ (average bubble separation).
- [ ] Dimensionality: Ensure all constants ($G, H_*$) are properly handled in the code units (Natural Units vs. Hz/units).
