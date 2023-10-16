from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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
