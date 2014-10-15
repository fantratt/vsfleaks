"""
Django settings for vsfleaks project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

is_dev=True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-omicj(p*3&onw&z&baluf=zb@$fkhrtjl-ce%4b(8#tgm2$wk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = is_dev

TEMPLATE_DEBUG = is_dev

if is_dev:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['univleaks.net', 'www.univleaks.net']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taggit',
    'taggit_templatetags',
    'vsfleakssite',
    'django_comments',
    'mptt',
    'tagging',
    'zinnia',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'zinnia.context_processors.version',  # Optional
)

ROOT_URLCONF = 'vsfleaks.urls'

WSGI_APPLICATION = 'vsfleaks.wsgi.application'

#For the django.sites packge
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
if is_dev:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'vsfleaks',
            'USER': 'vsfleaks',
            'PASSWORD': 'kmarx4ever'
        }
    }
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'sv-SE'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
if is_dev:
    STATIC_URL = '/static/'
    
    TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
    
    MEDIA_ROOT = '/media/'
else:
    STATIC_URL = 'http://static.univleaks.net/'

    STATIC_ROOT = '/home/tkman85/webapps/django_static/'

    TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

    MEDIA_ROOT = '/media/'