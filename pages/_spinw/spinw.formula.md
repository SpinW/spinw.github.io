---
{title: spinw.formula method, link: spinw.formula, summary: returns basic physical
    properties, keywords: sample, sidebar: sw_sidebar, permalink: spinw_formula, folder: spinw,
  mathjax: true}

---
 
### Syntax
 
`formula = formula(obj)`
 
### Description
 
`result = formula(obj)` returns chemical mass, density, cellvolume etc.
of `obj`.
 
### Examples
 
The formula of the crystal stored in the
[https://raw.githubusercontent.com/SpinW/Models/master/cif/Ca2RuO4.cif](https://raw.githubusercontent.com/SpinW/Models/master/cif/Ca2RuO4.cif) linked file will be
printed onto the Command Window.
 
```matlab
cryst = spinw('https://raw.githubusercontent.com/SpinW/Models/master/cif/Ca2RuO4.cif')
cryst.formula
```
*Output*
```
     Chemical formula:  Ca2O4Ru1
     Formula mass:       245.224 g/mol
     Formula in cell:          4 units
     Cell volume:        355.397 Å³
     Density:              4.583 g/cm³
```
 
 
### Name-Value Pair Arguments
 
`'obj'`
: [spinw](spinw) object.
 
### Output Arguments
 
`formula` struct variable with the following fields:
* `m`         Mass of the unit cell in g/mol units.
* `V`         Calculated volume of the unit cell in length units (defined in [spinw.unit](spinw_unit)).
* `rho`       Density in g/cm$$^3$$.
* `chemlabel` List of the different elements.
* `chemnum`   Number of the listed element names
* `chemform`  Chemical formula string.
 

{% include links.html %}
