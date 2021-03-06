"""
Django settings for shoutourbiz project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.contrib import messages

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '******'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_countries',
    'widget_tweaks',
    'debug_toolbar',
    'haystack',
    'django_forms_bootstrap',
]

INSTALLED_APPS += [
    'main',
    'internal',
    'profiles',
    'payments',
]

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'shoutourbiz.urls'

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
                'django.template.context_processors.csrf',
                # 'main.context_processors.uses_num',
            ],
        },
    },
]

WSGI_APPLICATION = 'shoutourbiz.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Toronto'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Haystack

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'main.custom_elasticsearch.ConfigurableElasticSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'shoutourbiz',
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

FORCE_SCRIPT_NAME = ''

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_URL = FORCE_SCRIPT_NAME + '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'main', 'media')

LOGIN_URL = FORCE_SCRIPT_NAME + '/login/'

PDF_ROOT = MEDIA_ROOT + '/pdf/'
PDF_ROOT = os.path.join(BASE_DIR, 'main', 'media', 'pdf')

#email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST_USER = 'noreply@shoutour.biz'
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

AUTH_USER_MODEL = 'main.AuthUser'

IG_ID =  '******'
IG_SECRET =  '******'
IG_API_URL = 'https://api.instagram.com/v1'

TW_KEY = '******'
TW_SECRET = '******'

JVZ_SECRET_KEY = '******'

PAYMENTS_PLANS = {
    "INTRO": {
        "stripe_plan_id": "intro",
        "name": "Intro Plan ($997/month)",
        "description": "Users can get 250 credits per month.",
        "price": 997,
        "currency": "usd",
        "interval": "month"
    },
    "SILVER": {
        "stripe_plan_id": "silver",
        "name": "Silver Plan ($1497/month)",
        "description": "Users can get 500 credites per month.",
        "price": 1497,
        "currency": "usd",
        "interval": "month"
    },
    "GOLD": {
        "stripe_plan_id": "gold",
        "name": "Gold Plan ($2997/month)",
        "description": "Users can get 1000 credits per month.",
        "price": 2997,
        "currency": "usd",
        "interval": "month",
    },
}

DEFAULT_FREE_CREDITS = 5

CELERY_IMPORTS = ['main.tasks', 'main.tasks_ipn']

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

ACCS_PER_PAGE = 20

PAYMENT_PLANS = {
    '0.50': (300, 1),
}

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
