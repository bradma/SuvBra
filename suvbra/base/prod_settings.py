from .base import *
import sys

DEBUG = False

TEMPLATE_DEBUG = False

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
    'USER' : '',
    'PASSWORD' : '',
    'HOST' : '',
    'PORT' : '',
    }
}