# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
# ---

# %% [markdown]
# # VueCore
# - implements at the moment some core acore analysis plots, see the analysis section
# - in the docs: [vuecore](https://vuecore.readthedocs.io)
# - will be used to define plotting functions for every analysis types in our core
#   analysis library, [acore](https://analytics-core.readthedocs.io)
# - at the moment the basic plots in vuecore only support the plotly backend, while
#   analysis plots can be generated as static (matplotlib) or interactive (plotly) plots
# - all complex analysis plots are available as static and interactive plots: in the
#   namespace `vuecore.static` and `vuecore.interactive`
#
# Colab specific setup:

# %%
import os

IN_COLAB = "COLAB_GPU" in os.environ

if IN_COLAB:
    # %pip install acore vuecore
    print("Done installing acore and vuecore in colab")

# %% [markdown] Import libraries

# %%
import os
import pathlib

import pandas as pd
import vuecore
from vuecore.plots.basic.histogram import create_histogram_plot

IN_COLAB = "COLAB_GPU" in os.environ

# %% [markdown]
# ## Proteomics data example
#
# - load from repository if in colab

# %%
dir_data = pathlib.Path("data")
fname = dir_data / "proteins" / "proteins.csv"
if IN_COLAB:
    fname = (
        "https://raw.githubusercontent.com/biosustain/dsp_workshop_dataviz_python"
        "/refs/heads/main/data/proteins/proteins.csv"
    )
df = (
    pd.read_csv(fname, index_col=0)
    .rename_axis("Protein_ID", axis=1)
    .stack()
    .reset_index(name="Intensity")
)
df

# %% to be continued Generate the advanced histogram plot
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


# %% [markdown] For now vuecore is built on top of ploltly:

# %%
type(fig)


# %% [markdown]
# ## Decomposition plots (PCA)
#
# Dimensionality reduction results (PCA, t-SNE, UMAP) from `acore` can be plotted
# directly with `vuecore.dimensionality_reduction`, as a static (matplotlib) or an
# interactive (plotly) figure. The proteins are the features, the samples are the
# observations, so we need the wide format (samples as rows) and a `group` column.

# %%
from acore.exploratory_analysis.decomposition import run_pca
from vuecore.dimensionality_reduction import (
    get_embedding_plot_interactive,
    get_embedding_plot_static,
)

# %%
df_wide = pd.read_csv(fname, index_col=0)
df_wide["group"] = df_wide.index.str.split("_").str[0]  # DMSO or Suf
df_wide[["group"]]

# %% [markdown] `run_pca` returns the components, loadings and explained variance, and
# the axis names (including explained variance). Proteins with missing values are dropped
# per default.

# %%
pca_results, pca_annotation = run_pca(df_wide, group="group")
pca_results[0]

# %% [markdown] Static version (matplotlib figure):

# %%
fig_static = get_embedding_plot_static(
    pca_results,
    pca_annotation,
    group="group",
    title="PCA of protein intensities",
)

# %% [markdown] Interactive version (plotly figure) - hover over the samples. The
# loadings of the proteins contributing most are added as arrows (biplot).

# %%
fig_interactive = get_embedding_plot_interactive(
    pca_results,
    pca_annotation,
    group="group",
    title="PCA of protein intensities",
)
fig_interactive


# %% [markdown]
# ## Current main namespace of `vuecore` and its submodules
#
# > This will be updated over time.

# %%
import inspect
import types

for n in (n for n in dir(vuecore) if not n.startswith("_")):
    o = getattr(vuecore, n)
    kind = (
        "module"
        if isinstance(o, types.ModuleType)
        else "class" if inspect.isclass(o) else "func" if callable(o) else "value"
    )
    _doc = (inspect.getdoc(o) or "").split(chr(10))[0][:70] if kind != "value" else ""
    print(f"{kind:<7}{n:<30}{_doc}")


# %%
