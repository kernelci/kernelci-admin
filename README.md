# KernelCI Admin Tools

This Python 3 tool can be used to perform various KernelCI admin operations,
such as managing API tokens.

## Settings

A `_settings.py` module needs to be created with settings for various hosts
running KernelCI back-end or front-end instances.  You can copy
`_sample_settings.py` as `_settings.py` and adjust it as required.

## Usage

The `kci` tool has a number of available commands to perform various operations
with a KernelCI backend API.  It provides a help message with the list of all
these commands when simply running `kci`:

```
Usage:
  kci COMMAND <OPTIONS>

Available commands:
  add_lab          Create a lab entry
  add_token        Create a user API token
  list_labs        List all the existing labs
  list_tokens      List all the existing tokens
```

Each command will also require some options.  Typically, commands need at least
a `--host=HOSTNAME` option to specify which KernelCI API you want to be
interacting with.  The name passed to the `--host` option is used to look up
information in the `_settings.py` module.

To get detailed help for any command, use the `--help` option:

```
$ ./kci add_lab --help
usage: kci [-h] --host {localhost} [--dry] --lab-name LAB_NAME --first-name
           FIRST_NAME --last-name LAST_NAME --email EMAIL

Create a lab entry

optional arguments:
  -h, --help            show this help message and exit
  --host {localhost}    Hostname of the API server
  --dry                 Dry run, do not send any request
  --lab-name LAB_NAME   Name of the lab i.e. lab-something
  --first-name FIRST_NAME
                        First name of the contact person
  --last-name LAST_NAME
                        Last name of the contact person
  --email EMAIL         Email address of the contact person
```
