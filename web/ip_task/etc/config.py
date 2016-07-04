
class Config(object):
    DEBUG = False
    DB_HOST = 'db'
    DB_USER = 'postgres'
    DB_NAME = 'postgres'
    LOGGING = {
                'version': 1,
                'disable_existing_loggers': False,
                'formatters': {
                    'message_only': {
                        'format': '%(asctime)s;%(message)s',
                        'datefmt': '%d-%m-%Y %H:%M:%S',
                    },
                    'basic': {
                        'format': '%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                    },
                },
                'handlers': {
                    'basic': {
                        'class': 'logging.StreamHandler',
                        'formatter': 'basic',
                    },
                },
                'loggers': {
                    'root': {
                        'handlers': ['basic'],
                    },
                    'backend': {
                        'handlers': ['basic'],
                        'level': 'DEBUG',
                        'propagate': True,
                        'qualname': 'backend',
                    },
                }
        }


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass
