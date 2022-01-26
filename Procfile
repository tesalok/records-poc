ps:scale web=1
release: python3 manage.py migrate
web: gunicorn search.wsgi --timeout 60 --log-file -