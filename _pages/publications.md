---
title: "Coley Lab - Publications"
layout: gridlay
excerpt: "Coley Lab -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

(Last updated June 17, 2024; also see [Google Scholar](https://scholar.google.com/citations?hl=en&user=l015S80AAAAJ&view_op=list_works&sortby=pubdate))

---

<style>
  .hanging-indent {
    margin-left: 20px;
    text-indent: -20px;
  }
</style>

{% for pub in site.data.publications %}
<!-- <p style="margin-top: 5px;"> -->
<p class="hanging-indent">
  {{ pub.authors }}
  "{{ pub.title }}".
  *{{ pub.journal }}*
  {{ pub.volume }}{% if pub.issue %}({{ (pub.issue) }}) {% endif %}, {{ pub.pages }} (**{{ pub.year }}**).
  {% if pub.url %} [{{ pub.url}}]({{pub.url}}) {% endif %}
</p>

{% if pub.preprint_doi_url %}
<p style="margin-left: 25px;">
  Preprint: *{{ pub.preprint_site }}*  ({{ pub.preprint_year }}) [{{ pub.preprint_doi_url}}]({{ pub.preprint_doi_url}})
</p>
{% endif %}
<!-- </p> -->
{% endfor %}