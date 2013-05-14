# Create your views here.
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from models import RestaurantReview, Restaurant, Dish
from forms import RestaurantForm, DishForm
from serializers import RestaurantSerializer, DishSerializer, RestaurantReviewSerializer

class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = 'myrestaurants/restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RestaurantDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context

class RestaurantCreate(CreateView):
    model = Restaurant
    template_name = 'myrestaurants/form.html'
    form_class = RestaurantForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreate, self).form_valid(form)

class DishCreate(CreateView):
    model = Dish
    template_name = 'myrestaurants/form.html'
    form_class = DishForm

    # def get_initial(self):
    #     initial = super(DishCreate, self).get_initial()
    #     initial['restaurant'] = Restaurant.objects.get(id=self.kwargs['pk'])
    #     return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        return super(DishCreate, self).form_valid(form)

def review(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    review = RestaurantReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        restaurant=restaurant)
    review.save()
    return HttpResponseRedirect(urlresolvers.reverse('myrestaurants:restaurant_detail', args=(restaurant.id,)))


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'restaurants': reverse('myrestaurants:restaurant-list', request=request, format=format),
        'dishes': reverse('myrestaurants:dish-list', request=request, format=format)
    })

class APIRestaurantList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = Restaurant
    serializer_class = RestaurantSerializer

class APIRestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    model = Restaurant
    serializer_class = RestaurantSerializer

class APIDishList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of groups.
    """
    model = Dish
    serializer_class = DishSerializer

class APIDishDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single group.
    """
    model = Dish
    serializer_class = DishSerializer

class APIRestaurantReviewList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = RestaurantReview
    serializer_class = RestaurantReviewSerializer

class APIRestaurantReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    model = RestaurantReview
    serializer_class = RestaurantReviewSerializer