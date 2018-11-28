---
{title: swplot.plotchem, link: swplot.plotchem, summary: plots polyhedra or chemical
    bonds, keywords: sample, sidebar: sw_sidebar, permalink: swplot_plotchem, folder: swplot,
  mathjax: true}

---
  
### Syntax
  
`swplot.plotchem(Name,Value)`
  
`hFigure = swplot.plotchem(Name,Value)`
 
### Description
  
`swplot.plotchem(Name,Value)` plots polyhedra around selected atoms, or
chemical bonds between atoms on an swplot figure. 
  
### Name-Value Pair Arguments
  
`'mode'`
: String that selects the type of the plot, one of the following:
  * `'poly'`      draws polyhedra around the center atoms
                  (default),
  * `'bond'`      draws bonds between the given atoms.
  
`'atom1'`
: Indices of atoms stored in [spinw.unit_cell](spinw_unit_cell) for the center atom
  of the polyhedra or the first atom of the bonds. Can be also a
  string that identifies the atoms by their labels.
  
`'atom2'`
: Indices or label of the atoms stored in [spinw.unit_cell](spinw_unit_cell). It
  determines the vertices of the polyhedra or gives the second
  atom of a bond.
  
`'extend'`
: If `true`, the starting of the bonds or center of polyhedra will be
  restricted within the given `range`, while the surrounding atoms or end
  of bonds (defined by `atom2`) are not restricted. if `extend` is set to
  `false`, only those bonds/polyhedra will be plotted that are completely
  inside the volume defined by the `range` parameter.
  
`'limit'`
: Can be a single number, which defines the number vertices of the
  polyhedra (`mode` set to `'poly'`) or the number of neighboring atoms
  (identified by`atom2`) that will be connected to `atom1`. If can be
  also a row vector with 2 elements `[dmin dmax]` that defines the
  neighbors of `atom1` via a minimum and maxium distance in Å units.
  Default value is 6 to plot octahedra around `atom1` type atoms (when
  `mode` is set to `poly`).
  
`'alpha'`
: Transparency of the plotted surfaces, value between 0 and 1 (1 for
  opaque, 0 for transparent). Default value is 1 for bonds and
  0.3 for polyhedron.
  
`'color'`
: Color of the objects, one of the following values:
  * `'auto'`      the color of all objects will be set to the color of
                  `atom1`,
  * `'colorname'` all objects will have the same color defined by the
                  string, e.g. `'red'`,
  * `[R G B]`     all objects will have the same color defined by the RGB
                  code.
  * `'none'`      no faces will be shown.
  
`'color2'`
: Color of the edges of the polyhedra (unused for bonds), default
  value is `'auto'` when the edge will have the same color as the faces,
  see the `color` parameter, using `'none'` will remove the edges.
  
`'radius0'`
: Radius of the bond cylinder, default value is 0.03 Å.
  
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
 
The name of the objects is `'chem'`.
To find the handles and the corresponding data on these objects, use e.g.
sObject = swplot.findobj(hFigure,'name','chem')`.
 

{% include links.html %}
