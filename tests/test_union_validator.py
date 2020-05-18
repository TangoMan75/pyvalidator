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

from pyvalidator.constraints.collections_validator import UnionValidator
from pyvalidator.type_hint import TypeHint


class TestUnionValidator(TestCase):
    union_fixtures = (
        {'alias': None, 'annotation': typing.Union[int, str],                    'category': typing._GenericAlias, 'origin': typing.Union},
        {'alias': None, 'annotation': typing.Union[int, typing.Union[int, str]], 'category': typing._GenericAlias, 'origin': typing.Union},
    )

    #################################################

    def test_union_validator_invalid_value_should_return_false(self):
        """==> union validator invalid value should return False"""
        for item in self.union_fixtures:
            hint = TypeHint(item.get('annotation'))
            validator = UnionValidator(hint, b'invalid')
            self.assertFalse(validator.is_valid)

    def test_union_validator_valid_value_should_return_true(self):
        """==> union validator valid value should return True"""
        for item in self.union_fixtures:
            hint = TypeHint(item.get('annotation'))
            validator = UnionValidator(hint, 'valid')
            self.assertTrue(validator.is_valid)
            validator = UnionValidator(hint, 666)
            self.assertTrue(validator.is_valid)

    def test_union_validator_nested_any_should_return_true(self):
        """==> union validator nested Any should return True"""
        hint = TypeHint(typing.Union[int, typing.Any])
        validator = UnionValidator(hint, b'valid')
        self.assertTrue(validator)
        validator = UnionValidator(hint, 666)
        self.assertTrue(validator)
