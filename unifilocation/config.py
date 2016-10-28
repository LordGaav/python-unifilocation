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

from omniconf import setting, omniconf_load


def _split_list(sep=","):
    def _split(line):
        if isinstance(line, (list, tuple)):
            return line
        return line.split(sep)
    return _split


def initialize_settings(load=True):
    setting("unifi.host", required=True,
            help="Hostname (not URL) for the Unifi API.")
    setting("unifi.port", _type=int, default=443,
            help="Unifi API port.")
    setting("unifi.version", required=True,
            help="Unifi API version (v2, v3, v4, v5).")
    setting("unifi.site", default="default",
            help="Unifi AP site.")
    setting("unifi.username", required=True,
            help="Unifi API username.")
    setting("unifi.password", required=True,
            help="Unifi API password.")

    if load:
        omniconf_load(autoconfigure_prefix="")


def initialize_cli_settings(load=True):
    setting("fields", _type=_split_list(),
            default=["username", "hostname", "essid", "ap"],
            help="Fields to show in output.")

    if load:
        omniconf_load(autoconfigure_prefix="")
