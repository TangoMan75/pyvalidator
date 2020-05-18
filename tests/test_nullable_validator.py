#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

import typing
from unittest import TestCase

from pyvalidator.constraints.nullable_validator import NullableValidator
from pyvalidator.type_hint import TypeHint


class TestNullableValidator(TestCase):
    nullable_fixtures = (
        {'alias': 'Any',      'annotation': typing.Any,              'category': typing._SpecialForm, 'origin': None},
        {'alias': 'Optional', 'annotation': typing.Optional[str],    'category': typing._SpecialForm, 'origin': None},
        {'alias': 'Optional', 'annotation': typing.Optional[int],    'category': typing._SpecialForm, 'origin': None},
        {'alias': None,       'annotation': typing.Union[str, None], 'category': typing._GenericAlias, 'origin': typing.Union},
        {'alias': None,       'annotation': typing.Union[int, None], 'category': typing._GenericAlias, 'origin': typing.Union},
    )

    #################################################

    def test_nullable_validator_invalid_value_should_return_false(self):
        """==> nullable validator invalid value should return False"""
        for item in self.nullable_fixtures:
            # Any is always valid
            if item.get('annotation') is not typing.Any:
                self.assertFalse(NullableValidator(TypeHint(item.get('annotation')), 'invalid_value'))
                self.assertFalse(NullableValidator(TypeHint(item.get('annotation')), 666))
                self.assertFalse(NullableValidator(TypeHint(item.get('annotation')), True))

    def test_nullable_validator_valid_value_should_return_true(self):
        """==> nullable validator valid value should return True"""
        for item in self.nullable_fixtures:
            self.assertTrue(NullableValidator(TypeHint(item.get('annotation')), None))
