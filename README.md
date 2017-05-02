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
