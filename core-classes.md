---
layout: page
title: pySpinW Core Classes and Methods
subtitle: Interacting with pySpinW
use_math: true
---

This page contains a list of the classes and functions that users will likely want to use. 
There are three broad categories (1) classes that users might create directly (2) helper functions 
(3) classes that users will use, but not create directly.

Classes and functions designed to called directly by the user are made accessible by doing `from pyspinw import *`

## User Facing Classes 

The user facing classes are for defining the system, there are also a number of helper functions that make it easier to create large numbers of them.

  * `LatticeSite` - Lattice position and spin of unit cells
  * `UnitCell` - The unit cell
  * `Structure` - Contains the magnetic structure details: a list of sites, the unit cell, spacegroup and supercell
  * `Exchange` interactions, multiple subclasses
  * `Hamiltonian`
  * `Sample` definitions, these are used to define things like twins and powders
  * Supercell definitions:
    * `PropagationVector` and `CommensuratePropagationVector`
    * `SupercellTransform` for use with the `TransformationSupercell`
    * Various `Supercell` subclasses


## Helper Functions
  * `spacegroup`


## Indirectly Created Classes

  * Spacegroup

# Detailed listing

## `LatticeSite`

## `UnitCell`

## 

## Supercell Classes

Supercells come in two flavours, commensurate and incommensurate. As there are differing strategies for calculations with commensurate and incommensurate structures, these are treated differently. The `Supercell` and `CommensurateSupercell` classes are abstract and cannot be created.

### Commensurate

  * `TiledSupercell`
  * `SummationSupercell`
  * `TransformationSupercell`

### Incommensurate

  * `RotatingSupercell`