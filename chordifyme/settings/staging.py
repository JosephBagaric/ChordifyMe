from .base import *

DEBUG = False

ALLOWED_HOSTS = []
BASE_URL = 'https://localhost:80'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'chordifyme_postgis',
        'PORT': '5432',
    }
}

SECRET_KEY = 'dst6@c&qy+nn0)-gu0+$p%$2qk#h6*#mx9%9x)1o3=&jy!2%n8'

# TLS/SSL settings

# https://docs.djangoproject.com/en/1.8/topics/security/#ssl-https
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# For performance reasons, let's set this to False and Nginx will take care of
# it. https://docs.djangoproject.com/en/1.8/ref/middleware/#ssl-redirect
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
