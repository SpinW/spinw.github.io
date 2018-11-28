---
{title: swpref.ge method, link: swpref.ge, summary: '>= (GE)   Greater than or equal
    relation for handles.', keywords: sample, sidebar: sw_sidebar, permalink: swpref_ge,
  folder: swpref, mathjax: true}

---
    H1 >= H2 performs element-wise comparisons between handle arrays H1 and
    H2.  H1 and H2 must be of the same dimensions unless one is a scalar.
    The result is a logical array of the same dimensions, where each
    element is an element-wise >= result.
 
    If one of H1 or H2 is scalar, scalar expansion is performed and the 
    result will match the dimensions of the array that is not scalar.
 
    TF = GE(H1, H2) stores the result in a logical array of the same 
    dimensions.
 
    See also SWPREF, SWPREF/EQ, SWPREF/GT, SWPREF/LE, SWPREF/LT, SWPREF/NE
Help for swpref/ge is inherited from superclass HANDLE

{% include links.html %}
