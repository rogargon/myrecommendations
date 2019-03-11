from django.contrib.auth.models import User
from django.test import TestCase

from .models import Restaurant, RestaurantReview


class RestaurantReviewTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        user3 = User.objects.create(username="user3")
        trendy = Restaurant.objects.create(name="Trendy Restaurant", user=user1)
        RestaurantReview.objects.create(rating=3, comment="Average...", restaurant=trendy, user=user1)
        RestaurantReview.objects.create(rating=5, comment="Excellent!", restaurant=trendy, user=user2)
        RestaurantReview.objects.create(rating=1, comment="Really bad!", restaurant=trendy, user=user3)
        Restaurant.objects.create(name="Unknown Restaurant", user=user1)

    def test_average_3reviews(self):
        """The average review for a restaurant with 3 reviews is properly computed"""
        restaurant = Restaurant.objects.get(name="Trendy Restaurant")
        self.assertEqual(restaurant.averageRating(), 3)

    def test_average_no_review(self):
        """The average review for a restaurant without reviews is 0"""
        restaurant = Restaurant.objects.get(name="Unknown Restaurant")
        self.assertEqual(restaurant.averageRating(), 0)
