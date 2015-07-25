# Project Suvbra
import os
import logging
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

"""
TEMPLATE_DIRS = (
	join(BASE_DIR, 'templates'),
)
"""

STATICFILES_DIRS = (
	join(BASE_DIR, 'media'),
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n(_^$$ljl8w63kk=ql#gdv_!#tr5(ersw(o0ueyqc$w1sz@n$s'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
	'sb',
)

THIRD_PARTY_APPS = (
    'bootstrap3',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'suvbra.urls'

WSGI_APPLICATION = 'suvbra.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/vagrant/Projects/SuvBra/templates/'],
        'APP_DIRS': False,
        'OPTIONS': {
            # ... some options here ...
        },
    },
]

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
