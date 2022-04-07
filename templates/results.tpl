{% extends "base.tpl" %}
{% block title %} U-Check.results {% endblock %}
{% block content %}
<div class="card my-2">
    <div class="card-header p-centered">
        <div class="card-title h1 p-centered ">Results</div>

    </div>
    <div class="card-subtitle p-centered" style="color:blue;">
        {{ url }}
    </div>
    <div class="card-body">

    </div>
    <div class="card-footer">
    </div>
</div>


{% if XSS %}
<div class="card my-2">
    <div class="card-header p-centered">
        <div class="card-title h1 p-centered ">XSS Results</div>

    </div>
    <div class="card-subtitle p-centered" style="color:blue;">
       This site is vulnerable to an XSS attack - {{ XSSResult }}
        A XSS or Cross-Site Scripting attack allows the execution
        of arbitrary third-party javascript on in otherwise legitimate website
    </div>
    <div class="card-body">
        {% if XSSResult %}


        This site is vulnerable to basic XSS!
        {% else %}

        This site is not vulnerable to basic XSS!
        {% endif %}
    </div>
    <div class="card-footer">
    </div>
</div>
{% endif %}


{% if SQL %}
<div class="card my-2">
    <div class="card-header p-centered">
        <div class="card-title h1 p-centered ">SQL Results</div>

    </div>
    <div class="card-subtitle p-centered" style="color:blue;">
        SQL Injection is an attack that targets the database.
        A hacker might enter malicious code that is taken in via text box and
        that code will trick that database into returning user information or even allow a hacker to make an admin account.
        {% if SQLResult %}


        This site is vulnerable to basic SQL injection!
        {% else %}

        This site is not vulnerable to basic SQL injection!
        {% endif %}
    </div>
    <div class="card-body">

    </div>
    <div class="card-footer">
    </div>
</div>
{% endif %}
{% endblock %}