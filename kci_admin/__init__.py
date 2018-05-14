# Copyright (C) 2018 Collabora Ltd
# Author: Guillaume Tucker <guillaume.tucker@collabora.com>
#
# This module is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

import argparse
import json
import urllib.parse

try:
    from _settings import HOSTS
except ImportError:
    print("Warning: no local _settings module found")
    from _sample_settings import HOSTS


def create_parser(descr):
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('--host', required=True, choices=HOSTS.keys(),
                        help="Hostname of the API server")
    parser.add_argument('--dry', action='store_true',
                        help="Dry run, do not send any request")
    return parser


def add_lab_request(hostname, opts):
    """Create a request to add a LAVA lab entry into the backend.

    The `hostname` is the name to look up in the HOSTS from the settings.

    The `opts` dictionary should contain the following fields:
    * name: Name of the LAVA lab
    * first_name: First name of a person to contact for the lab
    * last_name: Last name of a person to contact for the lab
    * email: Email address of a person to contact for the lab

    It returns a 3-tuple with (url, data, payload) suitable to be used with the
    standard `requests.post()` function.
    """
    host = HOSTS[hostname]

    headers = {
        "Authorization": host['token'],
        "Content-Type": "application/json"
    }

    payload = {
        "name": opts['lab_name'],
        "contact": {
            "name": opts['first_name'],
            "surname": opts['last_name'],
            "email": opts['email'],
        }
    }

    url = urllib.parse.urljoin(host['url'], "/lab")

    return url, json.dumps(payload), headers
