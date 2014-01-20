#!/usr/bin/env python
# -*- coding: utf-8 -*-

# system
import json
import logging
# pipped
import requests
# local
from settings import *


class FreeboxOSAPI(object):

    def __init__(self):
        """ Constructor """
        self.is_logged_in = False
        self.challenge = None
        self.session_token = None
        self.permissions = None
        self.password = None
        self.logger = create_logger()


    def get_app_token(self):
        """ Create a token for this app. You need physical access to grant it.
            It only needs to be done once. For now, the app token is
            hard-written in settings. """
        payload = {
            "app_id": APP_ID,
            "app_name": APP_NAME,
            "app_version": APP_VERSION,
            "device_name": DEVICE_NAME,
        }
        response = requests.post(AUTHORIZE, data=json.dumps(payload))
        app_token = self.get_result(response, 'app_token')
        if app_token:
            self.logger.info('App token: ' + app_token)
        else:
            self.logger.error('No app token, please create one!')

        return(app_token)


    def track_authorization(self):
        """ Check current authorization progress. """
        response = requests.get(AUTHORIZE + TRACK_ID)
        self.challenge = self.get_result(response, 'challenge')
        status = self.get_result(response, 'status')
        self.logger.info('Authorization status: ' + status)


    def get_result(self, response, result_name):
        """ Return the specified result from a successful response. """
        jr = json.loads(response.text)
        if 'success' in jr and jr['success'] == True:
            if 'result' in jr and result_name in jr['result']:
                return(jr['result'][result_name])
        return(0)


    def compute_password(self):
        """ Return the password to start a session. """
        if not self.password:
            from hashlib import sha1
            import hmac
            digest = None
            try:
                digest = hmac.new(APP_TOKEN, self.challenge, sha1)
            except:
                digest = hmac.new(bytes(APP_TOKEN, 'utf-8'),
                                    bytes(self.challenge, 'utf-8'), sha1)
            self.password = digest.hexdigest()
        return(self.password)


    def open_session(self):
        """ Open a session to work with. """
        self.track_authorization()
        payload = {
            "app_id": APP_ID,
            "password": self.compute_password(),
        }
        response = requests.post(SESSION, data=json.dumps(payload))
        self.session_token = self.get_result(response, 'session_token')
        if self.session_token:
            self.logger.info('Session opened')
            #permissions = self.get_result(response, 'permissions')
            #self.logger.info(permissions)
        else:
            self.logger.error(response.text)


    def get_headers(self):
        return({
            'X-Fbx-App-Auth': self.session_token,
            'Accept': 'text/plain',
        })


    def get_wifi_status(self):
        """ Return the wifi status: active/inactive. """
        response = requests.get(WIFI, headers=self.get_headers())
        active = self.get_result(response, 'active')
        if active:
            self.logger.info('Wifi is active')
        else:
            self.logger.info('Wifi is NOT active')
        return(active)


    def get_wifi_info(self):
        """ Return the wifi information: bss, name, id, active, etc. """
        response = requests.get(WIFI, headers=self.get_headers())
        json_res = json.loads(response.text)
        print(json.dumps(json_res, sort_keys=True, indent=4, separators=(',', ': ')))


    def toggle_wifi(self, active=False):
        """ Toggle the wifi state. """
        put_data = { 'ap_params': { 'enabled': active } }
        response = requests.put(WIFI_CONFIG, data=json.dumps(put_data),
                                headers=self.get_headers())
        jr = json.loads(response.text)
        if 'success' in jr and jr['success'] == True:
            self.logger.info('Wifi toggled')
        else:
            self.logger.error('Failed to update wifi status!')


    def wifi_on(self):
        if not self.get_wifi_status():
            self.toggle_wifi(True)
            time.sleep(1)
            self.get_wifi_status()


    def wifi_off(self):
        if self.get_wifi_status():
            self.toggle_wifi()
            time.sleep(1)
            self.get_wifi_status()

