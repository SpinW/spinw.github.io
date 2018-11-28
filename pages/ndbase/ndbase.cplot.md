---
{title: ndbase.cplot, link: ndbase.cplot, summary: produces interplolated color plot
    of scattered data, keywords: sample, sidebar: sw_sidebar, permalink: ndbase_cplot,
  folder: ndbase, mathjax: true}

---
 
hPlot = NDBASE.CPLOT(dat, 'option1', value1, ...)
 
Input:
 
dat       Data, either array of spec1d type or struct with fields x, y
          and z.
 
Options:
 
x         X-values for spec1d data.
scale     Scalar, determines the scaling between the x- and y-axis for
          the interpolation. Default is 'auto'.
npix      Number of pixels either scalar or 2 element vector
          [npixx npixy].
plot      Logical, if true a plot will be produced.
scatter   If true, dots are plotted at the position of the given data
          points. Default is true.
convhull  If true, the color map is shown only between the given data
          points (within the convex hull of the points), this is achieved
          by giving nan value for all interpolated points outside of the
          convex hull. Default is true.
log       Plot natural logarithm of the values.
 
Output
 
hPlot     Handle of the plot object.
 

{% include links.html %}
