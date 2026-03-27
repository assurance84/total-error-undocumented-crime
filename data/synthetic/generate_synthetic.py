import numpy as np
import pandas as pd

np.random.seed(2600)
n = 100000

# Synthetic data that matches the moments used in the Monte Carlo
df = pd.DataFrame({
    'rho_violent': np.random.beta(45, 17, n),
    'rho_property': np.random.beta(62, 24, n),
    'rho_homicide': np.random.beta(99, 1, n),
    'alpha_gamma': np.random.beta(50, 9, n),
    'delta_time': np.random.beta(30, 11, n)
})

df.to_csv('data/synthetic/synthetic_capture_params.csv', index=False)
print("Synthetic data generated — ready for replication")
