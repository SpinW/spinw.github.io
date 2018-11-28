---
{title: sw_bonddim, link: sw_bonddim, summary: find dimensionality of a periodic bond
    network, keywords: sample, sidebar: sw_sidebar, permalink: sw_bonddim, folder: swfiles,
  mathjax: true}

---
  
### Syntax
  
`l = sw_bonddim(c, {natom})`
  
### Description
  
`l = sw_bonddim(c, {natom})` splits the given periodic bond network into
disjunct subsystems and determines the dimensionality of each subsystem.
  
### Examples
 
Check the bond dimensionality of the triangular lattice:
 
```matlab
tri = sw_model('triAF')
```
*Output*
```
Preparing 'triAF' model ...
Creating the bond list (maxDistance = 10 Å, nCell = 7x5x2)...
...25 bonds are retained out of 440 generated!
... ready!
tri = 
     SpinW object, spinw class:
     Chemical formula: A1
     Space group:      P 0
     Lattice:
       a= 3.0000 Å, b= 3.0000 Å, c= 9.0000 Å
       α= 90.00°,   β= 90.00°,   γ=120.00°
     Magnetic atoms in the unit cell: 1
     Mode:
       symbolic: off, symmetry: off, textoutput: "stdout"
```
 
```matlab
sw_bonddim(tri.intmatrix.all)
```
*Output*
```
  0×0 empty struct array with fields:
    D
    base
    site
```
 
 
### Input Arguments
  
`C`
: Bond list in a matrix with dimensions of $$[5\times n_{bond}]$$, where the meaning of
  the rows are:
  * `#1:#3`   Lattice translations between the coupled atoms in
              lattice units (always integer).
  * `#4`      Index of the bond starting atom.
  * `#5`      Index of the bond end atom.
 
  For example for a chain along b-axis on a Bravais lattice:
      `C = [1;1;0;1;0]`
  
`nAtom`
: Number of atoms in the unit cell. If not given, the maximum
  atom index from the bond list is taken.
  
### Output Arguments
  
`L`
: Struct with the number of elements equal to the number of
          subsystems, it has the following fields:
  * `D`       Dimensionality of the subsystem $$(0\leq D\leq 3)$$.
  * `base`    Basis vectors spanning the subsystem stored in a
                      $$[3\times D]$$ matrix where each column denotes a basis
                      vector.
  * `site`    List of sites that belong to the subsystem.
 

{% include links.html %}
