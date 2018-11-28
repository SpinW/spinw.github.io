---
{title: swplot.tooltip, link: swplot.tooltip, summary: creates tooltip, keywords: sample,
  sidebar: sw_sidebar, permalink: swplot_tooltip, folder: swplot, mathjax: true}

---
  
### Syntax
  
`swplot.tooltip(switch)`
  
`swplot.tooltip(switch,hFigure)`
 
`swplot.tooltip(switch,hFigure,window)`
 
`status = swplot.tooltip`
 
### Description
  
`swplot.tooltip(switch)` creates/deletes the tooltip axis on the active
swplot figure.
   
`swplot.tooltip(switch,hFigure)` controls the tooltip on the swplot
figure referenced by `hFigure` handle.
  
`swplot.tooltip(switch,hFigure,window)` the `window` argument controls
whether the tooltip is shown in a separate window of not.
 
`status = swplot.tooltip` returns the tooltip status, one of the strings
`'on'`\|`'off'`.
 
### Examples
  
Add the tooltip to an [swplot] figure:
 
```matlab
swplot.figure
swplot.addcircle([0 0 0],[0 0 1],1)
swplot.tooltip
```
  
### Input Arguments
  
`switch`
: String, with recognised values of `'on'`\|`'off'` which switches the
  tooltip on/off respectively. If it is any other string, the text will
  be shown in the tooltip. Default value is 'on'.
  
`hFigure`
: Handle of the [swplot] figure. Default value is the active figure.
  
`window`
: If `true`, the tooltips will be shown in a separate window.
  Default value is `false`.
  
### Output Arguments
  
`status`
: String, one of the `'on'`\|`'off'` values depending on the status of
  the tooltip axis.
 

{% include links.html %}
