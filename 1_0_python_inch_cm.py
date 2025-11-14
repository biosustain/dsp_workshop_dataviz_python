# %% [markdown]
# # Python Function Introduction and a Inch-Centimeter Converter
# This example notebook is to illustrate how to create functions in Python.
# We will create a simple function that converts inches to centimeters and vice versa,
# a task you will sometimes need to do when reading journal instructions for figure 
# submission. Matplotlib, and thus Seaborn, use inches for figure size specifications,
# while many journals ask for figure sizes in centimeters.

# %%
def inch_to_cm(inches):
    """Convert inches to centimeters."""
    cm = inches * 2.54
    return cm

def cm_to_inch(cm):
    """Convert centimeters to inches."""
    inches = cm / 2.54
    return inches

# %% [markdown]
# ## Example Usage
# > For guidance, Nature's standard figure sizes are 89 mm wide (single column) 
# > and 183 mm wide (double column). The full depth of a Nature page is 247 mm.
# > Figures can also be a column-and-a-half where necessary (120–136 mm).
#
# [Source](https://www.nature.com/nature/for-authors/final-submission#:~:text=For%20guidance%2C%20Nature%27s%20standard%20figure,%28120%E2%80%93136%20mm%29.)

# %%
single_column_cm = 8.9  # in cm
double_column_cm = 18.3  # in cm
page_depth_cm = 24.7  # in cm
col_and_a_half_cm = 13.6  # in cm

# %%
single_column_inch = cm_to_inch(single_column_cm) # 3.5 inches
double_column_inch = cm_to_inch(double_column_cm) # 7.2 inches
page_depth_inch = cm_to_inch(page_depth_cm)    # 9.72 inches
col_and_a_half_inch = cm_to_inch(col_and_a_half_cm) # 5.35 inches

# Print the results
print(f"Single column width: {single_column_inch:.2f} inches")
print(f"Double column width: {double_column_inch:.2f} inches")
print(f"Page depth: {page_depth_inch:.2f} inches")
print(f"Column and a half width: {col_and_a_half_inch:.2f} inches")

# %% [markdown]
# ## Typed Function Definitions
# You can also add type hints to the function definitions to specify the expected input and output types
#
# def inch_to_cm(inches: float) -> float:
#     """Convert inches to centimeters."""
#     cm = inches * 2.54
#     return cm
#
# def cm_to_inch(cm: float) -> float:
#     """Convert centimeters to inches."""
#     inches = cm / 2.54
#     return inches
