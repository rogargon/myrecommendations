from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView

from rest_framework.urlpatterns import format_suffix_patterns

from models import Restaurant, Dish
from forms import RestaurantForm, DishForm
from views import RestaurantCreate, DishCreate, RestaurantList, RestaurantDetail, DishDetail, DishList, review, \
    APIDishDetail, APIDishList, APIRestaurantDetail, APIRestaurantList, APIRestaurantReviewDetail, APIRestaurantReviewList

urlpatterns = [
    # Home page
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('myrestaurants:restaurant_list')),
        name='home_page'),

    # List restaurants: /myrestaurants/restaurants.json
    url(r'^restaurants(\.(?P<extension>(json|xml)))?$',
        RestaurantList.as_view(),
        name='restaurant_list'),

    # Restaurant details, ex.: /myrestaurants/restaurants/1.json
    url(r'^restaurants/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
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
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
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
        review,
        name='review_create'),

    # RESTful API

    url(r'^api/auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/restaurants/$',
        APIRestaurantList.as_view(), name='restaurant-list'),
    url(r'^api/restaurants/(?P<pk>\d+)/$',
        APIRestaurantDetail.as_view(), name='restaurant-detail'),
    url(r'^api/dishes/$',
        login_required(APIDishList.as_view()), name='dish-list'),
    url(r'^api/dishes/(?P<pk>\d+)/$',
        APIDishDetail.as_view(), name='dish-detail'),
    url(r'^api/restaurantreviews/$',
        APIRestaurantReviewList.as_view(), name='restaurantreview-list'),
    url(r'^api/restaurantreviews/(?P<pk>\d+)/$',
        APIRestaurantReviewDetail.as_view(), name='restaurantreview-detail'),
]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api','json', 'xml'])
