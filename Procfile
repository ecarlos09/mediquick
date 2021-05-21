web: daphne --pythonpath mediquick mediquick.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: --pythonpath mediquick python manage.py runworker -v2