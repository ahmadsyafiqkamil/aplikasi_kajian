"""
Django settings for aplikasi_kajian project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# from kajian.templatetags import custom_tags

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uq^q7x=k+jm=2k4#0f5xs$toe(og25j^n9+eld%5#dgyrn3s&m'

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
    'kajian',
    'data_economy',
    'crispy_forms',
    'widget_tweaks',
    'ajax_datatable',
    # 'custom_tags',
    'notifications',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aplikasi_kajian.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'aplikasi_kajian.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.sqlite3.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_kajian',
        'USER': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        # 'PASSWORD': 'root'
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.sqlite3.models.BigAutoField'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles/'
STATICFILES_DIRS = [BASE_DIR / "static", ]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# LOGIN_REDIRECT_URL = '/kajian_list/'
LOGIN_REDIRECT_URL = '/'

# ajax-datatable

AJAX_DATATABLE_MAX_COLUMNS = 30
AJAX_DATATABLE_TRACE_COLUMNDEFS = False
AJAX_DATATABLE_TRACE_QUERYDICT = False
AJAX_DATATABLE_TRACE_QUERYSET = False
AJAX_DATATABLE_TEST_FILTERS = False
AJAX_DATATABLE_DISABLE_QUERYSET_OPTIMIZATION = False
AJAX_DATATABLE_STRIP_HTML_TAGS = True

# django notification

DJANGO_NOTIFICATIONS_CONFIG = {
    'SOFT_DELETE': True,
    # 'PAGINATE_BY': True,

}
