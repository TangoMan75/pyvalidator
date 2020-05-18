#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

import typing
import collections.abc
from unittest import TestCase

from pyvalidator.constraints.callable_validator import CallableValidator
from pyvalidator.type_hint import TypeHint


class TestCallableValidator(TestCase):
    callable_fixtures = (
        {
            'alias': 'Callable', 'annotation': typing.Callable,
            'category': typing._VariadicGenericAlias, 'origin': collections.abc.Callable
        },
        {
            'alias': 'Callable', 'annotation': typing.Callable[[int, str], str],
            'category': typing._GenericAlias, 'origin': collections.abc.Callable
        },
    )

    #################################################

    def test_callable_validator_invalid_value_should_return_false(self):
        """==> callable validator invalid value should return False"""
        for item in self.callable_fixtures:
            self.assertFalse(CallableValidator(TypeHint(item.get('annotation')), 'invalid_value'))

    def test_callable_validator_valid_value_should_return_true(self):
        """==> callable validator valid value should return True"""
        for item in self.callable_fixtures:
            hint = TypeHint(item.get('annotation'))
            validator = CallableValidator(hint, lambda: True)
            self.assertTrue(validator.is_valid)
