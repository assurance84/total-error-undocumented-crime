import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(2600)
n = 100000

# --- Beta priors (empirically anchored) ---
rho_violent = np.random.beta(45, 17, n)      # violent crime
rho_property = np.random.beta(62, 24, n)     # property crime
rho_homicide = np.random.beta(99, 1, n)      # homicide
alpha_gamma = np.random.beta(50, 9, n)
delta_time = np.random.beta(30, 11, n)

# --- Composite capture rates ---
c_violent = rho_violent * alpha_gamma * delta_time
c_property = rho_property * alpha_gamma * delta_time
c_homicide = rho_homicide * alpha_gamma * delta_time

# --- Implied true rate ratios ---
R_obs_violence = 0.50
R_true_violence = R_obs_violence / c_violent

R_obs_property = 0.25
R_true_property = R_obs_property / c_property

R_obs_homicide = 0.74
R_true_homicide = R_obs_homicide / c_homicide

# --- Results (replication check under seed 2600) ---
print("Violent R_true quantiles:", np.quantile(R_true_violence, [0.025, 0.25, 0.50, 0.75, 0.975]))
print("P(R_true_violent > 1):", np.mean(R_true_violence > 1.0))

print("Property R_true quantiles:", np.quantile(R_true_property, [0.025, 0.50, 0.975]))
print("P(R_true_property > 1):", np.mean(R_true_property > 1.0))

print("Homicide R_true quantiles:", np.quantile(R_true_homicide, [0.025, 0.50, 0.975]))
print("P(R_true_homicide >= 1):", np.mean(R_true_homicide >= 1.0))
