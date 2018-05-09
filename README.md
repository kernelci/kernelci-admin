# KernelCI Admin Tools

This set of Python 3 tools can be used to perform various KernelCI admin
operations, such as managing API tokens.

## Settings

A `_settings.py` module needs to be created with settings for various hosts
running KernelCI back-end or front-end instances.  You can copy
`_sample_settings.py` as `_settings.py` and adjust it as required.

## kci_add_lab

This tool can be used to define a new test lab entry in the KernelCI back-end.

```
Create a lab entry

positional arguments:
  name                  Name of the lab i.e. lab-something

optional arguments:
  -h, --help            show this help message and exit
  --first-name FIRST_NAME
                        First name of the contact person
  --last-name LAST_NAME
                        Last name of the contact person
  --email EMAIL         Email address of the contact person
  --host {localhost,other-host}
                        Hostname of the API server
  --dry                 Dry run, do not send any request
```
