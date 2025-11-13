# %% [markdown]
# # VueCore
# - implements at the moment not too many figures
# - will be used to define plotting functions for certain analysis types in our
#   core analysis library
# - at the moment only support the plotly backend
#
#
# Colab specific setup: 

# %%
import os

IN_COLAB = "COLAB_GPU" in os.environ

if IN_COLAB:
    # ! pip install vuecore

# %%
import pathlib

import pandas as pd
from vuecore.plots.basic.histogram import create_histogram_plot

# %% [markdown]
# ## Proteomics data example

# %%
fname = dir_data / "proteins" / "proteins.csv"
if IN_COLAB:
    fname = "https://raw.githubusercontent.com/biosustain/dsp_workshop_dataviz_python/refs/heads/main/data/proteins/proteins.csv"

# %%
dir_data = pathlib.Path("data")
df = (
    pd.read_csv(fname, index_col=0)
    .rename_axis("Protein_ID", axis=1)
    .stack()
    .reset_index(name="Intensity")
)
df

# %%
# to be continued
# Generate the advanced histogram plot
fig = create_histogram_plot(
    data=df,
    x="Intensity",
    color="Reference",
    barmode="overlay",
    histnorm="probability density",
    title="Protein intensities by sample",
    subtitle="Histogram with probability density normalized",
    labels={"Intensity": "Protein Intensity", "Reference": "Sample"},
    hover_data=["Protein_ID"],
    opacity=0.75,
)
fig


# %% [markdown]
# For now vuecore is built on top of ploltly:

# %%
type(fig)
