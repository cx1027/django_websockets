celery:
celery -A myproject worker --loglevel=info

django:
python manage.py runserver
http://127.0.0.1:8000/trigger-websocket/

daphne:
daphne -p 8765 myproject.asgi:application
http://127.0.0.1:8765/trigger-websocket/