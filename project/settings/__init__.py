"""

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os

from .envvars import get_envvar_string
from .database import DATABASES
from .apps import INSTALLED_APPS
from .middlewares import MIDDLEWARE_CLASSES
from .rest_settings import JWT_AUTH, REST_FRAMEWORK


SETTINGS_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT, _ = os.path.split(SETTINGS_ROOT)
PROJECT_BASE, APPNAME = os.path.split(PROJECT_ROOT)


# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 't!6@#(m612biw(r!d8-g3-=)(vn^3hxh@v=-bqqu@2==@9x!5@'
SECRET_KEY = get_envvar_string('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = '%s.urls' % APPNAME

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-US'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = '%s/static' % PROJECT_BASE