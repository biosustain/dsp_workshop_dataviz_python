# %% [markdown]
# # Seaborn (intro with proteomics data)
# - A statistical data visualization library based on Matplotlib.
# - Provides a high-level interface for drawing attractive statistical graphics.
# - [website](https://seaborn.pydata.org/)
#
# Use matplotlib objects if you need to modify aspects of the plot.

# %%
import os
import pathlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

IN_COLAB = "COLAB_GPU" in os.environ

# %% [markdown]
# ## Proteomics data example

# %%
fname = pathlib.Path("data") / "proteins" / "proteins.csv"
if IN_COLAB:
    fname = (
        "https://raw.githubusercontent.com/biosustain/dsp_workshop_dataviz_python"
        "/refs/heads/main/data/proteins/proteins.csv"
    )
df = pd.read_csv(fname, index_col=0).T
df

# %% [markdown]
# ### Horizontal Bar Plot
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

# %% [markdown]
# ### Customizing the Plot
# - You can customize the plot further using Matplotlib functions.

# %%
_ = ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment="right",
)
ax.get_figure().tight_layout()

# %% [markdown]
# ### Style the plot as in ggplot2

# %%
with plt.style.context("ggplot"):
    ax = sns.barplot(data=df)

# %% [markdown]
# The end.
