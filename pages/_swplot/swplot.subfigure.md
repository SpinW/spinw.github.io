---
{title: swplot.subfigure, link: swplot.subfigure, summary: changes position of figure
    window on the screen, keywords: sample, sidebar: sw_sidebar, permalink: swplot_subfigure,
  folder: swplot, mathjax: true}

---
  
### Syntax
  
`swplot.subfigure(m,n,p)`
  
`swplot.subfigure(m,n,p,hFigure)`
 
### Description
  
`swplot.subfigure(m,n,p)` changes the position of the current figure
window on the screen, the position is determined similarly to the Matlab
function [subplot](https://www.mathworks.com/help/matlab/ref/subplot.html). Here the screen is the canvas where the figure
window is positioned.
   
The function divides the display into an $$m$$-by-$$n$$ grid and moves the
figure window in the position specified by $$p$$. It numbers the figures by
row major, such that the first figure is the first column of the first
row, the second figure is the second column of the first row, and so on.
 
`swplot.subfigure(m,n,p,hFigure)` repositions the figure related to
`hFigure` handle.
  
### Input Arguments
  
`m,n,p`
: Integer numbers that define the figure window position.
  
`hFigure`
: Handle of the figure window, optional. Default value is [gcf](https://www.mathworks.com/help/matlab/ref/gcf.html).
 

{% include links.html %}
