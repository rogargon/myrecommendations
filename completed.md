MyRecommendations
=================

Recommendation applications developed using Django, including for the moment just:
- MyRestaurants

The project is developed following an Agile Behaviour Driven Development approach, as detailed in [https://github.com/rogargon/myrecommendations](https://github.com/rogargon/myrecommendations)

This document provides an overview of the final result, the completed application.


MyRestaurants Data Model
-----------------------------------

To define the 'myrestaurants' data model composed of **Restaurant**, **Dish**, **Review** and **RestaurantReview**, the following code has been added to *myrestaurants/models.py*:

```python
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    street = models.CharField(max_length=120, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    zipCode = models.CharField(max_length=120, blank=True, null=True)
    stateOrProvince = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    telephone = models.CharField(max_length=120, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('myrestaurants:restaurant_detail', kwargs={'pk': self.pk})

    def averageRating(self):
        reviewCount = self.restaurantreview_set.count()
        if not reviewCount:
            return 0
        else:
            ratingSum = sum([float(review.rating) for review in self.restaurantreview_set.all()])
            return ratingSum / reviewCount

class Dish(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="myrestaurants", blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, null=True, related_name='dishes', on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('myrestaurants:dish_detail', kwargs={'pkr': self.restaurant.pk, 'pk': self.pk})

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class RestaurantReview(Review):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

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
from myrestaurants.models import Restaurant, Dish, RestaurantReview

admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(RestaurantReview)
```

Now, you can run the server:

```bash
$ python manage.py runserver
```

And check that you can administrate the new models from:
[http://localhost:8000/admin](http://localhost:8000/admin)

MyRestaurants URLs Design
--------------------------

From the project root directory, *myrecommendations/urls.py* defines the URL at the whole project level and includes the
ones particular to the *myrestaurants* application:

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

The URL and view for the *myrestaurants* application are definied in *myrestaurantes/urls.py*:

```python
from django.urls import path
from django.utils import timezone
from django.views.generic import DetailView, ListView
from myrestaurants.models import Restaurant, Dish
from myrestaurants.forms import RestaurantForm, DishForm
from myrestaurants.views import RestaurantCreate, DishCreate, RestaurantDetail, review, LoginRequiredCheckIsOwnerUpdateView

app_name = "myrestaurants"

urlpatterns = [
    # List latest 5 restaurants: /myrestaurants/
    path('',
        ListView.as_view(
            queryset=Restaurant.objects.filter(date__lte=timezone.now()).order_by('-date')[:5],
            context_object_name='latest_restaurant_list',
            template_name='myrestaurants/restaurant_list.html'),
        name='restaurant_list'),

    # Restaurant details, ex.: /myrestaurants/restaurants/1/
    path('restaurants/<int:pk>',
        RestaurantDetail.as_view(),
        name='restaurant_detail'),

    # Restaurant dish details, ex: /myrestaurants/restaurants/1/dishes/1/
    path('restaurants/<int:pkr>/dishes/<int:pk>',
        DetailView.as_view(
            model=Dish,
            template_name='myrestaurants/dish_detail.html'),
        name='dish_detail'),

    # Create a restaurant, /myrestaurants/restaurants/create/
    path('restaurants/create',
        RestaurantCreate.as_view(),
        name='restaurant_create'),

    # Edit restaurant details, ex.: /myrestaurants/restaurants/1/edit/
    path('restaurants/<int:pk>/edit',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Restaurant,
            form_class=RestaurantForm),
        name='restaurant_edit'),

    # Create a restaurant dish, ex.: /myrestaurants/restaurants/1/dishes/create/
    path('restaurants/<int:pk>/dishes/create',
        DishCreate.as_view(),
        name='dish_create'),

    # Edit restaurant dish details, ex.: /myrestaurants/restaurants/1/dishes/1/edit/
    path('restaurants/<int:pkr>/dishes/<int:pk>/edit',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Dish,
            form_class=DishForm),
        name='dish_edit'),

    # Create a restaurant review, ex.: /myrestaurants/restaurants/1/reviews/create/
    path('restaurants/<int:pk>/reviews/create',
        review,
        name='review_create'),
]
```

Custom Class Views
------------------

Some of the views linked from *myrestaurants/urls.py* are custom class views in *myrestaurants/views.py* that provide
additional functionality like security checks:

```python
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

from myrestaurants.models import RestaurantReview, Restaurant, Dish
from myrestaurants.forms import RestaurantForm, DishForm

# Security Mixins

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'myrestaurants/form.html'

# HTML Views

class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = 'myrestaurants/restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RestaurantDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context

class RestaurantCreate(LoginRequiredMixin, CreateView):
    model = Restaurant
    template_name = 'myrestaurants/form.html'
    form_class = RestaurantForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreate, self).form_valid(form)

class DishCreate(LoginRequiredMixin, CreateView):
    model = Dish
    template_name = 'myrestaurants/form.html'
    form_class = DishForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        return super(DishCreate, self).form_valid(form)

@login_required()
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

The root template is defined in *base.html* in *myrestaurants/templates/myrestaurants*:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="{% static "style/base.css" %}" />
    <title>{% block title %}MyRestaurants by MyRecommendations{% endblock %}</title>
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

This root template is then extended with specific templates like the one to list restaurants, 
*restaurant_list.html* in *myrestaurants/templates/myrestaurants*:

```html
{% extends "myrestaurants/base.html" %}
{% block content %}
<h1>
    Restaurants
    {% if user.is_authenticated %}(<a href="{% url 'myrestaurants:restaurant_create' %}">add</a>){% endif %}
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

And *restaurant_detail.html* in *myrestaurants/templates/myrestaurants*, which includes the list of dishes and the review form:

```html
{% extends "myrestaurants/base.html" %}
{% block title %}MyRestaurants - {{ restaurant.name }}{% endblock %}
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

<h2>
    Dishes
    {% if user.is_authenticated %}
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
{% if restaurant.restaurantreview_set.all|length > 0 %}
    <p>
        Average rating {{ restaurant.averageRating|stringformat:".1f" }}
        {% with restaurant.restaurantreview_set.all|length as reviewCount %}
        from {{ reviewCount }} review{{ reviewCount|pluralize }}
        {% endwith %}
    </p>
</span>
<ul>
    {% for review in restaurant.restaurantreview_set.all %}
        <li>
            <p>
                {{ review.rating }} star{{ review.rating|pluralize }}
            </p>
            <p>{% if review.comment %}{{ review.comment }}{% endif %}</p>
            <p>Created by {{ review.user }} on {{ review.date }}</p>
        </li>
    {% endfor %}
</ul>
{% endif %}

</span>

<h3>Add Review</h3>
<form action="{% url 'myrestaurants:review_create' restaurant.id %}" method="post">
    {% csrf_token %}
    Message: <textarea name="comment" id="comment" rows="4"></textarea>
    <p>Rating:</p>
    <p>{% for rate in RATING_CHOICES %}
    <input type="radio" name="rating" id="rating{{ forloop.counter }}" value="{{ rate.0 }}" />
    <label for="choice{{ forloop.counter }}">{{ rate.1 }} star{{ rate.0|pluralize }}</label>
    <br/>{% endfor %}
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
from myrestaurants.models import Restaurant, Dish

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
{% load static %}
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
