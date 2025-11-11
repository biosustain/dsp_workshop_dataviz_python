# %% [markdown]
# # Figure 2A
# ![Figure 2a](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41467-024-53381-4/MediaObjects/41467_2024_53381_Fig2_HTML.png?as=webp)
# Caption: "Growth curve of the xylitol strain with (dark blue)
# or without (light blue) the CRISPRi switch induced. (...) Error bars and shaded
# areas indicate mean ± s.d. (n = 4 biological replicates (...)
# OD values (...) were measured using a Jenway 6705 UV/Vis spectrophotometer (...)"


# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# %%
fname = "figure_2a.csv"

# %%
data = pd.read_csv(fname, index_col=0).rename_axis(columns="replicate")
data.head()

# %%
data_long = (
    data.stack()
    .to_frame("OD600")
    .reset_index()
    .assign(
        condition=lambda x: x["replicate"].str.split("_").str[-1],
    )
)
data_long

# %% [markdown]
# Create a line plot with error bars for the measurement across the timepoints.
# Either use matplotlib or seaborn for a static plot.
# - seaborn lineplot with error bars indicating standard deviation:
#   [`seaborn.lineplot`](https://seaborn.pydata.org/generated/seaborn.lineplot.html)
# - matplotlib error bars used [`matplotlib.axes.Axes.errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html)

# %%
fig, ax = plt.subplots(figsize=(7, 5))

ax = sns.lineplot(
    data=data_long,
    x="time (h)",
    y="OD600",
    hue="condition",
    ax=ax,
)
ax.set(
    xlabel="Time (h)",
    ylabel="$\\text{OD}_{600}$",
    title="Growth curve of the xylitol strain with/without CRISPRi switch induced",
)
ax.legend(title="Condition")
fig.tight_layout()


# %%
# %% [markdown]
# <details>
# <summary>Show one solution code</summary>
#
# ```python
# display(sns.color_palette("Paired"))
# fig, ax = plt.subplots(figsize=(7, 5))
#
# ax = sns.lineplot(
#     data=data_long,
#     x="time (h)",
#     y="OD600",
#     hue="condition",
#     palette="Paired",
#     ci="sd",
#     marker="o",
#     err_style="bars",
#     err_kws={"capsize": 5},
#     ax=ax,
# )
# ax.set(
#     xlabel="Time (h)",
#     ylabel="$\\text{OD}_{600}$",
#     title="Growth curve of the xylitol strain with/without CRISPRi switch induced",
# )
# ax.legend(title="Condition")
# fig.tight_layout()
# ```
#
# </details>

# %%
