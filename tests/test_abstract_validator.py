#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from unittest import TestCase

from pyvalidator.constraints.abstract_validator import AbstractValidator
from pyvalidator.type_hint import TypeHint


class TestAbstractValidator(TestCase):

    def test_constructor_typeerror(self):
        """==> abstract validator invalid value in constructor should raise TypeError"""
        with self.assertRaises(TypeError):
            AbstractValidator('invalid_value', '')

    def test_constructor_typehint(self):
        """==> abstract validator valid value in constructor should not raise TypeError"""
        try:
            AbstractValidator(TypeHint(str), 'value')
        except Exception as e:
            self.fail(e)

    def test_hint_setter_typeerror(self):
        """==> abstract validator invalid value in setter should raise TypeError"""
        with self.assertRaises(TypeError):
            abstractvalidator = AbstractValidator()
            abstractvalidator.hint = 'invalid_value'

    def test_hint_setter(self):
        """==> abstract validator value in setter should not raise TypeError"""
        try:
            abstractvalidator = AbstractValidator()
            abstractvalidator.hint = TypeHint(str)
        except Exception as e:
            self.fail(e)

    def test_value_setter_and_getter(self):
        """==> abstract validator getter should return expected value"""
        abstractvalidator = AbstractValidator()
        abstractvalidator.value = 'valid_value'
        self.assertEqual(abstractvalidator.value, 'valid_value')

    def test_abstract_validator_should_raise_unboundlocalerror_when_typehint_not_set(self):
        """==> abstract validator should raise UnboundLocalError when TypeHint not set"""
        with self.assertRaises(UnboundLocalError):
            abstractvalidator = AbstractValidator()
            abstractvalidator.validate('valid_value')
