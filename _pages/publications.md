---
title: "Coley Lab - Publications"
layout: gridlay
excerpt: "Coley Lab -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

{% for pub in site.data.publications %}
<p style="margin-top: 5px;">{{ pub.authors }} "{{ pub.title }}". <i>{{ pub.journal }}</i> (**{{ pub.year }}**) </p>
{% endfor %}