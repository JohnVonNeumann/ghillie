#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of ghillie.
# https://github.com/JohnVonNeumann/ghillie

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2019, JohnVonNeumann <louiswillcock@gmail.com>

from setuptools import setup, find_packages
from ghillie import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='ghillie',
    version=__version__,
    description='User-Agent randomisation.',
    long_description='''
User-Agent randomisation.
''',
    keywords='user-agent, scraping, web',
    author='JohnVonNeumann',
    author_email='louiswillcock@gmail.com',
    url='https://github.com/JohnVonNeumann/ghillie',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'ghillie=ghillie.cli:main',
        ],
    },
)
