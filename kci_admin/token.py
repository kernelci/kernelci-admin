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
from . import  request_delete as kci_request_delete
from . import parser as kci_parser


description_create = "Create a user API token"
description_get_list = "List all the existing tokens"
description_remove = "Remove user API token"


def parser_create(descr=description_create):
    parser = kci_parser(descr)
    parser.add_argument('--username', required=True,
                        help="Username of the user")
    parser.add_argument('--email', required=True,
                        help="email address of the user")
    parser.add_argument('--admin', action='store_true',
                        help="enable admin permission")
    parser.add_argument('--superuser', action='store_true',
                        help="enable superuser permission")
    parser.add_argument('--get', action='store_true',
                        help="enable GET permission")
    parser.add_argument('--post', action='store_true',
                        help="enable POST permission")
    parser.add_argument('--delete', action='store_true',
                        help="enable DELETE permission")
    parser.add_argument('--new-tokens', action='store_true',
                        help="enable permission to create new tokens")
    parser.add_argument('--upload', action='store_true',
                        help="enable upload permission")
    return parser


def parser_list(descr=description_get_list):
    parser = kci_parser(descr)
    parser.add_argument('--username',
                        help="Only show details for this username")
    return parser


def parser_remove(descr=description_remove):
    parser = kci_parser(descr)
    parser.add_argument('--id', metavar='ID', required=True,
                        help='ObjectId (_id) of the token to remove')
    return parser


def request_create(hostname, payload):
    return kci_request(hostname, "/token", payload)


def request_remove(hostname, id_):
    return kci_request_delete(hostname,'/token/{}'.format(id_))


def get_list(hostname):
    data = kci_request_get(hostname, "/token")
    return data['result']


def get_dict(hostname):
    tokens_list = get_list(hostname)
    return {t['_id']['$oid']: t for t in tokens_list}
