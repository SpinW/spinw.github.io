---
{title: swplot.view, link: swplot.view, summary: controls the 3D view direction, keywords: sample,
  sidebar: sw_sidebar, permalink: swplot_view, folder: swplot, mathjax: true}

---
  
### Syntax
  
`swplot.view(ax)`
  
`swplot.view(ax, hFigure)`
 
### Description
  
`swplot.view(ax)` controls the plane that the camera sees. The
preconfigured options are pairs of $$abc$$ axes or $$hkl$$ reciprocal lattice
axes.
  
### Input Arguments
  
`ax`
: String that controls the view plane, recognised values are:
  * `'ab'`\|`'bc'`\|`'ac'`  the two axes define the view plane,
  * `'hk'`\|`'kl'`\|`'hl'`  the two reciprocal lattice vectors define
                            the view plane.
  
`hFigure`
: Handle of the swplot figure window, default value is the active swplot
  figure.
 

{% include links.html %}
