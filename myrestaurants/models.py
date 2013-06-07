# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Restaurant(models.Model):
    name = models.TextField()
    street = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    city = models.TextField(default="")
    zipCode = models.TextField(blank=True, null=True)
    stateOrProvince = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    telephone = models.TextField(blank=True, null=True)
    web = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=User.objects.get(id=1))
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('myrestaurants:restaurant_detail', kwargs={'pk': self.pk})
    def averageRating(self):
        ratingSum = 0.0
        for review in self.restaurantreview_set.all():
            ratingSum += review.rating
        reviewCount = self.restaurantreview_set.count()
        return ratingSum / reviewCount


class Dish(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to="myrestaurants", blank=True, null=True)
    user = models.ForeignKey(User, default=User.objects.get(id=1))
    date = models.DateField(default=date.today)
    restaurant = models.ForeignKey(Restaurant, null=True)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('myrestaurants:dish_detail', kwargs={'pkr': self.restaurant.pk, 'pk': self.pk})

class Review(models.Model):
    RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=User.objects.get(id=1))
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class RestaurantReview(Review):
    restaurant = models.ForeignKey(Restaurant)