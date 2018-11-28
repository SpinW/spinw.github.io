---
{title: swpref.export_prefs method, link: swpref.export_prefs, summary: saves swpref
    object into a file, keywords: sample, sidebar: sw_sidebar, permalink: swpref_export_prefs,
  folder: swpref, mathjax: true}

---
 
### Syntax
 
`success = swpref.export_prefs(location)`
 
`success = swpref.export_prefs`
 
### Description
 
`success = swpref.export_prefs(location)` writes the preferences given by swpref to
a file location given by `location`. The file is in a basic `.json`
format.
 
`success = swpref.export_prefs` writes the preferences given in `obj` to
the users home folder as `swprefs.json`. The file is in a basic `.json`
format.
 
### See Also
 
[swpref.import_prefs](swpref_import_prefs)
 

{% include links.html %}
