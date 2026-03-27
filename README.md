# Total Error Framework Extension of "The Measurement Trap"

**Replication archive and TEF extension** of  
*The Measurement Trap: Offense-Specific Identification Limits in Administrative Data on Undocumented Immigrant Criminality*.

This repository contains:
- Exact replication of the original Beta-distributed Monte Carlo sensitivity analysis (`np.random.seed(2600)`)
- New fully decomposed capture-rate models: \( c = \rho \times (\alpha \cdot \gamma) \times \delta \)
- Tightened empirical priors from 911-call data, MMP histories, and IDENT audits
- Multi-state DiD around enforcement shocks (Secure Communities)
- Homicide boundary-case analysis
- Comprehensive falsification grids and one-way/composite sensitivity tables

## Reproducibility
- All results use **synthetic data** that exactly preserve the moments and correlations needed for the Monte Carlo exercise.
- No restricted DPS/IDENT or 911-call microdata are included.
- Full replication is possible on any machine with Python 3.11+.

## How to reproduce
```bash
# 1. Clone the repo
git clone https://github.com/assurance84/total-error-undocumented-crime.git
cd total-error-undocumented-crime

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the full pipeline
cd code
python 00_original_replication.py          # reproduces original paper exactly
python 02_full_TEF_montecarlo.py           # main TEF results
python 05_falsification_grids.py           # robustness checks
