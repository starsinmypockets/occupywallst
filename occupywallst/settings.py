r"""

    occupywallst.settings
    ~~~~~~~~~~~~~~~~~~~~~

    This file is used to configure Django.

"""

from os.path import abspath, dirname, join
project_root = dirname(abspath(__file__))

DEBUG = False
PAYPAL_DEBUG = DEBUG
AUTHNET_DEBUG = DEBUG
TEMPLATE_DEBUG = DEBUG

MEDIA_ROOT = join(project_root, 'media')
GEOIP_PATH = join(project_root, 'data')
SHP_PATH = join(project_root, 'data')

ADMINS = (
    ('', 'errors@occupywallst.org'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'occupywallst',
    },
}

# store cache entries as json so node.js can read them.  also we don't
# need no goofy key prefixes
CACHES = {
    'default': {
        'BACKEND': 'occupywallst.memcachedjson.MemcachedCacheJSON',
        'KEY_FUNCTION': lambda key, key_prefix, version: key,
        'LOCATION': [
            '127.0.0.1:11211',
        ],
    }
}

BOLD = '\x1b[1m'
GREEN = '\x1b[32m'
RESET = '\x1b[0m'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': (GREEN + '%(asctime)s %(levelname)s %(name)s '
                       '%(filename)s:%(lineno)d ' + RESET + '%(message)s'),
        },
        'simple': {
            'format': GREEN + '%(levelname)s ' + RESET + '%(message)s',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django': {
            'level': 'WARNING',
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'level': 'WARNING',
            'handlers': ['console', 'mail_admins'],
            'propagate': False,
        },
        'occupywallst': {
            'level': 'WARNING',
            'handlers': ['console', 'mail_admins'],
            'propagate': False,
        },
    },
}

SITE_ID = 1
USE_I18N = True
USE_L10N = False
USE_THOUSAND_SEPARATOR = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_DOMAIN = '.occupywallst.org'
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
DEFAULT_CHARSET = 'utf-8'
ROOT_URLCONF = 'occupywallst.urls'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# change me in production
SECRET_KEY = 'oek(taazh36*h939oau#$%()dhueha39h(3zhc3##ev_jpfyd2'

TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

INSTALLED_APPS = [
    'occupywallst',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.gis',
]

try:
    from occupywallst.settings_local import *
except ImportError:
    pass
