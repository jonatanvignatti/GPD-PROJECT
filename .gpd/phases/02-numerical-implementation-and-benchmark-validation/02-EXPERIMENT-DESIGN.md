# Experiment Design: Numerical Implementation and Benchmark Validation

> **For gpd-executor:** This file contains parameter specifications, convergence criteria, and statistical analysis plans. Use these when executing computational tasks in this phase.

## Objective
Implement the unified gravitational wave (GW) spectral density formula (primarily the Sound Shell Model, SSM) and validate it against the numerical simulation results of Hindmarsh et al. (2015). The goal is to ensure the numerical implementation correctly reproduces the acoustic peak and spectral slopes.

## Target Quantities
| Quantity | Symbol | Dimensions | Expected Range | Required Accuracy | Validation |
|----------|--------|------------|----------------|-------------------|------------|
| GW Spectrum | $\Omega_{GW}(h^2)$ | dimensionless | $10^{-20} - 10^{-10}$ | 5% (peak) | Hindmarsh (2015) Fig 7 |
| Peak Frequency | $k_{peak}/H_*$ | $T^{-1}$ | $10 - 10^4$ | 5% | $k_{peak} \approx 2/R_*$ |
| Peak Amplitude | $\Omega_{peak}$ | dimensionless | $10^{-15} - 10^{-11}$ | 5% | Fitting formula in Eq (34) |
| UV Slope | $n_{UV}$ | dimensionless | $[-4, -3]$ | $\pm 0.1$ | $k^{-3}$ or $k^{-4}$ |
| IR Slope | $n_{IR}$ | dimensionless | $[+3, +5]$ | $\pm 0.1$ | $k^3$ causality |

## Control Parameters
The following parameters are chosen to match the benchmark cases in Hindmarsh et al. (2015) [arXiv:1504.03291].

| Parameter | Symbol | Range / Values | Sampling | N_points | Rationale |
|-----------|--------|----------------|----------|----------|-----------|
| Transition Strength | $\alpha$ | $\{0.01, 0.05, 0.1\}$ | Discrete | 3 | Spans weak to intermediate PTs |
| Wall Velocity | $v_w$ | $\{0.5, 0.92\}$ | Discrete | 2 | Subsonic (deflagration) vs Supersonic (detonation) |
| Efficiency Factor | $\kappa_{sw}$ | Function of $\alpha, v_w$ | Computed | - | Determined by fluid dynamics |
| Mean Bubble Separation | $H_* R_*$ | $[0.01, 0.5]$ | Log | 3 | Sets the physical scale of the peak |

## Numerical Parameters and Convergence
The "Unified Formula" involves the numerical integration of the velocity correlation function in the Sound Shell Model (SSM).

| Parameter | Symbol | Values | Expected Order | Convergence Criterion |
|-----------|--------|--------|----------------|----------------------|
| $k$-grid resolution | $N_k$ | $\{50, 100, 200\}$ | Linear | $\Delta \Omega / \Omega < 1\%$ |
| Integration Tolerance | `eps` | $\{10^{-3}, 10^{-5}\}$ | - | $\Delta \Omega / \Omega < 0.1\%$ |
| UV Cutoff | $k_{max}/H_*$ | $10^3 \times k_{peak}$ | - | Negligible power at cutoff |
| Shell thickness res | $dr$ | $\{0.01, 0.001\} R_*$ | 2nd | Integral stability |

## Grid Specification
Points will be sampled in a $(v_w, \alpha)$ grid:
1. $(v_w=0.5, \alpha=0.01)$ - Baseline weak deflagration.
2. $(v_w=0.92, \alpha=0.01)$ - Baseline weak detonation.
3. $(v_w=0.92, \alpha=0.1)$ - Stronger transition benchmark.

For each point, a 1D $k$-sweep will be performed:
- **Range:** $k \in [10^{-1}, 10^{4}] H_*$.
- **Spacing:** Logarithmic, 50 points per decade.

## Statistical Analysis Plan
Since the SSM is a semi-analytic approach, "samples" refer to the resolution of the integration.
- **Equilibration:** Not applicable (not a MC simulation).
- **Production:** A single high-resolution run per parameter point.
- **Error Estimation:** Difference between $N_k=100$ and $N_k=200$ will be treated as the numerical systematic error.
- **Consistency Check:** Verify that the integral of the spectrum $\int \Omega_{GW} d \ln k$ converges.

## Expected Scaling
- $\Omega_{peak} \propto (H_* R_*) \cdot \kappa_{sw}^2 \alpha^2$.
- $k_{peak} \propto 1/R_*$.
- IR limit: $\Omega_{GW} \sim k^3$.

## Computational Cost Estimate
Execution is expected to be efficient (Python/NumPy).

| Run Type | N_points | System Size | Steps/Samples | Est. Time/Point | Total Time |
|----------|----------|-------------|---------------|-----------------|------------|
| Pilot / Debug | 2 | $N_k=50$ | - | 5s | 10s |
| Convergence Study| 6 | $N_k=200$ | - | 20s | 2 min |
| Benchmark Sweep | 6 | $N_k=100$ | - | 10s | 1 min |
| **Total** | | | | | **~5 min** |

## Execution Order
1. **SSM Implementation:** Code the spectral kernel $C(k, \tau)$.
2. **Pilot Run:** $(v_w=0.92, \alpha=0.01)$ to verify peak position.
3. **Convergence Study:** Vary $N_k$ and integration tolerance.
4. **Production Sweep:** Run the 6 benchmark cases.
5. **Validation:** Plot against Hindmarsh (2015) data (extracted from paper).

## Suggested Task Breakdown (for planner)

| Task | Type | Dependencies | Est. Complexity |
|------|------|-------------|-----------------|
| implement_ssm_kernel | code | none | medium |
| run_convergence_study | validate | ssm_kernel | small |
| compute_benchmark_spectra | sim | convergence | small |
| validate_against_hindmarsh | analysis | benchmarks | medium |

