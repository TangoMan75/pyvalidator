#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from unittest import TestCase

from pyvalidator.pyfunctools import (get_args, get_varnames)


class FooBar:
    def foobar(self, foo_: str, bar_: str) -> str:
        pass

    def not_annotated(self, foo_, bar_):
        pass

    def no_args(self):
        pass


class TestPyfunctools(TestCase):

    ##################################################
    # Test get_varnames
    ##################################################

    def test_get_varnames(self):
        """==> get_varnames should return expected result"""
        varnames = get_varnames(FooBar.foobar)
        self.assertEqual(varnames, ('foo_', 'bar_'))
        varnames = get_varnames(FooBar.not_annotated)
        self.assertEqual(varnames, ('foo_', 'bar_'))
        varnames = get_varnames(FooBar.no_args)
        self.assertEqual(varnames, ())

    ##################################################
    # Test get_args
    ##################################################

    def test_get_args_no_annotations(self):
        """==> get_args should raise AttributeError when annotation missing"""
        function = FooBar.not_annotated
        args = ('foo', 'bar')
        kwargs = {}
        with self.assertRaises(AttributeError):
            get_args(function, args, kwargs)

    def test_get_args_no_kwargs(self):
        """==> get_args should return expected result"""
        function = FooBar.foobar
        args = ('foo', 'bar')
        kwargs = {}
        args_, kwargs_ = get_args(function, args, kwargs)
        self.assertEqual(args_, ())
        self.assertEqual(kwargs_, {'foo_': 'foo', 'bar_': 'bar', })

    def test_get_args_1_kwargs(self):
        """==> get_args should return expected result"""
        function = FooBar.foobar
        args = ('foo',)
        kwargs = {'bar_': 'bar'}
        args_, kwargs_ = get_args(function, args, kwargs)
        self.assertEqual(args_, ())
        self.assertEqual(kwargs_, {'foo_': 'foo', 'bar_': 'bar', })

    def test_get_args_no_args(self):
        """==> get_args should return expected result"""
        function = FooBar.foobar
        args = ()
        kwargs = {'foo_': 'foo', 'bar_': 'bar'}
        args_, kwargs_ = get_args(function, args, kwargs)
        self.assertEqual(args_, ())
        self.assertEqual(kwargs_, {'foo_': 'foo', 'bar_': 'bar', })
