"""
Django settings for bookmarks project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-ocvjf&p1d%!))e)dpp_uu39s-+=)w&!*oc$vl48o@n*_1fh%2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'account',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'productos',
    'miperfil',
    'rentas',

    'blog',


    # 3rd party app
    'django_markdown',
    'django_social_share',
    'taggit',
    'disqus',
    'social.apps.django_app.default',
    'debug_toolbar',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'bookmarks.urls'

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

WSGI_APPLICATION = 'bookmarks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

from django.core.urlresolvers import reverse_lazy

LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'soldiddfouns@gmail.com'
EMAIL_HOST_PASSWORD = 'solidd121314'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# python-social-auth settings
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.Facebook2OAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',

    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = '189689694716144'
SOCIAL_AUTH_FACEBOOK_SECRET = 'dcac20b747b1e307c9bc49d3cbadc6bb'

SOCIAL_AUTH_TWITTER_KEY = 'Svjtx7c5Z1w7Ah9ZL1W6dXhbh'
SOCIAL_AUTH_TWITTER_SECRET = 'aSpT8FPaHR41dWV16j74En48BWVSeoszLAUwhmDAOq77Sdh20L'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '369296056243-9bno3opb9vc2unhmah895hedtja36chs.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '6awUotnxUvCnRi3gIk5th6PL'

DISQUS_API_KEY = 'p7oKQ2Z9yGc8sCtcof4IM2hqsOCoMtbu9BONqi1W7kxPdjyWLRY9ezwUXWtxyXSN'
DISQUS_WEBSITE_SHORTNAME = 'SeRentaTodo'