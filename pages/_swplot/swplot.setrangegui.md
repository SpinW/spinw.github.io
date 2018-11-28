---
{title: swplot.setrangegui, link: swplot.setrangegui, summary: GUI to change the plotting
    range, keywords: sample, sidebar: sw_sidebar, permalink: swplot_setrangegui, folder: swplot,
  mathjax: true}

---
  
### Syntax
  
`swplot.setrangegui`
 
`swplot.setrangegui(hFigure)`
 
`swplot.setrangegui(~,~,hfigure)`
  
### Description
  
`swplot.setrangegui` produces a window that enables changing
the limits of the active swplot figure. After changing the range, every
object that is created with the `swplot.plot...` commands will be
replotted using the new `range` parameter.
   
`swplot.setrangegui(hFigure)` chow the gui for the swplot figure related
the `hFigure` handle.
   
`swplot.setrangegui(~,~,hfigure)` can be used in figure callbacks, for
example by assigning it to `'ClickedCallback'` property of a button.
  
### Input Arguments
  
`hFigure`
: Handle of the swplot figure. Default value is the active figure.
 

{% include links.html %}
