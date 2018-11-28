---
{title: swplot.plotion, link: swplot.plotion, summary: plots magnetic ion properties,
  keywords: sample, sidebar: sw_sidebar, permalink: swplot_plotion, folder: swplot,
  mathjax: true}

---
  
### Syntax
  
`swplot.plotion(Name,Value)`
  
`hFigure = swplot.plotion(Name,Value)`
 
### Description
  
`swplot.plotion(Name,Value)` visualizes selected properties of magnetic
ions stored in a [spinw](spinw) object onto an swplot figure. The supported
properties are the g-tensor and single ion anisotropy.
  
### Name-Value Pair Arguments
  
`'mode'`
: String that defines the type of property that is visualized:
  * `'aniso'`     ellipsoid is plotted to visualize single ion anisotropy,
  * `'g'`     	ellipsoid is plotted to visualize g-tensor.
  
`'scale'`
: Scaling factor for the size of the ellipsoid relative to the 
  shortest bond length. Default value is 1/3.
  
`'alpha'`
: Transparency (alpha value) of the ellipsoid (1 for opaque, 0 for
  transparent), default value is 0.3.
  
`'radius1'`
: Minimum radius of the ellipsoid, default value is 0.08 Å.
  
`'lineWidth'`
: Line width in pt of the main circles surrounding the ellipsoid, 
  if zero no circles are drawn. Default is 0.5 pt.
  
`'color'`
: Color of the ellipsoid, one of the following values:
  * `'auto'`      all ellipsoids get the color of the central atom,
  * `'colorname'` all ellipsoids will have the same color defined by the
                  string, e.g. `'red'`,
  * `[R G B]`     all ellipsoids will have the same color defined by the RGB
                  code.
`'color2'`
: Color of the lines of the main circles, default value is `'auto'` when
  the ellipses will have the same color as the ellipsoids. Can be either
  a row vector of RGB code or string of a color name, see the `color`
  parameter.
  
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
 
The name of the objects that are created are `'ion'` and `'ion_edge'`.
To find the handles and the corresponding data on these objects, use e.g.
sObject = swplot.findobj(hFigure,'name','ion')`.
 

{% include links.html %}
