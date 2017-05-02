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
