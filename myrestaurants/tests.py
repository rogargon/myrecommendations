from django.test import TestCase

from models import RestaurantReview, Restaurant


class RestaurantReviewTestCase(TestCase):
    def setUp(self):
        trendy = Restaurant.objects.create(name="Trendy Restaurant")
        RestaurantReview.objects.create(rating=3, comment="Average...", restaurant=trendy)
        RestaurantReview.objects.create(rating=5, comment="Excellent!", restaurant=trendy)
        RestaurantReview.objects.create(rating=1, comment="Really bad!", restaurant=trendy)
        Restaurant.objects.create(name="Unknown Restaurant")

    def test_average_3reviews(self):
        """The average review for a restaurant with 3 reviews is properly computed"""
        restaurant = Restaurant.objects.get(name="Trendy Restaurant")
        self.assertEqual(restaurant.averageRating(), 3)

    def test_average_no_review(self):
        """The average review for a restaurant without reviews is 0"""
        restaurant = Restaurant.objects.get(name="Unknown Restaurant")
        self.assertEqual(restaurant.averageRating(), 0)
