---
{title: ndbase.source, link: ndbase.source, summary: reads text data from multiple
    sources, keywords: sample, sidebar: sw_sidebar, permalink: ndbase_source, folder: ndbase,
  mathjax: true}

---
 
[dataStr, {info}] = SOURCE(dataSource, {type})
 
The function can read text data from the following sources:
  - local files, where the file location is specified in dataSource
  - download an url content, when dataSource begins with 'http'
 
Input:
 
dataSource    String, can be file name or url (starting with 'http').
{type}        Forces to treat data source as a certain type, optional.
              Possible values:
                  'auto'      Determine automatically whether file or
                              url, (default).
                  'file'      Local file.
                  'url'       Url adress.
 
Output:
 
dataStr       String in a char type row vector.
{info}        Additional information stored in a struct with fields:
  source      Data source (empty if string data was given).
  isfile      Logical variable, true if the source is a local file.
 

{% include links.html %}
