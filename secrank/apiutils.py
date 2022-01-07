#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import textwrap
import pandas as pd

trace = False
api_base_url = 'https://api.secrank.cn'


def print_roundtrip(response, *args, **kwargs):
    format_headers = lambda d: '\n'.join(f'{k}: {v}' for k, v in d.items())
    print(textwrap.dedent('''
        ---------------- request ----------------
        {req.method} {req.url}
        {reqhdrs}

        {req.body}
        ---------------- response ----------------
        {res.status_code} {res.reason} {res.url}
        {reshdrs}

        {res.text}
    ''').format(
        req=response.request, 
        res=response, 
        reqhdrs=format_headers(response.request.headers), 
        reshdrs=format_headers(response.headers), 
    ))


def call(token, path, params={}):
    headers = {
        "fdp-token": token
    }
    api_address = api_base_url + path

    hook = {}
    if trace:
        hook = {'response': print_roundtrip}
    rsp = requests.get(api_address, params=params, headers=headers, hooks=hook)
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

    return pd.DataFrame.from_dict(rsp_json['data'])
