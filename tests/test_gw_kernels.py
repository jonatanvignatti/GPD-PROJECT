import sys
import os
import numpy as np

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analysis.gw_spectrum import omega_gw_total, redshift_to_observer

def test_ir_slope():
    """
    Check k^3 scaling for k << k_p.
    """
    params = {
        'k_bub': 100.0,
        'k_sw': 100.0,
        'k_turb': 100.0,
        'alpha': 0.1,
        'beta_h': 100.0,
        'h_r_star': 0.1,
        'kappa_bub': 0.0,
        'kappa_sw': 0.1, # Sound waves have exact k^3 in my implementation
        'kappa_turb': 0.0,
        'v_w': 0.9,
        'tau_sw_h': 1.0,
        'h_star': 1.0
    }
    
    k1 = 0.01
    k2 = 0.02
    omega1 = omega_gw_total(np.array([k1]), params)[0]
    omega2 = omega_gw_total(np.array([k2]), params)[0]
    
    slope = np.log(omega2 / omega1) / np.log(k2 / k1)
    print(f"IR Slope (Sound Waves): {slope:.3f}")
    assert np.abs(slope - 3.0) < 0.1
    
    # Check Bubble kernel IR slope
    params['kappa_sw'] = 0.0
    params['kappa_bub'] = 0.1
    omega1 = omega_gw_total(np.array([k1]), params)[0]
    omega2 = omega_gw_total(np.array([k2]), params)[0]
    slope = np.log(omega2 / omega1) / np.log(k2 / k1)
    print(f"IR Slope (Bubbles): {slope:.3f}")
    # Derivation says 2.8 for the envelope approximation formula used.
    assert np.abs(slope - 2.8) < 0.1

def test_uv_slope():
    """
    Check mechanism-specific UV decay rates.
    """
    params = {
        'k_bub': 1.0,
        'k_sw': 1.0,
        'k_turb': 1.0,
        'alpha': 0.1,
        'beta_h': 100.0,
        'h_r_star': 0.1,
        'kappa_bub': 0.1,
        'kappa_sw': 0.0,
        'kappa_turb': 0.0,
        'v_w': 0.9,
        'tau_sw_h': 1.0,
        'h_star': 1.0
    }
    
    k1 = 100.0
    k2 = 200.0
    
    # Bubble UV Slope: k^{2.8} / k^{3.8} = k^{-1}
    omega1 = omega_gw_total(np.array([k1]), params)[0]
    omega2 = omega_gw_total(np.array([k2]), params)[0]
    slope = np.log(omega2 / omega1) / np.log(k2 / k1)
    print(f"UV Slope (Bubbles): {slope:.3f}")
    assert np.abs(slope - (-1.0)) < 0.1
    
    # Sound Wave UV Slope: k^3 / k^7 = k^{-4}
    params['kappa_bub'] = 0.0
    params['kappa_sw'] = 0.1
    omega1 = omega_gw_total(np.array([k1]), params)[0]
    omega2 = omega_gw_total(np.array([k2]), params)[0]
    slope = np.log(omega2 / omega1) / np.log(k2 / k1)
    print(f"UV Slope (Sound Waves): {slope:.3f}")
    assert np.abs(slope - (-4.0)) < 0.1
    
    # Turbulence UV Slope: k^3 / (k^{11/3} * k) = k^{-5/3}
    params['kappa_sw'] = 0.0
    params['kappa_turb'] = 0.1
    omega1 = omega_gw_total(np.array([k1]), params)[0]
    omega2 = omega_gw_total(np.array([k2]), params)[0]
    slope = np.log(omega2 / omega1) / np.log(k2 / k1)
    print(f"UV Slope (Turbulence): {slope:.3f}")
    assert np.abs(slope - (-5.0/3.0)) < 0.1

def test_limits():
    """
    Verify single-source limits.
    """
    params = {
        'k_bub': 10.0,
        'k_sw': 10.0,
        'k_turb': 10.0,
        'alpha': 0.1,
        'beta_h': 100.0,
        'h_r_star': 0.1,
        'kappa_bub': 0.1,
        'kappa_sw': 0.1,
        'kappa_turb': 0.1,
        'v_w': 0.9,
        'tau_sw_h': 1.0,
        'h_star': 1.0
    }
    k = np.array([10.0])
    
    # Total
    omega_tot = omega_gw_total(k, params)[0]
    
    # Individual
    params_bub = params.copy(); params_bub['kappa_sw'] = 0; params_bub['kappa_turb'] = 0
    omega_bub_val = omega_gw_total(k, params_bub)[0]
    
    params_sw = params.copy(); params_sw['kappa_bub'] = 0; params_sw['kappa_turb'] = 0
    omega_sw_val = omega_gw_total(k, params_sw)[0]
    
    params_turb = params.copy(); params_turb['kappa_bub'] = 0; params_turb['kappa_sw'] = 0
    omega_turb_val = omega_gw_total(k, params_turb)[0]
    
    assert np.abs(omega_tot - (omega_bub_val + omega_sw_val + omega_turb_val)) < 1e-15

def test_redshift():
    """
    Check redshifting benchmarks from 02-RESEARCH.md.
    """
    # For T_*=100 GeV, g_*=100, and f_*/H_*=10, verify f \approx 1.65 \times 10^{-4} Hz.
    # f_*/H_* = k / (2*pi) = 10 => k = 20*pi
    k = 20.0 * np.pi
    omega_source = 1e-5
    t_star = 100.0
    g_star = 100.0
    
    f_obs, omega_h2 = redshift_to_observer(k, omega_source, t_star, g_star)
    
    # Frequency check
    print(f"Redshifted Frequency: {f_obs:.4e} Hz")
    assert np.abs(f_obs / 1.65e-4 - 1.0) < 0.01
    
    # Energy Density check
    # Omega_GW h^2 \approx 1.67 \times 10^{-10}
    print(f"Redshifted Omega h^2: {omega_h2:.4e}")
    assert np.abs(omega_h2 / 1.67e-10 - 1.0) < 0.01

if __name__ == "__main__":
    try:
        test_ir_slope()
        test_uv_slope()
        test_limits()
        test_redshift()
        print("All tests PASSED.")
    except Exception as e:
        print(f"Tests FAILED: {e}")
        sys.exit(1)
