---
layout: page
title: pySpinW
subtitle: Overview
---

pySpinW is capable of calculating magnon dispersion curves, optimising magnetic structures, visualising systems, and predicting the results of inelastic scattering experiments. 
In general, we solve a system with a Hamiltonian of the form:

$\mathcal{H}=\sum_{i,j} \mathbf{S}_i J_{ij}\mathbf{S}_j + \sum_{i} \mathbf{S}_i A_i \mathbf{S}_i + \mathbf{B} \sum_{i} \mathbf{g}_i\mathbf{S}_i $

where $S_i$ are spin vector operators, $J_{ij}$ are 3x3 matrices describing pair coupling between spins, $A_{ij}$ are 3x3 anisotropy matrices, $B$ is external magnetic field and $g_i$ is the g-tensor.

The core calculations in pySpinW are a rust port of the core calculations in SpinW, calculations are set up using a python interface.

