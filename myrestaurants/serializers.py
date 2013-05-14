from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField
from models import Restaurant, Dish, RestaurantReview

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='myrestaurants:restaurant-detail')
    dishes = HyperlinkedRelatedField(many=True, read_only=True, view_name='myrestaurants:dish-detail')
    restaurantreview_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='myrestaurants:restaurantreview-detail')
    user = serializers.CharField(read_only=True)
    class Meta:
        model = Restaurant
        fields = ('url', 'name', 'street', 'number', 'city', 'zipCode', 'stateOrProvince',
                  'country', 'telephone', 'web', 'user', 'date', 'dishes', 'restaurantreview_set')

class DishSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='myrestaurants:dish-detail')
    restaurant = serializers.HyperlinkedRelatedField(view_name='myrestaurants:restaurant-detail')
    user = serializers.CharField(read_only=True)
    class Meta:
        model = Dish
        fields = ('url', 'name', 'description', 'price', 'image', 'user', 'date', 'restaurant')

class RestaurantReviewSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='myrestaurants:restaurantreview-detail')
    restaurant = serializers.HyperlinkedRelatedField(view_name='myrestaurants:restaurant-detail')
    user = serializers.CharField(read_only=True)
    class Meta:
        model = RestaurantReview
        fields = ('url', 'rating', 'comment', 'user', 'date', 'restaurant')