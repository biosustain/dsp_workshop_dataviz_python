# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: tags,-all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Data Analysis PXD040621
#
# Plan
# - read data and log2 transform intensity values
# - aggregate peptide intensities to protein intensities
# - format data from long to wide format
# - remove contaminant proteins
# - check for missing values
# - Clustermap of sample and proteins
# - differential analysis (Volcano Plots)
# - Enrichment Analysis
# - check for maltose update pathway (Fig. 3 in paper)

# %% tags=["hide-output"]
# %pip install acore vuecore

# %%
from pathlib import Path

import numpy as np
import pandas as pd

# %% [markdown]
# # Read in the data
# - `file_in`: input file with the quantified peptide data in MSstats format
#    as provided by quantms
#
# The file will be loaded from the repository if it is not present.

# %% tags=["parameters"]
file_in = Path("peptides") / "PXD040621_peptides.csv"
if not file_in.exists():
    file_in = (
        "https://raw.githubusercontent.com/biosustain/dsp_course_proteomics_intro/HEAD"
        "/data/PXD040621/processed/PXD040621.sdrf_openms_design_msstats_in.csv"
    )
df = pd.read_csv(file_in, sep=",", header=0)  # .set_index([])
df.head()


# %% [markdown]
# define the output folder for our VueGen report which we will create later

# %%
out_dir = "proteins"
out_dir = Path(out_dir)
out_dir.mkdir(parents=True, exist_ok=True)

# %% [markdown]
# We have the following columns in the data:
#
# ```python
# cols = [
#     "ProteinName",
#     "PeptideSequence",
#     "PrecursorCharge",
#     "FragmentIon",
#     "ProductCharge",
#     "IsotopeLabelType",
#     "Condition",
#     "BioReplicate",
#     "Run",
#     "Intensity",
#     "Reference",
# ]

# %% [markdown]
# # Log2 transform the intensity values
# - log2 transformations are common for lognormal distributed data

# %%
df["Intensity"] = np.log2(df["Intensity"].astype(float))
df.head()

# %% [markdown]
# # Exploratory and Data Quality Plots (peptide level)
# df["BioReplicate"] = df["BioReplicate"].replace({5: 1, 6: 2, 7: 3, 8: 4})
# fg = sns.displot(
#     data=df.rename(columns={"BioReplicate": "Rep", "Condition": "C."}),
#     x="Intensity",
#     col="C.",
#     row="Rep",
#     # hue="Reactor_ID",
#     kind="kde",
#     height=2,
#     aspect=1.1,
# )

# %% [markdown]
# # Aggregate the peptide intensities to protein intensities
# - we use the median of the peptide intensities for each protein
#
# There are more sophisticated ways to do this, e.g. using MaxLFQ, iBAQ, FlashLFQ, DirectLFQ, etc.
#
# - shorten sample name for readability

# %%
proteins = (
    df.groupby(["ProteinName", "Reference"])["Intensity"].median().unstack(level=0)
)
proteins.index = proteins.index.str.split("_").str[4:6].str.join("_")
proteins

# %% [markdown]
# # Remove contaminant proteins
# Remove the contaminant proteins which were added to the fasta file used in the data processing.
# Contaminant proteins are e.g. creation which gets into the sample from the human skin or hair
# when the sample is prepared.
#
# These are filtered out as they are most of the time not relevant, but a contamination.

# %%
decoy_proteins = proteins.filter(like="CON_", axis=1)
proteins = proteins.drop(decoy_proteins.columns, axis=1)
proteins

# %% [markdown]
# Create a label for each sample based on the metadata.
# - we will use a string in the sample name, but you can see how the metadata is organized

# %%
meta = df[["Condition", "BioReplicate", "Run", "Reference"]].drop_duplicates()
meta

# %%
label_encoding = {0: "control", 1: "10 µm sulforaphane"}
label_suf = pd.Series(
    proteins.index.str.contains("Suf_").astype(int),
    index=proteins.index,
    name="label_suf",
    dtype=np.int8,
).map(label_encoding)
label_suf

# %% [markdown]
# # Plot the data completeness for each protein.

# %%
view_name = "Protein"
out_dir.mkdir(parents=True, exist_ok=True)

# %%
view_name = "Protein"
ax = (
    proteins.notna()
    .sum()
    .sort_values()
    .plot(
        rot=45,
        ylabel=f"Number of Samples {view_name.lower()} was observed in",
    )
)
# ax.get_figure().savefig(
#     out_dir_subsection / f"data_completeness_step_plot.png",
#     bbox_inches="tight",
#     dpi=300,
# )

# %%
view_name = "Protein"
ax = (
    proteins.notna()
    .sum()
    .value_counts()
    .sort_index(ascending=False)
    .plot(
        kind="bar",
        title=f"Data Completeness per {view_name}",
        xlabel=f"Number of Samples {view_name.lower()} was observed in",
        ylabel=f"Number of {view_name}s",
        color="steelblue",
        figsize=(10, 6),
    )
)
# ax.get_figure().savefig(
#     out_dir_subsection / f"data_completeness_bar_plot.png",
#     bbox_inches="tight",
#     dpi=300,
# )

# %%
# Explode column names to examine split by '|'
proteins_meta = (
    proteins.columns.str.split("|", expand=True)
    .to_frame()
    .dropna(how="any", axis=1)
    .reset_index(drop=True)
)
proteins_meta.columns = ["Source", "ProteinName", "GeneName"]
proteins_meta["GeneName"] = proteins_meta["GeneName"].str.split("_").str[0]
proteins_meta.index = proteins.columns
proteins_meta.index.name = "identifier"
proteins_meta

# %% [markdown]
# For later in the enrichment analysis let's replace the protein identifier from the Fasta
# file with the UNIPROT ID

# %%
proteins.columns = proteins_meta["ProteinName"].rename("UniprotID")
proteins

# %% [markdown]
# And let's save a table with the data for inspection

# %%
proteins_meta.to_csv(out_dir / "proteins_identifiers.csv")
proteins.to_csv(out_dir / "proteins.csv")
