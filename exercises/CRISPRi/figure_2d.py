# %% [markdown]
# # Figure 2d (Rong, Frey et. al. 2024)
# ![Figure 2d](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41467-024-53381-4/MediaObjects/41467_2024_53381_Fig2_HTML.png?as=webp)
# Caption: "Growth curve of the xylitol strain with (dark blue)
# or without (light blue) the CRISPRi switch induced. (...) Error bars and shaded
# areas indicate mean ± s.d. (n = 4 biological replicates (...)
# OD values (...) were measured using a Jenway 6705 UV/Vis spectrophotometer (...)"


# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from numpy import nan

# %% [markdown]
# For protability the data is directly included as a dictionary. See the commented
# out code how the data was obtained from the CSV file [figure_2d.csv](figure_2d.csv).

# %% tags=["hide-input"]
# fname = "figure_2d.csv"
# data = (
#     (pd.read_csv(fname, header=[0, 1], index_col=0))
#     .rename_axis(index=[("time (h)", "")], columns=["condition", "replicate"])
#     .reset_index()
# )
# data.to_dict(orient="list")
data = {
    ("time (h)", ""): [0.5, 2.0, 3.0, 5.0, 7.0, 9.0, 11.25, 13.0, 15.0, 24.0, 27.5],
    ("IBA strain - OD600", "R1"): [
        0.103,
        0.116,
        0.23,
        0.75,
        2.1,
        3.97,
        5.63,
        7.43,
        8.2,
        7.72,
        7.36,
    ],
    ("IBA strain - OD600", "R2"): [
        0.1,
        0.111,
        0.22,
        0.74,
        2.02,
        3.84,
        4.37,
        7.14,
        8.14,
        7.63,
        7.78,
    ],
    ("IBA strain - OD600", "R3"): [
        0.097,
        0.117,
        0.216,
        0.74,
        1.89,
        3.67,
        5.35,
        7.03,
        7.72,
        7.65,
        7.72,
    ],
    ("Glucose (mM)", "R1"): [
        117.6111111,
        nan,
        nan,
        117.3888889,
        nan,
        nan,
        nan,
        79.05555556,
        nan,
        44.66666667,
        nan,
    ],
    ("Glucose (mM)", "R2"): [
        118.1111111,
        nan,
        nan,
        117.5,
        nan,
        nan,
        nan,
        81.27777778,
        nan,
        44.66666667,
        nan,
    ],
    ("Glucose (mM)", "R3"): [
        118.2777778,
        nan,
        nan,
        117.1666667,
        nan,
        nan,
        nan,
        81.55555556,
        nan,
        44.94444444,
        nan,
    ],
    ("Acetate (mM)", "R1"): [
        18.33333333,
        nan,
        nan,
        16.16666667,
        nan,
        nan,
        nan,
        3.5,
        nan,
        4.5,
        nan,
    ],
    ("Acetate (mM)", "R2"): [
        20.83333333,
        nan,
        nan,
        16.66666667,
        nan,
        nan,
        nan,
        5.833333333,
        nan,
        2.0,
        nan,
    ],
    ("Acetate (mM)", "R3"): [
        18.83333333,
        nan,
        nan,
        16.5,
        nan,
        nan,
        nan,
        4.166666667,
        nan,
        3.0,
        nan,
    ],
    ("IBA (mM)", "R1"): [
        0.0,
        nan,
        nan,
        0.0,
        nan,
        nan,
        nan,
        23.26167386,
        nan,
        53.36772159,
        nan,
    ],
    ("IBA (mM)", "R2"): [
        0.0,
        nan,
        nan,
        0.0,
        nan,
        nan,
        nan,
        22.78901023,
        nan,
        51.95629545,
        nan,
    ],
    ("IBA (mM)", "R3"): [
        0.0,
        nan,
        nan,
        0.0,
        nan,
        nan,
        nan,
        22.506725,
        nan,
        52.08759091,
        nan,
    ],
}
data = (
    pd.DataFrame(data)
    .set_index(("time (h)", ""))
    .rename_axis(index=["time (h)"], columns=["condition", "replicate"])
)
data

# %% [markdown]
# You will need to operate on a multi-index DataFrame.

# %%
#
