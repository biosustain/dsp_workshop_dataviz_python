# %% [markdown]
# # Matplotlib Configuration
#
# Matplotlib Runtime Configuration (rc) allows you to customize the default styles and 
# behaviors of plots. The rcParams dictionary stores these settings,
# such as font sizes, line widths,and color schemes.
# You can modify rcParams directly in your code to change the appearance of all plots globally.
# Example: `mpl.rcParams['lines.linewidth'] = 2.0`
# You can also use style sheets or the 'matplotlibrc' file for persistent configuration.
# %%
import matplotlib
import matplotlib.font_manager

print(matplotlib.rcParams['font.size'])  # Default font size (usually 'medium')
print(matplotlib.font_manager.font_scalings)  # Shows the scaling factors for each size keyword

# %% [markdown]
# Find the full list of rcParams you can modify
# See the documentation [here] and specifically 
# [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams).

# %%
matplotlib.rcParams['font.size'] = 14  # Set a new default font size


# %% [markdown]
# See them all below:

# %%
matplotlib.rcParams
