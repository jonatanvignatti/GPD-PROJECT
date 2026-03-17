import numpy as np

# ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly-plus, fourier_convention=physics, gauge_choice=TT, coordinate_system=comoving-x-physical-t

def omega_bub(k, k_bub, alpha, beta_h, kappa_bub, v_w):
    """
    Bubble collision spectrum (Envelope Approximation).
    Ref: Huber & Konstandin (2008).
    """
    a_bub = (1.0 / beta_h)**2 * (kappa_bub * alpha / (1.0 + alpha))**2 * (v_w**3 / (0.42 + v_w**2))
    # S_bub(k/k_bub) fitting formula
    # Omega_bub(k) ~ a_bub * 3.8 * (k/k_bub)^2.8 / (1 + 2.8 * (k/k_bub)^3.8)
    # Note: derivations/unified_gw_formalism.tex Eq (01.3)
    s_bub = 3.8 * (k / k_bub)**2.8 / (1.0 + 2.8 * (k / k_bub)**3.8)
    return a_bub * s_bub

def omega_sw(k, k_sw, alpha, h_r_star, kappa_sw, tau_sw_h):
    """
    Sound wave spectrum (Sound Shell Model).
    Ref: Hindmarsh et al. (2015, 2017, 2019).
    """
    # A_sw = 3 * (H_* R_*) * (kappa_sw * alpha / (1 + alpha))^2
    a_sw = 3.0 * h_r_star * (kappa_sw * alpha / (1.0 + alpha))**2
    
    # Suppression factor Upsilon = min(1, H_* tau_sw)
    upsilon = min(1.0, tau_sw_h)
    
    # Spectral shape from Hindmarsh (2019)
    # tilde_Omega_sw(k) = (k/k_p)^3 * (7 / (4 + 3 * (k/k_p)^2))^3.5
    kp = k_sw
    s_sw = (k / kp)**3 * (7.0 / (4.0 + 3.0 * (k / kp)**2))**3.5
    
    return a_sw * s_sw * upsilon

def omega_turb(k, k_turb, alpha, h_r_star, kappa_turb, h_star):
    """
    Turbulence spectrum (Kolmogorov).
    Ref: Caprini et al. (2016).
    """
    # A_turb = 3 * (H_* R_*) * (kappa_turb * alpha / (1 + alpha))^(3/2)
    a_turb = 3.0 * h_r_star * (kappa_turb * alpha / (1.0 + alpha))**1.5
    
    # Spectral shape: (k/k_turb)^3 / [(1 + k/k_turb)^(11/3) * (1 + 8*pi*k/H_*)]
    s_turb = (k / k_turb)**3 / ((1.0 + k / k_turb)**(11.0/3.0) * (1.0 + 8.0 * np.pi * k / h_star))
    
    return a_turb * s_turb

def omega_gw_total(k, params):
    """
    Unified GW spectral density formula.
    """
    # params is a dictionary containing all necessary constants
    k_bub = params.get('k_bub')
    k_sw = params.get('k_sw')
    k_turb = params.get('k_turb')
    alpha = params.get('alpha')
    beta_h = params.get('beta_h')
    h_r_star = params.get('h_r_star')
    kappa_bub = params.get('kappa_bub', 0.0)
    kappa_sw = params.get('kappa_sw', 0.0)
    kappa_turb = params.get('kappa_turb', 0.0)
    v_w = params.get('v_w')
    tau_sw_h = params.get('tau_sw_h', 1.0)
    h_star = params.get('h_star', 1.0) # Hubble rate at transition (often set to 1 in k/H_* units)

    res = np.zeros_like(k, dtype=float)
    if kappa_bub > 0:
        res += omega_bub(k, k_bub, alpha, beta_h, kappa_bub, v_w)
    if kappa_sw > 0:
        res += omega_sw(k, k_sw, alpha, h_r_star, kappa_sw, tau_sw_h)
    if kappa_turb > 0:
        res += omega_turb(k, k_turb, alpha, h_r_star, kappa_turb, h_star)
        
    return res
