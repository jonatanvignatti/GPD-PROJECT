# CONVENTIONS

This file defines the canonical conventions for the project "Gravitational Radiation from First-Order Phase Transitions". All derivations, numerical codes, and results must adhere to these conventions.

## 1. Unit System

| Quantity | Unit / Convention |
|----------|-------------------|
| Natural Units | $\hbar = c = k_B = 1$ |
| Energy Scale | Energy in GeV, Temperature in GeV |
| Time/Length | $1/E$ (inverse energy) |
| Planck Mass | $M_{pl} \approx 1.22 \times 10^{19}$ GeV |
| Reduced Planck Mass | $M_{P} = (8\pi G)^{-1/2} \approx 2.43 \times 10^{18}$ GeV |

**Dimension Map (Natural Units):**
- $[Length] = [Time] = [Energy]^{-1}$
- $[Mass] = [Energy]$
- $[Stress\text{-}Energy\ Tensor] = [Energy]^4$
- $[\Omega_{GW}] = [Dimensionless]$

## 2. Spacetime Conventions

| Category | Convention | Test Value / Verification |
|----------|------------|---------------------------|
| **Metric Signature** | $(- , +, +, +)$ | $ds^2 = -dt^2 + dx^2 + dy^2 + dz^2$ (flat) |
| **Coordinate Ordering** | $(t, x, y, z)$ | $x^0 = t, x^i = \mathbf{x}_i$ |
| **Index Notation** | Greek ($\mu, \nu \dots$): $0 \dots 3$, Latin ($i, j \dots$): $1 \dots 3$ | |
| **Levi-Civita Tensor** | $\epsilon_{0123} = +1$ | |
| **Riemann Tensor** | $R^\rho_{\sigma\mu\nu} = \partial_\mu \Gamma^\rho_{\nu\sigma} - \partial_\nu \Gamma^\rho_{\mu\sigma} + \dots$ | MTW sign convention |
| **Ricci Tensor** | $R_{\mu\nu} = R^\rho_{\mu\rho\nu}$ | MTW sign convention |
| **Einstein Equation** | $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ | $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R$ |

**Metric Signature Verification:**
- On-shell timelike 4-momentum $p^\mu = (E, \mathbf{0})$ gives $p^2 = p_\mu p^\mu = g_{00} (p^0)^2 = -E^2$.

## 3. Fourier Conventions

| Category | Convention | Test Value / Verification |
|----------|------------|---------------------------|
| **Fourier Pair (Space)** | $f(\mathbf{x}) = \int \frac{d^3k}{(2\pi)^3} e^{i\mathbf{k}\cdot\mathbf{x}} \tilde{f}(\mathbf{k})$ | $\text{FT}[\delta(\mathbf{x})] = 1$ |
| **Forward Transform** | $\tilde{f}(\mathbf{k}) = \int d^3x e^{-i\mathbf{k}\cdot\mathbf{x}} f(\mathbf{x})$ | |
| **4-momentum** | $p^0 = \omega$, $p^i = k^i$ | $p \cdot x = p^\mu x_\mu = -\omega t + \mathbf{k}\cdot\mathbf{x}$ |
| **Space-Time Phase** | $e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)}$ | $e^{ipx}$ |
| **Power Spectrum** | $\langle \tilde{A}(\mathbf{k}) \tilde{B}(\mathbf{k}') \rangle = (2\pi)^3 \delta^3(\mathbf{k} + \mathbf{k}') P_{AB}(k)$ | |

## 4. Gravitational Wave Observables

| Quantity | Definition |
|----------|------------|
| **Metric Perturbation** | $g_{\mu\nu} = a^2(\eta) (\eta_{\mu\nu} + h_{\mu\nu})$, with $h_{0\mu} = 0$ (TT gauge) |
| **Energy Density** | $\rho_{GW} = \frac{\langle \dot{h}_{ij} \dot{h}_{ij} \rangle}{32 \pi G}$ (in physical time $t$) |
| **Energy Spectrum** | $\Omega_{GW}(k) = \frac{1}{\rho_c} \frac{d \rho_{GW}}{d \ln k}$ |
| **Frequency** | $f = \frac{\omega}{2\pi} = \frac{k}{2\pi a}$ |

## 5. Phase Transition Parameters

| Symbol | Description | Standard Choice / Rationale |
|--------|-------------|-----------------------------|
| $v_w$ | Wall velocity | Variable in $[0, 1]$, defined in plasma frame |
| $\alpha$ | Transition strength | Ratio of latent heat to radiation energy density $\epsilon / \rho_{rad}$ |
| $\beta$ | Inverse duration | $\beta \approx \dot{\Gamma}/\Gamma$ |
| $H_*$ | Hubble at transition | Scale of GW production |
| $R_*$ | Bubble radius at collision | $R_* \approx (8\pi)^{1/3} v_w / \beta$ |

## 6. Reference Convention Maps

| Reference | Metric | Fourier | Units | Notes |
|-----------|--------|---------|-------|-------|
| Hindmarsh et al. (2015) | $(-+++)$ | $d^3k/(2\pi)^3$ | Natural | Matches this project |
| Caprini et al. (2016) | $(-+++)$ | $d^3k/(2\pi)^3$ | Natural | Standard review |
| Kosowsky et al. (1992) | $(+---)$ | $dk$ | Natural | Needs sign flip for metric, factors of $2\pi$ for Fourier |

## 7. Numerical Factor Registry

| Factor Source | Project Value | Rationale |
|---------------|---------------|-----------|
| Fourier Measure | $1/(2\pi)^3$ | Physics standard |
| GW Energy Density | $1/(32\pi G)$ | Einstein Eq + Isaacson energy definition in $(-+++)$ |
| Bubble Radius | $\beta/H_*$ vs $\beta$ | Scaled to Hubble time |

## 8. Dimensional Consistency Verification

- **Action:** $S$ is dimensionless. $[S] = 1$.
- **Lagrangian density:** $[L] = [Energy]^4$ in 4D.
- **Einstein Equation:** $[G_{\mu\nu}] = [Length]^{-2} = [Energy]^2$, $[T_{\mu\nu}] = [Energy]^4$, $[G] = [Energy]^{-2}$. So $[G_{\mu\nu}] = [G][T_{\mu\nu}] \implies [Energy]^2 = [Energy]^{-2}[Energy]^4 = [Energy]^2$. ✓
- **Power Spectrum:** $P(k)$ for field $A$ has dimensions $[A]^2 [Length]^3 = [A]^2 [Energy]^{-3}$.
- **$\Omega_{GW}$:** $\rho_{GW} / \rho_c$ is dimensionless. ✓
