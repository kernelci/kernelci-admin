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


def parser(descr):
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('--host', required=True, choices=HOSTS.keys(),
                        help="Hostname of the API server")
    parser.add_argument('--dry', action='store_true',
                        help="Dry run, do not send any request")
    return parser


def request(hostname, path, payload):
    host = HOSTS[hostname]
    url = urllib.parse.urljoin(host['url'], path)
    headers = {
        "Authorization": host['token'],
        "Content-Type": "application/json"
    }
    return url, headers, json.dumps(payload)
