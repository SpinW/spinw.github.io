---
layout: page
title: Tutorials
subtitle: Current SpinW tutorials
---

These tutorials can help to understand quickly how SpinW works. It is possible to download the Matlab code of any of the tutorials using the following Matlab command:

`grabcode('https://spinw.org/tutorials/01tutorial')`

where the link to the tutorial has to be pasted.

{% for tutorial in site.tutorials %}
  <h2>
    <a href="{{ tutorial.url }}">
      {{ tutorial.title }}
    </a>
  </h2>
  <p>{{ tutorial.subtitle }}</p>
{% endfor %}
