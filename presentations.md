---
layout: page
title: Presentations
subtitle: Presentations on SpinW
note:   [](<a href="{{ presentation.outerURL | prepend: site.baseurl }}?print-pdf" > Download PDF </a>)
---

This is where you get to learn SpinW!
{% assign ordered_pages = site.presentations | sort:"name" %}
{% for presentation in ordered_pages %}
  <h2>
  <a href="{{ presentation.outerURL | prepend: site.baseurl }}" target="_blank"> {{ presentation.title }} </a>
  </h2>
  <p>{{ presentation.content }}</p>
{% endfor %}
