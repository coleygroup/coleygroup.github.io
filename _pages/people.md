---
title: "Coley Research Group - People"
layout: gridlay
excerpt: "Coley Research Group: People"
sitemap: false
permalink: /people
---

# People

<!-- TODO: change to album view once we have >1 photo -->
{% for photo in site.data.photos %}
<div class="col-sm-12 clearfix" style="text-align: center; ">
<div style="display: flex; justify-content: center;">
<img class="group-pic" src="{{ site.url }}{{ site.baseurl }}/images/grouppic/{{ photo.name }}" alt="Group photo"/>
</div>
<i>{{ photo.description }}</i>
</div>
{% assign number_printed = forloop.index | modulo: 2 %}
{% if number_printed == 0 %}
</div>
<div class="row">
{% endif %}
{% endfor %}

<h2 style="text-align: center; padding-top: 30px">Principal Investigator</h2>
<div class="col-sm-12 clearfix" style="text-align: center; ">
<div style="text-align: center;">
<div class="image-cropper">
<img class="person-pic" src="{{ site.url }}{{ site.baseurl }}/images/teampic/Connor_Coley.jpg" alt="Connor W. Coley photo"/>
</div>
<h4><b>Connor W. Coley</b></h4>
<i>Associate Professor<br>
Class of 1957 Career Development Professor <br>
Department of Chemical Engineering <br>
Department of Electrical Engineering and Computer Science <br>
Schwarzman College of Computing<br>
Massachusetts Institute of Technology<br></i>
<a href="mailto:ccoley@mit.edu"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px"  fill="currentColor" class="bi bi-envelope-fill" viewBox="0 0 16 16"><path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414zM0 4.697v7.104l5.803-3.558zM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586zm3.436-.586L16 11.801V4.697z"/></svg></a>
<a href="https://www.linkedin.com/in/connorcoley/"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px"  fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16"><path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854zm4.943 12.248V6.169H2.542v7.225zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248S2.4 3.226 2.4 3.934c0 .694.521 1.248 1.327 1.248zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016l.016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225z"/></svg></a>
<p>Connor W. Coley is the Class of 1957 Career Development Professor and an Associate Professor at MIT in the Department of Chemical Engineering and the Department of Electrical Engineering and Computer Science. He received his B.S. and Ph.D. in Chemical Engineering from Caltech and MIT, respectively, and did his postdoctoral training at the Broad Institute. His research group at MIT works at the interface of chemistry and data science to develop models that understand how molecules behave, interact, and react and use that knowledge to engineer new ones, with an emphasis on therapeutic discovery.</p>
<p>Connor is a recipient of C&EN’s “Talented Twelve” award, Forbes Magazine’s “30 Under 30” for Healthcare, Technology Review’s 35 Innovators Under 35, the NSF CAREER award, the ACS COMP OpenEye Outstanding Junior Faculty Award, the Bayer Early Excellence in Science Award, the 3M NTFA, and was named a Schmidt AI2050 Early Career Fellow, a 2023 Samsung AI Researcher of the Year, a Scialog Fellow, and a Camille Dreyfus Teacher-Scholar. Connor has been further recognized for his teaching and mentorship by MIT's inaugural Common Ground Award for Excellence in Teaching, the Outstanding UROP Mentor Award in 2024, and the James W. Swan Outstanding Faculty Award for Graduate Teaching in Chemical Engineering in 2024 and 2025.</p>
</div>
</div>

<!-- Post-docs -->
<h2 style="text-align: center; padding: 30px">Postdoctoral Associates & Fellows and Research Scientists
</h2>
<div class="row">
{% for member in site.data.postdocs %}
<div class="col-sm-4 clearfix" style="text-align: center; ">
<div style="display: flex; justify-content: center;">
<div class="image-cropper">
<img class="person-pic" src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" alt="{{ member.name }} photo"/>
</div>
</div>
<h4><b>{{ member.name }}</b></h4>
<i>{{ member.info }} <br> </i>
<a href="mailto:{{ member.email }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px" fill="currentColor" class="bi bi-envelope-fill" viewBox="0 0 16 16"><path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414zM0 4.697v7.104l5.803-3.558zM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586zm3.436-.586L16 11.801V4.697z"/></svg></a>{% if member.twitter %}<a href="{{ member.twitter }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px" fill="currentColor" class="bi bi-twitter" viewBox="0 0 16 16"><path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334q.002-.211-.006-.422A6.7 6.7 0 0 0 16 3.542a6.7 6.7 0 0 1-1.889.518 3.3 3.3 0 0 0 1.447-1.817 6.5 6.5 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.32 9.32 0 0 1-6.767-3.429 3.29 3.29 0 0 0 1.018 4.382A3.3 3.3 0 0 1 .64 6.575v.045a3.29 3.29 0 0 0 2.632 3.218 3.2 3.2 0 0 1-.865.115 3 3 0 0 1-.614-.057 3.28 3.28 0 0 0 3.067 2.277A6.6 6.6 0 0 1 .78 13.58a6 6 0 0 1-.78-.045A9.34 9.34 0 0 0 5.026 15"/></svg></a>{% endif %}{% if member.linkedin %}<a href="{{ member.linkedin }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px"  fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16"><path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854zm4.943 12.248V6.169H2.542v7.225zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248S2.4 3.226 2.4 3.934c0 .694.521 1.248 1.327 1.248zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016l.016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225z"/></svg></a>{% endif %}{% if member.website %}<a href="{{ member.website }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px" fill="currentColor" class="bi bi-house-fill" viewBox="0 0 16 16"><path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L8 2.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293z"/><path d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293z"/></svg></a>{% endif %}
<p>{{ member.description }}</p>
</div>
{% assign number_printed = forloop.index | modulo: 3 %}
{% if number_printed == 0 %}
</div>
<div class="row">
{% endif %}
{% endfor %}
</div>

<!-- Grad students -->
---
<h2 style="text-align: center; padding: 30px">Graduate Students</h2>
<div class="row">
{% for member in site.data.grad_students %}
<div class="col-sm-4 clearfix" style="text-align: center; ">
<div style="display: flex; justify-content: center;">
<div class="image-cropper">
<img class="person-pic" src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" alt="{{ member.name }} photo"/>
</div>
</div>
<h4><b>{{ member.name }}</b></h4>
<i>{{ member.info }} <br> </i>
<a href="mailto:{{ member.email }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px" fill="currentColor" class="bi bi-envelope-fill" viewBox="0 0 16 16"><path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414zM0 4.697v7.104l5.803-3.558zM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586zm3.436-.586L16 11.801V4.697z"/></svg></a>{% if member.twitter %}<a href="{{ member.twitter }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px" fill="currentColor" class="bi bi-twitter" viewBox="0 0 16 16"><path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334q.002-.211-.006-.422A6.7 6.7 0 0 0 16 3.542a6.7 6.7 0 0 1-1.889.518 3.3 3.3 0 0 0 1.447-1.817 6.5 6.5 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.32 9.32 0 0 1-6.767-3.429 3.29 3.29 0 0 0 1.018 4.382A3.3 3.3 0 0 1 .64 6.575v.045a3.29 3.29 0 0 0 2.632 3.218 3.2 3.2 0 0 1-.865.115 3 3 0 0 1-.614-.057 3.28 3.28 0 0 0 3.067 2.277A6.6 6.6 0 0 1 .78 13.58a6 6 0 0 1-.78-.045A9.34 9.34 0 0 0 5.026 15"/></svg></a>{% endif %}{% if member.linkedin %}<a href="{{ member.linkedin }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px"  fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16"><path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854zm4.943 12.248V6.169H2.542v7.225zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248S2.4 3.226 2.4 3.934c0 .694.521 1.248 1.327 1.248zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016l.016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225z"/></svg></a>{% endif %}{% if member.website %}<a href="{{ member.website }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px" fill="currentColor" class="bi bi-house-fill" viewBox="0 0 16 16"><path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L8 2.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293z"/><path d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293z"/></svg></a>{% endif %}
<p>{{ member.description }}</p>
</div>
{% assign number_printed = forloop.index | modulo: 3 %}
{% if number_printed == 0 %}
</div>
<div class="row">
{% endif %}
{% endfor %}
</div>

---
<h2 style="text-align: center; padding: 30px">Software Developers</h2>
<div class="row">
{% for member in site.data.software_devs %}
<div class="col-sm-4 clearfix" style="text-align: center; ">
<div style="display: flex; justify-content: center;">
<div class="image-cropper">
<img class="person-pic" src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" alt="{{ member.name }} photo"/>
</div>
</div>
<h4><b>{{ member.name }}</b></h4>
<i>{{ member.info }} <br> </i>
<a href="mailto:{{ member.email }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px" fill="currentColor" class="bi bi-envelope-fill" viewBox="0 0 16 16"><path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414zM0 4.697v7.104l5.803-3.558zM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586zm3.436-.586L16 11.801V4.697z"/></svg></a>{% if member.twitter %}<a href="{{ member.twitter }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px" fill="currentColor" class="bi bi-twitter" viewBox="0 0 16 16"><path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334q.002-.211-.006-.422A6.7 6.7 0 0 0 16 3.542a6.7 6.7 0 0 1-1.889.518 3.3 3.3 0 0 0 1.447-1.817 6.5 6.5 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.32 9.32 0 0 1-6.767-3.429 3.29 3.29 0 0 0 1.018 4.382A3.3 3.3 0 0 1 .64 6.575v.045a3.29 3.29 0 0 0 2.632 3.218 3.2 3.2 0 0 1-.865.115 3 3 0 0 1-.614-.057 3.28 3.28 0 0 0 3.067 2.277A6.6 6.6 0 0 1 .78 13.58a6 6 0 0 1-.78-.045A9.34 9.34 0 0 0 5.026 15"/></svg></a>{% endif %}{% if member.linkedin %}<a href="{{ member.linkedin }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px"  fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16"><path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854zm4.943 12.248V6.169H2.542v7.225zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248S2.4 3.226 2.4 3.934c0 .694.521 1.248 1.327 1.248zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016l.016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225z"/></svg></a>{% endif %}{% if member.website %}<a href="{{ member.website }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px" fill="currentColor" class="bi bi-house-fill" viewBox="0 0 16 16"><path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L8 2.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293z"/><path d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293z"/></svg></a>{% endif %}
<p>{{ member.description }}</p>
</div>
{% assign number_printed = forloop.index | modulo: 3 %}
{% if number_printed == 0 %}
</div>
<div class="row">
{% endif %}
{% endfor %}
</div>


---
<h2 style="text-align: center; padding: 30px">Undergraduate and Postgraduate Researchers</h2>
<div class="row">
{% for member in site.data.undergrads %}
<div class="col-sm-4 clearfix" style="text-align: center; ">
<div style="display: flex; justify-content: center;">
<div class="image-cropper">
<img class="person-pic" src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" alt="{{ member.name }} photo"/>
</div>
</div>
<h4><b>{{ member.name }}</b></h4>
<i>{{ member.info }} <br> </i>
<a href="mailto:{{ member.email }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px" fill="currentColor" class="bi bi-envelope-fill" viewBox="0 0 16 16"><path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414zM0 4.697v7.104l5.803-3.558zM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586zm3.436-.586L16 11.801V4.697z"/></svg></a>{% if member.twitter %}<a href="{{ member.twitter }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px" fill="currentColor" class="bi bi-twitter" viewBox="0 0 16 16"><path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334q.002-.211-.006-.422A6.7 6.7 0 0 0 16 3.542a6.7 6.7 0 0 1-1.889.518 3.3 3.3 0 0 0 1.447-1.817 6.5 6.5 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.32 9.32 0 0 1-6.767-3.429 3.29 3.29 0 0 0 1.018 4.382A3.3 3.3 0 0 1 .64 6.575v.045a3.29 3.29 0 0 0 2.632 3.218 3.2 3.2 0 0 1-.865.115 3 3 0 0 1-.614-.057 3.28 3.28 0 0 0 3.067 2.277A6.6 6.6 0 0 1 .78 13.58a6 6 0 0 1-.78-.045A9.34 9.34 0 0 0 5.026 15"/></svg></a>{% endif %}{% if member.linkedin %}<a href="{{ member.linkedin }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px"  fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16"><path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854zm4.943 12.248V6.169H2.542v7.225zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248S2.4 3.226 2.4 3.934c0 .694.521 1.248 1.327 1.248zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016l.016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225z"/></svg></a>{% endif %}{% if member.website %}<a href="{{ member.website }}"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" style="margin-right: 5px; margin-left: 5px; margin-top: 10px" fill="currentColor" class="bi bi-house-fill" viewBox="0 0 16 16"><path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L8 2.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293z"/><path d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293z"/></svg></a>{% endif %}
<p>{{ member.description }}</p>
</div>
{% assign number_printed = forloop.index | modulo: 3 %}
{% if number_printed == 0 %}
</div>
<div class="row">
{% endif %}
{% endfor %}
</div>

## Lab Alumni
<i>Graduate students, postdoctoral associates & fellows, research scientists</i>
{% for member in site.data.alumni %}
{% if member.link %}
- [{{ member.name }}]({{ member.link }}) ({{ member.previous }}) {% if member.current %} &rarr; {{ member.current }} {% endif %}
{% else %}
- {{ member.name }} ({{ member.previous }}) {% if member.current %} &rarr; {{ member.current }} {% endif %}
{% endif %}
{% endfor %}

<i>Undergraduate students</i>
{% for member in site.data.alumni_ug %}
{% if member.link %}
- [{{ member.name }}]({{ member.link }}) ({{ member.previous }}) {% if member.current %} &rarr; {{ member.current }} {% endif %}
{% else %}
- {{ member.name }} ({{ member.previous }}) {% if member.current %} &rarr; {{ member.current }} {% endif %}
{% endif %}
{% endfor %}
