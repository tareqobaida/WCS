from .base import *

import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    '.whitecanvassoft.com',
    '13.234.89.0',  # aws ip
]


# TODO should log to file not console in production, will change later
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}
