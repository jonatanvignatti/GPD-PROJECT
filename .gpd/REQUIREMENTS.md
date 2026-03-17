# Requirements: Gravitational Radiation from First-Order Phase Transitions

**Defined:** 2026-03-17
**Core Research Question:** How do different modeling assumptions for electroweak first-order phase transitions move the GW signal in the (f, ω_GW) plane?

## Primary Requirements

### Analytical Derivations

- [ ] **ANAL-01**: Derive improved GW spectra combining bubble collisions, sound waves, and turbulence
- [ ] **ANAL-02**: Establish new analytical formula for the improved GW spectrum

### Numerical Validations

- [ ] **NUMR-01**: Implement code to compute GW spectra and compare with benchmarks
- [ ] **NUMR-02**: Quantify signal movement in (f, ω_GW) plane under different modeling assumptions

## Follow-up Requirements

### Extended Analysis

- **EXTD-01**: Study effect of turbulence decay rates on GW spectra
- **EXTD-02**: Incorporate non-electroweak phase transition scenarios

## Out of Scope

| Topic                     | Reason                                                           |
| ------------------------- | ---------------------------------------------------------------- |
| Experimental detection    | Outside the scope of theoretical modeling and benchmark comparison|

## Accuracy and Validation Criteria

| Requirement | Accuracy Target                         | Validation Method                      |
| ----------- | --------------------------------------- | -------------------------------------- |
| ANAL-01     | Exact analytic result                   | Check limiting cases and symmetries    |
| NUMR-01     | Reasonable agreement with benchmarks    | Direct comparison with Hindmarsh (2015)|

## Contract Coverage

| Requirement | Decisive Output / Deliverable | Anchor / Benchmark / Reference | Prior Inputs / Baselines | False Progress To Reject |
| ----------- | ----------------------------- | ------------------------------ | ------------------------ | ------------------------ |
| ANAL-01     | New analytical formula        | Hindmarsh (2015)               | -                        | Qualitative agreement    |
| NUMR-01     | Code & comparison plots       | Hindmarsh (2015)               | -                        | Qualitative agreement    |

## Traceability

| Requirement | Phase                                        | Status  |
| ----------- | -------------------------------------------- | ------- |
| ANAL-01     | Phase 1: Unified Formalism for GW Sources    | Pending |
| ANAL-02     | Phase 1: Unified Formalism for GW Sources    | Pending |
| NUMR-01     | Phase 2: Numerical Implementation            | Pending |
| NUMR-02     | Phase 3: Modeling Sensitivity                | Pending |

**Coverage:**

- Primary requirements: 4 total
- Mapped to phases: 4
- Unmapped: 0

---

_Requirements defined: 2026-03-17_
