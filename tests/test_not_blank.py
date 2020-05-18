#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from unittest import TestCase

from tests.dummy_not_blank import DummyNotBlank


class TestNotBlank(TestCase):

    def setUp(self):
        self.dummy = DummyNotBlank()

    def test_not_blank_properties_should_raise_valueerror(self):
        """==> not_blank properties should raise ValueError"""
        with self.assertRaises(ValueError):
            self.dummy.not_blank_bytearray = bytearray()
        with self.assertRaises(ValueError):
            self.dummy.not_blank_bytes = b''
        with self.assertRaises(ValueError):
            self.dummy.not_blank_complex = 0j
        with self.assertRaises(ValueError):
            self.dummy.not_blank_dict = {}
        with self.assertRaises(ValueError):
            self.dummy.not_blank_float = 0.0
        with self.assertRaises(ValueError):
            self.dummy.not_blank_frozenset = frozenset()
        with self.assertRaises(ValueError):
            self.dummy.not_blank_int = 0
        with self.assertRaises(ValueError):
            self.dummy.not_blank_list = []
        with self.assertRaises(ValueError):
            self.dummy.not_blank_range = range(0)
        with self.assertRaises(ValueError):
            self.dummy.not_blank_set = set()
        with self.assertRaises(ValueError):
            self.dummy.not_blank_str = ''
        with self.assertRaises(ValueError):
            self.dummy.not_blank_tuple = ()
