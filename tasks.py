#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pipped
from celery import task, Celery
# local
from freebos import FreeboxOSAPI
from settings import APP_ID, REDIS_HOST, REDIS_PORT

# celery
celery = Celery('freebos')
celery.config_from_object('settings')


@task
def task_connected_devices():
    api = FreeboxOSAPI()
    api.open_session()
    devices = api.connected_devices()

    if not devices and self.get_wifi_status():
        api.wifi_off()

