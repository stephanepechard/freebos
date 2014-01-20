#!/usr/bin/env python
# -*- coding: utf-8 -*-

# system
import argparse
import sys
# local
from freebos import FreeboxOSAPI


def usage():
    sys.exit("ERROR usage: switch_wifi.py [on|off]")


def open():
    api = FreeboxOSAPI()
    api.open_session()
    return(api)


def main(argv):

    if (len(argv) == 1):
        api = open()
        api.get_wifi_status()
    elif (len(argv) == 2):
        api = open()
        if (argv[1] == "on"):
            api.wifi_on()
        elif (argv[1] == "off"):
            api.wifi_off()
        else:
            usage()
    else:
        usage()


if __name__ == '__main__':
    main(argv=sys.argv)
