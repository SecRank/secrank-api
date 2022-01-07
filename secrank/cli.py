#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import yaml
import pandas as pd
import argparse
from os.path import expanduser

module_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(1, module_path)

from secrank import pdns
from secrank import whois
from secrank import logger
from secrank.exceptions import ArgumentsError


def main():
    log = logger.init(__name__)

    token = ''

    home = expanduser("~")
    license_file_path = os.path.join(home, '.secrank.lic')
    if not os.path.exists(license_file_path):
        print('Error: license not found. copy license file to your home directory (e.g. ~/.secrank.lic).')
        return
    with open(license_file_path) as license_file:
        license = json.loads(license_file.read())
        token = license['token']

    if len(token) == 0:
        print('Error: malformed license. please renew your license file (e.g. ~/.secrank.lic).')
        return

    api_type = ''
    if len(sys.argv) < 2:
        print('API type is not specified')
        print('Example: secrank pdns|whois|trends [options]')
        return

    parser = argparse.ArgumentParser(description='secrank command line tool', add_help=False)
    parser.add_argument('-view', '--view', dest='view', type=str, default='table', help='view type')
    parser.add_argument('-mw', '--max-column-width', dest='max_column_width', type=int, default=0, help='max column width')
    parser.add_argument('-top', '--top', dest='top', type=int, default=0, help='top rows')
    parser.add_argument('-tail', '--tail', dest='tail', type=int, default=0, help='last rows')
    parser.add_argument('-s', '--sort', dest='sort', type=str, default='', help='sort by')
    parser.add_argument('-st', '--sort-type', dest='sort_type', type=str, default='desc', help='asc or desc')
    args, _ = parser.parse_known_args(sys.argv[2:])

    sort_ascending = True
    if args.sort_type == 'desc':
        sort_ascending = False
    elif args.sort_type == 'asc':
        sort_ascending = True
    else:
        raise ArgumentsError('Invalid sort type')

    api_type = sys.argv[1]
    if api_type[0] == '-':
        print('Invalid api type: %s' % api_type)
        print('Example: secrank pdns|whois|trends [options]')
        return

    api = None
    if api_type == 'pdns':
        api = pdns.api
    elif api_type == 'whois':
        api = whois.api
    else:
        log.error('unknown api')
        return
    
    try:
        df = api(token, sys.argv[2:])

        pd.set_option('display.max_colwidth', args.max_column_width)

        if args.top > 0:
            df = df.head(args.top)
            pd.set_option('display.max_rows', None)
        elif args.tail > 0:
            df = df.tail(args.tail)
            pd.set_option('display.max_rows', None)
    
        if len(args.sort) > 0:
            sorts = args.sort.split(',')
            df = df.sort_values(by=sorts, ascending=sort_ascending).reset_index(drop=True)

        display_text = ''
        if args.view == 'table':
            display_text = df
        elif args.view == 'yaml':
            display_text = yaml.dump(
                df.reset_index().to_dict(orient='records'),
                sort_keys=False, width=72, indent=4,
                default_flow_style=None)
        elif args.view == 'csv':
            display_text = df.to_csv()
        else:
            display_text = df.to_json(orient='index', indent=2)
        print(display_text)
    except Exception as e:
        print(e)
        pass


if __name__ == '__main__':
    main()
