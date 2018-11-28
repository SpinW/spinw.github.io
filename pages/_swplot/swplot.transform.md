---
{title: swplot.transform, link: swplot.transform, summary: transforms objects on swplot
    figure, keywords: sample, sidebar: sw_sidebar, permalink: swplot_transform, folder: swplot,
  mathjax: true}

---
  
### Syntax
  
`swplot.transform(T)`
  
`swplot.transform(T, hFigure)`
 
`T = swplot.transform'
 
### Description
  
`swplot.transform(T)` transforms the objects on the active [swplot] figure
using the transformation matrix `T`.
   
`swplot.transform(T, hFigure)` transforms objects on the [swplot] figure
referenced by the `hFigure` handle.
 
`T = swplot.transform' returns the transfomation matrix of the active
[swplot] figure.
 
{% include note.html content=" If the figure is created without the `hgtransform` object, the
  transformation matrix moves the camera." %}
 
### Input Arguments
  
`M`
: Transformation matrix with the following dimensions:
  * $$[4\times4]$$      This follows the Matlab standard definition of coordinate transformations used by [hgtransform](https://www.mathworks.com/help/matlab/ref/hgtransform.html).
  * $$[3\times 4]$$     This is the SpinW format for space group 
                      transformations, see [swsym.str](swsym_str). 
  * $$[3\times 3]$$     This defines a rotation matrix only.
      
  Setting `M` to 0 returns the plot to the original orientation
  (equivalent to `M=eye(4)`).
  
`hFigure`
: Handle of the swplot figure window, default value if the handle of the
  active figure.
  
### Output Arguments
 
`T`
: Transformation matrix of the figure with dimensions of $$[4\times 4]$$.
    
### See Also
 
[swplot.figure](swplot_figure) \| [hgtransform](https://www.mathworks.com/help/matlab/ref/hgtransform.html)
 

{% include links.html %}
