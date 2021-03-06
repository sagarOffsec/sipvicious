#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
#       sipvicious/setup.py
#
#       Copyright (C) 2007-2020  Sandro Gauci <sandro@enablesecurity.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import io
from os import path
from setuptools import setup, find_packages
from sipvicious.libs.svhelper import __author__, __version__
this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    desc = f.read()

setup(name='sipvicious',
    version=__version__,
    description='SIPVicious suite is a set of tools that can be used to audit SIP based VoIP systems.',
    long_description = desc,
    long_description_content_type='text/markdown',
    author=__author__,
    author_email='sandro@enablesecurity.com',
    license='GPL',
    url='https://sipvicious.org',
    project_urls={
        "Bug Tracker": "https://github.com/EnableSecurity/sipvicious/issues",
        "Source Code": "https://github.com/EnableSecurity/sipvicious/tree/master",
    },
    download_url='https://github.com/EnableSecurity/sipvicious/archive/v%s.zip' % __version__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sipvicious_svmap = sipvicious.svmap:main',
            'sipvicious_svwar = sipvicious.svwar:main',
            'sipvicious_svcrack = sipvicious.svcrack:main',
            'sipvicious_svreport = sipvicious.svreport:main',
            'sipvicious_svcrash = sipvicious.svcrash:main',
            ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'Topic :: Internet',
        'Topic :: Security',
        'Topic :: System :: Networking',
        'Topic :: Communications :: Telephony',
        'Topic :: Communications :: Internet Phone',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    keywords='telephony sip audit scanner voip'
)
