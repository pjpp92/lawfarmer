"""
Django settings for blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4v=^1h4hwd^niw*(!=(6@hu*=ws&2sbisu4d!+i+ivx-&mgnnl'


DEBUG = TEMPLATE_DEBUG = True 

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main',

    'tinymce',
    'sorl.thumbnail',
    'mce_filebrowser',
    'south',
    'flatblocks',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blog.urls'

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
            'default': {
                 'ENGINE': 'django.db.backends.postgresql_psycopg2',
                 'NAME': 'lawfarmer',
                 'USER': 'postgres',
                 'PASSWORD': 'postgres',
                 'HOST': 'localhost',
                 'PORT': '',
               }
        }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/



LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

MEDIA_ROOT = (
    os.path.join(BASE_DIR, 'media')
)

MEDIA_URL = '/media/'

STATIC_ROOT = (
    os.path.join(BASE_DIR, 'static')
)

STATIC_URL = '/static/'


TINYMCE_DEFAULT_CONFIG = {
  'file_browser_callback': 'mce_filebrowser'
}