---
{title: swplot.translate, link: swplot.translate, summary: translates objects on swplot
    figure, keywords: sample, sidebar: sw_sidebar, permalink: swplot_translate, folder: swplot,
  mathjax: true}

---
  
### Syntax
  
`swplot.translate(mode)`
  
`swplot.translate(mode, hFigure)`
 
### Description
  
`swplot.translate(mode)` translates the objects of an active swplot
figure, where the coordinate system is defined by the plane of the figure
with horizontal $$x$$-axis, vertical $$y$$-axis and out-of-plane $$z$$-axis.
  
`swplot.translate(mode, hFigure)` acts on the figure referenced by the
`hFigure` handle.
 
### Input Arguments
  
`mode`
: Either a vector with three numbers that determine the translation 
  vector in the figure plane coordinate system, or `'auto'` that
  centers figure to the middle of the objects. Default value is `'auto'`.
  
`hFigure`
: Handle of the swplot figure, default value is the active figure.
  
### See Also
  
[swplot.zoom](swplot_zoom)
 

{% include links.html %}
