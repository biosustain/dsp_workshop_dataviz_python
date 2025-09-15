# %% [markdown]
# # Seaborn
# - A statistical data visualization library based on Matplotlib.
# - Provides a high-level interface for drawing attractive statistical graphics.
# - [website](https://seaborn.pydata.org/)
#
# Use matplotlib objects if you need to modify aspects of the plot.

# %%
import pathlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# %%
dir_data = pathlib.Path("data")
df = pd.read_csv(dir_data / "proteins" / "proteins.csv", index_col=0).T
df

# %% [markdown]
# ## Horizontal Bar Plot
# - Using the `orient` parameter to switch to horizontal orientation.
# - calculates the mean and standard deviation of the mean automatically

# %%
ax = sns.barplot(
    data=df,
    orient="h",
    errorbar=("pi", 50),
    capsize=0.4,
    err_kws={"color": ".5", "linewidth": 2.5},
    linewidth=2.5,
    edgecolor=".5",
    facecolor=(0, 0, 0, 0),
)

# %%
_ = ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment="right")
ax.get_figure().tight_layout()

# %%
with plt.style.context("ggplot"):
    ax = sns.barplot(data=df)

# %%
