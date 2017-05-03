MyRecommendations
=================

Recommendation applications developed using Django, including for the moment just:
- MyRestaurants

Developed following a Behaviour Driven Development approach.

The source code for this project is available from:
[https://github.com/rogargon/myrecommendations-bdd](https://github.com/rogargon/myrecommendations-bdd)


Starting the MyRecommendations Project
======================================

After installing [Python and Django](https://docs.djangoproject.com/en/1.10/topics/install/), 
the recommended approach is using [virtualenv](https://virtualenv.pypa.io/en/stable/), 
it is possible to create a new Django project from the command line, as also documented in the 
[Django Tutorial part 1](https://docs.djangoproject.com/en/1.10/intro/tutorial01/). 

In our case the project is called 'myrecommendations':

```bash
$ django-admin.py startproject myrecommendations

$ cd myrecommendations
```

In *myrecommendations/settings.py*, review your database settings. 
For instance, for an SQLite database, they should be:

```python
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

Finally, let Django take control of the database:

```bash
$ python manage.py migrate

```

The 'migrate' command looks at INSTALLED_APPS defined in 'settings.py' and creates
all required database tables according to the database settings.

Finally, create the admin user:

```bash
$ python manage.py createsuperuser

```

Creating the MyRestaurants Application
======================================

Now that the project is ready, it is time to define project applications. 
In the case of this tutorial there is just one application, called 'myrestaurants'. 
To create it, type the following command from the root folder of the project:

```bash
$ python manage.py startapp myrestaurants

```

Then, add 'myrestaurants' to the INSTALLED_APPS list in myrecommendations/settings.py

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

Finally, to keep track of the requirements of this project, for the moment mainly Django, we can execute
the command:

```bash
$ pip freeze > requirements.txt
```

This way we will get in the file *requirements.txt* all the required packages to execute the project:

```python
Django==1.10.6
```

Agile Behaviour Driven Development (BDD)
========================================

Now, we have the initial Django project and application that we will start filling with functionality.

The aim of this application is to help users keep track of the restaurants they have visitied, 
the dishes they have tasted there and to provide restaurant reviews for other users.

Consequently, and following a BDD approach, first we define the intended **features**:

* Register Restaurant
* Register Dish
* List Recent Restaurants
* View Restaurant
* View Dish
* Review Restaurant
* Edit Restaurant
* Edit Dish

For the moment, additional features like removing restaurants and dishes have not been considered, 
though they can be added in future iterations.

Next, we will start detailing each feature. For each one, a new file is generated in a *features/* folder. 
Each file provides details about the feature value, involved stakeholders and feature details following the template:

**In order to** <achieve some business value>, 
**As a** <stakeholder type>, 
**I want** <some new system feature> 

The result is the following list of feature files with their corresponding content in the *features/* folder:

- *register_restaurant.feature*
  **Feature**: Register Restaurant
    **In order to** keep track of the restaurants I visit
    **As a** user
    **I want** to register a restaurant together with its location and contact details
- *register_dish.feature*
  **Feature**: Register Dish
    **In order to** keep track of the dishes I eat
    **As a** user
    **I want** to register a dish in the corresponding restaurant together with its details
- *list_restaurants.feature*
  **Feature**: List Restaurants
    **In order to** keep myself up to date about registered restaurants
    **As a** user
    **I want** to list the last 10 registered restaurants
- *view_restaurant.feature*
  **Feature**: View Restaurant
    **In order to** know about a restaurant
    **As a** user
    **I want** to view the restaurant details including all its dishes and reviews
- *view_dish.feature*
  **Feature**: View Dish
    **In order to** know about a dish
    **As a** user
    **I want** to view the registered dish details
- *review_restaurant.feature*
  **Feature**: Register Review
    **In order to** share my opinion about a restaurant
    **As a** user
    **I want** to register a review with a rating and an optional comment about the restaurant
- *edit_restaurant.feature*
  **Feature**: Edit Restaurant
    **In order to** keep updated my previous registers about restaurants
    **As a** user
    **I want** to edit a restaurant register I created
- *edit_dish.feature*
  **Feature**: Edit Dish
    **In order to** keep updated my previous registers about dishes
    **As a** user
    **I want** to edit a dish register I created

## Tools ##

To facilitate the description of the feature scenarios, 
while connecting them to Python code that tests if the scenarios are satisfied by the application, 
we will use the Gherkin syntax and the Behave.

To install Behave:

```shell
$ pip install behave
```

Moreover, to make it possible to guide a browser from the test, and thus check if the application 
follows the expected behaviour from a end-user perspective, we will also use Splinter. 
It can be installed with the following command:

```shell
$ pip install splinter
```

These dependencies are also detailed, with explicit versions for each package that have been tested 
to work together, in the *requirements.txt* file available from the root folder of the myrecommendations project:

```python
Django==1.10.6
behave==1.2.5
splinter==0.7.5
```

Finally, for end-to-end test, it is necessary to have a browser to test from client side. With Splinter, 
different browsers can be configured for testing, for instance Firefox or Chrome. 
However, the most convenient way is to use a headless browsers (that does not require a user interface) like PhantomJS.

PhantomJS is available from http://phantomjs.org/download.html

You can also install it using different package managers. For instance with **apt** in Linux:

```bash
$ apt-get update
$ apt-get install phantomjs
```

Or **brew** in OSX:

```shell
$ brew update
$ brew install phantomjs
```

## Environment ##

After installing all the required tools for BDD, we also need to configure the testing environment. 
In this case, the Django application myrestaurant.

We do so in a file in the *features/* folder called *environment.py*:

```python
import os
import django
from behave.runner import Context
from django.shortcuts import resolve_url
from django.test.runner import DiscoverRunner
from django.test.testcases import LiveServerTestCase
from splinter.browser import Browser

os.environ["DJANGO_SETTINGS_MODULE"] = "myrecommendations.settings"

class ExtendedContext(Context):
    def get_url(self, to=None, *args, **kwargs):
        return self.test.live_server_url + (
            resolve_url(to, *args, **kwargs) if to else '')

def before_all(context):
    django.setup()
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.browser = Browser('phantomjs')

def before_scenario(context, scenario):
    context.old_db_config = context.test_runner.setup_databases()
    object.__setattr__(context, '__class__', ExtendedContext)
    context.test = LiveServerTestCase
    context.test.setUpClass()

def after_scenario(context, scenario):
    context.test.tearDownClass()
    del context.test
    context.test_runner.teardown_databases(context.old_db_config)

def after_all(context):
    context.test_runner.teardown_test_environment()
    context.browser.quit()
    context.browser = None
```

This file defines the Django settings to load and test, the context to be passed to each testing step, and then what to:

* **Before all tests**: setting Django, preparing it for testing and a browser session based on PhantomJS to act as the user.
* **Before each scenario**: the Django database is initialized, together with the context to be passed to each scenario step implementation with all the data about the current application status.
* **After each scenario**: the Django database is destroyed so the next scenario will start with a clean one. This way each scenario is independent from previous ones and interferences are avoided.
* **After all tests**: the testing environment is destroyed together with the browser used for testing.

Development of the MyRestaurants Features
=========================================

Now, it is time to start implementing the identified features. 
In Agile Behaviour Driven Development, the idea is to prioritise features based on their value for the stakeholders: 
product owners, users, clients, customers, developers, etc.
Following a BDD approach, we will specify first the intended behaviours through the 
different scenarios we might encounter for each feature. 

Then, we will start implementing the different steps that constitute each scenario and the application code 
to make it show the expected behaviour.

## Feature: Register Restaurant ##

The most important feature is Register Restaurant as this is the starting point to fill the application with data and 
satisfy their need of registering the restaurants they have visited.

The feature file *register_restaurant.feature* currently looks like:

```
Feature: Register Restaurant
  In order to keep track of the restaurants I visit
  As a user
  I want to register a restaurant together with its location and contact details
```

We will start detailing it by adding scenarios with the help of the stakeholders. 
Scenarios describe specific situations of use of a feature. 
Scenarios are described in terms of pre-conditions (Givens), 
events related with the specified feature (Whens) and outcomes (Thens).

For instance, the scenario when a user registers a restaurant proving just the minimal required data, 
the restaurant name, and taking into account that the user should exist and login before, 
while contain the following steps:

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

After defining the scenario, we can start the BDD process which implies that we start coding when a test fails. 
To trigger the BDD test we should type from the Python environment where Behave has been installed. 
From the project root:

```shell
$ behave
```

As a result, we will get in the console the templates to implement all the scenario steps that are not implemented yet:

```shell
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
The ones related with authentication and user management, as they are shared by almost all features, 
will also be implemented in a separate Python file, *authentication.py* in the *features/steps/* folder:

```python
from behave import *

use_step_matcher("parse")

@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, email='user@example.com', password=password)

@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/login'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('login').first.click()
```

Both steps are parameterized so we can use the steps to login users with any username and password, 
as long as we have previously created them and the password matches.

The first steps simply creates a new object based on the existing Django User class using the provided 
username and password, and a fixed e-mail.

The second step implements the user behaviour for login. The browser, created in *environment.py* and passed 
to the step through the context parameter, is used to browse to the login view, fill the login form inputs 
named 'username' and 'password' with the corresponding values and finally click the 'login' button.

To support this behaviour, we first link the login, and also logout, views from django.contrib.auth.views
in the project urls file, *myrecommendations/urls.py*:

```python
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^admin/', admin.site.urls),
]
```

And create the login form template as expected by the Django login view by default in *registration/login.html*.
However, to make it possible for Django to find templates, we first create a *templates* folder in the project root 
and another in the myrestaurants application, *myrestaurants/templates*. We then register them as default templates
folders in *myrecommendations/settings.py* defining 'DIRS' in TEMPLATES as detailed next:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

With this we will have implemented the first two steps in the *register_restaurant.feature* first scenario.
If we run **behave** again, we will get the following output, which shows that the first two step are implemented
while the last three are still pending:

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
