#
# Copyright (c) 2016 Nick Douma < n . douma [at] nekoconeko . nl >
#
# This file is part of unifilocation, a.k.a. python-unifilocation .
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3.0 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see
# <http://www.gnu.org/licenses/>.

from unifilocation.api import Unifi
from unifilocation.config import initialize_settings, initialize_cli_settings
from collections import OrderedDict
from omniconf import config, help_requested, version_requested, show_usage
from omniconf.exceptions import UnconfiguredSettingError
from tabulate import tabulate
import sys


def handle_flags():
    if help_requested():
        initialize_settings(load=False)
        initialize_cli_settings(load=False)
        show_usage(name="unifilocation")
    if version_requested():
        print "VERSION"
        sys.exit(0)


def load_config():
    try:
        initialize_settings()
        initialize_cli_settings()
    except UnconfiguredSettingError as use:
        print str(use)
        show_usage(name="unifilocation", exit=1)


def show_users():
    unifi = Unifi(host=config("unifi.host"), port=config("unifi.port"),
                  version=config("unifi.version"),
                  site_id=config("unifi.site"),
                  username=config("unifi.username"),
                  password=config("unifi.password"))

    fields = config("fields")
    _users = unifi.get_connected_users()
    users = []
    for user in _users:
        u = OrderedDict()
        for field in fields:
            if field in user:
                u[field] = user[field]
            else:
                u[field] = None
        users.append(u)
    users.sort(key=lambda x: x[fields[0]])
    print tabulate(users, headers="keys")


def main():
    handle_flags()
    load_config()
    show_users()

if __name__ == "__main__":
    main()
