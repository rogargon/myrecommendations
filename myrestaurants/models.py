from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

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

class Dish(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, null=True, default=User.objects.get(id=1))
    date = models.DateField(null=True, default=date.today)
    restaurant = models.ForeignKey(Restaurant, blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name

class Price(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.TextField()
    user = models.ForeignKey(User, null=True, default=User.objects.get(id=1))
    date = models.DateField(null=True, default=date.today)
    dish = models.ForeignKey(Dish, blank=True, null=True)

    def __unicode__(self):
        return u"%d %s" % (self.amount, self.currency)