#!/usr/bin/env python
# -*- coding: utf-8 -*-

# system
import argparse
import time
# local
from freebos import FreeboxOSAPI


def test_connected_devices():
    freebox_api = FreeboxOSAPI()
    freebox_api.open_session()    
    freebox_api.connected_devices()


def _test_open_session():
    freebox_api = FreeboxOSAPI()
    freebox_api.open_session()
    freebox_api.get_wifi_status()

