
# MyRecommendations

[![Build Status](https://travis-ci.org/rogargon/myrecommendations.svg?branch=master)](https://travis-ci.org/rogargon/myrecommendations)

Recommendation applications developed using Django, including for the moment just:

- MyRestaurants

The source code for this project is available from:
[https://github.com/rogargon/myrecommendations](https://github.com/rogargon/myrecommendations)

The project includes **unit testing** and **End-To-End tests** using Behave and PhantomJS. **CI/CD** (Continuous Integration and Continuous Deployment) using Travis-CI and Heroku. Deployed at: 
[http://myrecommendations.herokuapp.com/myrestaurants]()

# Starting the MyRecommendations Project

After installing [Python and Django](https://docs.djangoproject.com/en/1.10/topics/install/), the recommended approach is using [virtualenv](https://virtualenv.pypa.io/en/stable/), it is possible to create a new Django project from the command line, as also documented in the [Django Tutorial part 1](https://docs.djangoproject.com/en/1.10/intro/tutorial01/). 

In our case the project is called 'myrecommendations':

```bash
$ django-admin.py startproject myrecommendations

$ cd myrecommendations

$ mkdir templates
```

In *myrecommendations/settings.py*, review your database settings. For instance, for an SQLite database, they should be:

```python
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
And register the templates folder adding it to the list of 'DIRS':

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
```

Then, let Django take control of the database:

```bash
$ python manage.py migrate
```

The 'migrate' command looks at INSTALLED_APPS defined in 'settings.py' and creates all required database tables according to the database settings.

To conclude project creation, define the admin user:

```bash
$ python manage.py createsuperuser
```

# Creating the MyRestaurants Application

Now that the project is ready, it is time to define project applications. In the case of this tutorial there is just one application, called 'myrestaurants'. To create it, type the following command from the root folder of the project:

```bash
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

Finally, to keep track of the requirements of this project, for the moment mainly Django, we can execute the command:

```bash
$ pip freeze > requirements.txt
```

This way we will get in the file *requirements.txt* all the required packages to execute the project:

```python
Django==1.10.6
```

MyRestaurants Data Model
-----------------------------------

To define the 'myrestaurants' data model composed of **Restaurant**, **Dish**, **Review** and **RestaurantReview**, add the following code to the file *myrestaurants/models.py*:

```python
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Restaurant(models.Model):
    name = models.TextField()
    street = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    zipCode = models.TextField(blank=True, null=True)
    stateOrProvince = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    telephone = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name

class Dish(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="myrestaurants", blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, null=True, related_name='dishes')

    def __unicode__(self):
        return u"%s" % self.name

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class RestaurantReview(Review):
    restaurant = models.ForeignKey(Restaurant)
    
    class Meta:
        unique_together = ("restaurant", "user") # Only one review per user and restaurant
```

Once the model is defined, it is time to update the database schema to accommodate the previous data model entities:

```bash
$ python manage.py makemigrations myrestaurants

$ python manage.py migrate
```

Optionally, register your model with the administrative interface (if you have the admin application enabled under INSTALLED_APPS in *myrecommendations/settings.py*), so you get a user interface for CRUD operations for free in '<URL>/admin’.

First, in *myrecommendations/settings.py*, check that installed applications include:

```python
'django.contrib.admin',
```
Finally, in admin.py in the myrestaurants directory, include:

```python
from django.contrib import admin
import models

admin.site.register(models.Restaurant)
admin.site.register(models.Dish)
admin.site.register(models.RestaurantReview)
```

Now, you can run the server:

```bash
$ python manage.py runserver
```

And check that you can administrate the new models from:
[http://localhost:8000/admin]()

Designing MyRestaurants URLs 
--------------------------

From the project root directory, edit *myrecommendations/urls.py* and add to the list of **urlpatterns** those for the application:

```python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myrestaurants/', include('myrestaurants.urls', namespace='myrestaurants')),
]
```

In the *myrestaurants* application folder create *urls.py* with the following code:

```python
from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Restaurant, Dish
from forms import RestaurantForm, DishForm
from views import RestaurantCreate, DishCreate, RestaurantDetail

urlpatterns = [
# List latest 10 restaurants: /myrestaurants/
    url(r'^$',
        ListView.as_view(
            queryset=Restaurant.objects.filter(date__lte=timezone.now()).order_by('-date')[:10],
            context_object_name='latest_restaurant_list',
            template_name='myrestaurants/restaurant_list.html'),
        name='restaurant_list'),
# Restaurant details, ex.: /myrestaurants/restaurants/1/
    url(r'^restaurants/(?P<pk>\d+)/$',
        RestaurantDetail.as_view(),
        name='restaurant_detail'),
# Restaurant dish details, ex: /myrestaurants/restaurants/1/dishes/1/
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/$',
        DetailView.as_view(
        	model=Dish,
        	plate_name='myrestaurants/dish_detail.html'),
        name='dish_detail'),
# Create a restaurant, /myrestaurants/restaurants/create/
    url(r'^restaurants/create/$',
        RestaurantCreate.as_view(),
        name='restaurant_create'),
# Edit restaurant details, ex.: /myrestaurants/restaurants/1/edit/
    url(r'^restaurants/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
        	model = Restaurant,
        	template_name = 'myrestaurants/form.html',
        	form_class = RestaurantForm),
        name='restaurant_edit'),
# Create a restaurant dish, ex.: /myrestaurants/restaurants/1/dishes/create/
    url(r'^restaurants/(?P<pk>\\d+)/dishes/create/$',
    	DishCreate.as_view(),
        name='dish_create'),
# Edit restaurant dish details, ex.: /myrestaurants/restaurants/1/dishes/1/edit/
    url(r'^restaurants/(?P<pkr>\\d+)/dishes/(?P<pk>\\d+)/edit/$',
    	UpdateView.as_view(
    		model = Dish,
    		template_name = 'myrestaurants/form.html',
    		form_class = DishForm),
    	name='dish_edit'),
# Create a restaurant review, ex.: /myrestaurants/restaurants/1/reviews/create/
# Unlike the previous patterns, this one is implemented using a method view instead of a class view
    url(r'^restaurants/(?P<pk>\\d+)/reviews/create/$',
    	'myrestaurants.views.review',
    	name='review_create'),
]
```

Custom Class Views
------------------

Then, define the custom application class views in *myrestaurants/views.py* adding the following code:

```python
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from models import RestaurantReview, Restaurant, Dish
from forms import RestaurantForm, DishForm

class RestaurantDetail(DetailView):
	model = Restaurant
	template_name = 'myrestaurants/restaurant_detail.html'

	def get_context_data(self, **kwargs):
		context = super(RestaurantDetail, self).get_context_data(**kwargs)
		context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
		return context

class RestaurantCreate(CreateView):
	model = Restaurant
	template_name = 'myrestaurants/form.html'
	form_class = RestaurantForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(RestaurantCreate, self).form_valid(form)

class DishCreate(CreateView):
	model = Dish
	template_name = 'myrestaurants/form.html'
	form_class = DishForm
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
		return super(DishCreate, self).form_valid(form)

def review(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if RestaurantReview.objects.filter(restaurant=restaurant, user=request.user).exists():
        RestaurantReview.objects.get(restaurant=restaurant, user=request.user).delete()
    new_review = RestaurantReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        restaurant=restaurant)
    new_review.save()
    return HttpResponseRedirect(reverse('myrestaurants:restaurant_detail', args=(restaurant.id,)))
```

Application Templates
----------------------

First, create a *base.html* template in *myrestaurants/templates/myrestaurants*:

```html
{% load staticfiles %}
<html>
<head>
<link rel="stylesheet" href="{% static "style/base.css" %}" />
<title>{% block title %}MyRestaurants by MyRecommendations{% endblock %}</title>
</head>
<body>
<div id="header">
	{% block header %}
	{% if user.username %}<p>User {{ user.username }}</p>
	{% else %}<p><a href="/login/">Sign in</a></p>{% endif %}
	{% endblock %}
</div>
<div id="sidebar">
	{% block sidebar %}<ul><li><a href="/myrestaurants">Home</a></li></ul>{% endblock %}
</div>
<div id="content">
	{% block content %}
	{% if error_message %}<p><strong>{{ error_message}}</strong></p>{% endif %}
	{% endblock %}
</div>
<div id="footer">
	{% block footer %}{% endblock %}
</div>
</body>
</html>
```

Next create *restaurant_list.html* in *myrestaurants/templates/myrestaurants*:

```html
{% extends "myrestaurants/base.html" %}

{% block content %}
<h1>
	Restaurants 
	{% if user %}(<a href="{% url 'myrestaurants:restaurant_create' %}">add</a>){% endif %}
</h1>
<ul>
	{% for restaurant in latest_restaurant_list %}
		<li><a href="{% url 'myrestaurants:restaurant_detail' restaurant.id %}">
		{{ restaurant.name }}</a></li>
	{% empty %}<li>Sorry, no restaurants registered yet.</li>
	{% endfor %}
</ul>
{% endblock %}
```

And *restaurant_detail.html*, which includes the list of dishes and the review form also in *myrestaurants/templates/myrestaurants*:

```html
{% extends "myrestaurants/base.html" %}

{% block content %}
<h1>
	{{ restaurant.name }}
	{% if user == restaurant.user %}
		(<a href="{% url 'myrestaurants:restaurant_edit' restaurant.id %}">edit</a>)
	{% endif %}
</h1>

<h2>Address:</h2>
<p>
	{{ restaurant.street }}, {{ restaurant.number }} <br/>
	{{ restaurant.zipcode }} {{ restaurant.city }} <br/>
	{{ restaurant.stateOrProvince }} ({{ restaurant.country }})
</p>

<h2>Dishes
	{% if user %}
		(<a href="{% url 'myrestaurants:dish_create' restaurant.id %}">add</a>)
	{% endif %}
</h2>
<ul>
	{% for dish in restaurant.dishes.all %}
		<li><a href="{% url 'myrestaurants:dish_detail' restaurant.id dish.id %}">
		{{ dish.name }}</a></li>
	{% empty %}<li>Sorry, no dishes for this restaurant yet.</li>
	{% endfor %}
</ul>

<h2>Reviews</h2>
<ul>
	{% for review in restaurant.restaurantreview_set.all %}
		<li>
			<p>{{ review.rating }} star{{ review.rating|pluralize }}</p>
			<p>{% if review.comment %}{{ review.comment }}{% endif %}</p>
			<p>Created by {{ review.user }} on {{ review.date }}</p>
		</li>
	{% endfor %}
</ul>

<h3>Add Review</h3>
<form action="{% url 'myrestaurants:review_create' restaurant.id %}" method="post">
	{% csrf_token %}

	Message: <textarea name="comment" id="comment" rows="4"></textarea>
	<p>Rating:</p>
	<p>
		{% for rate in RATING_CHOICES %}
			<input type="radio" name="rating" id="rating{{ forloop.counter }}" value="{{ rate.0 }}" />
			<label for="choice{{ forloop.counter }}">{{ rate.1 }} star{{rate.0|pluralize }}</label>
			<br/>
		{% endfor %}
	</p>
	<input type="submit" value="Review" />
</form>
{% endblock %}

{% block footer %}
Created by {{ restaurant.user }} on {{ restaurant.date }}
{% endblock %}
```

Model Forms
------------

The model forms defined in the new file *forms.py* make it possible to generate forms from the *Restaurant* and *Dish* models to create and edit them:

```python
from django.forms import ModelForm
from models import Restaurant, Dish

class RestaurantForm(ModelForm):
	class Meta:
		model = Restaurant
		exclude = ('user', 'date',)

class DishForm(ModelForm):
	class Meta:
		model = Dish
		exclude = ('user', 'date', 'restaurant',)
```

And the template that shows them, *form.html* in *myrestaurants/templates/myrestaurants*:

```html
{% extends "myrestaurants/base.html" %}

{% block content %}

<form method="post" action="">
	{% csrf_token %}
	<table>
		{{ form.as_table }}
	</table>
	<input type="submit" value="Submit"/>
</form>

{% endblock %}
```

Schema Migration
================

Migrations are how Django stores changes to your models (and thus your database schema). Previously, after creating the database, we have enabled the migrations mechanism with the command:

```bash
$ python manage.py makemigrations myrestaurants
```

The previous command computes the changes to be performed to the schema, in this case to create it from scratch, and stores them in *myrestaurants/migrations/0001_initial.py*.

Then, the following command applied this changes and populates the database schema:

```bash
$ python manage.py migrate
```

From this moment, whenever the model is updated, it is possible to migrate the schema so the data already inserted in the database is adapted to the new schema database.

The previous step should be then repeated. First, to compute the changes to be done to the schema and all the instance data currently stored:

```bash
$ python manage.py makemigrations myrestaurants
```

This will generate a new migration file, like *myrestaurants/migrations/0002_...py*. Then, the changes are applied to synchronize the model and the database:

```bash
$ python manage.py migrate
```

**Note**: if the migrations mechanism is not activated for a particular app, when the app model is changed the database must be deleted and recreated.

Image Field
===========

The image field is a kind of field in the data model that allows associating images to model entities and storing them. 

First of all, it is necessary to install the Python image library Pillow. Follow:
[http://pillow.readthedocs.org/en/latest/installation.html](http://pillow.readthedocs.org/en/latest/installation.html)

Then, in myrecommendations/settings.py add:

```python
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

And in myrecommendations/urls.py, add at the end:

```python

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
    	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    		{'document_root': settings.MEDIA_ROOT, }),
)
```

Finally, in myrestaurants/models.py it is possible now to add an **ImageField** to the **Dish** class to store images of the dishes:

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

```bash
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

```shell
$ python manage.py test
```

