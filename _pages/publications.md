---
title: "Allan Lab - Publications"
layout: gridlay
excerpt: "Allan Lab -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

<ul>
{% for pub in site.data.research %}
{% if pub.direction == "predictive" %}
<li style="font-size: 13px; margin-top: 5px;">{{ pub.authors }} "{{ pub.title }}". <i>{{ pub.journal }}</i> ({{ pub.year }}) </li>
{% endif %}
{% endfor %}
</ul>
<br/>