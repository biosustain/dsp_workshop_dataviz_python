# %% [markdown]
# # Matplotlib
# - A comprehensive library for creating static, animated, and interactive visualizations in Python.
# - Built on NumPy arrays and designed to work with the broader SciPy stack.

# %%
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# %%
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.

# %% [markdown]
# ![Anatomy of a matplotlib figure](https://matplotlib.org/stable/_images/anatomy.png)
# %%
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
ax.grid()
plt.show()

# %% [markdown]
# Customize ticks
# - [Ticker API](https://matplotlib.org/stable/api/ticker_api.html)

# %%
ax.yaxis.set_major_locator(mpl.ticker.MaxNLocator(integer=True))
# ax.xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter("{x:.0f}"))
ax.xaxis.set_major_locator(mpl.ticker.MaxNLocator(integer=True))
ax.get_figure()
# %%
mu, sigma = 115, 15
x = mu + sigma * np.random.randn(10000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# the histogram of the data
n, bins, patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)

ax.set_xlabel('Length [cm]')
ax.set_ylabel('Probability')
ax.set_title('Aardvark lengths\n (not really)')
ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
ax.axis([55, 175, 0, 0.03])
ax.grid(True)

# %%
import pathlib

import pandas as pd

dir_data = pathlib.Path("data")
df = pd.read_csv(dir_data / 'proteins' / "proteins.csv", index_col=0)
df

# %%
x = df.iloc[0]
x

# %%
ax = x.hist()

# %%
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, bins=30, alpha=0.7, color='C0')

# %%
