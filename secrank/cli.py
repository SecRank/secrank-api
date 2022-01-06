#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

module_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(1, module_path)

from secrank import pdns
from secrank import logger


def main():
    log = logger.init(__name__)

    api_type = ''
    if len(sys.argv) < 2:
        print('API type is not specified')
        print('Example: secrank pdns|whois|trends [options]')
        return


    api_type = sys.argv[1]
    if api_type[0] == '-':
        print('Invalid api type: %s' % api_type)
        print('Example: secrank pdns|whois|trends [options]')
        return

    api = None
    if api_type == 'pdns':
        api = pdns.api

    if api is None:
        log.error('unknown api')
    else:
        try:
            df = api()
            print(df)
        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    main()
