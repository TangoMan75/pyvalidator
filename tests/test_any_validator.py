#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from typing import (Any)
from unittest import TestCase

from pyvalidator.constraints.any_validator import AnyValidator
from pyvalidator.type_hint import TypeHint


class TestAnyValidator(TestCase):
    expected_valid = (
        True,
        bytearray(b'bytearray'),
        b'bytes',
        1j,
        {'Dictionary': True},
        1.1,
        frozenset({1, 2, 3}),
        666,
        ['List'],
        memoryview(b''),
        range(1, 10),
        {1, 2, 3},
        'String',
        ('Tuple',),
        type,
        None,
    )

    #################################################

    def test_any_validator_should_return_false(self):
        """==> Any should always return False"""
        for value in self.expected_valid:
            self.assertFalse(AnyValidator(TypeHint(int), value))

    def test_any_validator_should_return_true(self):
        """==> Any should always return True"""
        for value in self.expected_valid:
            self.assertTrue(AnyValidator(TypeHint(Any), value))
