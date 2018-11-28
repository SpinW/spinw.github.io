---
{title: swpref.addprop method, link: swpref.addprop, summary: ADDPROP   Add dynamic
    property to MATLAB object., keywords: sample, sidebar: sw_sidebar, permalink: swpref_addprop,
  folder: swpref, mathjax: true}

---
    D = ADDPROP(H,'DynamicPropName') adds a dynamic property to the MATLAB 
    objects in array H.  The added property is associated only with
    the objects of H.  There is no effect on the class of H.  ADDPROP
    returns a META.DYNAMICPROPERTY object, which can be modified to 
    change property attributes or add property set and get methods.  
 
    A dynamic property can be removed from an object by calling DELETE on
    the META.DYNAMICPROPERTY object.
 
    See also SWPREF, HANDLE, META.DYNAMICPROPERTY
Help for swpref/addprop is inherited from superclass DYNAMICPROPS
    Reference page in Doc Center
       doc swpref/addprop

{% include links.html %}
