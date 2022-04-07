{% extends "base.tpl" %}
{% block title %} U-Check.home {% endblock %}
{% block content %}
<div class="card my-2">
  <div class="card-header p-centered">
    <div class="card-title h1 p-centered ">U-Check</div>

  </div>
   <div class="card-subtitle p-centered" style="color:blue;">
      U-Think! U-Check! U-Know!
    </div>
  <div class="card-body">
    <form action="/results" method="post">
      <div class="form-group">
      <input class="form-input form-inline" id="input-example-9" name="address" type="url"
             placeholder="Please enter a URL" >
      </input>
      <input type="Submit" value="Check!" class="btn btn-primary form-inline">
      </div>
      <div class="form-group">
        <label class="form-switch form-inline">
          <input type="checkbox" name="SQLbutton">
          <i class="form-icon"></i> Check for SQL injection
        </label>
        <label class="form-switch form-inline">
          <input type="checkbox" name="XSSbutton">
          <i class="form-icon"></i> Check for XSS
        </label>
      </div>
    </form>
  </div>
  <div class="card-footer">
  </div>
</div>
{% endblock %}