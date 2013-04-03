from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.utils import timezone

from myrestaurants.models import Restaurant, Dish
from myrestaurants.forms import RestaurantForm, DishForm
from myrestaurants.views import RestaurantCreate, DishCreate
from views import RestaurantDetail

urlpatterns = patterns('',
    # ex: /myrestaurants/
    url(r'^$',
        ListView.as_view(
            queryset=Restaurant.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
            context_object_name='latest_restaurant_list',
            template_name='myrestaurants/restaurant_list.html'),
        name='restaurant_list'),

    # ex: /myrestaurants/restaurants/1/
    url(r'^restaurants/(?P<pk>\d+)/$',
        RestaurantDetail.as_view(),
        name='restaurant_detail'),

    # ex: /myrestaurants/restaurants/create/
    url(r'^restaurants/create/$',
        RestaurantCreate.as_view(),
        name='restaurant_create'),

    # ex: /myrestaurants/restaurants/1/edit/
    url(r'^restaurant/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model = Restaurant,
            template_name = 'myrestaurants/restaurant_form.html',
            form_class = RestaurantForm),
        name='restaurant_edit'),

    # ex: /myrestaurants/restaurants/1/dishes/1/
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Dish,
            template_name='myrestaurants/dish_detail.html'),
        name='dish_detail'),

    # ex: /myrestaurants/restaurants/1/dishes/create/
    url(r'^restaurants/(?P<pk>\d+)/dishes/create/$',
        DishCreate.as_view(),
        name='dish_create'),

    # ex: /myrestaurants/restaurants/1/dishes/1/edit/
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model = Dish,
            template_name = 'myrestaurants/dish_form.html',
            form_class = DishForm),
        name='dish_edit'),

    # ex: /myrestaurants/restaurant/1/reviews/create/
    url(r'^restaurant/(?P<pk>\d+)/reviews/create/$',
    #    ReviewCreate.as_view(),
        'myrestaurants.views.review',
        name='review_create'),
)