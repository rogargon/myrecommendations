from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Restaurant, Dish, RestaurantReview


class RestaurantSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='myrestaurants:restaurant-detail')
    dishes = HyperlinkedRelatedField(many=True, read_only=True, view_name='myrestaurants:dish-detail')
    restaurantreview_set = HyperlinkedRelatedField(many=True, read_only=True,
                                                   view_name='myrestaurants:restaurantreview-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Restaurant
        fields = ('uri', 'name', 'street', 'number', 'city', 'zipCode', 'stateOrProvince',
                  'country', 'telephone', 'url', 'user', 'date', 'dishes', 'restaurantreview_set')


class DishSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='myrestaurants:dish-detail')
    restaurant = HyperlinkedRelatedField(view_name='myrestaurants:restaurant-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Dish
        fields = ('uri', 'name', 'description', 'price', 'image', 'user', 'date', 'restaurant')


class RestaurantReviewSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='myrestaurants:restaurantreview-detail')
    restaurant = HyperlinkedRelatedField(view_name='myrestaurants:restaurant-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = RestaurantReview
        fields = ('uri', 'rating', 'comment', 'user', 'date', 'restaurant')
