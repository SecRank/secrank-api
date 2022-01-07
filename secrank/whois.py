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
    parser = argparse.ArgumentParser(description='secrank-whois command line tool')

    parser.add_argument('-fc', '--find-column', dest='findcolumn', type=str, default='', help='column: org | email | phone | nameserver | name')
    parser.add_argument('-f', '--find', dest='find', type=str, default='', help='find value')
    parser.add_argument('-d', '--domain', dest='domain', type=str, default='', help='query domain')
    parser.add_argument('-l', '--limit', dest='limit', type=int, default=1000, help='limit')
    parser.add_argument('-c', '--columns', dest='columns', type=str, default='domainName,createdDate,updatedDate,expiresDate,adminName,adminEmail,registrantName,registrantEmail', help='columns: domainName, domainNames, createdDate, expiresDate, updatedDate, nameServers, whoisServerList, status, adminAddress, adminCity, adminCountry, adminEmail, adminFax, adminName, adminOrganization, adminPostalCode, adminState, adminTelephone, registrantAddress, registrantCity, registrantCountry, registrantEmail, registrantFax, registrantName, registrantOrganization, registrantPostalCode, registrantState, registrantTelephone, techAddress, techCity, techCountry, techEmail, techFax, techName, techOrganization, techPostalCode, techState, techTelephone')
    args, _ = parser.parse_known_args(argv)

    if (len(args.domain) == 0 and len(args.find) == 0) or (len(args.domain) > 0 and len(args.find) > 0):
        parser.print_help()
        raise ArgumentsError('Must specify one (and only one) argument for whois: -d or -s')

    params = {
        'limit': args.limit
    }
    api_path = ''
    if len(args.domain) > 0:
        api_path = '/whois/history/%s' % args.domain
    else:
        if len(args.findcolumn) == 0:
            api_path = '/whois/reverse/%s' % args.find
        else:
            api_path = '/whois/reverse'
            params['column'] = args.findcolumn
            params['value'] = args.find
    
    df = call(token, api_path, params=params)

    if len(args.domain) > 0:
        columns = args.columns.split(',')
        for column in df.columns:
            if column not in columns:
                df = df.drop(column, axis=1)

    return df

def call(token, api_path, params={}):
    records = apiutils.call(token, api_path, params)
    return pd.DataFrame.from_dict(records)

