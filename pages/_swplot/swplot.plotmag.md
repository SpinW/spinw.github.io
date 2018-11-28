---
{title: swplot.plotmag, link: swplot.plotmag, summary: plots magnetic structure, keywords: sample,
  sidebar: sw_sidebar, permalink: swplot_plotmag, folder: swplot, mathjax: true}

---
  
### Syntax
  
`swplot.plotmag(Name,Value)`
  
`hFigure = swplot.plotmag(Name,Value)`
### Description
  
`swplot.plotmag(Name,Value)` plots the magnetic structure stored in a
[spinw](spinw) object onto an swplot figure. The magnetic structure is
represented by arrows on the magnetic atoms.
  
### Name-Value Pair Arguments
  
`'mode'`
: String that defines the way the magnetic moments are plotted:
  * `'all'`       Plot both the rotation plane of single-k incommensurate
                  magnetic structures and the moment directions.
  * `'circle'`    Plot only the rotation plane of incommensurate
                  magnetic structures.
  * `'arrow'`     Plots only the moment directions.
  
`'label'`
: Whether to plot labels for magnetic atoms, default value is `true`.
  
`'dText'`
: Distance between atom and its text label, default value is 0.1
  Å.
  
`'fontSize'`
: Font size of the text labels in pt, default value is stored in
  `swpref.getpref('fontsize')`.
  
`'color'`
: Color of the magnetic moment vectors, one of the following values:
  * `'auto'`      all moments get the color of the magnetic atom,
  * `'colorname'` all moments will have the same color defined by the
                  string, e.g. `'red'`,
  * `[R G B]`     all moments will have the same color defined by the RGB
                  code.
  
`'scale'`
: Scaling factor for the lenght of the magnetic moments relative
  to the length of the shortest bond (if there are no bonds, 3 Å 
  is taken as bond length). Default value is 0.4.
  
`'normalize'`
: If `true`, all moment length will be normalized to the scale
  factor, default value is `false`.
  
`'radius0'`
: Radius value of arrow body, default value is 0.06 Å.
  
`'ang'`
: Angle of the arrow head in degree units, default value is 30 °.
  
`'lHead'`
: Length of the arrow head, default value is 0.5 Å.
  
`'alpha'`
: Transparency (alpha value) of the circle, representing the
  rotation plane of the moments, default value is 0.07.
  
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
 
The name of the objects are `'mag'`.
To find the handles and the corresponding data on these objects, use e.g.
sObject = swplot.findobj(hFigure,'name','mag')`.
 

{% include links.html %}
