from __future__ import unicode_literals

from django.db import models
from django.urls.base import reverse


class Restaurant(models.Model):
    name = models.TextField()

    def get_absolute_url(self):
        return reverse('myrestaurants:restaurant_detail', kwargs={'pk': self.pk})
