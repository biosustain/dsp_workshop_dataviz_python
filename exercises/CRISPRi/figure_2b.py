# %% [markdown]
# # Figure 2b (Rong, Frey et. al. 2024)
# ![Figure 2b](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41467-024-53381-4/MediaObjects/41467_2024_53381_Fig2_HTML.png?as=webp)
# Caption: "Growth curve of the xylitol strain with (dark blue)
# or without (light blue) the CRISPRi switch induced. (...) Error bars and shaded
# areas indicate mean ± s.d. (n = 4 biological replicates (...)
# OD values (...) were measured using a Jenway 6705 UV/Vis spectrophotometer (...)"


# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# %% [markdown]
# For protability the data is directly included as a dictionary. See the commented
# out code how the data was obtained from the CSV file [figure_2b.csv](figure_2b.csv).

# %%
# fname = "figure_2b.csv"
# data = pd.read_csv(fname).round(4)
# data.to_dict(orient="list")
data = {
    "timepoint (h)": [2, 12, 12, 16, 16, 30],
    "Uninduced_rep1": [1.8465, 1.8465, 1.8654, 1.8654, 1.7892, 1.7892],
    "Uninduced_rep2": [1.8806, 1.8806, 1.5969, 1.5969, 1.8764, 1.8764],
    "Uninduced_rep3": [2.0512, 2.0512, 1.5597, 1.5597, 1.627, 1.627],
    "Uninduced_rep4": [1.9217, 1.9217, 1.9355, 1.9355, 1.65, 1.65],
    "Induced_rep1": [2.1165, 2.1165, 2.1316, 2.1316, 2.3346, 2.3346],
    "Induced_rep2": [2.0487, 2.0487, 3.0061, 3.0061, 2.2944, 2.2944],
    "Induced_rep3": [2.0778, 2.0778, 2.1711, 2.1711, 2.4402, 2.4402],
    "Induced_rep4": [2.0859, 2.0859, 2.0865, 2.0865, 2.483, 2.483],
}
data = pd.DataFrame(data).set_index("timepoint (h)").rename_axis(columns="replicate")
data

# %%
