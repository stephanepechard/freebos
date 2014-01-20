#!/usr/bin/env python
# -*- coding: utf-8 -*-

# system
import argparse
import time
# local
from freebos import FreeboxOSAPI


def test_venv2():
    freebox_api = FreeboxOSAPI()
    freebox_api.open_session()

    #freebox_api.toggle_wifi()
    #time.sleep(1)
    #freebox_api.get_wifi_status()

