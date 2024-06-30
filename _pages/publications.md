---
title: "Coley Lab - Publications"
layout: gridlay
excerpt: "Coley Lab -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

(Last updated June 4, 2024; also see [Google Scholar](https://scholar.google.com/citations?hl=en&user=l015S80AAAAJ&view_op=list_works&sortby=pubdate))

---

{% for pub in site.data.publications %}
{% if pub.url %}
<p style="margin-top: 5px;">
  {{ pub.authors }} "<a href="{{ pub.url }}" target="_blank">{{ pub.title }}</a>". <i>{{ pub.journal }}</i> (**{{ pub.year }}**)
</p>
{% else %}
<p style="margin-top: 5px;">{{ pub.authors }} "{{ pub.title }}". <i>{{ pub.journal }}</i> (**{{ pub.year }}**) </p>
{% endif %}
{% endfor %}