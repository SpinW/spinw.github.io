---
{title: swpref.notify method, link: swpref.notify, summary: NOTIFY   Notify listeners
    of event., keywords: sample, sidebar: sw_sidebar, permalink: swpref_notify, folder: swpref,
  mathjax: true}

---
    NOTIFY(H,'eventname') notifies listeners added to the event named 
    EVENTNAME for handle object array H that the event is taking place.  
    H is the array of handles to the event source objects, and 'eventname'
    must be a character vector.
 
    NOTIFY(H,'eventname',ed) provides a way of encapsulating information 
    about an event which can then be accessed by each registered listener.
    ed must belong to the EVENT.EVENTDATA class.
 
    See also SWPREF, SWPREF/ADDLISTENER, SWPREF/LISTENER, EVENT.EVENTDATA, EVENTS
Help for swpref/notify is inherited from superclass HANDLE
    Reference page in Doc Center
       doc swpref/notify

{% include links.html %}
