---
title: "Coley Research Group - Resources"
layout: textlay
excerpt: "Resources."
sitemap: false
permalink: /resources.html
---

# Resources

### Group guide
---
We actively maintain a group guide detailing information about our values and Connor's attitude toward research and mentorship which can be found [here](https://docs.google.com/document/d/1K10WS0Bey9AGr17bpiak-A1dhQrkv5BBsQrsrwQ-H2g/edit).

<br/>

### Software and Tools
---
We are generally committed to providing open-source software and tools for the scientific community. Our group Github organization can be found [here](https://github.com/coleygroup), and we highlight a number of software tools below.

{% assign number_printed = 0 %}
{% for tool in site.data.software %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  {% if tool.image %}<img src="{{ site.url }}{{ site.baseurl }}/images/logopic/{{ tool.image }}" class="software-img" width="33%" style="float: left" />{% endif %}
  <pubtit>{{ tool.title }}</pubtit>
  <br/>
  <i> <a href="{{ tool.link.url }}"> {{ tool.link.url }} </a> </i>
  <hr>
  <p>{{ tool.description }}</p>
  <p><em>{{ tool.authors }}</em></p>
  <p><strong><a href="{{ tool.link.url }}">{{ tool.link.display }}</a></strong></p>
  <p class="text-danger"><strong> {{ tool.news1 }}</strong></p>
  <p> {{ tool.news2 }}</p>
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}