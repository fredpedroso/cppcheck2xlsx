# Cppcheck report converter from xml to xlsx

Tool that converts [cppcheck](http://cppcheck.sourceforge.net/) XML output to Excel (.xlsx) file.

## Features

The tool reads the cppcheck output xml file and generates an excel file containing the information below:

  - **ID**: id of error, and which are valid symbolnames.
  - **Severity**: Error, Information, Performance, Portability, Style, Warning.
  - **Message**: The error message in short format.
  - **Verbose**: The error message in long format.
  - **CWE**: CWE ID for the problem.
  - **File**: File where the possible issue is.
  - **Line**: Line where the possible issue is.

## Getting Started:

Clone the project repository: 

```
$ git clone [https://github.com/fredpedroso/cppcheck2xlsx.git](https://github.com/fredpedroso/cppcheck2xlsx.git)
```

### Requirements:

Install the requirements:

```
$ pip install -r requirements.txt
```

### Usage:

Generate the cppcheck report in xml:

```
$ cppcheck  -i src/ --xml --enable=all ./ 2> ./report-cppcheck.xml
```

Convert it to Excel (.xlsx) file:

```
$ python cppcheck2xlsx.py --path report-cppcheck.xml
```

The report will be generated in the _report_ folder.
