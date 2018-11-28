---
{title: swplot.raytriangle, link: swplot.raytriangle, summary: finds if a ray crosses
    a triangle, keywords: sample, sidebar: sw_sidebar, permalink: swplot_raytriangle,
  folder: swplot, mathjax: true}

---
  
### Syntax
  
`swplot.raytriangle(V,F,ray)`
  
### Description
  
`swplot.raytriangle(V,F,ray)` determines if a given ray crosses within a
triangle defined by its vertex coordinates. The code is optimised for
a single ray and multiple triangles.
  
### Input Arguments
  
`V`
: Vertex positions in a matrix with dimensions $$[n_{vertex}\times 3]$$.
  
`F`
: Faces in a matrix with dimensions $$[n_{face}\times 3]$$, where 
      $$max(F) = n_{vertex}$$.
  
`ray`
: Definition of the ray via 2 points in space, stored in a matrix with
  dimensions of $$[2\times 3]$$. The two points of the ray, $$P_1$$ and
  $$P_2$$, are stored in the first and second rows respectively. The ray
  points from $$P_1$$ to $$P_2$$.
 

{% include links.html %}
