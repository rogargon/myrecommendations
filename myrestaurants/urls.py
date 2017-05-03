from django.conf.urls import url
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from forms import RestaurantForm
from models import Restaurant

urlpatterns = [
    # Register a restaurant, from: /myrestaurants/register/
    url(r'^register/$',
        CreateView.as_view(
            model=Restaurant,
            template_name='form.html',
            form_class=RestaurantForm),
        name='restaurant_create'),
    # Restaurant details, from: /myrestaurants/1/
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Restaurant,
            template_name='restaurant_detail.html'),
        name='restaurant_detail'),
]
