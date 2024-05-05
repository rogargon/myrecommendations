from django.contrib.auth.decorators import login_required
from django.urls import path
from django.utils import timezone
from django.views.generic import DetailView, ListView
from myrestaurants.models import Restaurant, Dish
from myrestaurants.forms import RestaurantForm, DishForm
from myrestaurants.views import (RestaurantCreate, DishCreate, RestaurantDetail, review,
     LoginRequiredCheckIsOwnerUpdateView, APIDishDetail, APIDishList, APIRestaurantDetail, APIRestaurantList,
     APIRestaurantReviewDetail, APIRestaurantReviewList)
from rest_framework.urlpatterns import format_suffix_patterns

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

urlpatterns += [
    # RESTful API
    path('api/restaurants/',
        APIRestaurantList.as_view(), name='restaurant-list'),
    path('api/restaurants/<int:pk>/',
        APIRestaurantDetail.as_view(), name='restaurant-detail'),
    path('api/dishes/',
        login_required(APIDishList.as_view()), name='dish-list'),
    path('api/dishes/<int:pk>/',
        APIDishDetail.as_view(), name='dish-detail'),
    path('api/restaurantreviews/',
        APIRestaurantReviewList.as_view(), name='restaurantreview-list'),
    path('api/restaurantreviews/<int:pk>/',
        APIRestaurantReviewDetail.as_view(), name='restaurantreview-detail'),
]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json'])
