"""
Django settings for ostrovaweb project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ex7(i1v1)pq!rz(m#a-1z0dlk%d(m0rt01gs^5d1gp9dsk+f0a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.6.132','127.0.0.1','localhost','testserver']

INSTALLED_APPS = [

    # Project applications
    'tartrequests',
    'order',
    'delivery',
    'cashdesk',
    'store',
    'nomenclature',

    # not including it as installed, because it only supplies js/css, and those are being modified and inluded in own app static
    # 'datetimewidget',

    'suit',
    'django_object_actions',


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'mod_wsgi.server',

    # Report builder
    #'report_builder',

    # Object history
    'reversion',
    'reversion_compare',
    'django_select2',
    'djangobower',
    'storages'

]

BOWER_COMPONENTS_ROOT = BASE_DIR + '/components/'
BOWER_INSTALLED_APPS = (
    'jquery',
    'jquery-ui',
    'bootstrap',
    'fullcalendar',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'ostrovaweb.get_current_request.ThreadLocalMiddleware',
]

ROOT_URLCONF = 'ostrovaweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            PROJECT_ROOT + '/templates',
            'templates'  # needed for debug mode only
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.core.context_processors.request',
            ],
            'loaders': [
                'ostrovaweb.overridingLoader.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                #    'django.template.loaders.eggs.Loader',
            ]
        },
    },
]

WSGI_APPLICATION = 'ostrovaweb.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
]

SUIT_CONFIG = {
    'ADMIN_NAME': 'Парти център ERP',
    #'MENU_EXCLUDE': ('sites',),
    'MENU_OPEN_FIRST_CHILD': True,
    'MENU': (

        { 'app': 'tartrequests',
          'label': 'Поръчки за торти',
          'models': (
              {'url': '/fullcalendartarts', 'label': 'Календар Торти', 'permissions': ('tartrequests.view_tortarequest_calendar', )},
              'tortarequest',
              'tortapictureregister',
              'tortatasteregister',
              'tortapriceperclub',
              'tortapiececoding',
              'tortapicturecategory',
              'tortadeliveryaddress',
          ),
          },

        { 'app': 'order',
          'label': 'Поръчки за парти',
          'models': (
              {'url': '/fullcalendar', 'label': 'Календар', },
              'order', ),
        },

        {   'app': 'delivery',
            'label': 'Доставки',
            'models': ( 'delivery', ),
        },

        {   'app': 'cashdesk',
            'label': 'Каса',
            'models': ( 'cashdesk', 'cashdesk_detail_expense', 'cashdesk_detail_income', 'cashdesk_detail_transfer' ),
        },

        {   'app': 'store',
            'label': 'Склад',
            'models': ( 'stock_receipt_protocol', 'articlestore',  ),
        },

        {   'app': 'nomenclature',
            'label': 'Номенклатури',
            'models': ( 'supplier', 'articlegroup', 'article', 'club', 'saloon', 'cashdesk_groups_income', 'cashdesk_groups_expense' ),
        },

        {   'app': 'auth',
            'label': 'Контрол на достъпа',
            'models': ( 'user', 'group',)
        },
    )
}

# Database

# check for HEROKU presence (must MANUALLY add ON_HEROKU as a configuration variable)
# if 'ON_HEROKU' in os.environ:

import dj_database_url
DATABASES = {
   'default' :  dj_database_url.config(),
}
# else:
#     dbDriver = 'django.db.backends.oracle'
#     dbUser = 'OSTROVA'
#     dbPass = 'ostrova'
#     dbName = 'XE'
#
#     DATABASES = {
#         'default': {
#         'ENGINE': dbDriver,
#        'HOST': '192.168.6.1',
#         'PORT': '1521',
#         'SID':'XE',
#         'USER': dbUser,'PASSWORD': dbPass,
#         'OPTIONS': { 'threaded': True, },
#         },
#     }

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

# Internationalization
LANGUAGE_CODE = 'bg'
TIME_ZONE = 'Europe/Sofia'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static Files

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder'
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
]

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': '/home/osboxes/ostrovaweb/debug.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }

# MEDIA_ROOT = BASE_DIR + '/upload'
# MEDIA_URL = '/upload/'

TARTIMAGES_STORAGE = u'tartImages'
TART_CUSTOM_REQESTS_FOLDER = u'СОБСТВЕНО ИЗОБРАЖЕНИЕ'

AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = os.environ.get('BUCKETEER_AWS_ACCESS_KEY_ID',None)
AWS_SECRET_ACCESS_KEY = os.environ.get('BUCKETEER_AWS_SECRET_ACCESS_KEY', None)
AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKETEER_BUCKET_NAME', None)
MEDIA_URL = 'http://%s.s3.amazonaws.com/' % str(AWS_STORAGE_BUCKET_NAME)
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"