---
{title: swpref.isvalid method, link: swpref.isvalid, summary: ISVALID   Test handle
    validity., keywords: sample, sidebar: sw_sidebar, permalink: swpref_isvalid, folder: swpref,
  mathjax: true}

---
    TF = ISVALID(H) performs an element-wise check for validity on the 
    handle elements of H.  The result is a logical array of the same 
    dimensions as H, where each element is the element-wise validity 
    result.
 
    A handle is invalid if it has been deleted or if it is an element
    of a handle array and has not yet been initialized.
 
    See also SWPREF, SWPREF/DELETE
Help for swpref/isvalid is inherited from superclass HANDLE
    Reference page in Doc Center
       doc swpref/isvalid

{% include links.html %}
