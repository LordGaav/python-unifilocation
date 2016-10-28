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

from unifi.controller import Controller


class Unifi(object):
    def __init__(self, host, port, version, site_id, username, password):
        self.client = Controller(
            host=host, port=port, version=version, site_id=site_id,
            username=username, password=password
        )

    def __getattr__(self, _attr):
        return getattr(self.client, _attr)

    def get_connected_users(self):
        _users = self.client.get_clients()
        aps = self.client.get_aps()

        users = []
        for u in _users:
            user = u
            user['ap'] = None
            user['username'] = None

            if u['is_wired'] is False:
                user['ap'] = [ap['name'] for ap in aps
                              if ap['mac'] == u['ap_mac']][0]
            if "1x_identity" in u and u['1x_identity']:
                user['802.11x'] = u['1x_identity']
                user['username'] = u['1x_identity'].split("@")[0]
            users.append(u)
        return users
