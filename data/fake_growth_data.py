#!/usr/bin/env python3
import numpy as np
import os
import pandas as pd
import pathlib

# --- Helper function to simulate bacterial growth (logistic curve) ---
def sigmoid(t, L, k, t0):
    """
    L = max growth (carrying capacity)
    k = growth rate
    t0 = time of midpoint
    """
    return L / (1 + np.exp(-k * (t - t0)))

# --- Define experimental parameters ---
conditions = ['Anaerobic', 'Aerobic']
concentrations = ['DMSO', '20', '15', '10', '5', '2.5']
replicates = [1, 2, 3] # 3 replicates per experiment
time_points = np.linspace(0, 24, 13) # Measurements every 2 hours (0, 2, ... 24)

# List to hold all our data rows
data = []

# --- Loop through all experimental combinations ---
for cond in conditions:
    for conc in concentrations:
        for rep in replicates:
            
            # --- Set growth parameters based on plots ---
            # Start with default (Aerobic, DMSO)
            max_od = 0.9
            growth_rate = 0.8
            lag_phase = 6
            noise_level = 0.02
            
            # 1. Adjust for Anaerobic vs Aerobic
            if cond == 'Anaerobic':
                max_od = 0.65 # Lower carrying capacity
                growth_rate = 0.7 # Slower growth
            
            # 2. Adjust for SFN concentration
            # (Simulating the dose-dependent inhibition)
            if cond == 'Aerobic':
                if conc == '20': max_od *= 0.85
                elif conc == '15': max_od *= 0.90
                elif conc == '10': max_od *= 0.94
                elif conc == '5': max_od *= 0.97
                elif conc == '2.5': max_od *= 0.99
            
            if cond == 'Anaerobic':
                # Plot B shows a slight inhibition, but less than aerobic
                if conc == '20': max_od *= 0.94
                elif conc == '15': max_od *= 0.94
                elif conc == '10': max_od *= 0.95
                elif conc == '5': max_od *= 0.97
                elif conc == '2.5': max_od *= 0.99

            # 3. Add per-replicate random variability (for scatter in plots B/D)
            rep_max_od = max_od * np.random.uniform(0.95, 1.05)
            rep_growth_rate = growth_rate * np.random.uniform(0.9, 1.1)

            # --- Generate time-course for this single replicate ---
            for t in time_points:
                # Calculate the "perfect" OD
                base_od = sigmoid(t, rep_max_od, rep_growth_rate, lag_phase)
                
                # Add random measurement noise
                noise = np.random.normal(0, noise_level)
                final_od = max(0.01, base_od + noise) # OD can't be negative
                
                # Set initial OD at t=0
                if t == 0:
                    final_od = max(0.01, 0.05 + noise)

                # Append the row to our data list
                data.append({
                    'condition': cond,
                    'SFN concentration (µM)': conc,
                    'replicate': rep,
                    'time (h)': t,
                    'Bacterial growth (OD600)': final_od
                })

# --- Convert the list of dictionaries into a DataFrame ---
df = pd.DataFrame(data)

# Re-order concentration to match the plot's legend
df['SFN concentration (µM)'] = pd.Categorical(
    df['SFN concentration (µM)'], 
    categories=concentrations, 
    ordered=True
)

path_of_this_file = pathlib.Path(
    os.path.dirname(os.path.realpath(__file__)))
df.to_csv(path_of_this_file / "growth/fake_growth_data.csv", index=False)