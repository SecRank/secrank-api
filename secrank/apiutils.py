#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

api_base_url = 'https://api.secrank.cn'

def call(token, path, params={}):
    headers = {
        "fdp-token": token
    }
    api_address = api_base_url + path
    rsp = requests.get(api_address, params=params, headers=headers)
    if rsp.status_code != 200:
        raise Exception('API Gateway Error')
    rsp_json = rsp.json()
    if 'code' not in rsp_json:
        raise Exception('Invalid Response Format')
    if rsp_json['code'] != 200:
        error_msg = "Unknown"
        if 'status' in rsp_json:
            error_msg = rsp_json['status']
        raise Exception('Server Fail' % error_msg)
    if 'data' not in rsp_json:
        raise Exception('Invalid Response Format')
    return rsp_json['data']
