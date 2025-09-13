# %% [markdown]
# # Plotly Express
# - A high-level interface for creating visualizations with Plotly.
# - Simplifies the process of creating complex visualizations.
# - [website](https://plotly.com/python/plotly-express/)

# %%
import plotly.express as px

# %%
fig = px.line([1, 2, 3, 4], [1, 4, 2, 3])
fig

# %%
fig = px.line(x=[1, 2, 3, 4], y=[1, 4, 2, 3])

# %%
dir(fig)

# %% [markdown]
# Explore the most common function types intended for users
# using the first word as the indicator

# %%
from collections import Counter

items = Counter([x.split("_")[0] for x in dir(fig) if x.split("_")[0]])
items

# %%
import pathlib

import pandas as pd

dir_data = pathlib.Path("data")
df = pd.read_csv(dir_data / "proteins" / "proteins.csv", index_col=0).T
df


# %%
x = df.iloc[:, 0]

px.histogram(x)
# %%
px.histogram(df)

# %%
