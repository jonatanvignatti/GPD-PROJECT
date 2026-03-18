import csv
import json

import matplotlib.pyplot as plt
import numpy as np

# ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly-plus, fourier_convention=physics, coordinate_system=log-log-plane

def lisa_sensitivity(f):
    """Approximate LISA sensitivity curve (Omega_GW h^2)."""
    # Simple fitting function for LISA sensitivity
    # Ref: Robson et al. (2019) arXiv:1803.01944
    f_star = 19.09e-3
    L = 2.5e9
    P_oms = (1.5e-11)**2 * (1 + (2e-3/f)**4)
    P_acc = (3e-15)**2 * (1 + (0.4e-3/f)**2) * (1 + (f/8e-3)**4)
    
    S_n = (10/(3 * L**2)) * (P_oms + 4 * P_acc / (2 * np.pi * f)**4) * (1 + 0.6 * (f/f_star)**2)
    
    h2 = 0.7**2 # h=0.7
    H0 = 100 * 0.7 * 1e3 / 3.086e22 # H0 in SI units
    omega = (2 * np.pi**2 / (3 * H0**2)) * f**3 * S_n * h2
    return omega

def pta_sensitivity(f):
    """Rough PTA sensitivity region (Omega_GW h^2)."""
    # PTA is sensitive around 1e-9 to 1e-7 Hz
    # Typical limit is around 1e-10 in Omega_GW h^2
    # We'll use a simple V-shape for illustration
    center_f = 1e-8
    return 1e-10 * (f/center_f)**(-2) + 1e-10 * (f/center_f)**2

def load_csv(filepath):
    data = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                'v_w': float(row['v_w']),
                'alpha': float(row['alpha']),
                'model': row['model'],
                'f_p': float(row['f_p']),
                'omega_p': float(row['omega_p'])
            })
    return data

def main():
    # Load data
    data = load_csv('results/peak_trajectories.csv')
    
    # Load sensitivity matrix for annotations/checks
    with open('results/sensitivity_matrix.json', 'r') as f:
        sens_matrix = json.load(f)
        
    models = ['SSM', 'Bub', 'Mixed']
    colors = {'SSM': 'blue', 'Bub': 'red', 'Mixed': 'green'}
    markers = {0.01: 'o', 0.03: 's', 0.1: '^', 0.3: 'v', 0.6: 'D', 1.0: 'X'}
    
    alphas = sorted(list(set(d['alpha'] for d in data)))
    v_ws = sorted(list(set(d['v_w'] for d in data)))

    from matplotlib.backends.backend_pdf import PdfPages
    with PdfPages('results/displacement_maps.pdf') as pdf:
        # 1. Plot peak trajectories in the (f, Omega) plane
        plt.figure(figsize=(12, 8))
        for model in models:
            for alpha in alphas:
                m_a_data = [d for d in data if d['model'] == model and d['alpha'] == alpha]
                m_a_data.sort(key=lambda x: x['v_w'])
                
                if not m_a_data: continue
                
                f_p = [d['f_p'] for d in m_a_data]
                omega_p = [d['omega_p'] for d in m_a_data]
                
                label = f"{model} ($\\alpha={alpha}$)" if alpha == 1.0 else None
                plt.loglog(f_p, omega_p, color=colors[model], alpha=0.5, linestyle='--')
                plt.scatter(f_p, omega_p, color=colors[model], 
                            marker=markers[alpha], s=30, alpha=0.7, label=label)

        # Overlay sensitivity curves
        f_lisa = np.logspace(-5, 0, 100)
        plt.loglog(f_lisa, lisa_sensitivity(f_lisa), 'k-', alpha=0.8, label='LISA Sensitivity')
        
        f_pta = np.logspace(-10, -7, 50)
        plt.loglog(f_pta, pta_sensitivity(f_pta), 'k:', alpha=0.8, label='PTA (Est.)')
        
        plt.xlabel(r'Frequency $f$ [Hz]')
        plt.ylabel(r'$\Omega_{GW} h^2$')
        plt.title(r'GW Peak Displacement Map ($v_w \in [0.1, 0.95]$)')
        plt.grid(True, which="both", ls="-", alpha=0.2)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        pdf.savefig()
        plt.close()

        # 2. Vector field plot (drift as alpha increases)
        plt.figure(figsize=(10, 8))
        for model in models:
            for v_w in v_ws[::2]: # Sparsify for clarity
                v_data = [d for d in data if d['model'] == model and d['v_w'] == v_w]
                v_data.sort(key=lambda x: x['alpha'])
                
                if not v_data: continue
                
                f_p = np.array([d['f_p'] for d in v_data])
                omega_p = np.array([d['omega_p'] for d in v_data])
                
                plt.quiver(f_p[:-1], omega_p[:-1],
                           np.diff(f_p), np.diff(omega_p),
                           angles='xy', scale_units='xy', scale=1, color=colors[model], alpha=0.3)
                plt.loglog(f_p, omega_p, color=colors[model], alpha=0.2)
        
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel(r'Frequency $f$ [Hz]')
        plt.ylabel(r'$\Omega_{GW} h^2$')
        plt.title(r'Signal Drift Vectors (direction of increasing $\alpha$)')
        pdf.savefig()
        plt.close()

        # 3. Discrepancy plot
        plt.figure(figsize=(10, 6))
        for alpha in alphas:
            ssm_vals = [d['omega_p'] for d in data if d['model'] == 'SSM' and d['alpha'] == alpha]
            bub_vals = [d['omega_p'] for d in data if d['model'] == 'Bub' and d['alpha'] == alpha]
            
            # They should be sorted by v_w if data is sorted or we sort it here
            ssm_data = sorted([d for d in data if d['model'] == 'SSM' and d['alpha'] == alpha], key=lambda x: x['v_w'])
            bub_data = sorted([d for d in data if d['model'] == 'Bub' and d['alpha'] == alpha], key=lambda x: x['v_w'])
            
            ssm_omega = np.array([d['omega_p'] for d in ssm_data])
            bub_omega = np.array([d['omega_p'] for d in bub_data])
            
            if len(ssm_omega) == len(bub_omega) and len(ssm_omega) > 0:
                delta_omega = (ssm_omega - bub_omega) / ssm_omega
                plt.plot(v_ws, delta_omega, marker=markers[alpha], label=f'$\\alpha={alpha}$')
                
        plt.xlabel(r'Wall Velocity $v_w$')
        plt.ylabel(r'$(\Omega_{SSM} - \Omega_{Bub}) / \Omega_{SSM}$')
        plt.title(r'Relative Model Discrepancy (SSM vs Envelope)')
        plt.grid(True, alpha=0.3)
        plt.legend()
        pdf.savefig()
        plt.close()

    print("Displacement maps generated in results/displacement_maps.pdf")

if __name__ == "__main__":
    main()
