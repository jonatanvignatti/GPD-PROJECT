import numpy as np
import csv
import os
from analysis.gw_spectrum import omega_gw_total, redshift_to_observer

# Conventions
T_STAR = 100.0  # GeV
G_STAR = 106.75
HR_STAR = 0.1   # Mean bubble separation H_* R_*
BETA_H = 100.0  # beta/H_*

# Grid
v_w_grid = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
alpha_grid = [0.01, 0.03, 0.1, 0.3, 0.6, 1.0]
models = ['SSM', 'Bub', 'Mixed']

# Frequency grid (observer frame)
f_obs_grid = np.logspace(-9, 3, 12 * 100)  # 100 points per decade

def run_sweep():
    results = []
    raw_spectra = {}

    for v_w in v_w_grid:
        for alpha in alpha_grid:
            for model in models:
                # Setup parameters
                params = {
                    'alpha': alpha,
                    'v_w': v_w,
                    'beta_h': BETA_H,
                    'h_r_star': HR_STAR,
                    'tau_sw_h': 1.0,  # Assume long-lived sound waves for sensitivity baseline
                    'h_star': 1.0,
                    'k_bub': 100.0,   # k_p / H_* roughly beta/v_w
                    'k_sw': 100.0,
                    'k_turb': 100.0
                }
                
                # Model efficiency factors
                if model == 'SSM':
                    params['kappa_sw'] = 0.5 # Representative
                    params['kappa_bub'] = 0.0
                    params['kappa_turb'] = 0.0
                elif model == 'Bub':
                    params['kappa_sw'] = 0.0
                    params['kappa_bub'] = 0.5
                    params['kappa_turb'] = 0.0
                elif model == 'Mixed':
                    params['kappa_sw'] = 0.8 * 0.5
                    params['kappa_bub'] = 0.1 * 0.5
                    params['kappa_turb'] = 0.1 * 0.5

                # Compute source-frame spectrum
                # We need a k-grid that maps to our f_obs_grid
                # f_obs = 1.65e-5 * (k / 2pi) * (T/100) * (g/100)^(1/6)
                # k = f_obs / (1.65e-5 * (1/2pi) * (T/100) * (g/100)^(1/6))
                redshift_factor_f = 1.65e-5 * (1.0 / (2.0 * np.pi)) * (T_STAR / 100.0) * (G_STAR / 100.0)**(1.0/6.0)
                k_grid = f_obs_grid / redshift_factor_f
                
                omega_source = omega_gw_total(k_grid, params)
                
                # Redshift to observer
                _, omega_h2 = redshift_to_observer(k_grid, omega_source, T_STAR, G_STAR)
                
                # Store raw
                key = f"v{v_w}_a{alpha}_{model}"
                raw_spectra[key] = omega_h2
                
                # Peak Extraction (Task 2)
                idx_max = np.argmax(omega_h2)
                if 0 < idx_max < len(omega_h2) - 1:
                    # Surrounding points in log-log
                    x = np.log(f_obs_grid[idx_max-1:idx_max+2])
                    y = np.log(omega_h2[idx_max-1:idx_max+2])
                    
                    # Fit parabola y = ax^2 + bx + c
                    poly = np.polyfit(x, y, 2)
                    a, b, c = poly
                    
                    # Vertex x_p = -b / (2a)
                    x_p = -b / (2.0 * a)
                    f_p = np.exp(x_p)
                    omega_p = np.exp(a * x_p**2 + b * x_p + c)
                else:
                    f_p = f_obs_grid[idx_max]
                    omega_p = omega_h2[idx_max]
                
                results.append({
                    'v_w': v_w,
                    'alpha': alpha,
                    'model': model,
                    'f_p': f_p,
                    'omega_p': omega_p
                })

    # Save CSV
    os.makedirs('results', exist_ok=True)
    with open('results/peak_trajectories.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['v_w', 'alpha', 'model', 'f_p', 'omega_p'])
        writer.writeheader()
        writer.writerows(results)
    
    # Save Raw (npz)
    np.savez('results/raw_spectra.npz', f_obs=f_obs_grid, **raw_spectra)
    print(f"Sweep complete. 180 configurations saved. Peak positions in results/peak_trajectories.csv")

if __name__ == "__main__":
    run_sweep()
