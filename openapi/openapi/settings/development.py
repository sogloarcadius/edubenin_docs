from openapi.settings.base import *
from corsheaders.defaults import default_headers

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += ['corsheaders']

MIDDLEWARE += ['corsheaders.middleware.CorsMiddleware']

CORS_ALLOW_HEADERS = default_headers + (
    'Cache-Control',
)

CORS_ORIGIN_ALLOW_ALL = True

