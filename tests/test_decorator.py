#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from unittest import TestCase

from pyvalidator.validator import Validator


class FooBar(Validator):
    @Validator.type_check
    @Validator.not_blank
    def foobar(self, foo_: str, bar_: str) -> str:
        return foo_ + bar_

    @Validator.type_check
    @Validator.not_blank
    def not_blank(self, foo_: str, bar_: str) -> str:
        return foo_ + bar_

    @Validator.type_check
    @Validator.not_blank
    def not_annotated(self, foo_, bar_):
        pass

    @Validator.type_check
    @Validator.not_blank
    def no_args(self):
        pass


class TestDecorator(TestCase):

    def setUp(self):
        self.foobar = FooBar()

    def test_foobar(self):
        """==> foobar should return expected value"""
        self.assertEqual(self.foobar.foobar('foo', 'bar'), 'foobar')

    def test_decorator_typeerror(self):
        """==> validator should raise TypeError"""
        with self.assertRaises(TypeError):
            self.foobar.foobar(b'foo', b'bar')

    def test_decorator_valueerror(self):
        """==> validator should raise ValueError"""
        with self.assertRaises(ValueError):
            self.foobar.not_blank('', '')
