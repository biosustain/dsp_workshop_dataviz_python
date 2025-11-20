# %% [markdown]
# # Plotly Express
# - A high-level interface for creating visualizations with Plotly.
# - Simplifies the process of creating complex visualizations.
# - [website](https://plotly.com/python/plotly-express/)

# %%
import os
import plotly.express as px

IN_COLAB = "COLAB_GPU" in os.environ

if IN_COLAB:
    # !pip install kaleido

# %% [markdown]
# ## Line Plot
# - A simple line plot using Plotly Express.
# - the positional axis order is different from Matplotlib

# %%
fig = px.line([1, 2, 3, 4], [1, 4, 2, 3])
fig

# %% [markdown]
# Just be explicit, which is always a good idea!

# %%
fig = px.line(x=[1, 2, 3, 4], y=[1, 4, 2, 3])

# %% [markdown]
# The plotly Figure object offers many methods to update the
# [`Figure`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html).
# There is no
# separate axes object. The underlying data can be seen as a dictionary containing
# data and the layout to apply (as a json).

# %%
dir(fig)

# %% [markdown]
# Explore the most common function types intended for users
# using the first word as the indicator

# %%
from collections import Counter

items = Counter([x.split("_")[0] for x in dir(fig) if x.split("_")[0]])
items

# %% [markdown]
# ## Proteomics data example

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
df = pd.read_csv(fname, index_col=0).T
df

# %%
x = df.iloc[:, 0]

px.histogram(x)

# %%
px.histogram(df)

# %% [markdown]
# ## Set the default template to ggplot2
# - Similar to seaborn's style settings
# - Other templates: `'ggplot2'`, `'seaborn'`, `'simple_white'`, `'plotly'`,
#   `'plotly_white'`, `'plotly_dark'`, `'presentation'`, `'xgridoff'`,
#   `'ygridoff'`, `'gridon'`, `'none'`
#
# Check the [templates](https://plotly.com/python/templates/).

# %%
px.defaults.template = "ggplot2"

# %%
fig = px.histogram(df)
fig

# %% [markdown]
# ## Save a static image
# - either directly from the interactive figure using the :camera:
#   icon (first from the left)
# - or programmatically as shown below setting width and height in dots per inch (DPI)

# %%
# Plotly's write_image uses pixels for width and height.
# To specify inches or centimeters, convert to pixels using the DPI (dots per inch).
# Example: 1 inch = 2.54 cm; pixels = inches * dpi

dpi = 150  # you can change this value as needed

# For 6 inches x 4 inches
width_in = 6
height_in = 4
fig.write_image(
    "proteomics_histogram_plotly.png",
    width=width_in * dpi,
    height=height_in * dpi,
    scale=1,
)
fig.write_image(
    "proteomics_histogram_plotly.pdf",
    width=width_in * dpi,
    height=height_in * dpi,
    scale=1,
)
# %%
