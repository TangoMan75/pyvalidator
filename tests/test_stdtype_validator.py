#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from unittest import TestCase

from pyvalidator.constraints.stdtype_validator import StdtypeValidator
from pyvalidator.type_hint import TypeHint


class TestStdtypeValidator(TestCase):
    stdtype_fixtures = (
        {'name': 'bool', 'type': bool, 'valid': True, 'invalid': 'invalid_value'},
        {'name': 'bytearray', 'type': bytearray, 'valid': bytearray(b'bytearray'), 'invalid': 'invalid_value'},
        {'name': 'bytes', 'type': bytes, 'valid': b'bytes', 'invalid': 'invalid_value'},
        {'name': 'complex', 'type': complex, 'valid': 1j, 'invalid': 'invalid_value'},
        {'name': 'dict', 'type': dict, 'valid': {'Dictionary': True}, 'invalid': 'invalid_value'},
        {'name': 'float', 'type': float, 'valid': 1.1, 'invalid': 'invalid_value'},
        {'name': 'frozenset', 'type': frozenset, 'valid': frozenset({1, 2, 3}), 'invalid': 'invalid_value'},
        {'name': 'int', 'type': int, 'valid': 666, 'invalid': 'invalid_value'},
        {'name': 'list', 'type': list, 'valid': ['List'], 'invalid': 'invalid_value'},
        {'name': 'memoryview', 'type': memoryview, 'valid': memoryview(b'memoryview'), 'invalid': 'invalid_value'},
        {'name': 'range', 'type': range, 'valid': range(1, 10), 'invalid': 'invalid_value'},
        {'name': 'set', 'type': set, 'valid': {1, 2, 3}, 'invalid': 'invalid_value'},
        {'name': 'str', 'type': str, 'valid': 'String', 'invalid': ['invalid_value']},
        {'name': 'tuple', 'type': tuple, 'valid': ('Tuple',), 'invalid': 'invalid_value'},
        {'name': 'type', 'type': type, 'valid': type, 'invalid': 'invalid_value'},
    )

    #################################################

    def test_stdtype_validator_invalid_value_should_return_false(self):
        """==> stdtype validator invalid value should return False"""
        for item in self.stdtype_fixtures:
            self.assertFalse(StdtypeValidator(TypeHint(item.get('type')), item.get('invalid')))

    def test_stdtype_validator_valid_value_should_return_true(self):
        """==> stdtype validator valid value should return True"""
        for item in self.stdtype_fixtures:
            self.assertTrue(StdtypeValidator(TypeHint(item.get('type')), item.get('valid')))
