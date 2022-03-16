from .settings import *
import django_heroku

# IMPORTANT: to enable these settings in Heroku, set the corresponding environment variable using:
# $> heroku config:set DJANGO_SETTINGS_MODULE=myrecommendations.settings_heroku

DEBUG = True

ALLOWED_HOSTS = ['myrecommendations.herokuapp.com']
CSRF_TRUSTED_ORIGINS = ['https://myrecommendations.herokuapp.com']

# Configure Django App for Heroku.
django_heroku.settings(locals())
