MyRecommendations
=================

[![CI/CD](https://github.com/rogargon/myrecommendations/actions/workflows/cicd.yml/badge.svg)](https://github.com/rogargon/myrecommendations/actions)
[![Heroku App Status](https://heroku-shields.herokuapp.com/myrecommendations)](https://myrecommendations.herokuapp.com)

Recommendation applications developed using Django, including for the moment just:
- MyRestaurants

<p align="center">
   <img width="300" src="https://process.filestackapi.com/cache=expiry:max/resize=width:400/compress/P6Z7Ac0UTVWr260Fvg7x" alt="Django Application Structure"/>
</p>

The project is developed following an **Agile Behaviour Driven Development** approach. 
You can also follow the tutorial through the **videos** available from the **YouTube** playlist **"Django Web Project Tutorial"**:

<p align="center">
   <a href="https://www.youtube.com/playlist?list=PLJ0YJaEOtqlkdqTHfeYT4kVmcA4p8dfIr" target="_blank">
      <img width="300" src="https://ucarecdn.com/699e8d65-93a4-4aa6-bb47-17b0c11a6168/" alt="Django Web Project Video Tutorial"/>
   </a>
</p>

The source code for this project is available from this repository:
[https://github.com/rogargon/myrecommendations](https://github.com/rogargon/myrecommendations)

Starting the MyRecommendations Project from Scratch
===================================================

First of all, install the latest version of Python from [downloads](https://www.python.org/downloads/) and 
[pipenv](https://pipenv.readthedocs.io/en/latest/install/) to help you manage dependencies and virtual environments.

Then, create the folder for the new project, in our case the project is called 'myrecommendations':

```shell script
$ mkdir myrecommendations

$ cd myrecommendations
```

Once in the `myrecommendations` folder, activate the pipenv virtual environment to keep the Python packages
for your project organised and start by installing Django. Then, create a new Django project:

```shell script
$ pipenv shell

$ pipenv install Django

$ django-admin startproject myrecommendations .
```

In *myrecommendations/settings.py*, review your database settings. For instance, for an SQLite database, they should be:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'),
    }
}
```

Then, back from the root folder of the project, let Django take control of the database by running:

```shell script
$ python manage.py migrate
```

The 'migrate' command looks at INSTALLED_APPS defined in 'settings.py' and creates all required database tables according to the database settings.

To conclude project creation, define the admin user:

```shell script
$ python manage.py createsuperuser
```

Creating the MyRestaurants Application
======================================

Now that the project is ready, it is time to define project applications. In the case of this tutorial there is just one application, called 'myrestaurants'. 
To create it, type the following command from the root folder of the project:

```shell script
$ python manage.py startapp myrestaurants
```

Then, add 'myrestaurants' to the INSTALLED_APPS list in *myrecommendations/settings.py*:

```python
INSTALLED_APPS = [
    'myrestaurants',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Agile Behaviour Driven Development (BDD)
========================================

Now, we have the initial Django project and application that we will start filling with functionality.

The aim of this application is to help users keep track of the restaurants they have visitied, the dishes they have tasted there and to provide restaurant reviews for other users.

Consequently, and following a BDD approach, first we define the intended **features**:

* Register Restaurant
* Register Dish
* List Recent Restaurants
* View Restaurant
* View Dish
* Review Restaurant
* Edit Restaurant
* Edit Dish

For the moment, additional features like removing restaurants and dishes have not been considered, though they can be added in future iterations.

Next, we will start detailing each feature. For each one, a new file is generated in a *features/* folder. Each file provides details about the feature value, involved stakeholders and feature details following the template:

**In order to** [achieve some business value], \
**As a** [stakeholder type], \
**I want** [some new system feature]. 

The result is the following list of feature files with their corresponding content in the *features/* folder:

- *register_restaurant.feature* \
  **Feature**: Register Restaurant \
    **In order to** keep track of the restaurants I visit, \
    **As a** user \
    **I want** to register a restaurant together with its location and contact details.
- *register_dish.feature* \
  **Feature**: Register Dish \
    **In order to** keep track of the dishes I eat, \
    **As a** user, \
    **I want** to register a dish in the corresponding restaurant together with its details.
- *list_restaurants.feature* \
  **Feature**: List Restaurants \
    **In order to** keep myself up to date about registered restaurants, \
    **As a** user, \
    **I want** to list the last 10 registered restaurants.
- *view_restaurant.feature* \
  **Feature**: View Restaurant \
    **In order to** know about a restaurant, \
    **As a** user, \
    **I want** to view the restaurant details including all its dishes and reviews.
- *view_dish.feature* \
  **Feature**: View Dish \
    **In order to** know about a dish, \
    **As a** user, \
    **I want** to view the registered dish details.
- *review_restaurant.feature* \
  **Feature**: Register Review \
    **In order to** share my opinion about a restaurant, \
    **As a** user, \
    **I want** to register a review with a rating and an optional comment about the restaurant.
- *edit_restaurant.feature* \
  **Feature**: Edit Restaurant \
    **In order to** keep updated my previous registers about restaurants, \
    **As a** user, \
    **I want** to edit a restaurant register I created.
- *edit_dish.feature* \
  **Feature**: Edit Dish \
    **In order to** keep updated my previous registers about dishes, \
    **As a** user, \
    **I want** to edit a dish register I created.

## Tools ##

To facilitate the description of the feature scenarios, while connecting them to Python code that tests if the scenarios are satisfied by the application, we will use the Gherkin syntax and the Behave tool. 

To get Behave and integrate it with Django, install:

```shell script
$ pipenv install behave
$ pipenv install behave-django
```

And add the 'behave_django' application at the end of the INSTALLED_APPS list in *myrecommendations/settings.py*:

```python
INSTALLED_APPS = [
    'myrestaurants',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'behave_django',
]
```

Moreover, to make it possible to guide a browser from the test, and thus check if the application follows the expected behaviour from a end-user perspective, we will also use Splinter. It can be installed with the following command:

```shell script
$ pipenv install splinter
```

Finally, for end-to-end test, it is necessary to have a browser to test from client side. With Splinter, different browsers can be configured for testing, for instance Chrome, the most common one. 

Assuming Chrome is already installed in your computer, the only requirement to use it for automated testing is the ChromeDriver, available for Windows, Linux and Mac from [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)

You can also install it using different package managers. For instance with **apt** on Linux:

```shell script
apt-get update
apt-get install chromedriver
```

Or **[Brew](https://brew.sh)** on OSX:

```shell script
brew update
brew install chromedriver
xattr -d com.apple.quarantine $(which chromedriver)
```

Or **[Chocolatey](https://chocolatey.org/docs/installation)** on Windows:

```shell script
choco install chromedriver
```

### Testing with Firefox instead of Chrome ###

Alternatively, for Firefox, install the browser:

``` 
sudo apt-get update
sudo apt-get install firefox
``` 

Then, download Geckodriver and unpack it from [https://github.com/mozilla/geckodriver/releases/](https://github.com/mozilla/geckodriver/releases/)

Finally, add the geckodriver to your path:

```
export PATH=$PATH:/your/path/to/geckodriver
```

And configure the test environment in `environment.py`, as detailed next, to use `firefox` instead of `chrome`.

## Environment ##

After installing all the required tools for BDD, we also need to configure the testing environment. In this case, the Django application myrestaurant.

We do so in a file in the *features/* folder called *environment.py*:

```python
from splinter.browser import Browser

def before_all(context):
    context.browser = Browser('chrome', headless=True)

def after_all(context):
    context.browser.quit()
    context.browser = None
```

This file defines the Django settings to load and test, the context to be passed to each testing step, and then what to:

* **Before all tests**: setting Google Chrome as the browser used to act as the user.
* **After all tests**: closing the browser used for testing.

Development of the MyRestaurants Features
=========================================

Now, it is time to start implementing the identified features. In Agile Behaviour Driven Development, the idea is to prioritise features based on their value for the stakeholders: product owners, users, clients, customers, developers, etc.

Following a BDD approach, we will specify first the intended behaviours through the different scenarios we might encounter for each feature. 

Then, we will start implementing the different steps that constitute each scenario and the application code to make it show the expected behaviour.

## Feature: Register Restaurant ##

The most important feature is Register Restaurant as this is the starting point to fill the application with data and satisfy the need of registering the restaurants users have visited.

The feature file *register_restaurant.feature* currently looks like:

```
Feature: Register Restaurant
  In order to keep track of the restaurants I visit
  As a user
  I want to register a restaurant together with its location and contact details
```

We will start detailing it by adding scenarios with the help of the stakeholders. Scenarios describe specific situations of use of a feature. Scenarios are described in terms of pre-conditions (Givens), events related with the specified feature (Whens) and outcomes (Thens).

For instance, the scenario when a user registers a restaurant proving just the minimal required data, the restaurant name, and taking into account that the user should exist and login before, while contain the following steps:

```gherkin
  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register just restaurant name
    Given I login as user "user" with password "password"
    When I register restaurant
      | name        |
      | The Tavern  |
    Then I'm viewing the details page for restaurant by "user"
      | name        |
      | The Tavern  |
    And There are 1 restaurants
```

After defining the scenario, we can start the BDD process which implies that we start coding when a test fails. To trigger the BDD test we should type from the Python environment where Behave has been installed. From the project root:

```shell script
$ python manage.py behave
```

As a result, and after creating the `features/steps` folder, we will get in the console the templates to implement all the scenario steps that are not implemented yet:

```text
You can implement step definitions for undefined steps with these snippets:

@given(u'Exists a user "user" with password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists a user "user" with password "password"')

@given(u'I login as user "user" with password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I login as user "user" with password "password"')
    
@when(u'I register restaurant')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I register restaurant')

@then(u'I\'m viewing the details page for restaurant by "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for restaurant by "user"')

@then(u'There are 1 restaurants')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 restaurants')
```

We will use separate step implementation files for each feature. 

### Authentication Steps ###

The ones related with authentication and user management, as they are shared by almost all features, will also be implemented in a separate Python file, *authentication.py* in the *features/steps/* folder:

```python
from behave import *

use_step_matcher("parse")

@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, email='user@example.com', password=password)

@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/accounts/login/?next=/myrestaurants/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('login').first.click()
```

Both steps are parameterized, so we can use the steps to login users with any username and password, as long as we have previously created them and the password matches.

The first steps simply creates a new object based on the existing Django User class using the provided username and password, and a fixed e-mail.

The second step implements the user behaviour for login. The browser, created in *environment.py* and passed to the step through the context parameter, is used to browse to the login view, fill the login form inputs named 'username' and 'password' with the corresponding values and finally click the 'login' button.

To support this behaviour, we first link the login, and also logout, views from django.contrib.auth.views in the project urls file, *myrecommendations/urls.py*:

```python
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
]
```

And create the login form template as expected by the Django login view by default in *registration/login.html*. However, to make it possible for Django to find templates, we first create a *templates* folder in the project root and another in the myrestaurants application, *myrestaurants/templates*. We then register them as default templates folders in *myrecommendations/settings.py* defining 'DIRS' in TEMPLATES as detailed next:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        ...
```

Then, we can define the login form in *templates/registration/login.html*:

```html
<html>
<head><title>MyRecommendations Login Form</title></head>
<body>
    {% if form.errors %}
        <p>Your username and password didn't match. Please try again.</p>
    {% endif %}
    <form method="post" action="{% url 'login' %}">
        {% csrf_token %}
        <table>
            <tr>
                <td>{{ form.username.label_tag }}</td>
                <td>{{ form.username }}</td>
            </tr>
            <tr>
                <td>{{ form.password.label_tag }}</td>
                <td>{{ form.password }}</td>
            </tr>
        </table>
        <input type="submit" value="login" />
        <input type="hidden" name="next" value="{{ next }}" />
    </form>
</body>
</html>
```

With this we will have implemented the first two steps in the *register_restaurant.feature* first scenario. If we run **behave** again, we will get the following output, which shows that the first two step are implemented while the last three are still pending:

```text
  Scenario: Register just restaurant name                 # features/register_restaurant.feature:9
    Given Exists a user "user" with password "password"   # features/steps/authentication.py:6 0.301s
    Given I login as user "user" with password "password" # features/steps/authentication.py:12 1.207s
    When I register restaurant                            # None
      | name       |
      | The Tavern |
    Then I'm viewing the details page for restaurant      # None
      | name       |
      | The Tavern |
    And There are 1 restaurants                           # None

  0 features passed, 1 failed, 7 skipped
  0 scenarios passed, 1 failed, 0 skipped
  2 steps passed, 0 failed, 0 skipped, 3 undefined
```

### Register Restaurant Step ###

The undefined steps are related with the Register Restaurant feature and are implemented in *features/steps/register_restaurant.py*:

```python
from behave import *
import operator
from functools import reduce
from django.db.models import Q

use_step_matcher("parse")

@when(u'I register restaurant')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('myrestaurants:restaurant_create'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Submit').first.click()

@then(u'I\'m viewing the details page for restaurant by "{user}"')
def step_impl(context, user):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from myrestaurants.models import Restaurant
    restaurant = Restaurant.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(restaurant)

@then(u'There are {count:n} restaurants')
def step_impl(context, count):
    from myrestaurants.models import Restaurant
    assert count == Restaurant.objects.count()
```

The first step, for each table row provided as step input, browses to the myrestaurants restaurant_create view and fills the displayed form inputs with the corresponding row data identified by the table headings. For instance, if the name of the restaurant to be created is provided, the corresponding input named 'name' is filled the the corresponding table cell. Finally, after filling all provided form inputs, it is submitted.

The second step implementation filters the registered restaurants by combinining all the criteria provided in the step input table. Then, it checks that the browser is currently displaying the details page for that particular restaurant.

The third *register_restaurant.py* step implementation checks that there are currently registered the provided amount of restaurants.

If we try to run this steps using behave, they will fail because none of the requested views is implemented yet, neither the Restaurant model or the forms to register a restaurant.

First of all, we will implement the model. For the moment, given the requirements in the Register Restaurant feature, we just need a text field for the name. Consequently, we can add in *myrestaurants/models.py*:

```python
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
```

We can then update the database to accomodate this new entity by running:

```shell script
$ python manage.py makemigrations myrestaurants
```

The result is that the first migation of the data model for the myrestaurants application is created:

```
Migrations for 'myrestaurants':
  myrestaurants/migrations/0001_initial.py:
    - Create model Restaurant
```

It can be then applied to create the tables in the database that will accommodate instances of the Restaurant model:

```shell script
$ python manage.py migrate
```

Now we can implement the 'myrestaurants:restaurant_create' view where the browser navigates to in the first step implemented in *register_restaurant.py*. It is defined in *myrestaurants/urls.py* and linked to the URL 'restaurants/create':

```python
from django.urls import path
from django.views.generic.edit import CreateView
from myrestaurants.forms import RestaurantForm
from myrestaurants.models import Restaurant

app_name = "myrestaurants"

urlpatterns = [
    # Register a restaurant, from: /myrestaurants/create
    path('restaurants/create',
        CreateView.as_view(
            model=Restaurant,
            template_name='myrestaurants/form.html',
            form_class=RestaurantForm),
        name='restaurant_create'),
]
```

To publish the URLs and views defined in *myrestaurants/urls.py* and make them accessible from the project, they should be included from the global URLs file *myrecommendations/urls.py*:

```python
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='myrestaurants:restaurant_list'), name='home'),
    path('admin/', admin.site.urls),
    path('myrestaurants/', include('myrestaurants.urls', namespace='myrestaurants')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
]
```

This way, the views defined for the myrestaurants application will be available from '/myrestaurants/...' and their names in the 'myrestaurants' namespace.

The current view is a Django Model View for the creation of new model entities, a **CreateView**. It is associated to Restaurant, because it will create instances of this model, and requires a form to be displayed together with template where the form will be shown.

Django provides the class ModelForm to automatically implement forms to create and update model entities. To create restaurants, we define a RestaurantForm subclass of ModelForm in *myrestaurants/forms.py*:

```python
from django.forms import ModelForm
from myrestaurants.models import Restaurant

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ()
```

Model Forms generate appropriate form inputs with validation for all the model fields that are not explicitly excluded. Currently, it will generate just a test input for the 'name' field.

Forms are displayed using a template that renders them. We will thus start defining the templates for the myrestaurants application in *myrestaurants/templates/myrestaurants*.

The first one is a base template that defines the common structure for all application templates, *myrestaurants/templates/myrestaurants/base.html*:

 ```html
<html>
<head>
    <title>{% block title %}MyRestaurants by MyRecommentdations{% endblock %}</title>
</head>
<body>
<div id="header">
    {% block header %}
        {% if user.is_authenticated %}
            <p>User: {{ user.username }} | <a href="{% url 'logout' %}?next={{request.path}}">logout</a></p>
        {% else %}
            <p><a href="{% url 'login' %}?next={{request.path}}">login</a></p>
        {% endif %}
    {% endblock %}
</div>
<div id="sidebar">
    {% block sidebar %}
        <ul>
            <li><a href="/myrestaurants/">Home</a></li>
        </ul>
    {% endblock %}
</div>
<div id="content">
    {% block content %}
        {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% endblock %}
</div>
<div id="footer">
    {% block footer %}{% endblock %}
</div>
</body>
</html>
 ```

This base template defines the global HTML structure and names subsections of it, called **block**, that can  be replaced by more specific templates.

The *myrestaurants/templates/myrestaurants/form.html* template is a template extending the base one that displays a form in the content block:

```html
{% extends "myrestaurants/base.html" %}

{% block content %}
<form method="post" enctype="multipart/form-data" action="">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
    </table>
    <input type="submit" value="Submit"/>
</form>
{% endblock %}
```

With this, we have implemented everything needed to suport the 'I register a restaurant' step. If we execute **behave**, 3 steps now pass and the following error message is the output for the failing step:

```text
ImproperlyConfigured: No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
```

### Restaurant Details Step ###

This is because Django doesn't know what to after the restaurant is created. The default behaviour is to redirect the user to the view displaying the newly created model entity and the way to determine that URL is by calling the 'get_absolute_url' method for the model. We will thus add in *myrestaurants/model.py*:

```python
from django.db import models
from django.urls.base import reverse

class Restaurant(models.Model):
    name = models.TextField()

    def get_absolute_url(self):
        return reverse('myrestaurants:restaurant_detail', kwargs={'pk': self.pk})
```

We don't fix a URL but return the URL associated to the view responsible for showing the details of a restaurant. The URL is built using the identifier of the entity to be displayed, which is passed as a kwargs parameter.

Now, we need to define this view in *myrestaurants/urls.py* by adding a new URL pattern:

```python
    ...,
    # Restaurant details, /myrestaurants/1
    path('restaurants/<int:pk>',
        DetailView.as_view(
            model=Restaurant,
            template_name='myrestaurants/restaurant_detail.html'),
        name='restaurant_detail'),
]
```

This one corresponds to a Django class view named **DetailView**, responsible for displaying instances of the associated model using the provided template.

The template also extends the base one and for the moment just displays the associate restaurant instance provided by the DetailView to the template *myrestaurants/templates/myrestaurants/restaurant_detail.html*:

```html
{% extends "myrestaurants/base.html" %}
{% block content %}
<h1>
    {{ restaurant.name }}
</h1>
{% endblock %}
```

This concludes the implementation of the first scenario of *features/register_restaurant.feature*. If we run **behave** again, we will get that all steps in the scenario have passed:

```text
  Scenario: Register just restaurant name                 # features/register_restaurant.feature:9
    Given Exists a user "user" with password "password"   # features/steps/authentication.py:6 0.313s
    Given I login as user "user" with password "password" # features/steps/authentication.py:12 0.859s
    When I register restaurant                            # features/steps/register_restaurant.py:8 0.382s
      | name       |
      | The Tavern |
    Then I'm viewing the details page for restaurant      # features/steps/register_restaurant.py:18 0.013s
      | name       |
      | The Tavern |
    And There are 1 restaurants                           # features/steps/register_restaurant.py:26 0.001s

1 feature passed, 0 failed, 7 skipped
1 scenario passed, 0 failed, 0 skipped
5 steps passed, 0 failed, 0 skipped, 0 undefined
```

The objective is now to continue defining additional scenarios for Register Restaurant feature that specify, for instance, the rest of the model fields the stakeholders expect to be capable of defining to capture the restaurant details they want to register.

# Finished MyRestaurants Application #

The same has been done for the rest of the features. They are available from the [features/](features) folder and have 
been completely implemented to fulfill the requested functionality, as shown by the fact that all the Behave tests are passing.

In addition to the source code in this repository, which constitutes the final application implementing all the previous 
[features/](features), there is an additional [completed](completed.md) document providing an overview of the resulting application.

Image Field
===========

The image field is a kind of field in the data model that allows associating images to model entities and storing them. 

First of all, it is necessary to install the Python image library Pillow. Follow:
[http://pillow.readthedocs.org/en/latest/installation.html](http://pillow.readthedocs.org/en/latest/installation.html)

Then, in myrecommendations/settings.py add:

```python
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
```

And in myrecommendations/urls.py, add at the end:

```python
from django.conf import settings
from django.views.static import serve

urlpatterns += [
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT, })
]
```

Finally, in myrestaurants/models.py add an **ImageField** to the **Dish** class to store images of the dishes:

```python
	image = models.ImageField(upload_to="myrestaurants", blank=True, null=True)
```

This field can be then used from the templates to display images, for instance to the *dish_detail.html* template to be added in myrestaurants/templates/myrestaurants:

```djangotemplate
{% extends "myrestaurants/base.html" %}

{% block content %}

<h1>
	{{ dish.name }}
	{% if user == dish.user %}
		(<a href="{% url 'myrestaurants:dish_edit' dish.restaurant.id dish.id %}">edit</a>)
	{% endif %}
</h1>

<p>{{ dish.description }}</p>

{% if dish.image %}
	<p><img src="{{ dish.image.url }}"/></p>
{% endif %}

<p>Served by 
	<a href="{% url 'myrestaurants:restaurant_detail' dish.restaurant.id %}">
		{{ dish.restaurant.name}}
	</a>
</p>

{% endblock %}

{% block footer %}
	Created by {{ dish.user }} on {{ dish.date }}
{% endblock %}
```

It is also important, when editing the image field using forms, to add the appropriate encoding to be used when uploading the image. To do that, edit *form.html* and include the appropriate *enctype* attribute:

```html
{% extends "myrestaurants/base.html" %}

{% block content %}

<form method="post" enctype="multipart/form-data" action="">
	{% csrf_token %}
	<table>
		{{ form.as_table }}
	</table>
	<input type="submit" value="Submit"/>
</form>

{% endblock %}
```

And remember, if you modify the class Dish to add the new image field *image*, you will need to migrate the database to upload the relevant tables so they include the new field:

```shell script
$ python manage.py makemigrations myrestaurants

$ python manage.py migrate
```
Otherwise, you will need to remove the database file and start from scratch.

# Unit Testing #

Testing the Restaurant averageRating method using unit tests in the *myrestaurants/tests.py*:

```python
from django.contrib.auth.models import User
from django.test import TestCase
from models import RestaurantReview, Restaurant

class RestaurantReviewTestCase(TestCase):
    def setUp(self):
        trendy = Restaurant.objects.create(name="Trendy Restaurant")
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        user3 = User.objects.create(username="user3")
        RestaurantReview.objects.create(rating=3, comment="Average...", restaurant=trendy, user=user1)
        RestaurantReview.objects.create(rating=5, comment="Excellent!", restaurant=trendy, user=user2)
        RestaurantReview.objects.create(rating=1, comment="Really bad!", restaurant=trendy, user=user3)
        Restaurant.objects.create(name="Unknown Restaurant")

    def test_average_3reviews(self):
        """The average review for a restaurant with 3 reviews is properly computed"""
        restaurant = Restaurant.objects.get(name="Trendy Restaurant")
        self.assertEqual(restaurant.averageRating(), 3)

    def test_average_no_review(self):
        """The average review for a restaurant without reviews is 0"""
        restaurant = Restaurant.objects.get(name="Unknown Restaurant")
        self.assertEqual(restaurant.averageRating(), 0)
```

To run the tests:

```shell script
$ python manage.py test
```
