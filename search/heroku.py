from search.settings import *
import dj_database_url, os
DEBUG = True

ALLOWED_HOSTS = ['*']  # allow all

DATABASES = {
    'default':dj_database_url.config(default=os.getenv('DATABASE_URL')),
}
