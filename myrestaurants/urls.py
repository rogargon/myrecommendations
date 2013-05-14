from django.conf.urls import patterns, url, include
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from rest_framework.urlpatterns import format_suffix_patterns

from models import Restaurant, Dish
from forms import RestaurantForm, DishForm
from views import RestaurantCreate, DishCreate, RestaurantDetail, \
    APIDishDetail, APIDishList, APIRestaurantDetail, APIRestaurantList, \
    APIRestaurantReviewDetail, APIRestaurantReviewList

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
    url(r'^restaurants/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model = Restaurant,
            template_name = 'myrestaurants/form.html',
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
            template_name = 'myrestaurants/form.html',
            form_class = DishForm),
        name='dish_edit'),

    # ex: /myrestaurants/restaurants/1/reviews/create/
    url(r'^restaurants/(?P<pk>\d+)/reviews/create/$',
        'myrestaurants.views.review',
        name='review_create'),
)

#RESTful API
urlpatterns += patterns('',
    url(r'^api/$', 'api_root'),
    url(r'^api/restaurants/$', APIRestaurantList.as_view(), name='restaurant-list'),
    url(r'^api/restaurants/(?P<pk>\d+)/$', APIRestaurantDetail.as_view(), name='restaurant-detail'),
    url(r'^api/dishes/$', APIDishList.as_view(), name='dish-list'),
    url(r'^api/dishes/(?P<pk>\d+)/$', APIDishDetail.as_view(), name='dish-detail'),
    url(r'^api/restaurantreviews/$', APIRestaurantReviewList.as_view(), name='restaurantreview-list'),
    url(r'^api/restaurantreviews/(?P<pk>\d+)/$', APIRestaurantReviewDetail.as_view(), name='restaurantreview-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api' ,'json',])