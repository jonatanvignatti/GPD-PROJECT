---
phase: 01-unified-formalism-for-gw-sources
plan: 02
depth: full
one-liner: "Verified the unified GW spectral density formula against limiting cases and established benchmarks, and documented the modeling error budget."
provides:
  - "Verification of unified formula in acoustic, bubble, and turbulence limits"
  - "Energy conservation confirmation (rho_GW << epsilon)"
  - "Modeling error budget and uncertainty markers for transition timescales"
affects:
  - 02-numerical-implementation-and-benchmark-validation

methods:
  added: ["Limiting-case verification", "Energy density integration"]
  patterns: ["Benchmark reproduction protocol"]

key-files:
  modified: ["derivations/unified_gw_formalism.tex"]
  created: ["analysis/error_budget.md"]

key-decisions:
  - "Adopted Sound Shell Model as the primary acoustic source benchmark"
  - "Used Kolmogorov UV scaling for late-time turbulence"

conventions:
  - "Natural units: hbar = c = k_B = 1"
  - "Metric signature: (-+++) [mostly-plus]"
  - "Fourier: Physics convention"

plan_contract_ref: ".gpd/phases/01-unified-formalism-for-gw-sources/01-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-benchmark-reproduction:
      status: passed
      summary: "The unified formula reduces correctly to SSM and envelope approximation in appropriate limits."
      linked_ids: [deliv-gw-verification, test-gw-benchmark-consistency, Ref-Hindmarsh2015]
      evidence:
        - verifier: gpd-executor
          method: analytical reduction
          confidence: high
          claim_id: claim-benchmark-reproduction
          deliverable_id: deliv-gw-verification
          acceptance_test_id: test-gw-benchmark-consistency
          reference_id: Ref-Hindmarsh2015
          evidence_path: "derivations/unified_gw_formalism.tex"
    claim-energy-conservation:
      status: passed
      summary: "Integrated GW energy density is many orders of magnitude smaller than latent heat (rho_GW/epsilon ~ 10^-7)."
      linked_ids: [deliv-error-budget]
  deliverables:
    deliv-gw-verification:
      status: passed
      path: derivations/unified_gw_formalism.tex
      summary: "Mathematical verification of the unified formula's limiting cases."
      linked_ids: [claim-benchmark-reproduction, test-gw-benchmark-consistency]
    deliv-error-budget:
      status: passed
      path: analysis/error_budget.md
      summary: "Systematic identification of modeling assumptions and their impact."
      linked_ids: [claim-energy-conservation]
  acceptance_tests:
    test-gw-benchmark-consistency:
      status: passed
      summary: "Verified reduction to sound shell model fitting function."
      linked_ids: [claim-benchmark-reproduction, deliv-gw-verification, Ref-Hindmarsh2015]
  references:
    Ref-Hindmarsh2015:
      status: completed
      completed_actions: [read, compare, cite]
      summary: "Used as the primary benchmark for the acoustic-dominated limit."
  forbidden_proxies:
    fp-gw-proxy:
      status: rejected
      notes: "Strict quantitative benchmark comparison was performed."

duration: 15min
completed: 2026-03-18
---

# Phase 01: Unified Formalism for GW Sources - Plan 02 Summary

**Verified the unified GW spectral density formula against limiting cases and established benchmarks, and documented the modeling error budget.**

## Performance

- **Duration:** 15 min
- **Started:** 2026-03-18T10:00:00Z
- **Completed:** 2026-03-18T10:15:00Z
- **Tasks:** 2
- **Files modified:** 1
- **Files created:** 1

## Key Results

- **Benchmark Reproduction [CONFIDENCE: HIGH]**: Unified formula $\Omega_{\text{GW}}(k)$ reduces to Sound Shell Model (SSM) in the acoustic limit ($\kappa_{\text{bub, turb}} \to 0$) and to the envelope approximation in the bubble collision limit ($\kappa_{\text{sw, turb}} \to 0$).
- **Energy Conservation [CONFIDENCE: HIGH]**: Integrated GW energy density satisfies $\rho_{\text{GW}} / \epsilon \ll 1$ (typically $10^{-7}$ for EWPT parameters).
- **UV Scaling [CONFIDENCE: MEDIUM]**: Late-time turbulence follows $k^{-11/3}$ UV scaling, consistent with Kolmogorov stationary turbulence.

## Task Commits

1. **Task 1: Verify limiting cases and reproduce benchmarks** - `ee6a33b` (derive)
2. **Task 2: Energy conservation check and error budget establishment** - `3942938` (document)

## Files Created/Modified

- `derivations/unified_gw_formalism.tex` - Added verification derivations for limiting cases.
- `analysis/error_budget.md` - Established the error budget and energy conservation analysis.

## Next Phase Readiness

- The unified analytical framework is now verified against known limits.
- Ready for Phase 02: Numerical implementation and comparison with full simulation results.

## Contract Coverage

- Claim IDs advanced:
    - `claim-benchmark-reproduction` -> passed
    - `claim-energy-conservation` -> passed
- Deliverable IDs produced:
    - `deliv-gw-verification` -> derivations/unified_gw_formalism.tex
    - `deliv-error-budget` -> analysis/error_budget.md
- Acceptance test IDs run:
    - `test-gw-benchmark-consistency` -> passed
- Reference IDs surfaced:
    - `Ref-Hindmarsh2015` -> completed_actions: [read, compare, cite]

## Equations Derived

**Eq. (01.3):**
\begin{equation}
    \rho_{GW} = \rho_c \int_{0}^{\infty} \Omega_{GW}(k) d\ln k \ll \epsilon
\end{equation}

**Eq. (01.4):**
\begin{equation}
    \Omega_{\text{GW}}(k) \to \Omega_{\text{sw}}(k) \approx 3 (H_* R_*) \left( \frac{\kappa_{\text{sw}} \alpha}{1 + \alpha} \right)^2 \tilde{\Omega}_{\text{sw}}(k) \Upsilon(t)
\end{equation}

## Validations Completed

- Checked reduction to Sound Shell Model (SSM) formula.
- Checked reduction to envelope approximation.
- Dimensional analysis of unified formula [dimensionless].
- Order-of-magnitude estimates for EWPT parameters ($f_p \sim 10^{-3}$ Hz).

## Decisions & Deviations

- None - followed plan as specified.

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---------------|------------|----------------|----------------|
| Linear Superposition | $v_w \gtrsim 0.61$ | $\sim 5\%$ | $v_w < 0.5$ (deflagrations) |
| Kolmogorov UV scaling | Stationary turbulence | High uncertainty | Early times, non-Kolmogorov regimes |

---
_Phase: 01-unified-formalism-for-gw-sources_
_Completed: 2026-03-18_
