---
{title: swplot.plotatom, link: swplot.plotatom, summary: plots crystal structure,
  keywords: sample, sidebar: sw_sidebar, permalink: swplot_plotatom, folder: swplot,
  mathjax: true}

---
  
### Syntax
  
`swplot.plotatom(Name,Value)`
  
`hFigure = swplot.plotatom(Name,Value)`
 
### Description
  
`swplot.plotatom(Name,Value)` plots the crystal structure of a SpinW
object onto an swplot figure where each atom is shown as a sphere. It can
display text labels, control the radius and color of the spheres.
   
`hFigure = swplot.plotatom(Name,Value)` returns the handle of the swplot
figure.
 
### Name-Value Pair Arguments
  
`'mode'`
: String that defines the types of atoms to plot:
  * `'all'`       plot all atoms (default),
  * `'mag'`       plot magnetic atoms only,
  * `'nonmag'`    plot non-magnetic atoms only.
  
`'label'`
: Whether to plot the labels of the atoms, default value is `false`.
  
`'dText'`
: Distance between the atom and its text label, default value is 0.1
  Å.
  
`'fontSize'`
: Font size of the atom labels in pt, default value is read using
  `swpref.getpref('fontsize')`.
  
`'radius'`
: Defines the atom radius, one of the following strings:
  * `'fix'`       Sets the radius of all atoms to the value
                  of the `radius0` parameter,
  * `'auto'`      determine the atom radius based on the atom
                  label (e.g. the radius of Cr atom is
                  `sw_atomdata('Cr','radius')`) and multiply the value by
                  the `radius0` parameter.
 
`'radius0'`
: Constant atom radius, default value is 0.3 Å.
  
`'color'`
: Color of the atoms, one of the following values:
  * `'auto'`      all atom gets the color stored in [spinw.unit_cell](spinw_unit_cell),
  * `'colorname'` all atoms will have the same color defined by the
                  string, e.g. `'red'`,
  * `[R G B]`     all atoms will have the same color defined by the RGB
                  code.
 
#### General paraters
 
These parameters have the same effect on any of the `swplot.plot...`
functions.
 
`'obj'`
: [spinw](spinw) object.
  
`'unit'`
: Unit in which the plotting range is defined. It can be one of the
  following strings:
  * `'lu'`        plot range is defined in lattice units (default),
  * `'xyz'`       plot range is defined in the $$xyz$$ Cartesian coordinate
                  system in Å units.
 
`'range'`
: Defines the plotting range. Depending on the `unit` parameter, the
  given range can be in lattice units or in units of the $$xyz$$ Cartesian
  coordinate system. It is either a matrix with dimensions of $$[3\times
  2]$$ where the first and second columns define the lower and upper plot
  limits respectively. It can be alternatively a vector with three
  elements `[a,b,c]` which is equivalent to `[0 a;0 b;0 c]`. Default
  value is `[0 1;0 1;0 1]` to show a single cell.
  
`'figure'`
: Handle of the swplot figure. Default value is the active figure handle.
  
`'legend'`
: Whether to show the plot on the legend, default value is `true`.
 
`'tooltip'`
: If `true`, the tooltips will be shown when clicking on the plot
  objects. Default value is `true`.
  
`'shift'`
: Column vector with 3 elements, all object positions will be
  shifted by the given value in Å units. Default value is
  `[0;0;0]`.
  
`'replace'`
: If `true` the plot will replace the previous plot of the same type.
  Default value is `true`.
  
`'translate'`
: If `true`, the plot will be centered, independent of the range. Default
  value is `false`.
  
`'zoom'`
: If `true`, the swplot figure will be zoomed to make the plot objects
  cover the full figure. Default is `true`.
  
`'copy'`
: If `true`, a clone of the [spinw](spinw) object will be saved in the
  swplot figure data which can be retwrived using
  `swplot.getdata('obj')`. If `false`, the handle of the original [spinw](spinw)
  object is saved which is linked to the input `obj` and so it changes
  when `obj` is changed. Default value is `false`.
  
`nMesh`
: Mesh of the ellipse surface, a triangulation class object or an
  integer that used to generate an icosahedron mesh with $$n_{mesh}$$
  number of additional subdivision into triangles. Default value is
  stored in `swpref.getpref('nmesh')`, see also [swplot.icomesh](swplot_icomesh).
  
`nPatch`
: Number of vertices on any patch object that is not the icosahedron,
  default value is stored in `swpref.getpref('npatch')`.
 
### Output Arguments
  
`hFigure`
: Handle of the swplot figure.
 
The name of the objects that are created are `'atom'` and `'atom_label'`.
To find the handles and the corresponding data on these objects, use e.g.
sObject = swplot.findobj(hFigure,'name','atom')`.
 

{% include links.html %}
