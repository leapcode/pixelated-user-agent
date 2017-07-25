#!/usr/bin/env python
#
# Copyright (c) 2014-2017 ThoughtWorks, Inc.
# Copyright (c) 2017 LEAP Encryption Access Project
#
# Pixelated is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pixelated is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Pixelated. If not, see <http://www.gnu.org/licenses/>.

import datetime
import os
from setuptools import setup, find_packages
import time

now = datetime.datetime.now()
timestamp = time.strftime('%Y%m%d%H%M', now.timetuple())


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

required = [
    'requests',  # TODO deprecate!!!
    'pyasn1',
    'chardet',
    'whoosh',
    'twisted']

setup(name='leap.pixelated',
      version='1.0.%s' % timestamp,
      description='Twisted API with a RESTful service for the Pixelated front-end.',
      long_description=read('README.md'),
      author='LEAP Encryption Access Project',
      author_email='info@leap.se',
      url='https://github.com/leapcode/pixelated-user-agent',
      license='GNU Affero General Public License v3 or later (AGPLv3+)',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      install_requires=required,
      include_package_data=True)
