---
{title: swplot.plotcell, link: swplot.plotcell, summary: plots unit cell, keywords: sample,
  sidebar: sw_sidebar, permalink: swplot_plotcell, folder: swplot, mathjax: true}

---
  
### Syntax
  
`swplot.plotcell(Name,Value)`
  
`hFigure = swplot.plotcell(Name,Value)`
 
### Description
  
`swplot.plotcell(Name,Value)` plots the edges of the unit cell or
multiple unit cells.
  
### Name-Value Pair Arguments
  
`'mode'`
: String that determines how the cells are plotted:
  * `'inside'`    unit cells are plotted inside the volume defined by the
                  given `range` parameter (default),
  * `'single'`    a single unit cell is plotted at the origin,
  * `'outside'`   unit cells are plotted inclusive the volume defined
                  by the `range` parameter.
  
`'color'`
: Color of the edges of the cells, one of the following values:
  * `'auto'`      all edges will be black,
  * `'colorname'` all edges will have the same color defined by the
                  string, e.g. `'red'`,
  * `[R G B]`     all edges will have the same color defined by the RGB
                  code.
  
`'lineStyle'`
: Determines the line style of the edges. Possible values are:
  * `'--'`        dahsed edges (default),
  * `'-'`         edges as continuous lines,
  * `':'`         edges as dotted lines,
  * `'-.'`        edges as dash-dotted lines.
  
`'lineWdith'`
: Line width of the edges, default value is 1 pt.
  
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
 
The name of the objects `'cell'`.
To find the handles and the corresponding data on these objects, use e.g.
sObject = swplot.findobj(hFigure,'name','cell')`.
 

{% include links.html %}
