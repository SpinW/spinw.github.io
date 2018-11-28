---
layout: page
title: Installation
subtitle: How to install SpinW
---
# What you need
   * recent version of *Matlab* (the code is tested mostly on the latest versions R2013a-R2014a)
   * no extra Matlab toolbox is necessary for numerical calculations
   * for the optional symbolic calculations the *Symbolic Math Toolbox* is necessary

# How to install SpinW
   * unzip the downloaded SpinW files into a folder, e.g. `spinw`, there will be a subdirectory like `spinw_2-0beta_rev195`, where 2-0 is the version and rev195 is the revision number
   * add all the subdirectories of `spinw/spinw_2-0beta_rev195` to the Matlab path
   * to make the path permanent put the following command into the `startup.m` file (by using `edit startup` command): `addpath(genpath([YOUR_PATH '/spinw/spinw_2-0beta_rev195']))` where `YOUR_PATH` is the path of the SpinW folder

# Updating
   * since SpinW is under active development, the files are often updated (new features, bug fixes)
   * to update your installation, execute the `sw_update()` function in the Matlab Command Line, this will check for the latest available version and downloads it into a new subfolder under `/spinw/` and adds the new files to the Matlab search path
   * to make the new path permanent, edit the `startup.m` file as written above
   * execute the ``clear classes`` command in the Command Line to clear the Matlab cache of user defined classes

<h1 class="text-center">Have fun!</h1>
