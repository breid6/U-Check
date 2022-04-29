<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
<head>
    <title>{% block title %}{% endblock %}</title>
     <link rel="stylesheet" href="/static/spectre.min.css" />
    <link rel="stylesheet" href="/static/spectre-exp.min.css" />
    <link rel="stylesheet" href="/static/spectre-icons.min.css" />
</head>
<body>
<header class="navbar">
  <section class="navbar-section">
    <a href="/" class="btn btn-link">Home</a>
    <a href="#" class="btn btn-link">Examples</a>
  </section>
  <section class="navbar-center">
      <button class="btn btn-primary btn-large my-2" >
        <div class="icon icon-check">
        </div>
      </button>
  </section>
  <section class="navbar-section">
    <a href="https://github.com/breid6/U-Check" class="btn btn-link">GitHub</a>
  </section>
</header>
<div class="container">
  <div class="columns">
    <div class="column col-2"></div>
    <div class="column col-8">
          {% block content %}{% endblock %}
    </div>
    <div class="column col-2"></div>
  </div>
</div>

</body>
</html>