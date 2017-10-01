web: python manage.py runserver
web: gunicorn line-echoboy.wsgi --log-file -
heroku config:set DISABLE_COLLECTSTATIC=1