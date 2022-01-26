release: python3 manage.py migrate
web: gunicorn search.wsgi --timeout 60 --log-file -