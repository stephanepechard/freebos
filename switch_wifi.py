#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from freebos import FreeboxOSAPI

def main():
    freebox_api = FreeboxOSAPI()
    freebox_api.open_session()

    freebox_api.toggle_wifi()
    time.sleep(1)
    freebox_api.get_wifi_status()


if __name__ == '__main__':
    main()
