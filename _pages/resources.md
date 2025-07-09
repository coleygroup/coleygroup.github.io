---
title: "Coley Research Group - Resources"
layout: textlay
excerpt: "Resources."
sitemap: false
permalink: /resources
---

# Resources

### Group guide
---
We actively maintain a group guide detailing information about our values and Connor's attitude toward research and mentorship which can be found [here](https://docs.google.com/document/d/1K10WS0Bey9AGr17bpiak-A1dhQrkv5BBsQrsrwQ-H2g/edit).

<br/>

### Learning Resources
---
A curated collection of external resources, tutorials, and tools that we recommend for learning about computational chemistry, machine learning, and chemical informatics.

{% for category in site.data.resources.categories %}
#### {{ category.name }}
*{{ category.description }}*

{% assign category_resources = site.data.resources.learning_resources | where: "category", category.name %}
{% for resource in category_resources %}
- **[{{ resource.title }}]({{ resource.url }})** - {{ resource.description }}
{% endfor %}

{% endfor %}