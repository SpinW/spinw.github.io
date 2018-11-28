---
layout: page
title: Tutorials
subtitle: Current SpinW tutorials
---

This is where you get to learn stuff!

{% for tutorial in site.tutorials %}
  <h2>
    <a href="{{ tutorial.url }}">
      {{ tutorial.title }}
    </a>
  </h2>
  <p>{{ tutorial.subtitle }}</p>
{% endfor %}
