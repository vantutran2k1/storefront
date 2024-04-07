from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-hp28vo5*_s6-_b9jul7yqw29b*)xl*#qn08mkf#fmo1n)2k+)n'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST': 'mysql',
        'USER': 'root',
        'PASSWORD': 'MyPassword'
    }
}

CELERY_BROKER_URL = 'redis://redis:6379/1'

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}
