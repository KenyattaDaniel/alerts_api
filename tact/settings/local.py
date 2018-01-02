# settings/local.py
from .base import *


# Debug should always remain True during development
DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dgldev',
        'USER': get_env_variable('DB_USER'),
        'PASSWORD': get_env_variable('DB_PASS'),
        'HOST': 'localhost',
        'PORT': get_env_variable('DB_PORT'),
    }
}
