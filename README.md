MyRecommendations
================

Recommendation applications developed using Django, including for the moment just:
- MyRestaurants

Developed following a Behaviour Driven Development approach.

The source code for this project is available from:
[https://github.com/rogargon/myrecommendations/tree/bdd]()

Starting a Project
==============
After installing [Python and Django](https://docs.djangoproject.com/en/1.10/topics/install/), 
it is possible to create a new Django project from the command line, as also documented in the 
[Django Tutorial part 1](https://docs.djangoproject.com/en/1.10/intro/tutorial01/). 

In our case the project is called 'myrecommendations':

```bash
$ django-admin.py startproject myrecommendations

$ cd myrecommendations
```

In myrecommendations/settings.py

- Review your database settings, for instance for an SQLite database they should be:

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
python manage.py createsuperuser

```