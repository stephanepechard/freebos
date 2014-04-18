# system
from datetime import timedelta


# current data
APP_TOKEN = "RFYyRYZw0by11rWlZaM8Lex5CfMTLtg9zpi7GszBUoX2vJSXqxxGQ8AvPqjiBDTQ"
TRACK_ID = '5'


# this app
APP_ID = "fr.freebox.cosmicapp"
APP_NAME = "Cosmic App"
APP_VERSION = "0.0.1",
DEVICE_NAME = "marvin"


# Freebox OS API
API = 'http://mafreebox.freebox.fr/api/v1/'
AUTHORIZE = API + 'login/authorize/'
LOGIN = API + 'login/'
SESSION = API + 'login/session/'
WIFI = API + 'wifi/'
WIFI_CONFIG = API + 'wifi/config/'
WIFI_STATIONS = API + 'wifi/stations/'


# Celery configuration
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
BROKER_URL = 'redis://' + REDIS_HOST + ':' + str(REDIS_PORT) + '/9'
CELERY_DEFAULT_QUEUE = APP_ID
CELERY_TIMEZONE = 'Europe/Paris'
CELERY_IMPORTS = ('tasks')
CELERYD_CONCURRENCY = 1
CELERYBEAT_SCHEDULE = {
    'connected_devices-every-10-minutes': {
        'task': 'tasks.connected_devices',
        'schedule': timedelta(minutes=10),
    },
}


# logger
def create_logger():
    import logging
    logger = logging.getLogger(APP_NAME)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

    steam_handler = logging.StreamHandler()
    steam_handler.setLevel(logging.DEBUG)
    steam_handler.setFormatter(formatter)
    logger.addHandler(steam_handler)

    return(logger)
