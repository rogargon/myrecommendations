from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from django.utils import timezone
from models import *
from views import DishDetail

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
            template_name = "myrestaurants/restaurant_detail.html"),
        name='restaurant_detail'),

    # ex: /myrestaurants/restaurant/1/dish/1/
    url(r'^restaurant/(?P<pkr>\d+)/dish/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Dish,
            template_name='myrestaurants/dish_detail.html'),
        name='dish_detail'),
)