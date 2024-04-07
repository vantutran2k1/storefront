from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-hp28vo5*_s6-_b9jul7yqw29b*)xl*#qn08mkf#fmo1n)2k+)n'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'MyPassword'
    }
}
