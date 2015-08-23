# Project Suvbra
import os
import logging
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATICFILES_DIRS = (
	join(BASE_DIR, 'media'),
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n(_^$$ljl8w63kk=ql#gdv_!#tr5(ersw(o0ueyqc$w1sz@n$s'

DEBUG = True

TEMPLATE_DEBUG = True

#Permission redirection
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = ''

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
    'rest_framework',
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
"""
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
"""

ROOT_URLCONF = 'suvbra.urls'

WSGI_APPLICATION = 'suvbra.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/vagrant/Projects/SuvBra/templates/',
            '/home/vagrant/.virtualenvs/suvbra/lib/python3.4/site-packages/rest_framework/templates/'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ]
        },
    },
]

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'SuvBra_DB',
       'USER' : 'Admin',
       'PASSWORD' : '[neTz,7F',
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
