from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView

from models import Restaurant, Dish
from forms import RestaurantForm, DishForm
from views import RestaurantCreate, DishCreate, RestaurantDetail

urlpatterns = patterns('',
    # List latest 5 restaurants: /myrestaurants/
    url(r'^$',
        ListView.as_view(
            queryset=Restaurant.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
            context_object_name='latest_restaurant_list',
            template_name='myrestaurants/restaurant_list.html'),
        name='restaurant_list'),

    # Restaurant details, ex.: /myrestaurants/restaurants/1/
    url(r'^restaurants/(?P<pk>\d+)/$',
        RestaurantDetail.as_view(),
        name='restaurant_detail'),

    # Create a restaurant: /myrestaurants/restaurants/create/
    url(r'^restaurants/create/$',
        RestaurantCreate.as_view(),
        name='restaurant_create'),

    # Edit restaurant details, ex: /myrestaurants/restaurants/1/edit/
    url(r'^restaurants/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Restaurant,
            form_class=RestaurantForm,
            template_name='myrestaurants/form.html'),
        name='restaurant_edit'),

    # Restaurant dish details, ex: /myrestaurants/restaurants/1/dishes/1/
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Dish,
            template_name='myrestaurants/dish_detail.html'),
        name='dish_detail'),

    # Create a restaurant dish, ex: /myrestaurants/restaurants/1/dishes/create/
    url(r'^restaurants/(?P<pk>\d+)/dishes/create/$',
        DishCreate.as_view(),
        name='dish_create'),

    # Edit restaurant dish details, ex: /myrestaurants/restaurants/1/dishes/1/edit/
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Dish,
            form_class=DishForm,
            template_name='myrestaurants/form.html'),
        name='dish_edit'),

    # Create a restaurant review using function, ex: /myrestaurants/restaurants/1/reviews/create/
    url(r'^restaurants/(?P<pk>\d+)/reviews/create/$',
        'myrestaurants.views.review',
        name='review_create'),
)