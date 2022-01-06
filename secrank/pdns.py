#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import argparse
import requests
import pandas as pd
from os.path import expanduser
from secrank import apiutils
from secrank.exceptions import ArgumentsError

token = ''

home = expanduser("~")
license_file_path = os.path.join(home, '.secrank.lic')
if not os.path.exists(license_file_path):
    print('Error: license not found. copy license file to your home directory (e.g. ~/.secrank.lic).')
    exit()
with open(license_file_path) as license_file:
    license = json.loads(license_file.read())
    token = license['token']

if len(token) == 0:
    print('Error: malformed license. please renew your license file (e.g. ~/.secrank.lic).')
    exit()

rtypes = {
    '': -1,
    'A': 1,
    'NS': 2,
    'CNAME': 5,
    'SOA': 6,
    'MX': 15,
    'TXT': 16,
    'AAAA': 28,
    'SRV': 33,
    'DNAME': 39,
    'DS': 43,
    'RRSIG': 46,
    'NSEC': 47,
    'NSEC3': 50
}

def api():
    parser = argparse.ArgumentParser(description='secrank-pdns command line tool')

    parser.add_argument('-d', '--domain', dest='domain', type=str, default='', help='query domain')
    parser.add_argument('-a', '--answer', dest='answer', type=str, default='', help='response rrdata')
    parser.add_argument('-s', '--sort', dest='sort', type=str, default='', help='sort by')
    parser.add_argument('-l', '--limit', dest='limit', type=int, default=1000, help='limit')
    parser.add_argument('-st', '--sort-type', dest='sort_type', type=str, default='desc', help='sort by')
    parser.add_argument('-rtype', '--rtype', dest='rtype', type=str, default='', help='request type')
    parser.add_argument('-top', '--top', dest='top', type=int, default=0, help='top rows')
    parser.add_argument('-tail', '--tail', dest='tail', type=int, default=0, help='last rows')
    parser.add_argument('-mw', '--max-column-width', dest='max_column_width', type=int, default=0, help='max column width')

    args, _ = parser.parse_known_args()

    if (len(args.domain) == 0 and len(args.answer) == 0) or (len(args.domain) > 0 and len(args.answer) > 0):
        parser.print_help()
        raise ArgumentsError('Must specify one (and only one) argument for pdns: -d or -a')

    sort_ascending = True
    if args.sort_type == 'desc':
        sort_ascending = False
    elif args.sort_type == 'asc':
        sort_ascending = True
    else:
        raise ArgumentsError('Invalid sort type')

    api_path = ''
    if len(args.domain) > 0:
        api_path = '/flint/rrset/%s' % args.domain
    else:
        api_path = '/flint/rdata/%s' % args.answer

    if len(api_path) == 0:
        raise Exception('Invalid API path')

    df = call(api_path, rtype=args.rtype, limit=args.limit)

    if len(args.sort) > 0:
        sorts = args.sort.split(',')
        df = df.sort_values(by=sorts, ascending=sort_ascending).reset_index(drop=True)

    df['time_first'] = df['time_first'].astype('datetime64[s]')
    df['time_last'] = df['time_last'].astype('datetime64[s]')

    if args.top > 0:
        df = df.head(args.top)
        pd.set_option('display.max_rows', None)
    elif args.tail > 0:
        df = df.tail(args.tail)
        pd.set_option('display.max_rows', None)

    pd.set_option('display.max_colwidth', args.max_column_width)
    
    return df

def call(api_path, rtype='', limit=1000):
    params = {
        'limit': limit
    }
    if rtype is not None:
        params['rtype'] = rtypes[rtype.upper()] 
    records = apiutils.call(api_path, token, params)
    return pd.DataFrame.from_dict(records)

