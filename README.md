# Data visualization in Python

Workshop material for 19th November 2025

## How to use material

There are two main ways we intend to use the material provided as executable notebooks: 
Colab and GitHub Codespaces.

### Google Colab

Every tutorial or exercise can be opened in colab using the launch button on
the **top right**: 🚀 (grey rocket if available)

![Open in Colab](assets/open_in_colab.png)

### GitHub Codespace
Launch the repository in a Codespace by clicking the button below:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/biosustain/dsp_workshop_dataviz_python)

Make sure you are logged into your GitHub account.

### Local or elsewhere

Get the repository and install the requirements from `requirements.txt`.

```bash
git clone https://github.com/biosustain/dsp_workshop_dataviz_python.git
cd dsp_workshop_dataviz_python
# create an environment, e.g. using venv
source venv/bin/activate  # on Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Local build of website

```bash
pip install -r requirements.txt
sphinx-build -nW --keep-going -b html .  _build
open _build/index.html
```


# Material

- https://python-graph-gallery.com/
