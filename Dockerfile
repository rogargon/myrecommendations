FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv
RUN pipenv install --system --deploy

COPY myrecommendations ./myrecommendations
COPY myrestaurants ./myrestaurants
COPY templates ./templates
COPY manage.py ./
# Copy media files just for demo purposes
COPY media ./media

ENV PORT 8000
EXPOSE $PORT
RUN python manage.py collectstatic --noinput --clear
# Init DB if local, might also require `$> python manage.py createsuperuser`
RUN python manage.py migrate
# Set DJANGO_SETTINGS_MODULE=myrecommendations.settings_heroku when deploying on Heroku
CMD gunicorn -b 0.0.0.0:$PORT myrecommendations.wsgi