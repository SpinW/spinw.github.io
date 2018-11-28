---
{title: swplot.plotbond, link: swplot.plotbond, summary: plots bonds, keywords: sample,
  sidebar: sw_sidebar, permalink: swplot_plotbond, folder: swplot, mathjax: true}

---
  
### Syntax
  
`swplot.plotbond(Name,Value)`
  
`hFigure = swplot.plotbond(Name,Value)`
 
### Description
  
`swplot.plotbond(Name,Value)` plots the magnetic bonds stored in
[spinw.coupling](spinw_coupling). It can plot bonds using different styles, such as
arrows, lines or cylinders and allows controlling the the line style,
cylinder radius, color, etc. The command can also plot cylinders with
radii that are dependent on the strength of the exchange interaction
assigned to the particular bond.
  
### Name-Value Pair Arguments
  
`'mode'`
: String that defines the style of the bond:
  * `'cylinder'`   bonds are plotted as cylinders connecting the two atoms
                  (default),
  * `'arrow'`      bonds are plotted as arrows (default if DM
                  interactions are present),
  * `'line'`       bonds are plotted as lines,
  * `'empty'`      no bonds are plotted.
  
`'mode2'`
: String that defines what object is plotted on the middle of the bond:
  * `'none'`      don't plot anything on the bond (default),
  * `'antisym'`   plot the antisymmetric part (DM vector) of the 
                  exchange on the middle point of the bond
                  (default if DM vectors are non-zero),
  * `'sym'`       plot an ellipsoid (corresponding to the symmetric
                  exchange) on the middle of the bond.
  
`'sign'`
: String that defines how the ellipsoids are generated for exchange
  matrices that contain both negative and positive eigenvalues.
  Possible values are:
  * `'abs'`       The absolute value of the eigenvalues is used,
                  this works nicely except that AFM and FM values
                  will have the same radius (default).
  * `'min'`       If there is a negative eigenvalue, it is
                  shifted to zero with all other egeinvalues
                  equally. This works nicely to emphasize AFM
                  type values in the exchange matrix. Problem is
                  that 0 exchange values can be assigned non-zero
                  radius.
  * `'max'`       Same as `'min'`, except the positive eigenvalues are
                  shifted to zero. This works nicely to emphasize
                  FM type exchange values, has the same problem
                  as the `'min'` option.
  
`'linewidth'`
: Defines the bond radius if `mode` is set to `line`, one of the folling
  strings:
  * `'fix'`       All lines will have a width defined by the `linewidth0`
                  parameter (default).
  * `'lin'`       Lines will have a width that is depending 
                  linearly on the exchange matrix on the bond:
                         `~Width ~ sum(abs(J))`, 
                  where the largest line width on
                  the strongest bond is given by `linewidth0`.
  * `'pow'`       Same as `'auto'`, but the line width is a
                  power function of the exchange value:
                  `W~(sum(abs(J))).^widthpow`.
  
`'widthpow'`
: Defines the power that determines the linewidth if `linewidth`
  parameter is set to `'pow'`.
  
`'linewidth0'`
: Line width in pt used to draw the bond if `mode` parameter is `'line'`. 
  Default value is 0.5.
  
`'lineStyle'`
: Determines the line style when `mode` parameter is `'line'`. Possible
  values are:
  * `'auto'`      Bonds are plotted as continuous/dashed lines
                  depending on the label of the corresponding
                  matrix (dashed line is used if the matrix
                  label ends with `'-'`, otherwise continuous) (default).
  * `'--'`        Bonds are plotted as dashed lines.
  * `'-'`         Bonds are plotted as lines.
  * `':'`         Bonds are plotted using dotted lines.
  * `'-.'`        Bonds are plotted using dash-dotted lines.
  
`'zero'`
: If `true`, bonds with zero exchange matrix will be plotted as
  well. Default value is `true`.
  
`'radius0'`
: Radius of the cylinder when `mode` parameter is set to `'cylinder'`.
  Default value is 0.05 Å.
  
`'radius1'`
: Radius of the DM vector and the minimum radius of the 
  ellipsoid, default value is 0.08 Å.
  
`'radius2'`
: Constant atom radius, default value is 0.3 Å.
  
`'radius'`
: Defines the atom radius (important for arrow bonds, to avoid
  overlap with the spheres of the atoms), see [swplot.plotatom](swplot_plotatom):
  * `'fix'`       Sets the radius of all atoms to the value
                  given by the `radius2` parameter.
  * `'auto'`      use radius data from database based on the atom
                  label multiplied by the `radius2` option value.
  
`'ang'`
: Angle of the arrow head in degree units, default value is 30°.
  
`'lHead'`
: Length of the arrow head, default value is 0.3 Å.
  
`'scale'`
: Scaling factor for the length of the DM vector or the size of
  the ellipsoid relative to the shortest bond length. Default 
  value is 1/3.
  
`'color'`
: Color of the bonds, one of the following values:
  * `'auto'`      all bonds gets the color stored in [spinw.matrix](spinw_matrix),
  * `'colorname'` all bonds will have the same color defined by the
                  string, e.g. `'red'`,
  * `[R G B]`     all bonds will have the same color defined by the given
                  RGB code.
  
`'color2'`
: Color of the ellipse or DM vector on the bond:
  * `'auto'`      all object get the color of the bond,
  * `'colorname'` all object will have the same color defined by the
                  string, e.g. `'red'`,
  * `[R G B]`     all objects will have the same color defined by the
                  given RGB code.
  
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
 
The name of the objects that are created are `'bond'`.
To find the handles and the corresponding data on these objects, use e.g.
sObject = swplot.findobj(hFigure,'name','bond')`.
 
*[DM]: Dzyaloshinskii-Moriya
*[FM]: FerroMagnet
*[AFM]: AntiFerromagnet
 

{% include links.html %}
