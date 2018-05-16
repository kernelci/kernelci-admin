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

from . import request as kci_request
from . import request_get as kci_request_get
from . import parser as kci_parser


description_create = "Create a lab entry"
description_get_list = "List all the existing labs"


def parser_create(descr=description_create):
    parser = kci_parser(descr)
    parser.add_argument('--lab-name', required=True,
                        help="Name of the lab i.e. lab-something")
    parser.add_argument('--first-name', required=True,
                        help="First name of the contact person")
    parser.add_argument('--last-name', required=True,
                        help="Last name of the contact person")
    parser.add_argument('--email', required=True,
                        help="Email address of the contact person")
    return parser


def parser_list(descr=description_get_list):
    parser = kci_parser(descr)
    parser.add_argument('--lab-name',
                        help="Only show details for this given lab")
    return parser


def request_create(hostname, opts):
    """Return a request to create a new LAVA lab entry in the backend.

    The `hostname` is the name to look up in the HOSTS from the settings.

    The `opts` dictionary should contain the following fields:
    * name: Name of the LAVA lab
    * first_name: First name of a person to contact for the lab
    * last_name: Last name of a person to contact for the lab
    * email: Email address of a person to contact for the lab

    It returns a 3-tuple with (url, headers, data) suitable to be used with the
    standard `requests.post()` function.
    """
    payload = {
        "name": opts['lab_name'],
        "contact": {
            "name": opts['first_name'],
            "surname": opts['last_name'],
            "email": opts['email'],
        }
    }
    return kci_request(hostname, "/lab", payload)


def get_list(hostname):
    data = kci_request_get(hostname, "/lab")
    return data['result']
