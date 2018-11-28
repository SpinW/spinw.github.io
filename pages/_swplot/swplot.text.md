---
{title: swplot.text, link: swplot.text, summary: creates text at a 3D position, keywords: sample,
  sidebar: sw_sidebar, permalink: swplot_text, folder: swplot, mathjax: true}

---
  
### Syntax
  
`hText = swplot.text(r, string)`
  
`hText = swplot.text(r, string, fontSize)`
 
`hText = swplot.text(handle, ...)`
 
### Description
  
`hText = swplot.text(r, string)` creates single or multiple text in 3D
space.
   
`hPatch = swplot.text(handle, ...)` adds the generated text object to a
given axis referenced by `handle`.
   
### Input Arguments
  
`handle`
: Handle of an axis object, default value is [gca](https://www.mathworks.com/help/matlab/ref/gca.html).
  
`r`
: Coordinate of the center of the text for a single text or
  matrix with dimensions $$[3\times n_{obj}]$$ for multiple text.
  
`string`
: String that contains the text or cell of strings when multiple
  text is drawn.
  
`fontSize`
: Font size in pt, default value is stored in `swpref.getpref('fontsize')`.
  
### See Also
  
[text](https://www.mathworks.com/help/matlab/ref/text.html)
 

{% include links.html %}
