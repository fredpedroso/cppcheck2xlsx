
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Module responsible for converting cppcheck xml report to xlsx file """

import os
import xml.dom.minidom
from source.report import generate_report
from source.parser_report_xml import get_base_report

def xml2xlsx(xml_report_path):
    """
    Cppcheck Xml to Xlsx
    """

    # Get cppcheck report list
    cppcheck_xml = xml.dom.minidom.parse(xml_report_path)
    base_report = get_base_report(cppcheck_xml)

    # Generate report
    generate_report(base_report)