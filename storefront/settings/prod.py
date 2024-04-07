import dj_database_url

from .common import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = []

DATABASES = {
    'default': dj_database_url.config()
}

CELERY_BROKER_URL = os.environ.get('REDIS_URL')
