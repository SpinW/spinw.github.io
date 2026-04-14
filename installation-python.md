---
layout: page
title: Installation
subtitle: How to install pySpinW
---
# What you need
   * An installation of python, version 3.10 or above (3.12 recommended)
   * Recommended: An Integrated Devolopment Environment (IDE), such as VSCode or PyCharm

# How to install SpinW
We recommend that you use a virtual environment, for details of how to do this see below. 
pySpinW is available through pip, so to install you simply type:

```pip install spinw-python```

# Updating

Updating to the latest pySpinW can be done through pip

```pip install --upgrade package_name```

# Setting up a virtual environment

## Windows

Many IDEs automatically set this up for you, so using your IDE's tools are the recommended method. However, here is how to do it from the terminal:

If you have a modern python set-up, you can create a python 3.12 virtual environment with

```py -3.12 -m venv VENV_NAME```

where `VENV_NAME` is a arbitrary name given to you virtual environment (often people use `.venv`). 
If you don't have a modern setup that supports the `py` command,
you can use the following, as long as your python version is newer than 3.10

```python -m venv VENV_NAME```

Then "activate" this environment with

```VENV_NAME\Scripts\Activate```

Depending on how you are running this, you might need to run this first:

```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```

## MacOS and Linux

You can create a python virtual environment with

```python -m venv VENV_NAME```

where `VENV_NAME` is a arbitrary name given to you virtual environment (often people use `.venv`). To activate it, use

```source VENV_NAME/bin/activate```


## Conda

Alternatively, you can install a virtual environment using the `conda` or `mamba` program. First download and install it from [this link](https://github.com/conda-forge/miniforge?tab=readme-ov-file#install), then create a virtual environment called `pyspinw`:

```mamba create -n pyspinw python=3.12```

Then activate this environment and install PySpinW as above:

```mamba activate pyspinw```
```pip install spinw-python```

## Jupyter

Many of the tutorials use Jupyter notebooks, which can be installed using:

```pip install notebook```


<h1 class="text-center">Have fun!</h1>
