#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import argparse
import pandas as pd
import plotext as plt
from secrank import apiutils
from secrank.exceptions import ArgumentsError

def api(token, argv):
    parser = argparse.ArgumentParser(description='secrank-trends command line tool')

    parser.add_argument('-v', '--verbose', dest='verbose', action="store_true", help='Verbose')
    parser.add_argument('-d', '--domain', dest='domain', type=str, default='', help='query domain')
    parser.add_argument('-b', '--begin', dest='begin', type=str, default='', help='date begin')
    parser.add_argument('-e', '--end', dest='end', type=str, default='', help='date end')
    parser.add_argument('-l', '--last', dest='last', type=int, default=0, help='last days')
    parser.add_argument('-sld', '--sld', dest='sld', action="store_true", help='sld')
    parser.add_argument('-c', '--columns', dest='columns', type=str, default='totalCount,clientipCount', help='columns: noError,totalCount,aCount,aaaaCount,nsCount,cnameCount,soaCount,mxCount,txtCount,srvCount,dnameCount,dsCount,rrsigCount,nsecCount,nsec3Count,nullCount,clientipCount,subdomainCount,pointIPaCount,pointIPaaaaCount,pointIPcnameCount,pointIPdnameCount,pointIPdsCount,pointIPmxCount,pointIPnsCount,pointIPnsec3Count,pointIPnsecCount,pointIPnullCount,pointIPrrsigCount,pointIPsoaCount,pointIPsrvCount,pointIPtotalCount,pointIPtxtCount')
    args, _ = parser.parse_known_args(argv)

    if len(args.domain) == 0:
        parser.print_help()
        raise ArgumentsError('Must specify domain for trends: -d')

    if args.last > 0:
        date_end = datetime.datetime.now() + datetime.timedelta(days=-1)
        date_begin = datetime.datetime.now() + datetime.timedelta(days=-args.last)
    else:
        delta = 7
        date_end = args.end
        if date_end == '':
            date_end = datetime.datetime.now() + datetime.timedelta(days=-1)

        date_begin = args.begin
        if date_begin == '':
            date_begin = datetime.datetime.now() + datetime.timedelta(days=-delta)

    days = []
    for i in range((date_end-date_begin).days):
        days.append((date_end + datetime.timedelta(days=i)).strftime('%Y%m%d'))

    params = {
        'type': 'fqdn',
        'start': date_begin.strftime('%Y%m%d'),
        'end': date_end.strftime('%Y%m%d')
    }
    if args.sld:
        params['type'] = 'sld'
    else:
        params['type'] = 'fqdn'
    api_path = '/trends/domain/%s' % args.domain
    
    df = apiutils.call(token, api_path, params=params)

    columns = args.columns.split(',')
    for column in df.columns:
        if column not in columns:
            df = df.drop(column, axis=1)

    plt.subplots(2, 1)

    plt.subplots(1, 1)
    plt.plotsize(150, 20)
    plt.title("Domain Trends (Requests)")
    plt.clc()
    plt.bar(days, df['totalCount'], orientation = "v", width = 0.3)
    plt.show()

    plt.subplots(2, 1)
    plt.span(1, 20)
    plt.plotsize(150, 20)
    plt.title("Domain Trends (Clients)")
    plt.clc()
    plt.bar(days, df['clientipCount'], orientation = "v", width = 0.3)

    plt.show()

    if not args.verbose:
        return None
    return df
