# %% [markdown]
# # Matplotlib
# - A comprehensive library for creating static, animated, and interactive visualizations in Python.
# - Built on NumPy arrays and designed to work with the broader SciPy stack.

# %%
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# %% [markdown]
# ## Basic Line Plot
# From Getting Started.

# %%
fig, ax = plt.subplots()  # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()  # Show the figure.

# %% [markdown]
# ![Anatomy of a matplotlib figure](https://matplotlib.org/stable/_images/anatomy.png)
# %%
fig, ax = plt.subplots()  # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
ax.grid()
plt.show()

# %% [markdown]
# Customize ticks
# - [Ticker API](https://matplotlib.org/stable/api/ticker_api.html)

# %%
ax.yaxis.set_major_locator(mpl.ticker.MaxNLocator(integer=True))
# ax.xaxis.set_major_locator(mpl.ticker.MaxNLocator(integer=True))
ax.get_figure()

# %%
mu, sigma = 115, 15
x = mu + sigma * np.random.randn(10000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
# the histogram of the data
n, bins, patches = ax.hist(x, 50, density=True, facecolor="C0", alpha=0.75)

ax.set_xlabel("Length [cm]")
ax.set_ylabel("Probability")
ax.set_title("Aardvark lengths\n (not really)")
ax.text(75, 0.025, r"$\mu=115,\ \sigma=15$")
ax.axis([55, 175, 0, 0.03])
ax.grid(True)

# %%
# ## Proteomics data example
# - plotting a histogram via the pandas interface

# %%
import os
import pathlib

import pandas as pd

IN_COLAB = "COLAB_GPU" in os.environ


fname = pathlib.Path("data") / "proteins" / "proteins.csv"
if IN_COLAB:
        fname = (
        "https://raw.githubusercontent.com/biosustain/dsp_workshop_dataviz_python"
        "/refs/heads/main/data/proteins/proteins.csv"
    )

df = pd.read_csv(fname , index_col=0)
df

# %%
x = df.iloc[0]
x

# %%
ax = x.hist()

# %%
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, bins=30, alpha=0.7, color="C0")


# %% [markdown]
# ## Available styles
# Choose your preferred style with it's defaults
# [here](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)
#
# ```python
# plt.style.use('ggplot')
# ```
#
# ![ggplot](https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_008_2_00x.png)
# ![seaborn_v0_8-bright](https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_012_2_00x.png)
# ![seaborn_v0_8-white](https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_025_2_00x.png)

# %%
with plt.style.context("ggplot"):
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(x, bins=30, alpha=0.7)

# %%
