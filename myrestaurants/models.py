# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Address(models.Model):
    street = models.TextField()
    number = models.IntegerField()
    city = models.TextField()
    zipCode = models.TextField(null=True, blank=True, default="")
    stateOrProvince = models.TextField(blank=True)
    country = models.TextField()
    user = models.ForeignKey(User, null=True, default=User.objects.get(id=1))
    date = models.DateField(null=True, default=date.today)

    def __unicode__(self):
        return u"%s, %s. %s %s, %s (%s)" % (
            self.street, self.number, self.zipCode if self.zipCode else "", self.city, self.stateOrProvince, self.country)

class Restaurant(models.Model):
    name = models.TextField()
    address = models.ForeignKey(Address, blank=True, null=True)
    telephone = models.TextField(blank=True)
    url = models.URLField(blank=True)
    user = models.ForeignKey(User, null=True, default=User.objects.get(id=1))
    date = models.DateField(null=True, default=date.today)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('myrestaurants:restaurant_detail', kwargs={'pk': self.pk})


class Dish(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, null=True, default=User.objects.get(id=1))
    date = models.DateField(null=True, default=date.today)
    restaurant = models.ForeignKey(Restaurant, blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('myrestaurants:dish_detail', kwargs={'pkr': self.restaurant.pk, 'pk': self.pk})

class Review(models.Model):
    RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, null=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=User.objects.get(id=1))
    date = models.DateField(null=True, default=date.today)

class RestaurantReview(Review):
    restaurant = models.ForeignKey(Restaurant)