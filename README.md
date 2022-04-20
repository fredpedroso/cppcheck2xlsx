# cppcheck2xlsx

Tool to generate the cppcheck report in an Excel file (.xlsx)

## Features

  - **ID**: id of error, and which are valid symbolnames.
  - **Severity**: The possible severities ()
  - **Message**: The error message in short format
  - **Verbose**: The error message in long format
  - **CWE**: CWE ID for the problem
  - **File**: File where the possible issue is
  - **Line**: Line where the possible issue is

## Getting Started:

Clone the project repository: 

```
git clone https://github.com/fredpedroso/cppcheck2xlsx
```

### Requirements:

Install the requirements:

```
pip install -r requirements.txt
```

### How to use:

Running:

```
python cppcheck2xlsx.py --path <file.xml>
```

The report will be generated in the _report_ folder.