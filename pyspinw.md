---
layout: page
title: pySpinW Overview
use_math: true
---

<div class="row text-center">
    <img src="/img/pyspinw_logo.png" alt="SpinW Hamiltonian" />
</div>


pySpinW is capable of calculating magnon dispersion curves, optimising magnetic structures, visualising systems, and predicting the results of inelastic scattering experiments. 
In general, we solve a system with a Hamiltonian of the form:

<div class="row text-center">
    <img src="/img/hamiltonian.png" alt="SpinW Hamiltonian" />
</div>

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


The following is a list of the classes and functions that users will likely want to use. 
There are three broad categories (1) classes that users might create directly (2) helper functions 
(3) classes that users will use, but not create directly.

Classes and functions designed to called directly by the user are made accessible by doing `from pyspinw import *`

## User Facing Classes 

The user facing classes are for defining the system, there are also a number of helper functions that make it easier to create large numbers of them.

  * `LatticeSite` - Lattice position and spin of unit cells
  * `UnitCell` - The unit cell
  * `Structure` Contains the magnetic structure details: a list of sites, the unit cell, spacegroup and supercell
  * Exchange interactions, one of
    * `HeisenbergExchange` scalar exchange term
    * `DMExchange` Dzyaloshinskii–Moriya exchange
    * `Exchange` is the most general exchange term, specify a matrix
    * `DiagonalExchange` diagonal matrix with independent entries
    * `XYExchange` matrix with same value entries, and on in x and y diagonals
    * `XXZExchange` diagonal, same value in x and y, different in z
    * `IsingExchange` only a z term
  * Anisotropy, either 
    * `AxisMagnitudeAnisotropy` specified by an axis and signed magnitude
    * `Anisotropy` general matrix form
  * `Hamiltonian` this holds all the data for doing energy calculations, it is the main object that functions are called on, these include
    * `energy_plot`, `spagetti_plot` and `spaghetti_plot_dual` for plotting
    * `energies_and_intensities` for getting the data from calculations
    * `text_summary` and `print_summary` for getting information in text form
    * `expanded` Converts a supercell structure into single large cell
    * `ground_state` returns a new Hamiltonian with an minimal energy ground state
    * `parameterized` constructs a function (callable) of specified coupling/anisotropy parameters
  * Sample definitions, these are used to define the macroscopic structure
    * `Twin` is used to represent twinned systems
    * `Powder` is used to represent powder samples, and provides some methods for fitting
  * Supercell definitions:
    * `PropagationVector` and `CommensuratePropagationVector` are used to define propagation vectors
    * There are various `Supercell` subclasses:
      * `TiledSupercell`
      * `SummationSupercell`
      * `TransformationSupercell`
      * `RotationSupercell`
  * `SupercellTransform` is for use with the `TransformationSupercell`
    


## Helper Functions
  * `spacegroup` - takes a string describing a spacegroup and returns a `Spacegroup` object. This function is capable of dealing with many different ways of writing the spacegroup, including though an partial operator list.
  * `generate_*` functions
    * `generate_sites` automatically creates a list of sites
    * `generate_exchanges` automatically creates a list of exchanges
  * `view` Graphically show a Hamiltonian

## Indirectly Created Classes

  * `Spacegroup` - these contain details
  * `HamiltonianParameterization`
  * `PowderParameterization`
