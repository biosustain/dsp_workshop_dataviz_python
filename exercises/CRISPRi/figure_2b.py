# %% [markdown]
# # Figure 2b (Rong, Frey et. al. 2024)
# ![Figure 2b](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41467-024-53381-4/MediaObjects/41467_2024_53381_Fig2_HTML.png?as=webp)
# Caption: "Growth curve of the xylitol strain with (dark blue)
# or without (light blue) the CRISPRi switch induced. (...) Error bars and shaded
# areas indicate mean ± s.d. (n = 4 biological replicates (...)
# OD values (...) were measured using a Jenway 6705 UV/Vis spectrophotometer (...)"


# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# %% [markdown]
# For protability the data is directly included as a dictionary. See the commented
# out code how the data was obtained from the CSV file [figure_2b.csv](figure_2b.csv).

# %%
# fname = "figure_2b.csv"
# data = pd.read_csv(fname).round(4)
# data.to_dict(orient="list")
data = {
    "timepoint (h)": [2, 12, 12, 16, 16, 30],
    "Uninduced_rep1": [1.8465, 1.8465, 1.8654, 1.8654, 1.7892, 1.7892],
    "Uninduced_rep2": [1.8806, 1.8806, 1.5969, 1.5969, 1.8764, 1.8764],
    "Uninduced_rep3": [2.0512, 2.0512, 1.5597, 1.5597, 1.627, 1.627],
    "Uninduced_rep4": [1.9217, 1.9217, 1.9355, 1.9355, 1.65, 1.65],
    "Induced_rep1": [2.1165, 2.1165, 2.1316, 2.1316, 2.3346, 2.3346],
    "Induced_rep2": [2.0487, 2.0487, 3.0061, 3.0061, 2.2944, 2.2944],
    "Induced_rep3": [2.0778, 2.0778, 2.1711, 2.1711, 2.4402, 2.4402],
    "Induced_rep4": [2.0859, 2.0859, 2.0865, 2.0865, 2.483, 2.483],
}
data = pd.DataFrame(data).set_index("timepoint (h)").rename_axis(columns="replicate")
data

# %%
data_long = data.stack().to_frame("yield").reset_index()
data_long["condition"] = data_long["replicate"].str.split("_").str[0]
data_long


# %% [markdown]
# Create a bar plot with error bars for the measurement across the timepoints.
# Either use matplotlib or seaborn for a static plot.

# %%
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    data=data_long,
    x="timepoint (h)",
    y="yield",
    hue="condition",
    ax=ax,
)

# %% [markdown]
# Add individual data points
# <details>
# <summary>Show code of one soluti}on</summary>
#
# ```python
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.barplot(
#     data=data_long,
#     x="timepoint (h)",
#     y="yield",
#     hue="condition",
#     ci="sd",
#     capsize=0.1,
#     errwidth=2,
#     edgecolor="black",
#     linewidth=1.5,
#     palette=["#4A90E2", "#A8D5F7"],
#     ax=ax,
# )
# ```
# </details>


# %% [markdown]
# ## Claude Sonnet 4.5
# Prompt: "Can you generate some example data and code to generate the following plot using Python?"
# Context: adding a screenshot of Figure 2b from Rong, Frey et. al. 2024

# %% tags=["hide-input"]
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Example data
time_intervals = ['2-12', '12-16', '16-30']

# Individual replicate measurements
induced_data = [
    [2.05, 2.15, 2.1],      # 2-12h
    [2.3, 2.4, 2.5],        # 12-16h
    [2.5, 2.55, 2.6]        # 16-30h
]

uninduced_data = [
    [1.9, 1.95, 2.0],       # 2-12h
    [1.7, 1.75, 1.8],       # 12-16h
    [1.68, 1.73, 1.78]      # 16-30h
]

# Calculate means and standard errors
induced_means = [np.mean(d) for d in induced_data]
uninduced_means = [np.mean(d) for d in uninduced_data]
induced_sem = [np.std(d, ddof=1) / np.sqrt(len(d)) for d in induced_data]
uninduced_sem = [np.std(d, ddof=1) / np.sqrt(len(d)) for d in uninduced_data]

# Perform t-tests for statistical significance
p_values = [stats.ttest_ind(ind, unind).pvalue 
            for ind, unind in zip(induced_data, uninduced_data)]

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Bar positions
x = np.arange(len(time_intervals))
width = 0.35

# Create bars
bars1 = ax.bar(x - width/2, induced_means, width, 
               label='Induced', color='#4A90E2', 
               edgecolor='black', linewidth=1.5,
               yerr=induced_sem, capsize=5, error_kw={'linewidth': 2})

bars2 = ax.bar(x + width/2, uninduced_means, width,
               label='Uninduced', color='#A8D5F7',
               edgecolor='black', linewidth=1.5,
               yerr=uninduced_sem, capsize=5, error_kw={'linewidth': 2})

# Add individual data points
for i, (ind_points, unind_points) in enumerate(zip(induced_data, uninduced_data)):
    # Induced points
    x_induced = np.random.normal(i - width/2, 0.04, size=len(ind_points))
    ax.scatter(x_induced, ind_points, color='white', 
               edgecolor='black', s=80, linewidth=1.5, zorder=3)
    
    # Uninduced points
    x_uninduced = np.random.normal(i + width/2, 0.04, size=len(unind_points))
    ax.scatter(x_uninduced, unind_points, color='white',
               edgecolor='black', s=80, linewidth=1.5, zorder=3)

# Add significance asterisks
for i, p_val in enumerate(p_values):
    if p_val < 0.05:
        y_max = max(induced_means[i] + induced_sem[i], 
                    uninduced_means[i] + uninduced_sem[i])
        ax.plot([i - width/2, i + width/2], [y_max + 0.15, y_max + 0.15], 
                'k-', linewidth=1.5)
        ax.text(i, y_max + 0.2, '*', ha='center', va='bottom', 
                fontsize=20, fontweight='bold')

# Customize the plot
ax.set_ylabel('Yield (mmol mol$^{-1}$)', fontsize=14, fontweight='bold')
ax.set_xlabel('Time interval (h)', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(time_intervals, fontsize=12)
ax.set_ylim(0, 3)
ax.set_yticks([0, 1, 2, 3])
ax.tick_params(axis='both', which='major', labelsize=11)

# Add legend
ax.legend(loc='upper left', fontsize=12, frameon=False)

# Add grid
ax.grid(axis='y', linestyle='-', alpha=0.3, zorder=0)
ax.set_axisbelow(True)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

plt.tight_layout()
plt.show()

# Print statistical results
print("\nStatistical Analysis:")
print("-" * 50)
for i, interval in enumerate(time_intervals):
    print(f"\n{interval} hours:")
    print(f"  Induced: {induced_means[i]:.3f} ± {induced_sem[i]:.3f}")
    print(f"  Uninduced: {uninduced_means[i]:.3f} ± {uninduced_sem[i]:.3f}")
    print(f"  p-value: {p_values[i]:.4f} {'*' if p_values[i] < 0.05 else ''}")

# %%
