---
title: "Coley Lab - Publications"
layout: publications
excerpt: "Coley Lab -- Publications."
sitemap: false
permalink: /publications
---
<!-- Custom CSS -->
<style>
  .hanging-indent {
    margin-left: 20px;
    text-indent: -20px;
  }
  .btn-xs {
    padding: 2px 5px;
    font-size: 9px;
    line-height: 1.5;
    border-radius: 3px;
    border: none;
    box-shadow: none;
    background-color: #0059b3; /* Bootstrap primary color */
    color: white;
  }
  .btn-xs:hover, .btn-xs:focus, .btn-xs:active {
    background-color: #011f4b; /* Darker shade of primary color */
    box-shadow: none;
  }
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
</style>

<!-- START OF PAGE -->
# Publications

(Last updated Feb. 18, 2025. See [Google Scholar](https://scholar.google.com/citations?hl=en&user=l015S80AAAAJ&view_op=list_works&sortby=pubdate) for most up-to-date publications)

<!-- Display all possible research themes as filter buttons -->
<p>
  {% assign themes = site.data.research_themes %}
  **Research Themes:** (select to filter)
  {% for theme in themes %}<span class="badge badge-pill badge-pill-custom filter-button" data-theme="{{ theme.name }}" data-color="{{ theme.color }}" data-darker-color="{{ theme.darker_color }}" style="background-color: {{ theme.color }}">{{ theme.name }}</span>
  {% endfor %}
</p>

---

<!-- Display all publications -->
{% assign themes = site.data.research_themes %}
{% for pub in site.data.publications %}
<!-- Citations -->
<div class="publication-item" data-themes="{{ pub.themes | join: ',' }}">
  <p class="hanging-indent">
    {{ pub.authors }}.
    {% if pub.url %} [{{ pub.title }}]({{ pub.url }}). {% else %} {{pub.title}}. {% endif %}*{{ pub.journal }}*{% if pub.volume %} {{ pub.volume }}{% if pub.issue %}({{ pub.issue }}){% endif %},{% endif %}{% if pub.pages %} {{ pub.pages }}{% endif %}. ({{ pub.year }})
    {% if pub.doi %} DOI: {{ pub.doi }} {% elsif pub.preprint %} *preprint: {{ pub.preprint }}*{% endif %}
  </p>
  <!-- Buttons and tags -->
  {% if pub.preprint_url or pub.themes %}
  <p style="margin-left: 20px; margin-top: -11px">
    {% if pub.preprint_url %}<a href="{{ pub.preprint_url }}" class="btn btn-xs btn-primary">Preprint</a>{% endif %}{% if pub.themes %}{% for theme in pub.themes %}{% assign theme_data = themes | where: "name", theme | first %}{% if theme_data %} <span class="badge badge-pill badge-pill-custom" style="background-color: {{ theme_data.color }}">{{ theme }}</span>{% endif %}{% endfor %}
    {% endif %}
  </p>
  {% endif %}
</div>
{% endfor %}

<!-- JavaScript for filtering publications -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    const filterButtons = document.querySelectorAll('.filter-button');
    const publicationItems = document.querySelectorAll('.publication-item');

    filterButtons.forEach(button => {
      const originalColor = button.getAttribute('data-color');
      const darkerColor = button.getAttribute('data-darker-color');

      // Log the colors to the console to verify correct retrieval
      console.log('Original Color:', originalColor);
      console.log('Darker Color:', darkerColor);

      button.addEventListener('click', function() {
        this.classList.toggle('active');
        if (this.classList.contains('active')) {
          this.style.backgroundColor = darkerColor;
        } else {
          this.style.backgroundColor = originalColor;
        }
        filterPublications();
      });
    });

    function filterPublications() {
      const activeThemes = Array.from(filterButtons)
                                .filter(btn => btn.classList.contains('active'))
                                .map(btn => btn.getAttribute('data-theme'));

      publicationItems.forEach(item => {
        const itemThemes = item.getAttribute('data-themes').split(',');

        if (activeThemes.length === 0 || activeThemes.some(theme => itemThemes.includes(theme))) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    }
  });
</script>
