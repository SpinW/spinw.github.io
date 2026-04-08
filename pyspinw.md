---
layout: page
title: pySpinW
subtitle: Overview
use_math: true
---

pySpinW is capable of calculating magnon dispersion curves, optimising magnetic structures, visualising systems, and predicting the results of inelastic scattering experiments. 
In general, we solve a system with a Hamiltonian of the form:

{% raw %}
$\mathcal{H}=\sum_{i,j} \mathbf{S}_i J_{ij}\mathbf{S}_j + \sum_{i} \mathbf{S}_i A_i \mathbf{S}_i + \mathbf{B} \sum_{i} \mathbf{g}_i\mathbf{S}_i $
{% endraw %}

where $S_i$ are spin vector operators, $J_{ij}$ are 3x3 matrices describing pair coupling between spins, $A_{ij}$ are 3x3 anisotropy matrices, $B$ is external magnetic field and $g_i$ is the g-tensor.

The core calculations in pySpinW are a rust port of the core calculations in SpinW, calculations are set up using a python interface. Unlike SpinW, pySpinW uses a constructive method for specifying simulations, a simple example is this for a Heisenberg ferromagnetic chain:

```python
from pyspinw import *

# Define the unit cell
unit_cell = UnitCell(1,1,1)

# Specify a magnetic atom at (0,0,0), with moment (0,0,1)
x = LatticeSite(0, 0, 0, 0, 0, 1, name="X")

# Create a magnetic structure (this could include a spacegroup, or 
# supercell structure, but we don't do so here)
structure = Structure([x], unit_cell=unit_cell)

# A single exchange between atoms in neighbouring unit cells (in the x direction)
exchanges = [HeisenbergExchange(x, x, cell_offset=(1,0,0), j=-1)]

# Create a Hamiltonian object that holds things together 
hamiltonian = Hamiltonian(structure, exchanges)
```

