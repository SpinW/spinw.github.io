---
{title: ndbase.corrphon, link: ndbase.corrphon, summary: subtract incoherent phonons
    from magnetic data in d2d object, keywords: sample, sidebar: sw_sidebar, permalink: ndbase_corrphon,
  folder: ndbase, mathjax: true}

---
 
NDBASE.CORRPHON(d2d,'option1',value1,...)
 
Options:
 
qphon         Q-range where the phonon background is to be fitted in
              units of A^-1. Recommended range is above 4 A^-1, where the
              magnetic signal is negligible due to the form factor. It is
              also possible to given an upper value. For no upper limit,
              use inf. Default value is [4 5].
 

{% include links.html %}
