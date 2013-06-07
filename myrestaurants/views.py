# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core import urlresolvers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

from rest_framework import generics, permissions

from models import RestaurantReview, Restaurant, Dish
from forms import RestaurantForm, DishForm
from serializers import RestaurantSerializer, DishSerializer, RestaurantReviewSerializer

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = 'myrestaurants/restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RestaurantDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context

class RestaurantCreate(LoginRequiredMixin, CreateView):
    model = Restaurant
    template_name = 'myrestaurants/form.html'
    form_class = RestaurantForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreate, self).form_valid(form)

class DishCreate(LoginRequiredMixin, CreateView):
    model = Dish
    template_name = 'myrestaurants/form.html'
    form_class = DishForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        return super(DishCreate, self).form_valid(form)

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'myrestaurants/form.html'

@login_required()
def review(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    review = RestaurantReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        restaurant=restaurant)
    review.save()
    return HttpResponseRedirect(urlresolvers.reverse('myrestaurants:restaurant_detail', args=(restaurant.id,)))

### RESTful API views ###

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user

class APIRestaurantList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Restaurant
    serializer_class = RestaurantSerializer

class APIRestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Restaurant
    serializer_class = RestaurantSerializer

class APIDishList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Dish
    serializer_class = DishSerializer

class APIDishDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Dish
    serializer_class = DishSerializer

class APIRestaurantReviewList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = RestaurantReview
    serializer_class = RestaurantReviewSerializer

class APIRestaurantReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = RestaurantReview
    serializer_class = RestaurantReviewSerializer