web: gunicorn todolist.wsgi --log-file -
web: python manage.py migrate && gunicorn todolist.wsgi