# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from models import *

class DishDetail(DetailView):
    model = Dish
    template_name = "myrestaurants/dish_detail.html"

    def get_object(self):
        self.object = super(DishDetail, self).get_object()
        return self.object

    def get_context_data(self, **kwargs):
        context = super(DishDetail, self).get_context_data(**kwargs)
        context['restaurant'] = self.object.restaurant
        return context