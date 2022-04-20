
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Cppcheck XML Parser
'''


def get_base_report(xml_report_path):
    '''
    Get base report from cppcheck report

    @param xml_report_path: cppcheck report xml dom
    @type  xml_report_path: xml dom

    @return: cppcheck report
    @rtype: list
    '''
    report_data = []
    report_errors = xml_report_path.getElementsByTagName('error')

    for error in report_errors:
        # Issue Base Information
        error_id = error.getAttribute('id')                         # id of error, and which are valid symbolnames
        error_severity = error.getAttribute('severity')             # The possible severities for messages
        error_msg = error.getAttribute('msg')                       # The error message in short format
        error_verbose = error.getAttribute('verbose')               # The error message in long format
        error_cwe = error.getAttribute('cwe')                       # CWE ID for the problem
        symbols = error.getElementsByTagName('symbol')              # Symbol
        error_symbols = symbols[0].firstChild.nodeValue if len(symbols) > 0 else "<none>"

        # Issue Location Information
        error_locations = error.getElementsByTagName('location')
        for location in error_locations:
            error_file = location.getAttribute('file')              # File where the possible issue is
            error_line = location.getAttribute('line')              # Line where the possible issue is

            report_data.append((
                error_id,
                error_severity,
                error_msg,
                error_verbose,
                error_cwe,
                error_file,
                error_line,
                error_symbols
            ))

    return report_data
