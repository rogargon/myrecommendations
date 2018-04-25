from .settings import *
import dj_database_url

# IMPORTANT: to enable these settings in Heroku, set the corresponding environment variable using:
# $> heroku config:set DJANGO_SETTINGS_MODULE=myrecommendations.settings_heroku

DEBUG = False

ALLOWED_HOSTS = ['myrecommendations-bdd.herokuapp.com']


MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Parse database configuration from $DATABASE_URL

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
