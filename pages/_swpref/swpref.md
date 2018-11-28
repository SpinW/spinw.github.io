---
{title: swpref class, link: swpref class, summary: class to store and retrieve persistent
    settings, keywords: sample, sidebar: sw_sidebar, permalink: swpref, folder: swpref,
  mathjax: true}

---
 
### Syntax
 
`pref = swpref`
 
`pref = swpref('default')`
 
### Description
 
`pref = swpref` retrieves and creates a preference object.
 
`pref = swpref('default')` resets all preferences to default values.
 
The settings sotred in the `swpref` class for spinw objects will
persist during a single Matlab session. It is different from the
Matlab built-in preferences, as swpref resets all settings to factory
default after every restart of Matlab.
 
### Examples
 
We change the fontsize value and show that it is retained even when a
new instance of the object is created:
 
```matlab
pref = swpref
pref.fontsize
```
*Output*
```
    12
```
 
```matlab
pref.fontsize = 18
pref2 = swpref
pref.fontsize
```
*Output*
```
    18
```
 
```matlab
pref2.fontsize
```
*Output*
```
    18
```
 
 
### Properties
 
Properties can be changed by directly assigning a new value to them.
Once a new value to a given property is assigned, it will be retained
until the end of a MATLAB session, even if a new class instance is
created.
 
### Methods
 
Methods are the different commands that require an `swpref` object as
a first input, thus they can be called as `method1(obj,...)`,
alternatively the equivalent command is `obj.method1(...)`.
 
* [swpref.get](swpref_get) retrieves a preference value
* [swpref.set](swpref_set) sets a preference value
* [swpref.export](swpref_export) saves swpref object into a file
* [swpref.import](swpref_import) imports swpref object from file
 
Commands are methods which can be called without first creating a
preference object `swpref.command(....)`.
 
* [swpref.getpref](swpref_getpref) retrieves a preference value
* [swpref.setpref](swpref_setpref) sets a preference value
 

{% include links.html %}
