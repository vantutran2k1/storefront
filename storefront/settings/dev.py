from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-378v86$#m2@=kox96ijee)l*te(9%)f+#(5pd)bb%f%pgcj+9$'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'storefront',
		'HOST': 'localhost',
		'USER': 'root',
		'PASSWORD': 'root'
	}
}

MIDDLEWARE += ['silk.middleware.SilkyMiddleware']

CELERY_BROKER_URL = 'redis://localhost:6379/1'
CACHES = {
	'default': {
		'BACKEND': 'django_redis.cache.RedisCache',
		'LOCATION': 'redis://127.0.0.1:6379/2',
		'OPTIONS': {
			'CLIENT_CLASS': 'django_redis.client.DefaultClient',
		}
	}
}

EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525
