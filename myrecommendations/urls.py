"""myrecommendations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='myrestaurants:restaurant_list'), name='home'),
    path('admin/', admin.site.urls),
    path('myrestaurants/', include('myrestaurants.urls', namespace='myrestaurants')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
]

# if settings.DEBUG:
# Used even in production though not recommended: https://devcenter.heroku.com/articles/s3-upload-python
urlpatterns += [
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT, })
]
