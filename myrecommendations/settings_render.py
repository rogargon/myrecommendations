from .settings import *

# IMPORTANT: to enable these settings in Render, set the corresponding environment variable using:
# DJANGO_SETTINGS_MODULE=myrecommendations.settings_render

DEBUG = True

ALLOWED_HOSTS = ['myrecommendations.onrender.com']
CSRF_TRUSTED_ORIGINS = ['https://myrecommendations.onrender.com']

INSTALLED_APPS = [
    'myrestaurants',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap4'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
