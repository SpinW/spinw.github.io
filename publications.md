---
layout: page
title: Publications
subtitle: How to cite and where we have been used.
---
# Papers on SpinW

Please cite the following paper if you use the code:
  <article class="post-preview">
    <a href="http://iopscience.iop.org/article/10.1088/0953-8984/27/16/166002">
	  <h2 class="post-title">Linear spin wave theory for single-Q incommensurate magnetic structures</h2>
    </a>
    <div class="post-entry-container">
      <div class="post-entry">
        S. Toth and B. Lake<br />
        <strong>J. Phys.: Condens. Matter</strong> 27, 166002 (2015).
      </div>
    </div>
   </article>

# Papers citing SpinW

The most up to date list of citing papers can be found on dimensions.ia:

<span class="__dimensions_badge_embed__" data-doi="10.1088/0953-8984/27/16/166002" data-legend="hover-right" data-style="large_circle"></span><script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>

<div class="posts-list">
  {% for post in site.posts %}
  {% if post.categories contains "publications" %}
  <article class="post-preview">
    <a href="{{ post.urlLink }}">
	  <h3 class="post-title">{{ post.title }}</h3>
    </a>
    <p class="post-meta">
      Posted on {{ post.date | date: "%B %-d, %Y" }}
    </p>
    <div class="post-entry-container">
      <div class="post-entry">
        {{ post.content }}
      </div>
    </div>
   </article>
   {% endif %}
  {% endfor %}
</div>

{% if paginator.total_pages > 1 %}
<ul class="pager main-pager">
  {% if paginator.previous_page %}
  <li class="previous">
    <a href="{{ paginator.previous_page_path | prepend: site.baseurl | replace: '//', '/' }}">&larr; Newer Posts</a>
  </li>
  {% endif %}
  {% if paginator.next_page %}
  <li class="next">
    <a href="{{ paginator.next_page_path | prepend: site.baseurl | replace: '//', '/' }}">Older Posts &rarr;</a>
  </li>
  {% endif %}
</ul>
{% endif %}
