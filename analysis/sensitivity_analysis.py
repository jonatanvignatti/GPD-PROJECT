import math
import csv
import json
import os

def load_data(filepath):
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

def compute_jacobian(model_data):
    # Organize into grid
    v_ws = sorted(list(set(d['v_w'] for d in model_data)))
    alphas = sorted(list(set(d['alpha'] for d in model_data)))
    
    ln_v_w = [math.log(v) for v in v_ws]
    ln_alpha = [math.log(a) for a in alphas]
    
    # Initialize grids
    n_v = len(v_ws)
    n_a = len(alphas)
    grid_fp = [[0.0 for _ in range(n_a)] for _ in range(n_v)]
    grid_Op = [[0.0 for _ in range(n_a)] for _ in range(n_v)]
    
    for d in model_data:
        i = v_ws.index(d['v_w'])
        j = alphas.index(d['alpha'])
        grid_fp[i][j] = math.log(d['f_p'])
        grid_Op[i][j] = math.log(d['omega_p'])
    
    def derivative_1d(x, y, axis):
        n_v = len(y)
        n_a = len(y[0])
        grad = [[0.0 for _ in range(n_a)] for _ in range(n_v)]
        
        if axis == 0: # over v_w
            for i in range(1, n_v - 1):
                for j in range(n_a):
                    grad[i][j] = (y[i+1][j] - y[i-1][j]) / (x[i+1] - x[i-1])
            # Boundaries
            for j in range(n_a):
                grad[0][j] = (y[1][j] - y[0][j]) / (x[1] - x[0])
                grad[n_v-1][j] = (y[n_v-1][j] - y[n_v-2][j]) / (x[n_v-1] - x[n_v-2])
        else: # over alpha
            for i in range(n_v):
                for j in range(1, n_a - 1):
                    grad[i][j] = (y[i][j+1] - y[i][j-1]) / (x[j+1] - x[j-1])
                # Boundaries
                grad[i][0] = (y[i][1] - y[i][0]) / (x[1] - x[0])
                grad[i][n_a-1] = (y[i][n_a-1] - y[i][n_a-2]) / (x[n_a-1] - x[n_a-2])
        return grad

    J_vw_fp = derivative_1d(ln_v_w, grid_fp, 0)
    J_alpha_fp = derivative_1d(ln_alpha, grid_fp, 1)
    J_vw_Op = derivative_1d(ln_v_w, grid_Op, 0)
    J_alpha_Op = derivative_1d(ln_alpha, grid_Op, 1)
    
    return {
        'v_w': v_ws,
        'alpha': alphas,
        'J_vw_fp': J_vw_fp,
        'J_alpha_fp': J_alpha_fp,
        'J_vw_Op': J_vw_Op,
        'J_alpha_Op': J_alpha_Op
    }

def main():
    data = load_data('results/peak_trajectories.csv')
    
    results = {}
    for model in ['SSM', 'Bub', 'Mixed']:
        model_data = [d for d in data if d['model'] == model]
        if model_data:
            results[model] = compute_jacobian(model_data)
    
    # Save to JSON
    with open('results/sensitivity_matrix.json', 'w') as f:
        json.dump(results, f, indent=2)
    print("Sensitivity matrix saved to results/sensitivity_matrix.json")

if __name__ == "__main__":
    main()
