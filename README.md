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
