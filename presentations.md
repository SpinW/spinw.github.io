---
layout: page
title: Presentations
subtitle: All the SpinW presentations
---

This is where you get to see stuff!
{% for presentation in site.presentations %}
  <h2>
  <a href="{{ presentation.outerURL | prepend: site.baseurl }}" target="_blank"> {{ presentation.title }} </a>
  </h2>
  <p>{{ presentation.content }}</p>  
{% endfor %}
