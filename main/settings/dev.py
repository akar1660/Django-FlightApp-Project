from .base import *

DEBUG = config('DEBUG')

DEV_APPS = [
    "debug_toolbar",
]

INSTALLED_APPS += DEV_APPS

DEV_MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

MIDDLEWARE = DEV_MIDDLEWARE + MIDDLEWARE

INTERNAL_IPS = [
    "127.0.0.1",
]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
