#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from unittest import TestCase

from pyvalidator.constraints.not_blank_validator import NotBlankValidator
from pyvalidator.type_hint import TypeHint


class TestNotBlankValidator(TestCase):
    stdtype_fixtures = (
        {'name': 'bytearray', 'type': bytearray, 'valid': bytearray(b'bytearray'), 'invalid': b''},
        {'name': 'bytes', 'type': bytes, 'valid': b'bytes', 'invalid': bytearray()},
        {'name': 'complex', 'type': complex, 'valid': 1j, 'invalid': 0j},
        {'name': 'dict', 'type': dict, 'valid': {'Dictionary': True}, 'invalid': {}},
        {'name': 'float', 'type': float, 'valid': 1.1, 'invalid': 0.0},
        {'name': 'frozenset', 'type': frozenset, 'valid': frozenset({1, 2, 3}), 'invalid': frozenset()},
        {'name': 'int', 'type': int, 'valid': 666, 'invalid': 0},
        {'name': 'list', 'type': list, 'valid': ['List'], 'invalid': []},
        {'name': 'memoryview', 'type': memoryview, 'valid': memoryview(b'memoryview'), 'invalid': memoryview(b'')},
        {'name': 'range', 'type': range, 'valid': range(1, 10), 'invalid': range(0)},
        {'name': 'set', 'type': set, 'valid': {1, 2, 3}, 'invalid': set()},
        {'name': 'str', 'type': str, 'valid': 'String', 'invalid': ''},
        {'name': 'tuple', 'type': tuple, 'valid': ('Tuple',), 'invalid': ()},
    )

    #################################################

    def test_not_blank_validator_invalid_value_should_return_false(self):
        """==> not_blank validator invalid value should return False"""
        for item in self.stdtype_fixtures:
            self.assertFalse(NotBlankValidator(TypeHint(item.get('type')), item.get('invalid')))

    def test_not_blank_validator_valid_value_should_return_true(self):
        """==> not_blank validator valid value should return True"""
        for item in self.stdtype_fixtures:
            self.assertTrue(NotBlankValidator(TypeHint(item.get('type')), item.get('valid')))
