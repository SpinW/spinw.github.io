---
{title: swplot.zoom, link: swplot.zoom, summary: zooms to objects, keywords: sample,
  sidebar: sw_sidebar, permalink: swplot_zoom, folder: swplot, mathjax: true}

---
  
### Syntax
  
`swplot.zoom(mode)`
  
`swplot.zoom(mode, hFigure)`
 
### Description
  
`swplot.zoom(mode)` controls the zoom (angle of view of the virtual
camera) level on the active [swplot] figure.
  
`swplot.zoom(mode, hFigure)` controls the zoom on the swplot figure
referenced by the `hFigure` handle.
 
### Input Arguments
  
`mode`
: Either a number determining the relative zoom value, or `'auto'`
  that zooms to fit every object into the figure.
  
`hFigure`
: Handle of the swplot figure, default value is the active swplot figure.
  
### See Also
  
[swplot.figure](swplot_figure)
 

{% include links.html %}
