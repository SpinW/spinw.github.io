---
layout: page
title: Presentations
subtitle: All SpinW presentations
---

This is where you get to see stuff!

{% for presentation in site.presentations %}
  <h2>
    <a href="{{ presentation.url }}">
      {{ presentation.title }}
    </a>
  </h2>
  <p>{{ presentation.subtitle }}</p>
{% endfor %}
