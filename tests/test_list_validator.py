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

from pyvalidator.constraints.collections_validator import ListValidator
from pyvalidator.type_hint import TypeHint


class TestListValidator(TestCase):
    list_fixtures = (
        {'alias': 'FrozenSet', 'annotation': typing.FrozenSet[str], 'category': typing._GenericAlias, 'origin': frozenset},
        {'alias': 'List',      'annotation': typing.List[str],      'category': typing._GenericAlias, 'origin': list}, 
        {'alias': 'Set',       'annotation': typing.Set[str],       'category': typing._GenericAlias, 'origin': set},
        {'alias': 'Tuple',     'annotation': typing.Tuple[str],     'category': typing._GenericAlias, 'origin': tuple},
    )

    list_no_parameter_fixtures = (
        {'alias': 'FrozenSet', 'annotation': typing.FrozenSet, 'category': typing._GenericAlias, 'origin': frozenset},
        {'alias': 'List',      'annotation': typing.List,      'category': typing._GenericAlias, 'origin': list}, 
        {'alias': 'Set',       'annotation': typing.Set,       'category': typing._GenericAlias, 'origin': set},
        {'alias': 'Tuple',     'annotation': typing.Tuple,     'category': typing._GenericAlias, 'origin': tuple},
    )

    list_expected_valid = ('one', 'two', 'three')
    list_expected_invalid = (1, 2, 3)

    #################################################

    nested_list_fixtures = (
        {'alias': 'FrozenSet', 'annotation': typing.FrozenSet[typing.FrozenSet[str]], 'category': typing._GenericAlias, 'origin': frozenset},
        {'alias': 'List',      'annotation': typing.List[typing.List[str]],           'category': typing._GenericAlias, 'origin': list},
        {'alias': 'Set',       'annotation': typing.Set[typing.Set[str]],             'category': typing._GenericAlias, 'origin': set},
        {'alias': 'Tuple',     'annotation': typing.Tuple[typing.Tuple[str]],         'category': typing._GenericAlias, 'origin': tuple},
    )

    nested_list_expected_valid = (('one', 'two', 'three'), ('one', 'two', 'three'), ('one', 'two', 'three'))
    nested_list_expected_invalid = ((1, 2, 3), (1, 2, 3), (1, 2, 3))

    #################################################

    nested_union_fixtures = (
        {'alias': 'FrozenSet', 'annotation': typing.FrozenSet[typing.Union[int, str]], 'category': typing._GenericAlias, 'origin': frozenset},
        {'alias': 'List',      'annotation': typing.List[typing.Union[int, str]],      'category': typing._GenericAlias, 'origin': list}, 
        {'alias': 'Set',       'annotation': typing.Set[typing.Union[int, str]],       'category': typing._GenericAlias, 'origin': set},
        {'alias': 'Tuple',     'annotation': typing.Tuple[typing.Union[int, str]],     'category': typing._GenericAlias, 'origin': tuple},
    )

    nested_union_expected_valid = ('one', 'two', 'three', 1, 2, 3)
    nested_union_expected_invalid = (0j, 0.1, b'invalid')

    #################################################

    def test_list_validator_should_return_false(self):
        """==> list validator should return false"""
        for item in self.list_fixtures:
            self.assertFalse(ListValidator(TypeHint(item.get('annotation')), self.list_expected_invalid))

    def test_list_validator_should_return_true(self):
        """==> list validator should return true"""
        for item in self.list_fixtures:
            self.assertTrue(ListValidator(TypeHint(item.get('annotation')), self.list_expected_valid))

    def test_list_validator_alias_with_no_parameter_should_return_true(self):
        """==> list validator alias with no parameter should return true"""
        for item in self.list_no_parameter_fixtures:
            hint = TypeHint(item.get('annotation'))
            validator = ListValidator(hint, self.list_expected_valid)
            self.assertTrue(validator)

    #################################################
    # Test recursive
    #################################################

    def test_nested_list_validator_should_return_false(self):
        """==> nested list validator should return false"""
        for item in self.nested_list_fixtures:
            self.assertFalse(ListValidator(TypeHint(item.get('annotation')), self.nested_list_expected_invalid))

    def test_nested_list_validator_should_return_true(self):
        """==> nested list validator should return true"""
        for item in self.nested_list_fixtures:
            hint = TypeHint(item.get('annotation'))
            validator = ListValidator(hint, self.nested_list_expected_valid)
            self.assertTrue(validator)

    #################################################
    # Union
    #################################################

    def test_nested_union_should_return_false(self):
        """==> nested union should return false"""
        for item in self.nested_union_fixtures:
            hint = TypeHint(item.get('annotation'))
            validator = ListValidator(hint, self.nested_union_expected_invalid)
            self.assertFalse(validator)

    def test_nested_union_should_return_true(self):
        """==> nested union should return true"""
        for item in self.nested_union_fixtures:
            hint = TypeHint(item.get('annotation'))
            validator = ListValidator(hint, self.nested_union_expected_valid)
            self.assertTrue(validator)
    
    #################################################
    # Any
    #################################################

    def test_nested_any_in_list_should_return_true(self):
        """==> nested any in list should return true"""
        hint = TypeHint(typing.List[typing.Any])
        validator = ListValidator(hint, self.list_expected_valid)
        self.assertTrue(validator)
        validator = ListValidator(hint, self.list_expected_invalid)
        self.assertTrue(validator)

