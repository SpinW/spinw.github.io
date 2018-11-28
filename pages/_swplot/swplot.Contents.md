---
{title: swplot package, link: swplot package, summary: package for 3D plotting, keywords: sample,
  sidebar: sw_sidebar, permalink: swplot, folder: swplot, mathjax: true}

---
 
The package contains functions that can create and control plotting of 3D
objects. It contains low level functions to plot specific shapes on any
figure (cylinder, line, arrow, ellipsoid, polyhedron, sphere, text) that
are vectorized for fast plotting of multiple objects using a single
[matlab:patch] command. Moreover it provides the [swplot.plot](swplot_plot) command to
plot multiple objects with specific color, transparency, label and legend
on the swplot figure including tha ability for smooth rotation and
translations via the mouse (that are much better than the default 3D
rotation with mouse in Matlab). Moreover it has high level commands to
plot crystals from SpinW objects (`swplot.plot...` commands).
 
### Files
 
#### Basic 3D objects
 
Plots primitive geometrical shapes, able to plot multiple objects when
input is vectorized. Can give considerable speedup because a single patch
command is used to plot multiple shapes.
 
* [swplot.arrow](swplot_arrow) creates a 3D arrow patch
* [swplot.circle](swplot_circle) creates a 3D circle surface patch
* [swplot.cylinder](swplot_cylinder) creates a closed/open 3D cylinder patch
* [swplot.ellipsoid](swplot_ellipsoid) creates a 3D ellipsoid patch
* [swplot.line](swplot_line) creates 3D line patch
* [swplot.polyhedron](swplot_polyhedron) creates convex polyhedra or polygon from vertex list
* [swplot.text](swplot_text) creates text at a 3D position
 
#### Creating and modifying swplot figure
 
These functions provide complete control over the transformations,
objects on an swplot figure. These are the alternatives to the Matlab
built in commands that control 3D plot axes. The advantage here is the
smooth mouse rotation/zoom functionality, nice legend and ability to
assign a tooltip text to any object that is triggered by a mouse click on
the object.
 
* [swplot.activefigure](swplot_activefigure) returns the handle of the active swplot figure
* [swplot.add](swplot_add) adds a graphical object to an swplot figure
* [swplot.base](swplot_base) sets the basis vectors of an swplot figure
* [swplot.clear](swplot_clear) clears swplot figure
* [swplot.close](swplot_close) closes swplot figure
* [swplot.delete](swplot_delete) deletes objects and corresponding data from swplot figure
* [swplot.export](swplot_export) exports swplot figure into raster/vector image
* [swplot.figure](swplot_figure) creates swplot figure
* [swplot.findobj](swplot_findobj) finds object data on swplot figure
* [swplot.getdata](swplot_getdata) gets the data stored in an swplot figure
* [swplot.legend](swplot_legend) adds legend to the swplot figure
* [swplot.mouse](swplot_mouse) adds mouse callbacks to swplot figure
* [swplot.plot](swplot_plot) plots objects to swplot figure
* [swplot.tooltip](swplot_tooltip) creates tooltip
* [swplot.transform](swplot_transform) transforms objects on swplot figure
* [swplot.translate](swplot_translate) translates objects on swplot figure
* [swplot.view](swplot_view) controls the 3D view direction
* [swplot.zoom](swplot_zoom) zooms to objects
 
#### Plotting SpinW object on swplot figure
 
These high level plot commands are used to plot different types of data
that is stored in the [spinw](spinw) object. All inputs of these commands can be
controlled from the [spinw.plot](spinw_plot) command.
 
* [swplot.plotatom](swplot_plotatom) plots crystal structure
* [swplot.plotbase](swplot_plotbase) plots basis vectors
* [swplot.plotbond](swplot_plotbond) plots bonds
* [swplot.plotcell](swplot_plotcell) plots unit cell
* [swplot.plotchem](swplot_plotchem) plots polyhedra or chemical bonds
* [swplot.plotion](swplot_plotion) plots magnetic ion properties
* [swplot.plotmag](swplot_plotmag) plots magnetic structure
 
#### Related functions
 
Helper function that can be also used as standalone.
 
* [swplot.color](swplot_color) generates RGB code from color name
* [swplot.icomesh](swplot_icomesh) creates mesh by subdividing icosahedron faces
* [swplot.logo](swplot_logo) creates the SpinW logo
* [swplot.subfigure](swplot_subfigure) changes position of figure window on the screen
* [swplot.subplot](swplot_subplot) create subplots with variable gaps between axes
 

{% include links.html %}
