# from search.settings import *
# DEBUG = True

# ALLOWED_HOSTS = ['*']  # allow all

# DATABASES = {
#     'default':
#         {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'country',
#             'HOST': 'localhost',
#             'PORT': '5432',
#             'USER': 'postgres',
#             'PASSWORD': ''
#         }
# }
from search.settings import *
import dj_database_url, os
DEBUG = True

ALLOWED_HOSTS = ['*']  # allow all

DATABASES = {
    'default':dj_database_url.config(default=os.getenv('DATABASE_URL')),
}
