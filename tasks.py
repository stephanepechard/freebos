#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pipped
from celery import task
import redis
# local
from freebos import FreeboxOSAPI
from settings import APP_ID, REDIS_HOST, REDIS_PORT


@task
def task_connected_devices():
    api = FreeboxOSAPI()
    api.open_session()
    devices = api.connected_devices()

#    red = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
#    key = APP_ID + '.connected_devices'

    if not devices and self.get_wifi_status():
        api.wifi_off()
