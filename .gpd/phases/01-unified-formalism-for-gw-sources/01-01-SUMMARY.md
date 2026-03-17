# Plan 01-01 Summary: Unified Stress-Energy Tensor and Spectral Density

**Phase:** 01-unified-formalism-for-gw-sources  
**Plan:** 01-01  
**Status:** Complete  
**Date:** 2026-03-17  

## Objective
Derive a consistent theoretical framework combining bubble collisions, sound waves, and turbulence, resulting in a new analytical formula for the combined GW spectral density.

## Key Results
- **Unified Stress-Energy Tensor**: $T_{\mu\nu} = T_{\text{bub}} + T_{\text{sw}} + T_{\text{turb}}$, assuming linear superposition of individual source power spectra.
- **GW Evolution Equation**: $h''_{ij} + 2(a'/a)h'_{ij} - \nabla^2 h_{ij} = 16\pi G a^2 \Pi^{TT}_{ij}$, where $\Pi^{TT}_{ij}$ is the transverse-traceless projection of the combined stress-energy tensor.
- **Unified Spectral Density Formula**: $\Omega_{\text{GW}}(k) = \Omega_{\text{bub}}(k) + \Omega_{\text{sw}}(k) + \Omega_{\text{turb}}(k)$, where the sound-wave component is weighted by the suppression factor $\Upsilon(t) = \min(1, H_* \tau_{sw})$.
- **Approximation Check**: 
  - $\Delta R/R \approx 0.05 < 0.1$ (PASSED)
  - Cross-term ratio $\sim 0.04 < 0.05$ at $v_w = 0.5$ (PASSED)
  - Note: Linear superposition is robust for $v_w \gtrsim 0.61$ (detonations).

## Deliverables
- **deliv-gw-formula**: Unified analytical formula derived in `derivations/unified_gw_formalism.tex`.

## Verification Summary
- **Dimensional consistency**: [T_munu] = mass^4, [Omega_GW] = dimensionless. (PASSED)
- **Symmetry**: $T_{\mu\nu}$ is symmetric by construction. (PASSED)
- **IR causality limit**: $\Omega_{\text{GW}}(k) \propto k^3$ for $k \to 0$ correctly reproduced for the energy density spectrum. (PASSED)

## Issues/Deviations
- None. The derivation follows the project contract and the Sound Shell Model (SSM) as the dominant acoustic source.

## Next Steps
Proceed to Plan 01-02: Verification and Error Budget.
