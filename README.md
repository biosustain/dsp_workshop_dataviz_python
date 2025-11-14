# Data visualization in Python

We are pleased to invite you to our workshop on Introduction to Data Visualization using
Python, designed to help you transform raw data into meaningful and insightful visuals.
You will learn to create static plots in Matplotlib, Seaborn and interactive plots
in plotly. It will build upon the foundations of good visualization practices laid out
in the [R Course](https://biosustain.github.io/dsp_workshop_datavizR/)
(which you can, but do not have to attend).

My main aim is to get you ready to prompt more precisely Large Language Models (in their
Chat Bot interface or elsewhere) to create plot templates, you can then adjust to your
liking. Knowing some of the core concepts and terms of the Python plotting libraries
helps a lot with that.

This workshop can help you get started to make plots outside of programs
like Origin or Graphpad PRISM. It will help you to create plots using scripting which
you can (if you need to) edit in programs like Inkscape or Adobe Illustrator.

## Time and Place

- **Prerequisites**: 
    - Bring your laptop
    - a Google account (for Colab), 
    - or a GitHub account (for Codespaces).
- **Date**: Wednesday, 19th November 2025, 10:00 to 14:00
- **Location**: Building 208 - room 011 - ALC2

## Agenda

| Time          | Agenda Item                                                                                               |
| ------------- | --------------------------------------------------------------------------------------------------------- |
| 10.00 – 10.15 | Hello, coffee and setup                                                                                   |
| 10.15 – 10.45 | General considerations on handling plots created by scripts for publication <br> (size, saving plot data) |
| 10.45 – 11.15 | Matplotlib and seaborn basics                                                                             |
| 11.15 – 11.30 | Break                                                                                                     |
| 11.30 – 12.00 | Interactive plotly plots                                                                                  |
| 12.00 – 12.30 | Lunch break                                                                                               |
| 12.30 – 14.00 | Advanced plots, editing with LLMs and your questions                                                      |

## How to use material

There are two main ways we intend to use the material provided as executable notebooks:
Colab and GitHub Codespaces.

These hints on writing basic Markdown syntax might be helpful:
[Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

### Google Colab

Every tutorial or exercise can be opened in colab using the launch button on
the **top right**: 🚀 (grey rocket if available)

![Open in Colab](assets/open_in_colab.png)

Colab intro video:

- [basic](https://www.youtube.com/watch?v=inN8seMm7UI) - 3mins
- [Gemini in Colab (AI assistant)](https://www.youtube.com/watch?v=V7RXyqFUR98) - 5mins
  (by now there are even editing code cell capabilities)
- [broader](https://www.youtube.com/watch?v=FXKMmilL70w) - 15mins

### GitHub Codespace

Launch the repository in a Codespace by clicking the button below:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/biosustain/dsp_workshop_dataviz_python)

Make sure you are logged into your [GitHub account](https://github.com/join).

Then you can use VS Code in the Browser with a GitHub Codespace connected.

Please have a look at the (video) tutorials before the course:

- VSCode in the Browser: [vscode-web](https://code.visualstudio.com/docs/setup/vscode-web)
  ( we will connect a remote machine using a codespace)
- Codespaces: [codespaces/quickstart](https://docs.github.com/en/codespaces/quickstart)

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
