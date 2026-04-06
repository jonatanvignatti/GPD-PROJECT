# Research Project Description

## Core Research Question
Explain the CMB angular power spectrum (C_ℓ) as a function of multipole moment ℓ using a particle physics model that connects CMB anisotropy to neutrino masses and beyond Standard Model (BSM) relics.

## Model Approach
- Focus on sterile neutrinos and general BSM physics
- Develop a model-agnostic framework to compute CMB power spectra
- Allow flexible parameter scanning of neutrino sector and BSM relic properties

## Computational Strategy
- Use CLASS/CAMB as a black-box Boltzmann solver
- Modify the code to accept custom neutrino/B
SM parameter inputs
- Validate against ΛCDM baseline before exploring BSM scenarios

## Key Signatures
- Deviations in damping tail shape, peak structure, or polarization spectra
- Anomalies in TE/EE/BB power spectra indicative of new physics

## Benchmarks for Validation
- Exact reproduction of Planck 2018 ΛCDM spectra within 1σ
- Consistency with BBN constraints and existing neutrino limits
- Cross-validation with independent Boltzmann codes

## Experimental Probes
- Planck 2018 temperature and polarization data
- ACT and SPT measurements for small-scale power
- Future CMB-S4 experiments for enhanced precision

## Timeline (Phased)
1. Framework setup and ΛCDM validation
2. Parameter scans for Neff and sterile neutrino properties
3. BSM relic effect exploration
4. Comparative analysis with observational datasets

## Required Artifacts
- .gpd/PROJECT.md project context
- .gpd/config.json workflow settings
- .gpd/REQUIREMENTS.md detailed requirements
- .gpd/ROADMAP.md phase structure
- .gpd/STATE.md project state tracking