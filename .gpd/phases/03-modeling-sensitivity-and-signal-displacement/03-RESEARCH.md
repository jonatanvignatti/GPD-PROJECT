# Phase 03: Modeling Sensitivity and Signal Displacement - Research

**Researched:** 2026-03-18
**Domain:** Computational Cosmology / Gravitational Wave Sensitivity
**Confidence:** HIGH

## Summary
Phase 03 focuses on quantifying how variations in physical modeling assumptions (wall velocity $v_w$, sound shell thickness, and turbulence decay) displace the gravitational wave (GW) signal in the frequency-amplitude plane $(f, \Omega_{GW} h^2)$. The goal is to move beyond fixed benchmarks and establish a sensitivity matrix for the modeling parameters.

## Mathematical Framework: Peak Displacement Analysis
The displacement of the GW signal can be characterized by the shift of the spectral peak $(f_p, \Omega_p)$.
- **Peak Frequency Scaling ($f_p$):** 
  - For sound waves (SSM): $f_{p, sw} \approx \frac{2}{R_*}$ (redshifted).
  - For bubbles (Envelope): $f_{p, bub} \approx \frac{0.62}{R_* (1.8 - 0.1 v_w + v_w^2)^{1/2}}$.
  - Sensitivity: $d \ln f_p / d \ln v_w$ identifies how the "color" of the signal shifts.
- **Peak Amplitude Scaling ($\Omega_p$):**
  - $\Omega_{p, sw} \propto (H_* R_*) \cdot \kappa_{sw}^2 \alpha^2 \cdot \Upsilon(t)$.
  - $\Omega_{p, bub} \propto (H_* R_*)^2 \cdot \kappa_{bub}^2 \alpha^2 \cdot \frac{v_w^3}{0.42 + v_w^2}$.
  - Sensitivity: $d \ln \Omega_p / d \ln v_w$ and $d \ln \Omega_p / d \ln \alpha$.

## Modeling Assumptions to Test
1. **Wall Velocity ($v_w$):** Vary from subsonic deflagrations ($v_w \sim 0.1$) to supersonic detonations ($v_w \to 1.0$).
2. **Sound Shell Thickness ($L_{sh}$):** 
   - **Thin-shell approximation:** Valid for $v_w \approx c_s$.
   - **Thick-shell effects:** Significant for deflagrations; impacts the UV slope and peak width.
3. **Turbulence Decay ($\tau_{turb}$):** 
   - Stationary vs. decaying turbulence.
   - Impact on the $k^{-11/3}$ (Kolmogorov) vs $k^{-2}$ (shock-like) spectral slopes.

## Computational Strategy: Parameter Sweeps
- **Grid Generation:** Create a $(\alpha, v_w)$ grid with $10 \times 10$ points to map the "signal drift" vectors.
- **Displacement Maps:** Visualize the trajectory of the peak $(f_p, \Omega_p)$ in the observer frame as $v_w$ is varied.
- **Sensitivity Matrix:** Compute the Jacobian $J_{ij} = \partial (\ln f_p, \ln \Omega_p) / \partial (\ln v_w, \ln \alpha, \ln \text{model})$.

## Literature & Benchmarks
- **Caprini et al. (2019) [arXiv:1910.13125]:** Review of modeling uncertainties and signal characterization.
- **Gowling & Hindmarsh (2021) [arXiv:2106.05984]:** Detailed study of the sound shell model and its sensitivity to $v_w$.
- **Roper Pol et al. (2020) [arXiv:1903.08585]:** Turbulence modeling and spectral variability.

## Validation Checklist
- [ ] **Limit Check:** Displacement vectors should vanish as modeling parameters approach the Hindmarsh (2015) benchmark values.
- [ ] **Linearity Check:** Verify if the displacement in the log-log plane is approximately linear for small parameter variations.
- [ ] **Resolution Check:** Ensure the frequency grid is fine enough to resolve peak shifts of $\sim 5\%$.
