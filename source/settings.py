#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Settings module. """

import logging
import os

# Directories
HOME = os.getcwd()                              # home
TEMPLATE_DIR = os.path.join(HOME, 'template/')  # template
REPORT_DIR = os.path.join(HOME, 'report/')      # report

# Report template
REPORT_TEMPLATE = os.path.join(TEMPLATE_DIR, 'cppcheck_report_template.xlsx')

# Logging
def config_logging():
    """
    Logging format
    """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M')
