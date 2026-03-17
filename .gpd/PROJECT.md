# Gravitational Radiation from First-Order Phase Transitions

## What This Is

Construct and compare improved GW spectra for electroweak first-order phase transitions by consistently combining bubble collisions, sound waves, and turbulence, and quantify how modeling assumptions (wall velocity, sound shell model) move the signal in the (f, ω_GW) plane.

## Core Research Question

How do different modeling assumptions for electroweak first-order phase transitions move the GW signal in the (f, ω_GW) plane?

## Scoping Contract Summary

### Contract Coverage

- Consistent combination of bubble collisions, sound waves, and turbulence in GW spectra
- Acceptance signal: Comparison plots showing signal movement in (f, ω_GW) plane
- False progress to reject: Qualitative agreement without rigorous benchmark comparison

### User Guidance To Preserve

- **User-stated observables:** GW Spectra (f, ω_GW)
- **User-stated deliverables:** Code for generating improved GW spectra, comparison plots (LISA/PTA/post-merger), and a new analytical formula
- **Must-have references / prior outputs:** Hindmarsh et al. (2015)
- **Stop / rethink conditions:** Inconsistent results compared to benchmark (Hindmarsh 2015)

### Scope Boundaries

**In scope**

- Consistent combination of bubble collisions, sound waves, and turbulence in GW spectra
- Propagation to present-day observables (LISA/PTA/post-merger detectors)
- Testing of wall velocity and sound shell model assumptions
- Comparison with prior benchmarks (e.g., Hindmarsh et al. 2015)

**Out of scope**

- Experimental detection (LISA, PTA)
- Non-electroweak phase transitions
- Gravitational wave background from other sources

### Active Anchor Registry

- Hindmarsh 2015: Hindmarsh et al., Phys. Rev. D 92, 123009 (2015)
  - Why it matters: Primary published comparison target
  - Carry forward: planning | execution | verification | writing
  - Required action: read | compare | cite

### Carry-Forward Inputs

- None confirmed yet.

### Skeptical Review

- **Weakest anchor:** Turbulence decay rates
- **Unvalidated assumptions:** Wall velocity modeling, Sound shell approximations
- **Competing explanation:** None yet.
- **Disconfirming observation:** Signal moving unexpectedly outside (f, ω_GW) plane benchmarks
- **False progress to reject:** Qualitative trend match without the decisive benchmark comparison

### Open Contract Questions

- Which specific sound shell model to prioritize?
- Which turbulence decay rates to consider?

## Research Questions

### Answered

(None yet — investigate to answer)

### Active

- [ ] [ANAL-01] Derive improved GW spectra combining bubble collisions, sound waves, and turbulence
- [ ] [ANAL-02] Establish new analytical formula for the improved GW spectrum
- [ ] [NUMR-01] Implement code to compute GW spectra and compare with benchmarks
- [ ] [NUMR-02] Quantify signal movement in (f, ω_GW) plane under different modeling assumptions

### Out of Scope

- [Question 1] — Experimental detection (LISA, PTA)

## Research Context

### Physical System

Electroweak phase transition in the early universe.

### Theoretical Framework

Cosmological first-order phase transitions and gravitational wave production.

### Key Parameters and Scales

| Parameter | Symbol | Regime  | Notes   |
| --------- | ------ | ------- | ------- |
| Wall velocity | v_w | [0, 1] | modeling assumption |
| Sound shell model | - | - | modeling assumption |

### Known Results

- Hindmarsh 2015 — Hindmarsh et al., Phys. Rev. D 92, 123009 (2015)

### What Is New

Consistent combination of all three sources (bubbles, sound, turbulence) and quantification of modeling assumption impacts on signal position.

### Target Venue

Physical Review D or Journal of Cosmology and Astroparticle Physics.

### Computational Environment

Local workstation or cluster for numerical integrations.

## Notation and Conventions

See .gpd/CONVENTIONS.md for all notation and sign conventions.

## Unit System

Natural units (ħ = c = k_B = 1).

## Requirements

See .gpd/REQUIREMENTS.md for the detailed requirements specification.

## Key References

- Hindmarsh 2015: Hindmarsh et al., Phys. Rev. D 92, 123009 (2015)

## Constraints

- **Accuracy**: Result should agree with benchmarks in appropriate limits.

## Key Decisions

| Decision                                    | Rationale              | Outcome   |
| ------------------------------------------- | ---------------------- | --------- |
| Minimal initialization — defer deep scoping | Fast project bootstrap | — Pending |

---

_Last updated: 2026-03-16 after initialization_
