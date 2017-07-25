#!/usr/bin/env python
#
# Copyright (c) 2014 ThoughtWorks, Inc.
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

from setuptools import setup

import datetime
import time

now = datetime.datetime.now()
timestamp = time.strftime('%Y%m%d%H%M', now.timetuple())

setup(name='leap.pixelated-www',
      version='1.0.%s' % timestamp,
      description='Static Assets for the Pixelated User Agent UI',
      author='LEAP Encryption Access Project',
      author_email='info@leap.se',
      url='http://github.com/leapcode/pixelated-user-agent',
      license='GNU Affero General Public License v3 or later (AGPLv3+)',
      namespace_packages=['leap'],
      packages=['leap.pixelated_www'],
      package_data={
          '': ['protected/*',
               'protected/css/*',
               'protected/fonts/*',
               'public/*']})
