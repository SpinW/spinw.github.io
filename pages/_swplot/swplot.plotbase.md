---
{title: swplot.plotbase, link: swplot.plotbase, summary: plots basis vectors, keywords: sample,
  sidebar: sw_sidebar, permalink: swplot_plotbase, folder: swplot, mathjax: true}

---
  
### Syntax
  
`swplot.plotbase(Name,Value)`
  
`hFigure = swplot.plotbase(Name,Value)`
 
### Description
  
`swplot.plotbase(Name,Value)` plots the three basis vectors that define
the coordinate system of the plot, either the $$abc$$ lattice vectors,
$$xyz$$ Descartes coodinate system or the $$hkl$$ reciprocal lattice vectors.
  
### Name-Value Pair Arguments
  
`'mode'`
: String that determines the type of basis vectors to plot. Possible
  values are:
  * `abc`     plots the lattice vectors (default),
  * `hkl`     plots the reciprocal lattice vectors,
  * `xyz`     plots the $$xyz$$ Descartes coordinate system.
  
`'length'`
: Determines the length of the 3 basis vectors. If 0, the
  length won't be rescaled. If non-zero, the `length` parameter
  determines the length of the plotted vectors in Å. Default value is
  2 Å.
  
`'label'`
: Logical variable, plots the vector labels if `true`. Default value is 
  `true`.
  
`'color'`
: Color of the arrows, either a cell of three color name strings or a
  matrix with dimensions of $${3\times 3]$$ where each column defines the
  RGB values of a color. Default value is `{'red' 'green' 'blue'}`.
  
`'R'`
: Radius of the arrow body, default value is 0.06 Å.
  
`'alpha'`
: Head angle of the arrow in degree units, default value is 30°.
  
`'lHead'`
: Length of the arrow head, default value is 0.5 Å.
  
`'d'`
: Distance from origin in $$xyz$$ units, default value is `[1 1 1]`.
  
`'dtext'` : Distance of the label from the arrow in xyz units, default
  value is 0.5 Å.
  
#### General paraters
 
These parameters have the same effect on any of the `swplot.plot...`
functions.
 
`'obj'`
: [spinw](spinw) object.
  
`'figure'`
: Handle of the swplot figure. Default value is the active figure handle.
  
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
 
`nPatch`
: Number of vertices on any patch object that is not the icosahedron,
  default value is stored in `swpref.getpref('npatch')`.
 

{% include links.html %}
