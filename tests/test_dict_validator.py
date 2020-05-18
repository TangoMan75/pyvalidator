#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

import collections.abc
import typing
from unittest import TestCase

from pyvalidator.constraints.collections_validator import DictValidator
from pyvalidator.type_hint import TypeHint


class TestDictValidator(TestCase):

    dict_fixtures = (
        {'alias': 'Dict', 'annotation': typing.Dict[int, str], 'category': typing._GenericAlias, 'origin': dict},
    )

    dict_no_parameter_fixtures = (
        {'alias': 'Dict', 'annotation': typing.Dict, 'category': typing._GenericAlias, 'origin': dict},
    )

    dict_expected_valid = {1: 'one', 2: 'two', 3: 'three'}
    dict_expected_invalid = {'one': 1, 'two': 2, 'three': 3}

    #################################################

    nested_dict_fixtures = (
        {'alias': 'Dict', 'annotation': typing.Dict[int, typing.Dict[int, str]], 'category': typing._GenericAlias, 'origin': dict},
    )

    nested_dict_expected_valid = {
        1: {1: 'one', 2: 'two', 3: 'three'},
        2: {1: 'one', 2: 'two', 3: 'three'},
        3: {1: 'one', 2: 'two', 3: 'three'},
    }

    nested_dict_expected_invalid = {
        1: {'one': 1, 'two': 2, 'three': 3},
        2: {'one': 1, 'two': 2, 'three': 3},
        3: {'one': 1, 'two': 2, 'three': 3},
      }

    #################################################

    nested_union_fixtures = (
        {'alias': 'Dict', 'annotation': typing.Dict[int, typing.Union[int, str]], 'category': typing._GenericAlias, 'origin': dict},
    )

    nested_union_expected_valid = {1: 'one', 2: 'two', 3: 'three', 1: 1, 2: 2, 3: 3}
    nested_union_expected_invalid = {1: 0j, 2: 0.1, 3: b'invalid'}

    #################################################

    def test_dict_validator_should_return_false(self):
        """==> dict validator should return false"""
        for item in self.dict_fixtures:
            self.assertFalse(DictValidator(TypeHint(item.get('annotation')), self.dict_expected_invalid))

    def test_dict_validator_should_return_true(self):
        """==> dict validator should return True"""
        for item in self.dict_fixtures:
            hint = TypeHint(item.get('annotation'))
            validator = DictValidator(hint, self.dict_expected_valid)
            self.assertTrue(validator)

    def test_dict_validator_alias_with_no_parameter_should_return_true(self):
        """==> dict validator alias with no parameter should return True"""
        for item in self.dict_no_parameter_fixtures:
            hint = TypeHint(item.get('annotation'))
            validator = DictValidator(hint, self.dict_expected_valid)
            self.assertTrue(validator)

    #################################################
    # Test recursive
    #################################################

    def test_nested_dict_validator_should_return_false(self):
        """==> nested dict validator should return False"""
        for item in self.nested_dict_fixtures:
            self.assertFalse(
                DictValidator(TypeHint(item.get('annotation')), self.nested_dict_expected_invalid)
            )

    def test_nested_dict_validator_should_return_true(self):
        """==> nested dict validator should return True"""
        for item in self.nested_dict_fixtures:
            self.assertTrue(
                DictValidator(TypeHint(item.get('annotation')), self.nested_dict_expected_valid)
            )

    #################################################
    # Union
    #################################################

    def test_nested_union_should_return_false(self):
        """==> nested union should return False"""
        for item in self.nested_union_fixtures:
            hint = TypeHint(item.get('annotation'))
            validator = DictValidator(hint, self.nested_union_expected_invalid)
            self.assertFalse(validator)

    def test_nested_union_should_return_true(self):
        """==> nested union should return True"""
        for item in self.nested_union_fixtures:
            hint = TypeHint(item.get('annotation'))
            validator = DictValidator(hint, self.nested_union_expected_valid)
            self.assertTrue(validator)

    #################################################
    # Any
    #################################################

    def test_nested_any_in_dict_should_return_true(self):
        """==> nested any in dict should return True"""
        hint = TypeHint(typing.Dict[int, typing.Any])
        validator = DictValidator(hint, self.nested_union_expected_valid)
        self.assertTrue(validator)
        validator = DictValidator(hint, self.nested_union_expected_invalid)
        self.assertTrue(validator)

