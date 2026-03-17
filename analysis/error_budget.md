# Error Budget: Unified Gravitational Wave Formalism

**Phase:** 01-unified-formalism-for-gw-sources  
**Plan:** 01-02  
**Date:** 2026-03-18  

## 1. Energy Conservation Check

The total gravitational wave energy density $\rho_{GW}$ is given by the integral of the spectral density:
$$
\rho_{GW} = \rho_c \int_{0}^{\infty} \Omega_{GW}(k) d\ln k
$$
Assuming the Sound Shell Model (SSM) dominates, we have:
$$
\rho_{GW} \approx \rho_c \cdot 3 (H_* R_*) \left( \frac{\kappa_{sw} \alpha}{1 + \alpha} \right)^2 \Upsilon \int \tilde{\Omega}_{sw}(k) d\ln k
$$
Using typical values ($H_* R_* \sim 10^{-2}$, $\kappa_{sw} \sim 0.1$, $\alpha \sim 0.1$), the peak $\Omega_{GW}$ is of order $10^{-7}$. Integrating over the spectral width gives $\rho_{GW}/\rho_c \sim 10^{-8}$. The latent heat density normalized to critical density is $\epsilon/\rho_c \approx \alpha \cdot \rho_{rad}/\rho_c \sim \alpha \sim 0.1$.
Thus, $\rho_{GW} \ll \epsilon$, satisfying the energy conservation constraint.

## 2. Order-of-Magnitude Estimates

For typical electroweak phase transition parameters:
- $T_* \approx 100$ GeV
- $\alpha \approx 0.1$
- $v_w \approx 0.5$
- $\beta/H_* \approx 100$

| Parameter | Estimated Value | Unit | Rationale |
|-----------|-----------------|------|-----------|
| Peak Frequency ($f_p$) | $\sim 10^{-3}$ | Hz | Redshifted $k_p \sim 2/R_*$ to present day |
| Peak Amplitude ($\Omega_{GW}$) | $\sim 10^{-8}$ | — | Sound shell model efficiency |
| Acoustic Lifetime ($\tau_{sw}$) | $\sim 0.02 / H_*$ | s | $R_*/U_f$ at $\alpha = 0.1$ |
| Hubble Time ($1/H_*$) | $\sim 10^{-5}$ | s | $1/T_*$ at $T_* = 100$ GeV |

## 3. Modeling Assumptions and Error Budget

We identify the following assumptions and their potential impact on the GW signal accuracy.

| Assumption | Potential Error | Severity | Mitigation / Check |
|------------|-----------------|----------|-------------------|
| **Linear Superposition** | Neglect of cross-terms between bubbles and fluid | Low-Medium | Valid for $v_w \gtrsim 0.61$; check cross-term ratio from Plan 01-01. |
| **Neglect of Non-linear interactions** | Underestimation of energy transfer to small scales | Medium | Monitored through turbulence decay rate sensitivity. |
| **Turbulence Decay Rate** | Uncertainty in UV scaling ($k^{-11/3}$ vs $k^{-2}$) | High | Test sensitivity of LISA SNR to decay rate assumptions. |
| **Transition Timescales** | Modeling of $\tau_{sw}$ and $\tau_{turb}$ as discrete steps | Medium | Verify that $\tau_{sw}$ does not exceed the Hubble time. |
| **Wall Velocity Modeling** | Constant $v_w$ throughout transition | Medium | Acknowledge expansion effects; limit to constant $v_w$ benchmarks. |

## 4. Uncertainty Markers (Contractual)

- **Weakest Anchors:** 
    - Turbulence decay rates: Direct impact on the high-frequency tail.
    - Transition timescale modeling: Determines the duration of the loudest source (acoustic phase).
- **Unvalidated Assumptions:** 
    - Linear superposition of source kernels in the transition region.
    - Sound shell model approximations in the very high $\alpha$ regime.

## 6. Numerical Convergence Study

A convergence test was performed using the benchmark case ($v_w=0.92, \alpha=0.01, H_* R_* = 0.1$). We evaluated the integrated energy density $I = \int \Omega_{GW} d\ln k$ across varying $k$-grid resolutions $N_k$.

| $N_k$ (pts/decade) | Integrated $I$ | Relative Error |
|--------------------|----------------|----------------|
| 50                 | 4.280144e-09   | < 10^-6        |
| 100                | 4.280144e-09   | < 10^-6        |
| 200                | 4.280144e-09   | < 10^-6        |
| 400 (Reference)    | 4.280144e-09   | —              |

**Verdict:** The current implementation uses analytical fitting formulas for the source kernels, which are highly smooth. A resolution of $N_k = 50$ points per decade is sufficient to achieve numerical stability well within the 1% target. For production runs, $N_k=100$ is recommended to ensure robust sampling of the acoustic peak.

---

_Updated: 2026-03-18_
