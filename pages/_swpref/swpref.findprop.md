---
{title: swpref.findprop method, link: swpref.findprop, summary: FINDPROP   Find property
    of MATLAB handle object., keywords: sample, sidebar: sw_sidebar, permalink: swpref_findprop,
  folder: swpref, mathjax: true}

---
    p = FINDPROP(H,'PROPNAME') finds and returns the META.PROPERTY object
    associated with property name PROPNAME of scalar handle object H.
    PROPNAME must be a string.  It can be the name of a property defined 
    by the class of H or a dynamic property added to scalar object H.
   
    If no property named PROPNAME exists for object H, an empty 
    META.PROPERTY array is returned.
 
    See also SWPREF, SWPREF/FINDOBJ, DYNAMICPROPS, META.PROPERTY
Help for swpref/findprop is inherited from superclass HANDLE
    Reference page in Doc Center
       doc swpref/findprop

{% include links.html %}
