from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView

from models import Restaurant, Dish
from forms import RestaurantForm, DishForm
from views import RestaurantCreate, DishCreate, RestaurantList, RestaurantDetail, DishDetail, DishList

urlpatterns = [
    # Home page
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('myrestaurants:restaurant_list', kwargs={'extension': 'html'})),
        name='home_page'),

    # List restaurants: /myrestaurants/restaurants.json
    url(r'^restaurants\.(?P<extension>(json|xml|html))$',
        RestaurantList.as_view(),
        name='restaurant_list'),

    # Restaurant details, ex.: /myrestaurants/restaurants/1.json
    url(r'^restaurants/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        RestaurantDetail.as_view(),
        name='restaurant_detail'),

    # Create a restaurant: /myrestaurants/restaurants/create/
    url(r'^restaurants/create/$',
        RestaurantCreate.as_view(),
        name='restaurant_create'),

    # Edit restaurant details, ex.: /myrestaurants/restaurants/1/edit/
    url(r'^restaurants/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Restaurant,
            template_name='myrestaurants/form.html',
            form_class=RestaurantForm),
        name='restaurant_edit'),

    # Restaurant dishes list, ex.: /myrestaurants/restaurants/1/dishes.json
    url(r'^restaurants/(?P<pk>\d+)/dishes\.(?P<extension>(json|xml))$',
        DishList.as_view(),
        name='dish_list'),

    # Restaurant dish details, ex.: /myrestaurants/restaurants/1/dishes/1.json
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        DishDetail.as_view(),
        name='dish_detail'),

    # Create a restaurant dish, ex: /myrestaurants/restaurants/1/dishes/create/
    url(r'^restaurants/(?P<pk>\d+)/dishes/create/$',
        DishCreate.as_view(),
        name='dish_create'),

    # Edit restaurant dish details, ex: /myrestaurants/restaurants/1/dishes/1/edit/
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Dish,
            template_name='myrestaurants/form.html',
            form_class=DishForm),
        name='dish_edit'),

    # Create a restaurant review using function, ex: /myrestaurants/restaurants/1/reviews/create/
    url(r'^restaurants/(?P<pk>\d+)/reviews/create/$',
        'myrestaurants.views.review',
        name='review_create'),
]
