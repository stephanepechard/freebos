#!/usr/bin/env python
# -*- coding: utf-8 -*-

# system
import argparse
import sys
import time
# local
from freebos import FreeboxOSAPI


def usage():
    sys.exit("ERROR usage: switch_wifi.py [on|off]")


def open():
    api = FreeboxOSAPI()
    api.open_session()
    return(api)


def close(api):
    time.sleep(1)
    api.get_wifi_status()

def main(argv):

    if (len(argv) == 1):
        api = open()
        api.get_wifi_status()
    elif (len(argv) == 2):
        api = open()
        if (argv[1] == "on"):
            api.wifi_on()
            close(api)
        elif (argv[1] == "off"):
            api.wifi_off()
            close(api)
        else:
            usage()
    else:
        usage()


if __name__ == '__main__':
    main(argv=sys.argv)
