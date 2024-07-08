"""
Django settings for hotels project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
# Vijay/django_pro/hotels/setting.py
import sys
import os


BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
# with open("C:/Users/Vijay/py_pro/test.txt", 'r') as file:
#     first_line = file.readline().strip()
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vf46304t(3p5%&42#ld+^zc=+!1o1w+b*eh1t%$!)3s97y#*+z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    "base.apps.BaseConfig",
    "accounts.apps.AccountsConfig",
    "rooms.apps.RoomsConfig",
    "restaurant.apps.RestaurantConfig",
    "reviews.apps.ReviewsConfig",
    "message.apps.MessageConfig",
]
liabrarias=[
    "rest_framework",
     'django_celery_results',
    'django_celery_beat',
    ]
INSTALLED_APPS+=liabrarias
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
        "django.middleware.security.SecurityMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.main.customeMiddleware',
]

ROOT_URLCONF = 'hotels.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"
            ],
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

WSGI_APPLICATION = 'hotels.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'user_databse',
#         'USER': 'user_databse_user',
#         'PASSWORD': 'ItGsxeYeqbYUdQLoLh8GsMGcjUHAXU7o',
#         'HOST': 'dpg-cpujmqqj1k6c738bgv8g-a.oregon-postgres.render.com',
#         'PORT': '5432',
#     }
# }
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')

import os


print("Database settings:")
print("NAME:", os.environ.get('hotels'))
print("USER:", os.environ.get('root'))
print("PASSWORD:", os.environ.get('vijay'))
print("HOST:", os.environ.get('DATABASE_HOST'))
print("PORT:", os.environ.get('DATABASE_PORT'))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('hotels'),
        'USER': os.environ.get('root'),
        'PASSWORD': os.environ.get('vijay'),
        'HOST': os.environ.get('localhost'),
        'PORT': os.environ.get('DATABASE_PORT', '3306'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME':   'hotels',
#         'USER': 'root',
#         'PASSWORD':'vijay',
#         'HOST':'localhost',
#         'PORT':'3306',
        
#     }
# }


# # import dj_database_url
# # DATABASES["default"]=dj_database_url.parse("postgresql://user_databse_user:ItGsxeYeqbYUdQLoLh8GsMGcjUHAXU7o@dpg-cpujmqqj1k6c738bgv8g-a.oregon-postgres.render.com/user_databse")

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # For development
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    
MEDIA_ROOT= BASE_DIR / "media"
MEDIA_URL='/media/'
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# SET THE SETTING FOR THE SENDING EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'vijaygholve77v@gmail.com'
EMAIL_HOST_PASSWORD = 'uoyn xeho visj fblr'


CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_TIMEZONE = "Asia/Kolkata"
CELERY_RESULT_BACKEND = "django-db"
CELERY_ENABLE_UTC = False

# Retain existing behavior for retrying connections on startup
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

task_serializer = 'json'
result_serializer = 'json'
timezone = 'Asia/Kolkata'
accept_content = ['json']
result_backend = 'django-db'
