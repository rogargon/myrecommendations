# Create your views here.

from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

from myrestaurants.models import Restaurant, Dish

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

class RestaurantCreate(CreateView):
    model = Restaurant

class RestaurantUpdate(UpdateView):
    model = Restaurant