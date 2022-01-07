#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import pandas as pd
from secrank import apiutils

from secrank.exceptions import ArgumentsError

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

def api(token, argv):
    parser = argparse.ArgumentParser(description='secrank-pdns command line tool')

    parser.add_argument('-d', '--domain', dest='domain', type=str, default='', help='query domain')
    parser.add_argument('-a', '--answer', dest='answer', type=str, default='', help='response rrdata')
    parser.add_argument('-l', '--limit', dest='limit', type=int, default=1000, help='limit')
    parser.add_argument('-rtype', '--rtype', dest='rtype', type=str, default='', help='request type')

    args, _ = parser.parse_known_args(argv)

    if (len(args.domain) == 0 and len(args.answer) == 0) or (len(args.domain) > 0 and len(args.answer) > 0):
        parser.print_help()
        raise ArgumentsError('Must specify one (and only one) argument for pdns: -d or -a')

    api_path = ''
    if len(args.domain) > 0:
        api_path = '/flint/rrset/%s' % args.domain
    else:
        api_path = '/flint/rdata/%s' % args.answer

    if len(api_path) == 0:
        raise Exception('Invalid API path')

    df = call(token, api_path, rtype=args.rtype, params={
        'limit': args.limit,
    })

    df['time_first'] = df['time_first'].astype('datetime64[s]')
    df['time_last'] = df['time_last'].astype('datetime64[s]')

    return df

def call(token, api_path, rtype='', params={}):
    if rtype is not None:
        params['rtype'] = rtypes[rtype.upper()] 
    records = apiutils.call(token, api_path, params)
    return pd.DataFrame.from_dict(records)

