import numpy as np
import os
from analysis.gw_spectrum import omega_gw_total

def run_convergence_study():
    # Benchmark parameters (v_w=0.92, alpha=0.01, H_* R_* = 0.1)
    params = {
        'k_bub': 10.0, # Approximate for v_w=0.92
        'k_sw': 20.0,  # k_p ~ 2 / R_* = 2 / 0.1 = 20
        'k_turb': 20.0,
        'alpha': 0.01,
        'beta_h': 100.0,
        'h_r_star': 0.1,
        'kappa_bub': 0.0,
        'kappa_sw': 0.01, # Example value
        'kappa_turb': 0.0,
        'v_w': 0.92,
        'tau_sw_h': 1.0,
        'h_star': 1.0
    }

    n_k_values = [50, 100, 200, 400]
    results = {}

    k_min = 1e-1
    k_max = 1e4

    for n_per_decade in n_k_values:
        n_decades = np.log10(k_max / k_min)
        num_points = int(n_per_decade * n_decades)
        k_grid = np.logspace(np.log10(k_min), np.log10(k_max), num_points)
        
        omega = omega_gw_total(k_grid, params)
        
        # Integration I = int Omega d(ln k)
        ln_k = np.log(k_grid)
        integral = np.trapezoid(omega, ln_k)
        results[n_per_decade] = integral
        print(f"N_k={n_per_decade}: I = {integral:.6e}")

    # Relative errors
    ref_val = results[400]
    print("\nRelative Errors (w.r.t. N_k=400):")
    error_summary = []
    for n in n_k_values:
        rel_err = abs(results[n] - ref_val) / ref_val
        print(f"N_k={n}: {rel_err:.4%}")
        error_summary.append((n, results[n], rel_err))
        
    return error_summary

if __name__ == "__main__":
    run_convergence_study()
