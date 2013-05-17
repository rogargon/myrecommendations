from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Restaurant, Dish, RestaurantReview

class RestaurantSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='myrestaurants:restaurant-detail')
    dishes = HyperlinkedRelatedField(many=True, read_only=True, view_name='myrestaurants:dish-detail')
    restaurantreview_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='myrestaurants:restaurantreview-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Restaurant
        fields = ('url', 'name', 'street', 'number', 'city', 'zipCode', 'stateOrProvince',
                  'country', 'telephone', 'web', 'user', 'date', 'dishes', 'restaurantreview_set')

class DishSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='myrestaurants:dish-detail')
    restaurant = HyperlinkedRelatedField(view_name='myrestaurants:restaurant-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Dish
        fields = ('url', 'name', 'description', 'price', 'image', 'user', 'date', 'restaurant')

class RestaurantReviewSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='myrestaurants:restaurantreview-detail')
    restaurant = HyperlinkedRelatedField(view_name='myrestaurants:restaurant-detail')
    user = CharField(read_only=True)
    class Meta:
        model = RestaurantReview
        fields = ('url', 'rating', 'comment', 'user', 'date', 'restaurant')