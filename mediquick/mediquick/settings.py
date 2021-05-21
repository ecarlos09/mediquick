"""
Django settings for mediquick project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
import channels
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import join
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
import environ
env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY') if env('SECRET_KEY')==None else os.environ['SECRET_KEY']
# SECRET_KEY = os.environ['SECRET_KEY']
# with open('./.env') as f:
#     SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False
# DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

HOST_URL = 'https://medi-quick.herokuapp.com'
# if DEBUG:
#     HOST_URL = 'http://127.0.0.1:8000'



ALLOWED_HOSTS = ['https://medi-quick.herokuapp.com/']
# ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'bootstrap4',
    'channels',
    'chat',
    'codes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'public',
    'doctors',
    'patients',
    'users',
    'rest_framework',
    
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mediquick.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
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

WSGI_APPLICATION = 'mediquick.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # "default": {
    #     "ENGINE" : "django.db.backends.sqlite3",
    #     "NAME": os.path.join(BASE_DIR, "sqlite3"),
    #     # "DATABASE_URL": os.environ['DATABASE_URL']
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3')
        }
    }
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


'''Outlook settings'''
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_HOST_USER = 'mediquick.adm1n@outlook.com'
# EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 25

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'login'


# two factor
AUTH_USER_MODEL = 'users.CustomUser'
# two factor end

'''Database configuration'''
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# prod_db  =  dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(prod_db)
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# import psycopg2
# conn = psycopg2.connect(DATABASES['default']['DATABASE_URL'], sslmode='require')

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# two factor end 

# CHAT FEATURE SETTINGS STARTS 
# ASGI_APPLICATION = 'mediquick.routing.application'
ASGI_APPLICATION = "mediquick.asgi.application"

# CHANNEL_LAYERS = {
#     'default': {
#         # 'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         # 'CONFIG': {
#         #     "hosts": [('127.0.0.1', 6379)],
#         # },
#         "BACKEND": "asgiref.inmemory.ChannelLayer",
#         "ROUTING": "core.routing.channel_routing",
#     },
# }
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        #"BACKEND": "asgi_redis.RedisChannelLayer",
        'CONFIG': {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
        # "ROUTING": "mediquick.routing.channel_routing",
    },
}

MESSAGES_TO_LOAD = 30

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    # 'DEFAULT_PAGINATION_CLASS':
    #     'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 100
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.TokenAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    #     'rest_framework.authentication.BasicAuthentication',
    # ),
}


PROJECT_ROOT = BASE_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

''' Deployment configuration '''

django_heroku.settings(locals())

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'build/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Collect static files here
STATIC_URL = '/static/'
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_ROOT = 'static/media'
MEDIA_URL = '/media/'

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
#     '/var/www/static/',
# ]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# STATICFILES_DIRS = []

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

