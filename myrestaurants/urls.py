from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.utils import timezone

from myrestaurants.models import Restaurant, Dish
from myrestaurants.forms import RestaurantForm, DishForm
from myrestaurants.views import RestaurantCreate, DishCreate

urlpatterns = patterns('',
    # ex: /myrestaurants/
    url(r'^$',
        ListView.as_view(
            queryset=Restaurant.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
            context_object_name='latest_restaurant_list',
            template_name='myrestaurants/restaurant_list.html'),
        name='restaurant_list'),

    # ex: /myrestaurants/restaurant/1/
    url(r'^restaurant/(?P<pk>\d+)/$',
        DetailView.as_view(
            model = Restaurant,
            template_name = 'myrestaurants/restaurant_detail.html'),
        name='restaurant_detail'),

    # ex: /myrestaurants/restaurant/1/edit/
    url(r'^restaurant/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model = Restaurant,
            template_name = 'myrestaurants/restaurant_form.html',
            form_class = RestaurantForm),
        name='restaurant_edit'),

    # ex: /myrestaurants/restaurant/create/
    url(r'^restaurant/create/$',
        RestaurantCreate.as_view(),
        name='restaurant_create'),

    # ex: /myrestaurants/restaurant/1/dish/1/
    url(r'^restaurant/(?P<pkr>\d+)/dish/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Dish,
            template_name='myrestaurants/dish_detail.html'),
        name='dish_detail'),

    # ex: /myrestaurants/restaurant/1/dish/1/edit/
    url(r'^restaurant/(?P<pkr>\d+)/dish/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model = Dish,
            template_name = 'myrestaurants/dish_form.html',
            form_class = DishForm),
        name='dish_edit'),

    # ex: /myrestaurants/restaurant/1/dish/create/
    url(r'^restaurant/(?P<pk>\d+)/dish/create/$',
        DishCreate.as_view(),
        name='dish_create'),
)