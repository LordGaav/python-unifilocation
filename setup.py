#!/usr/bin/env python
#
# Copyright (c) 2016 Nick Douma < n . douma [at] nekoconeko . nl >
#
# This file is part of unifilocation, a.k.a. python-unifiloaction .
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


from setuptools import setup, find_packages

DESCRIPTION = "Reads the Unifi API and determine the presence of users."
# LONG_DESCRIPTION = open('README.rst').read()
LONG_DESCRIPTION = ""
NAME = "unifilocation"
VERSION = "0.1.0"
BUILD = "aaaaaa"


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license="LGPL3",
    author="Nick Douma",
    author_email="n.douma@nekoconeko.nl",
    url="https://github.com/LordGaav/python-unifilocation",
    packages=find_packages(),
    # data_files=[('', ['README.rst'])],
    dependency_links=[
        "https://github.com/LordGaav/unifi-api/tarball/master#egg=unifi-1.2.6beta"
    ],
    install_requires=[
        "unifi>=1.2.6beta",
        "omniconf>=1.1.0",
        "tabulate"
    ],
    entry_points={
        "console_scripts": [
            "{0} = {1}.cli:main".format(NAME, NAME)
        ]
    }
)
