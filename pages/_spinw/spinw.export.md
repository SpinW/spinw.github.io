---
{title: spinw.export method, link: spinw.export, summary: export data into file, keywords: sample,
  sidebar: sw_sidebar, permalink: spinw_export, folder: spinw, mathjax: true}

---
  
### Syntax
  
`export(obj,Name,Value)`
  
`outStr = export(obj,Name,Value)`
 
### Description
  
`export(obj,Name,Value)` exports different types of spinw object data.
 
`outStr = export(obj,Name,Value)` returns a string instead of writing the
data into a file.
 
### Examples
  
In this example the crystal structure is imported from the `test.cif`
file, and the atomic positions are saved into the `test.pcr` file for
FullProf refinement (the pcr file needs additional text to work with
FullProf).
 
```matlab
cryst = sw('test.cif');
cryst.export('format','pcr','path','test.pcr');
```
 
### Input arguments
 
`obj`
: [spinw](spinw) object.
 
### Name-Value Pair Arguments
 
`'format'`
: Determines the output data and file type. The supported file formats
  are:
  * `'pcr'`   Creates part of a .pcr file used by [FullProf](https://www.ill.eu/sites/fullprof). It exports the
    atomic positions.
  * `'MC'`    Exports data into a custom file format for Monte Carlo simulations.
 
`'path'`
: Path to a file into which the data will be exported, `out` will
  be `true` if the file succesfully saved, otherwise `false`.
 
`'fileid'`
: File identifier that is already opened in Matlab using the
  `fileid = fopen(...)` command. Don't forget to close the file
  afterwards.
   
#### File format dependent options:
   
`'perm'` (`pcr`)
: Permutation of the $$xyz$$ atomic positions, default value is `[1 2 3]`.
   
`'boundary'` (`MC`)
: Boundary conditions of the extended unit cell. Default value is `{'per'
  'per' 'per'}`. The following strings are accepted:
  * `'free'`  Free, interactions between extedned unit cells are omitted.
  * `'per'`   Periodic, interactions between extended unit cells are
    retained.
   
{% include note.html content=" If neither `path` nor `fileid` is given, the `outStr` will be a
cell containing strings for each line of the text output." %}
   

{% include links.html %}
