---
{title: swplot.polyhedron, link: swplot.polyhedron, summary: creates convex polyhedra
    or polygon from vertex list, keywords: sample, sidebar: sw_sidebar, permalink: swplot_polyhedron,
  folder: swplot, mathjax: true}

---
  
### Syntax
  
`hPatch = swplot.polyhedron(vertices)`
  
`hPatch = swplot.polyhedron(handle, ...)`
 
### Description
  
`hPatch = swplot.polyhedron(vertices)` creates convex polyhedra or
polygon from a given vertex list (unordered list of 3D coordinates). To
draw the polyhedron the convex hull of the given point cloud is
calculated using [convhulln](https://www.mathworks.com/help/matlab/ref/convhulln.html). It is automatically detected if the
given vertex points lie on a plane in which case the convex polygon is
drawn.
   
`hPatch = swplot.polyhedron(handle, ...)` adds the generated patch object
to a given axis if `handle` is an axis handle or adds the polyhedron to
an existing [patch](https://www.mathworks.com/help/matlab/ref/patch.html) object, if the given `handle` points to a
patch object.
  
### Input Arguments
  
`vertices`
: Matrix with dimensions of $$[3\times n_{obj}\times n_{point}]$$, where
  $$n_{obj}$$ is the number of polyhedra to draw, $$n_{point}$$ is the number
  of vertices per polyhedron.
  
### See Also
  
[convhulln](https://www.mathworks.com/help/matlab/ref/convhulln.html)
 

{% include links.html %}
