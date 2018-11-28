---
{title: ndbase.spaghetti, link: ndbase.spaghetti, summary: creates spaghetti plot
    from d2d objects, keywords: sample, sidebar: sw_sidebar, permalink: ndbase_spaghetti,
  folder: ndbase, mathjax: true}

---
 
udat = NDBASE.SPAGHETTI(dat, 'option1', value1, ...)
 
Input:
 
dat       Array of d2d class objects with nDat member. Typically Horace
          cuts.
 
Options:
 
flip      Vector of nDat logical values, if any value is true the
          corresponding data is flipped along the horizontal axis.
          Default is false(1,nDat).
label     Cell of strings for the x-axis label. There has to be nDat+1
          strings.
dashed    If true, black dashed line is drawn between cuts. Default is
          true.
ylim      If true, the upper limit of the vertical axis is automatically
          determined. Default is true.
plot      If true, plot is created. Default is true.
pad       If true, the output data is padded with nans on the top and
          right side. Then it can be plotted directly using surf():
              udat = ndbase.spaghetti(dat,'pad',true);
              coo = cell(1,2);
              [coo{:}] = ndgrid(udat.x,udat.y);
              surf(coo{:},udat.sig);
axscale   Scale of the unit on the x-axis. Defines what A^-1 value
          corresponds to unit 1. Default value is 1.
 
Output:
 
udat      United data in simple struct with the following fields:
              x       Column vector of x-coordinate edge bins (nX+1).
              y       Column vector of y-coordinate edge bins (nY+1).
              sig     Signal matrix with dimensions [nX nY].
              err     Error matrix with dimensions [nX nY].
              ylabel  Label of the y-axis, string.
              xlim    Limits of the x-axis, row vector with 2 elements.
              ylim    Limits of the y-axis, row vector with 2 elements.
              clim    Limits of the c-axis, row vector with 2 elements.
 

{% include links.html %}
