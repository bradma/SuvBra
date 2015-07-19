from .base_settings import *
import sys

DEBUG = True

TEMPLATE_DEBUG = True

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