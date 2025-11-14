# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: fmg
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Pandas

# %% [markdown]
# The standard data manipulation framework in Python (many others make use of at least part of its functionalities or are compatible with it)

# %% [markdown]
# We are not going in-depth - we are just showing some basic functionalities which are important for plotting.

# %%
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pathlib
import seaborn as sns

# %%
DATA_DIR = pathlib.Path().cwd() / "data/growth"

# %% [markdown]
# ## 1. DATA I/O (Input/Output)

# %% [markdown]
# ### 1. Read Data

# %% [markdown]
# Let us load in some fake data made to fit some plots from a Proteomics paper.

# %%
df = pd.read_csv(DATA_DIR / "fake_growth_data.csv")

# %% [markdown]
# Inspect the first few lines.  

# %%
df.head()

# %% [markdown]
# You could also omit .head() and it will automatically shorten the output based on your rendering settings.

# %%
df

# %% [markdown]
# ### 1.2 Write it to A File

# %% [markdown]
# Write a dataframe to a .csv file. (We make a folder first to store our own output).

# %%
my_output_dir = DATA_DIR / "my_data"
if not os.path.exists(my_output_dir):
    os.mkdir(my_output_dir)

df.to_csv(my_output_dir / "fake_data.csv")

# %% [markdown]
# `pd.read_csv()` and `.to_csv()` are the general input/output functions (among some more). Meaning: they work for other common files too (.txt, .tsv) and some more domain-specific files that are however in a (somewhat) tabular format (e.g. .vcf).
# In other words - as long as it looks like a table, you can read /write to it, regardless of the file extension.  
#
# To demonstrate, let us save it to a .tsv file. The difference is that it is **tab**-separated values instead of **comma**-separated values in a .csv file.

# %%
df.to_csv(my_output_dir / "fake_data.tsv", sep="\t")

# %% [markdown]
# It can make sense to imit the index column, as Pandas automatically creates one when you read it, even if it already exists. (Otherwise you specify e.g. `index_col=0` when reading it - try it out to see the difference).

# %%
df.to_csv(my_output_dir / "fake_data.tsv", sep="\t", index=False)

# %% [markdown]
# You can also read/write zipped file. Pandas will try to detect it automatically, but you can specify it yourself:

# %%
df.to_csv(my_output_dir / "fake_data.tsv.gz", sep="\t", index=False, compression="gzip")

# %%
#pd.read_csv(my_output_dir / "fake_data.tsv.gz", sep="\t", compression="gzip")

# %% [markdown]
# ## 2. Data Manuipulation

# %% [markdown]
# ### 2.1 Rename

# %% [markdown]
# The column names are written in a human-readable format, with spaces and brackets. It can be a good practice however to write them in a more programming-friendly way. We can easily do it by using a dictionary with the syntax  
# `{<old-name>: <new-name>}`

# %%
df2 = df.rename(columns={
    "SFN concentration (µM)": "sfn_conc_mumolar",
    "time (h)": "time_h",
    "Bacterial growth (OD600)": "bact_growth_od600"
})

# %% [markdown]
# We can do this - or many other operations - inplace for brevity.

# %%
df.rename(columns={
    "SFN concentration (µM)": "sfn_conc_mumolar",
    "time (h)": "time_h",
    "Bacterial growth (OD600)": "bact_growth_od600"
}, inplace=True)

# %% [markdown]
# ### 2.2 Filtering by Conditions

# %% [markdown]
# As we can see, we have data for aerobic and anaerobic conditions. If we are only interested in looking at e.g. the aerobic data, we can do it like this:

# %%
df_aerobic = df[df["condition"] == "Aerobic"]

# %% [markdown]
# We can also filter by multile conditions. For example, get all anaerobic data from DMSO, where the OD600 is below a value of 0.4:

# %%
df_multi_condition = df[
    (df["condition"] == "Anaerobic")
    & (df["sfn_conc_mumolar"] == "DMSO")
    & (df["bact_growth_od600"] < 0.4)
]

# %% [markdown]
# ### 2.3 Adding Data By Conditions

# %% [markdown]
# Part of data transformation is adding in new variables based on other columns in the table. This can be also just for plotting. For example, we could wish to color our plot on whether our bacteria are in their stationary phase or not. Then, we would add a variable called `is_stationary()` that we use to subset parts of our data for plotting (we will show how later with seaborn). We use NumPy for this purpose with the syntax
# `(<condition(s)>, <output-if-true>, <output-if-false>)`.

# %%
df["is_stationary"] = np.where(
    df["bact_growth_od600"] >= 0.55, True, False
)

# %% [markdown]
# ### 2.4 Aggregating Data

# %% [markdown]
# Maybe we are more interested in the maximum or average OD or alike in our experiment. We could just use `.max()` for example but it would give us the maximum value across all variables. If however we wish to distinguish between different cases (like anaerobic/aerobic), then it makes sense to group our data first.
# Here, we show how to aggregate across all replicates:

# %%
df_rep_agg = (
    df
        .groupby(["time_h", "condition", "sfn_conc_mumolar"])
        ["bact_growth_od600"]
        .mean()
        .reset_index()
)

# %% [markdown]
# We put our command in brackets so we can write it out in multiple lines to show it better. We also reset the index at the end to transform the .Series object back into a .DataFrame object.

# %% [markdown]
# We can also aggregate multiple things at once:

# %%
df_multi_agg = (
    df
        .groupby(["time_h", "condition", "sfn_conc_mumolar"])
        .agg({
            "is_stationary": ["count"],
            "bact_growth_od600": ["min", "mean", "max",]
        })
        .reset_index()
)

# %% [markdown]
# ### 2.5 Adding Data by Aggregation

# %% [markdown]
# Previosly, we just added the `is_stationary` variable based on a guess. We could also do it more programmatically. We do it here in two steps:
# 1. Adding a column indicating the maximum OD600 for that condition-sfn-replicate, minus a tolerance
# 2. Conditioning on that new column

# %%
df["stationary_od"] = (
    df
        .groupby(["condition", "sfn_conc_mumolar", "replicate"])
        ["bact_growth_od600"]
        .transform(lambda col: col.max() - 0.1)
)
df["is_stationary"] = np.where(
    df["bact_growth_od600"] >= df["stationary_od"], True, False
)

# %% [markdown]
# That tolerance could also be calculated in a similar way, e.g. based on the standard deviation (we leave that as an exercise if you want to try it out yourself).

# %% [markdown]
#

# %% [markdown]
# There are many more useful transformations, but we end here by having shown some that you could already use in more advanced plots.

# %% [markdown]
#
