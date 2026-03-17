import numpy as np

def calculate_ratios(T_star=100, v_w=0.5, alpha=0.1, cs=1/np.sqrt(3)):
    # Efficiency factor for sound waves (approximate)
    kappa_v = alpha / (0.73 + 0.083 * np.sqrt(alpha) + alpha) # approximate formula for detonation/strong transitions
    # RMS fluid velocity
    U_f = np.sqrt(3/4 * kappa_v * alpha / (1 + alpha))
    
    # beta/H ratio (typically 10-1000)
    beta_H = 100
    
    # Bubble radius at collision
    R_star = (8*np.pi)**(1/3) * v_w / (beta_H) # in Hubble units
    
    # Sound shell thickness approximation: Delta R / R_star
    # For deflagrations (v_w < cs), Delta R / R_star is large.
    # For detonations (v_w > cs), Delta R / R_star ~ (v_w - cs)/v_w ?
    # Let's use the plan's criterion: Delta R / R_star < 0.1
    
    delta_R_R = abs(v_w - cs) / v_w
    
    # Cross-term ratio estimation
    # Assume cross-terms scale as U_f^2 / v_w^2 ? No.
    # Actually, the cross-terms are negligible if the durations are separated.
    # tau_sw / H^{-1} = R_star / U_f
    tau_sw_H = R_star / U_f
    
    # If tau_sw_H >> beta_H^{-1}, then sound waves dominate over bubble collisions.
    # Bubble collision duration ~ beta_H^{-1}
    # Sound wave duration ~ tau_sw_H
    
    cross_term_ratio = (1/beta_H) / tau_sw_H
    
    return {
        "delta_R_R": delta_R_R,
        "cross_term_ratio": cross_term_ratio,
        "U_f": U_f,
        "R_star": R_star,
        "tau_sw_H": tau_sw_H
    }

if __name__ == "__main__":
    benchmark = calculate_ratios(T_star=100, v_w=0.5, alpha=0.1)
    print(f"Benchmark ratios: {benchmark}")
    
    # Check criteria
    print(f"Delta R/R < 0.1: {benchmark['delta_R_R'] < 0.1}")
    print(f"Cross-term ratio < 0.05: {benchmark['cross_term_ratio'] < 0.05}")

    # Let's try v_w = 0.9 (detonation)
    detonation = calculate_ratios(T_star=100, v_w=0.9, alpha=0.1)
    print(f"Detonation (v_w=0.9) ratios: {detonation}")
