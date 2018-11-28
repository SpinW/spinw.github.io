---
{title: swplot.tooltipcallback, link: swplot.tooltipcallback, summary: callback for
    displaying tooltip, keywords: sample, sidebar: sw_sidebar, permalink: swplot_tooltipcallback,
  folder: swplot, mathjax: true}

---
  
### Syntax
  
`swplot.tooltipcallback(obj,hit,hFigure,hTransform)`
  
### Description
  
`swplot.tooltipcallback(obj,hit,hFigure,hTransform)` is the callback
function that is automatically added to any object on an [swplot] figure
that is created using one of the `swplot.plot...` commands with `tooltip`
parameter set to `true`.
  
### Input Arguments
  
`obj`
: [spinw](spinw) object.
  
`hit`
:  Hit object, defines the point where the mouse clicked.
  
`hFigure`
: Handle of parent swplot figure.
  
`hTransform`
: Parent [hgtransform](https://www.mathworks.com/help/matlab/ref/hgtransform.html) object if exists.
  
### See Also
  
[swplot.tooltip](swplot_tooltip)
 

{% include links.html %}
