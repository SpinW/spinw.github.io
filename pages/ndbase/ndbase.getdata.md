---
{title: ndbase.getdata, link: ndbase.getdata, summary: extract data from different
    type of objects, keywords: sample, sidebar: sw_sidebar, permalink: ndbase_getdata,
  folder: ndbase, mathjax: true}

---
 
dat = NDBASE.GETDATA(dndobj, 'option1',value1,...)
 
Currently works with dnd objects.
 
 
Input:
 
dndobj        Object of dnd type.
 
Options:
 
binType       Type of the output bin:
                  'center'    Center bin, default.
                  'edge'      Edge bin (storing edge value of each bin).
axUnit        Unit of the axis:
                  'default'   Units as it is given in the dnd object,
                              default.
                  'A-1'       Units of A^-1.
emptyval      Value for empty pixels. Default is nan.
 
Output:
 
dat           Structure with the following fields:
                  sig     Storing the signal in a matrix with dimensions
                          [nAx1 nAx2 ...].
                  err     Standard deviation of the signal stored in a
                          matrix with same dimensions.
                  ax      Axes stored in a cell: {ax1 ax2 ...}. Each axn
                          is a column vector with nAxn or nAxn+1 number
                          of elements for center and edge bins
                          respectively.
 

{% include links.html %}
