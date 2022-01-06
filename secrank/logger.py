#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

def init(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s]%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

