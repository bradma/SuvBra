from .base_settings import *
import sys

DEBUG = True

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'SuvBra_DB',
       'USER' : 'Admin',
       'PASSWORD' : '[neTz,7F',
       'HOST' : 'localhost',
       'PORT' : '',
    }
}