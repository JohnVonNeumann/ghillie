#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of ghillie.
# https://github.com/JohnVonNeumann/ghillie

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2019, JohnVonNeumann <louiswillcock@gmail.com>

from preggy import expect

from ghillie import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.1.0')
