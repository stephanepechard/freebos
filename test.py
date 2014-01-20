#!/usr/bin/env python
# -*- coding: utf-8 -*-

# system
import argparse
import time
# local
from freebos import FreeboxOSAPI
from switch_wifi import main

def test():
    main()

def test_open_session():
    freebox_api = FreeboxOSAPI()
    freebox_api.open_session()

    #freebox_api.toggle_wifi()
    #time.sleep(1)
    freebox_api.get_wifi_status()

