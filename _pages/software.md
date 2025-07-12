---
title: "Coley Research Group - Software"
layout: textlay
excerpt: "Software."
sitemap: false
permalink: /software
---

<!-- Custom CSS -->
<style>
  .badge-pill-custom {
      margin-left: 5px;
      border-radius: 10rem;
      padding: 0.18em 0.6em;
      font-size: 13px;
  }
  .filter-button {
      margin-right: 5px;
      cursor: pointer;
  }
  .software-item.deprecated {
      filter: grayscale(100%);
      opacity: 0.7;
  }
</style>

# Software

We are committed to providing open-source software and tools for the scientific community. Our group Github organization can be found [here](https://github.com/coleygroup). Below, we highlight a number of software tools from our publications. Older software tools that we believe have been fully supplanted by more recent ones are greyed out. 

<!-- Display all possible research themes as filter buttons -->
<p>
  {% assign themes = site.data.research_themes %}
  **Research Themes:** (select to filter)
  {% for theme in themes %}<span class="badge badge-pill badge-pill-custom filter-button" data-theme="{{ theme.name }}" data-color="{{ theme.color }}" data-darker-color="{{ theme.darker_color }}" style="background-color: {{ theme.color }}">{{ theme.name }}</span>{% endfor %}
</p>
---

{% assign number_printed = 0 %}
{% for tool in site.data.software %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="software-item col-sm-6 clearfix {% if tool.deprecated %}deprecated{% endif %}" data-themes="{{ tool.themes | join: ',' }}">
 <div class="well">
  {% if tool.image %}<img src="{{ site.url }}{{ site.baseurl }}/images/logopic/{{ tool.image }}" class="software-img" style="float:left;" />{% endif %}
  <pubtit>{{ tool.title }}</pubtit>
  <div style="clear: both;"></div>
  {% if tool.links -%}{% for l in tool.links -%}<strong>{{ l.label }}:</strong> <a href="{{ l.url }}">{{ l.url }}</a><br/>{%- endfor -%}{% elsif tool.link -%}<a href="{{ tool.link.url }}">{{ tool.link.url }}</a>{%- endif %}
  <hr>
  <p>{{ tool.description }}</p>
  <p><em>{{ tool.authors }}</em></p>
  <p class="text-danger"><strong> {{ tool.news1 }}</strong></p>
  <p> {{ tool.news2 }}</p>
  {% if tool.themes %}{% for theme in tool.themes %}{% assign theme_data = themes | where: "name", theme | first %}{% if theme_data %}<span class="badge badge-pill badge-pill-custom" style="background-color: {{ theme_data.color }}">{{ theme }}</span>{% endif %}{% endfor %}
  {% endif %}
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

<hr>

## Open software that we contribute to

{% assign contributed = site.data.contributed_software %}
{% if contributed and contributed.size > 0 %}
{% assign number_printed = 0 %}
{% for tool in contributed %}

{% assign even_odd_contrib = number_printed | modulo: 2 %}

{% if even_odd_contrib == 0 %}
<div class="row">
{% endif %}

<div class="software-item col-sm-6 clearfix" data-themes="{{ tool.themes | join: ',' }}">
 <div class="well">
  {% if tool.image %}<img src="{{ site.url }}{{ site.baseurl }}/images/logopic/{{ tool.image }}" class="software-img" style="float:left;" />{% endif %}
  <pubtit>{{ tool.title }}</pubtit>
  <div style="clear: both;"></div>
  {% if tool.links -%}{% for l in tool.links -%}<strong>{{ l.label }}:</strong> <a href="{{ l.url }}">{{ l.url }}</a><br/>{%- endfor -%}{% elsif tool.link -%}<a href="{{ tool.link.url }}">{{ tool.link.url }}</a>{%- endif %}
  <hr>
  <p>{{ tool.description }}</p>
  <p><em>{{ tool.authors }}</em></p>
  <p class="text-danger"><strong> {{ tool.news1 }}</strong></p>
  <p> {{ tool.news2 }}</p>
  {% if tool.themes %}{% for theme in tool.themes %}{% assign theme_data = themes | where: "name", theme | first %}{% if theme_data %}<span class="badge badge-pill badge-pill-custom" style="background-color: {{ theme_data.color }}">{{ theme }}</span>{% endif %}{% endfor %}
  {% endif %}
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd_contrib == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd_contrib = number_printed | modulo: 2 %}
{% if even_odd_contrib == 1 %}
</div>
{% endif %}
{% endif %}

<!-- JavaScript for filtering software items -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    const filterButtons = document.querySelectorAll('.filter-button');
    const softwareItems = document.querySelectorAll('.software-item');

    filterButtons.forEach(button => {
      const originalColor = button.getAttribute('data-color');
      const darkerColor = button.getAttribute('data-darker-color');

      button.addEventListener('click', function() {
        this.classList.toggle('active');
        if (this.classList.contains('active')) {
          this.style.backgroundColor = darkerColor;
        } else {
          this.style.backgroundColor = originalColor;
        }
        filterSoftware();
      });
    });

    function filterSoftware() {
      const activeThemes = Array.from(filterButtons)
                                .filter(btn => btn.classList.contains('active'))
                                .map(btn => btn.getAttribute('data-theme'));

      softwareItems.forEach(item => {
        const itemThemes = item.getAttribute('data-themes').split(',');
        if (activeThemes.length === 0 || activeThemes.every(theme => itemThemes.includes(theme))) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    }
  });
</script>
