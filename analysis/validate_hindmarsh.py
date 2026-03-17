import numpy as np
import matplotlib.pyplot as plt
import os
from analysis.gw_spectrum import omega_sw, redshift_to_observer

def kappa_sw_benchmark(alpha, v_w):
    """
    Simplified efficiency factor for sound waves.
    Ref: Espinosa et al. (2010).
    """
    # Just a fit to have consistent values for benchmarks
    if v_w > 0.9: # Detonations
        return alpha / (0.73 + 0.083 * np.sqrt(alpha) + alpha)
    else: # Deflagrations
        return alpha**0.5 / (0.2 + alpha**0.5) # Rough estimate

def run_validation():
    v_w_list = [0.5, 0.92]
    alpha_list = [0.01, 0.05, 0.1]
    h_r_star = 0.1
    
    k = np.logspace(-1, 4, 200)
    
    plt.figure(figsize=(10, 6))
    
    for v_w in v_w_list:
        for alpha in alpha_list:
            kappa = kappa_sw_benchmark(alpha, v_w)
            k_p = 2.0 / h_r_star # Benchmark peak frequency
            
            # Source spectrum
            omega = omega_sw(k, k_p, alpha, h_r_star, kappa, tau_sw_h=1.0)
            
            # Peak amplitude from Eq (34) Hindmarsh (2015) - source frame
            # Omega_peak = 3 * (H_* R_*) * (kappa_sw * alpha / (1 + alpha))^2 * s_sw(k_p)
            # s_sw(k_p) = (1)^3 * (7 / (4 + 3))^3.5 = 1.0
            omega_peak_expected = 3.0 * h_r_star * (kappa * alpha / (1.0 + alpha))**2
            omega_peak_actual = np.max(omega)
            
            rel_diff = abs(omega_peak_actual - omega_peak_expected) / omega_peak_expected
            print(f"v_w={v_w}, alpha={alpha}: Peak Amp Diff = {rel_diff:.4%}")
            
            # Peak frequency check
            k_p_actual = k[np.argmax(omega)]
            rel_diff_k = abs(k_p_actual - k_p) / k_p
            print(f"v_w={v_w}, alpha={alpha}: Peak Freq Diff = {rel_diff_k:.4%}")
            
            label = f"$v_w={v_w}, \\alpha={alpha}$"
            plt.loglog(k, omega, label=label)
            
    plt.xlabel("$k/H_*$")
    plt.ylabel("$\\Omega_{GW}(k)$")
    plt.title("GW Spectrum Benchmark Validation (Hindmarsh 2015)")
    plt.grid(True, which="both", alpha=0.3)
    plt.legend()
    
    os.makedirs("data/benchmarks", exist_ok=True)
    plt.savefig("data/benchmarks/hindmarsh_comparison.pdf")
    print("\nSaved comparison plot to data/benchmarks/hindmarsh_comparison.pdf")

if __name__ == "__main__":
    run_validation()
