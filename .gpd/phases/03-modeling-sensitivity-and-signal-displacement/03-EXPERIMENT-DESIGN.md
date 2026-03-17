# Experiment Design: Modeling Sensitivity and Signal Displacement

> **For gpd-executor:** This file contains parameter specifications, convergence criteria, and statistical analysis plans. Use these when executing computational tasks in Phase 03.

## Objective
Quantify the displacement of the gravitational wave (GW) signal in the $(f, \Omega_{GW} h^2)$ plane resulting from variations in physical modeling assumptions ($v_w, \alpha$, and model choice).

## Target Quantities
| Quantity | Symbol | Dimensions | Expected Range | Required Accuracy | Validation |
|----------|--------|------------|----------------|-------------------|------------|
| Peak Frequency | $f_p$ | Hz | $10^{-6}$ to $10^{-2}$ | 1% relative | Match analytic $2/R_*$ limit |
| Peak Amplitude | $\Omega_p h^2$ | dimensionless | $10^{-20}$ to $10^{-8}$ | 5% relative | Match Hindmarsh (2015) benchmarks |
| Spectral Slope (IR) | $n_{IR}$ | dimensionless | $\sim 2.8$ to $3.0$ | 0.1 absolute | Causality limit $k^3$ |
| Spectral Slope (UV) | $n_{UV}$ | dimensionless | $-1.0$ to $-4.0$ | 0.1 absolute | Model-specific (e.g., -4 for SW) |
| Sensitivity Jacobian | $J_{ij}$ | dimensionless | $O(1)$ | 10% relative | Linearity check $\Delta \ln Y \approx J \Delta \ln X$ |

## Control Parameters
| Parameter | Symbol | Range | Sampling | N_points | Rationale |
|-----------|--------|-------|----------|----------|-----------|
| Wall velocity | $v_w$ | $[0.1, 0.95]$ | Uniform | 10 | Capture deflagration to detonation transition |
| Phase strength | $\alpha$ | $[0.01, 1.0]$ | Log-spaced | 6 | Cover weak to strong transitions |
| Modeling Model | Model | {SSM, Bub, Mixed} | Categorical | 3 | Compare different physics assumptions |

## Numerical Parameters and Convergence
| Parameter | Symbol | Values | Expected Order | Convergence Criterion |
|-----------|--------|--------|----------------|----------------------|
| Frequency Samples | $N_f$ | 100, 200, 400 | $O(N_f^{-1})$ | Peak shift $< 0.1\%$ |
| Finite Diff Step | $\Delta v_w$ | 0.01, 0.005 | $O(\Delta^2)$ | Jacobian stable to 1% |

## Grid Specification
The primary experiment uses a $(\alpha, v_w)$ grid:
- $v_w \in \{0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95\}$
- $\alpha \in \{0.01, 0.03, 0.1, 0.3, 0.6, 1.0\}$
- Models:
    - **SSM:** Sound Shell Model (Sound wave dominated, $\kappa_{sw} > 0, \kappa_{bub}=0$)
    - **Bub:** Envelope Approximation (Bubble collision dominated, $\kappa_{bub} > 0, \kappa_{sw}=0$)
    - **Mixed:** Combined (80% SW, 10% Bub, 10% Turb)

## Statistical Analysis Plan
### Peak Identification
Peaks $(f_p, \Omega_p)$ shall be identified using quadratic interpolation around the numerical maximum of $\log_{10} \Omega_{GW}(\log_{10} f)$ to ensure sub-grid resolution.

### Sensitivity Matrix (Jacobian)
Compute the sensitivity matrix at a reference point $(v_w=0.5, \alpha=0.1)$:
$$ J = \begin{pmatrix} \frac{\partial \ln f_p}{\partial \ln v_w} & \frac{\partial \ln f_p}{\partial \ln \alpha} \\ \frac{\partial \ln \Omega_p}{\partial \ln v_w} & \frac{\partial \ln \Omega_p}{\partial \ln \alpha} \end{pmatrix} $$
Using central finite differences: $\frac{\partial \ln Y}{\partial \ln X} \approx \frac{\ln Y(X+\Delta) - \ln Y(X-\Delta)}{2 \ln(1 + \Delta/X)}$.

### Linearity Check
Verify the linear approximation by comparing $J \Delta \ln X$ with the actual displacement at the grid corners.

## Expected Scaling
- **Sound Waves:** $f_p \propto v_w^{-1}$ (roughly, since $R_* \propto v_w$). $\Omega_p \propto v_w \alpha^2$.
- **Bubbles:** $f_p$ has weaker $v_w$ dependence. $\Omega_p \propto v_w^3 \alpha^2$.

## Computational Cost Estimate
| Run Type | N_points | Grid Size | Steps/Samples | Est. Time/Point | Total Time |
|----------|----------|-----------|---------------|-----------------|------------|
| Parameter sweep | 180 | $N_f=200$ | 1 | 0.01s | < 1 min |
| Convergence study| 3 | $N_f=400$ | 1 | 0.02s | < 1 min |
| Sensitivity Matrix| 4 | $N_f=200$ | 2 | 0.01s | < 1 min |
| **Total** | | | | | **~5 min CPU** |

## Execution Order
1. **Pilot:** Run single point $(v_w=0.92, \alpha=0.1)$ for SSM and Bub; compare with Phase 02 benchmarks.
2. **Convergence:** Test $N_f \in \{100, 200, 400\}$ to lock frequency resolution.
3. **Production Sweep:** Execute the full 180-point grid.
4. **Jacobian Calculation:** Compute the sensitivity matrix at the reference point.
5. **Visualization:** Generate "displacement maps" showing peak trajectories in the $(f, \Omega)$ plane.

## Suggested Task Breakdown (for planner)

| Task | Type | Dependencies | Est. Complexity |
|------|------|-------------|-----------------|
| Setup experiment script | code | Phase 02 lib | small |
| Run convergence study | validate | script | small |
| Execute parameter sweep | sim | convergence | medium |
| Calculate sensitivity matrix | analysis | sweep | medium |
| Generate comparison plots | analysis | sweep | small |
