#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Main Module. """

import logging
from source.settings import config_logging
from source.arguments import parse_args
from source.xml2xlsx import xml2xlsx
from source import __version__

def main():
    """
    cppcheck2xlsx main
    """
    # configure logging
    config_logging()

    # input arguments
    args = parse_args()
    if args.path is not None:
        xml2xlsx(args.path)
    elif args.version:
        logging.info('cppcheck2xlsx version %s', __version__)
