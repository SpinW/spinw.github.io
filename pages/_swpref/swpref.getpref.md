---
{title: swpref.getpref method, link: swpref.getpref, summary: retrieves a preference
    value, keywords: sample, sidebar: sw_sidebar, permalink: swpref_getpref, folder: swpref,
  mathjax: true}

---
 
### Syntax
 
`allPref = swpref.getpref`
 
`selPref = swpref.getpref(name)`
 
`val = swpref.getpref(name,[])`
 
### Description
 
`allPref = swpref.getpref` returns all preference in a struct where each
field-value pair corresponds to a prefernce name-value pair.
 
`selPref = swpref.getpref(name)` returns a struct that contains the
value, name and label of the selected preference.
 
`val = swpref.getpref(name,[])` just returns the stored value
corresponding to `name` preference.
 
{% include note.html content=" The preferences are reset after every restart of Matlab, unlike the
Matlab built-in preferences that are persistent between Matlab sessions.
If you want certain preferences to keep after closing matlab, define them
in the `startup.m` file." %}
 
{% include warning.html content=" This is a legacy function. It is better to use `pref = swpref` and then
use regular `pref.name = value` or `set(pref, name, value)` syntax." %}
 
### See Also
 
[swpref.setpref](swpref_setpref)
 

{% include links.html %}
