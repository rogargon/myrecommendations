# Create your views here.
import user

from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from myrestaurants.models import Restaurant, Dish
from myrestaurants.forms import RestaurantForm, DishForm

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
    template_name = 'myrestaurants/restaurant_form.html'
    form_class = RestaurantForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreate, self).form_valid(form)

class DishCreate(CreateView):
    model = Dish
    template_name = 'myrestaurants/dish_form.html'
    form_class = DishForm

    def get_initial(self):
        initial = super(DishCreate, self).get_initial()
        initial['restaurant'] = Restaurant.objects.get(id=self.kwargs['pk'])
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DishCreate, self).form_valid(form)