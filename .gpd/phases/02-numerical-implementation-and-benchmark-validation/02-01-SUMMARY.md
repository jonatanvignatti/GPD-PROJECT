---
phase: 02-numerical-implementation-and-benchmark-validation
plan: 01
depth: full
provides:
  - deliv-gw-spectrum-lib
  - deliv-gw-tests
completed: 2026-03-18
one-liner: "Implemented unified GW spectral density library and verified IR/UV slopes and redshifting logic."
subsystem: [computation, validation]
tags: [gravitational-waves, sound-shell-model, redshifting, numerical-implementation]
requires:
  - phase: 01-unified-formalism-for-gw-sources
    provides: [unified GW spectrum formula]
affects: [02-02-PLAN.md]
methods:
  added: [Numerical implementation of GW source kernels, Redshifting transformation to observer frame]
  patterns: [Vectorized spectral evaluation in NumPy, Systematic IR/UV slope verification]
key-files:
  created: [analysis/gw_spectrum.py, tests/test_gw_kernels.py]
conventions:
  - "metric = (-+++)"
  - "natural units (hbar=c=k_B=1)"
  - "Physics Fourier convention"
plan_contract_ref: ".gpd/phases/02-numerical-implementation-and-benchmark-validation/02-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-kernel-consistency:
      status: passed
      summary: "Implemented kernels reproduce IR k^3 (or fitting equivalent) and mechanism-specific UV slopes (p=1, 4, 5/3)."
      linked_ids: [deliv-gw-spectrum-lib, deliv-gw-tests, test-uv-ir-slopes]
      evidence:
        - verifier: gpd-executor
          method: slope extraction via numerical differentiation
          confidence: high
          claim_id: claim-kernel-consistency
          deliverable_id: deliv-gw-tests
          acceptance_test_id: test-uv-ir-slopes
          evidence_path: "tests/test_gw_kernels.py"
    claim-redshift-accuracy:
      status: passed
      summary: "Observer-frame frequency and Omega_GW h^2 match research benchmarks within 1%."
      linked_ids: [deliv-gw-spectrum-lib, test-redshift-check]
      evidence:
        - verifier: gpd-executor
          method: benchmark comparison (T_*=100 GeV)
          confidence: high
          claim_id: claim-redshift-accuracy
          deliverable_id: deliv-gw-spectrum-lib
          acceptance_test_id: test-redshift-check
          evidence_path: "tests/test_gw_kernels.py"
  deliverables:
    deliv-gw-spectrum-lib:
      status: passed
      path: "analysis/gw_spectrum.py"
      summary: "Python library with kernels and redshift logic."
    deliv-gw-tests:
      status: passed
      path: "tests/test_gw_kernels.py"
      summary: "Pytest-compatible test suite for physical consistency."
  acceptance_tests:
    test-uv-ir-slopes:
      status: passed
      summary: "IR slope ~3, UV slopes ~ -1, -4, -1.67 verified."
    test-single-source-limit:
      status: passed
      summary: "Summing individual kernels matches total spectrum."
    test-redshift-check:
      status: passed
      summary: "Frequency and amplitude redshifted correctly for 100 GeV benchmark."
  references:
    Ref-Hindmarsh2015:
      status: completed
      completed_actions: [read, use]
      summary: "Used for sound wave kernel spectral shape and normalization benchmarks."
---

# Phase 02: Numerical Implementation Summary

**Implemented unified GW spectral density library and verified IR/UV slopes and redshifting logic.**

## Performance

- **Duration:** 15 min
- **Started:** 2026-03-18T10:00:00Z
- **Completed:** 2026-03-18T10:15:00Z
- **Tasks:** 3
- **Files modified:** 2

## Key Results

- Created `analysis/gw_spectrum.py` containing vectorized implementations of bubble, sound wave, and turbulence kernels.
- Verified IR causality limit ($\Omega \sim k^3$) and mechanism-specific UV decay ($k^{-1}, k^{-4}, k^{-5/3}$).
- Validated redshifting transformation against research benchmarks ($f \approx 1.65 \times 10^{-4}$ Hz for 100 GeV transition).

## Task Commits

1. **Task 1: Implement Spectral Kernels** - `3cb1b65` (implement source kernels)
2. **Task 2: Implement Redshifting** - `b795298` (add redshift_to_observer)
3. **Task 3: Unit Testing** - `cf1d887` (physical limit verification)

## Files Created/Modified

- `analysis/gw_spectrum.py` - Core numerical library for GW spectra.
- `tests/test_gw_kernels.py` - Unit test suite for verifying implementation.

## Next Phase Readiness

The core numerical engine is ready for the benchmark validation sweep (Plan 02-02).

## Equations Implemented

**Eq. (02.1):**
$$ \Omega_{\text{bub}}(k) \approx \mathcal{A}_{\text{bub}} \frac{3.8 (k/k_p)^{2.8}}{1 + 2.8 (k/k_p)^{3.8}} $$

**Eq. (02.2):**
$$ \tilde{\Omega}_{\text{sw}}(k) \approx (k/k_p)^3 \left( \frac{7}{4 + 3 (k/k_p)^2} \right)^{7/2} $$

**Eq. (02.3):**
$$ \Omega_{\text{turb}}(k) \approx \mathcal{A}_{\text{turb}} \frac{(k/k_{\text{turb}})^3}{[1 + (k/k_{\text{turb}})]^{11/3} (1 + 8\pi k / H_*)} $$

## Validations Completed

- **IR Slope Check:** Sound waves and turbulence show exact $k^3$ scaling. Bubble fitting formula shows $k^{2.8}$.
- **UV Slope Check:** Bubbles ($k^{-1}$), Sound Waves ($k^{-4}$), Turbulence ($k^{-1.64} \approx -5/3$).
- **Redshift Benchmarks:** Frequencies and amplitudes match analytic formulas from `02-RESEARCH.md` within 0.1%.

## Decisions & Deviations

- **Decision:** Used the Hindmarsh (2019) fitting formula for sound waves as it is the current numerical standard for the SSM.
- **Decision:** Implemented redshifting assuming standard radiation dominance, consistent with the project scope.

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source |
| -------- | ------ | ----- | ----------- | ------ |
| Bubble Peak Power | $s_{bub}(k_p)$ | 1.0 | N/A | Normalization |
| Sound Wave Peak Power | $s_{sw}(k_p)$ | 1.0 | N/A | Normalization |
| Turbulence peak factor | $s_{turb}(k_p)$ | ~0.1 | N/A | Fitting function |

---

_Phase: 02-numerical-implementation-and-benchmark-validation_
_Completed: 2026-03-18_
