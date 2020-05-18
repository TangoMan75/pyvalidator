#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled

 with this source code in the file LICENSE.
"""

from typing import Any

from pyvalidator.constraints.abstract_validator import AbstractValidator
from pyvalidator.type_hint import TypeHint


class NotBlankValidator(AbstractValidator):
    stdtypes = (
        bytes, bytearray, complex, dict, float, frozenset, int, list, memoryview, range, set, str, tuple, type
    )

    def __init__(self, hint: TypeHint = None, value: Any = None) -> None:
        super().__init__(hint, value)

    @property
    def is_supported(self) -> bool:
        for type_ in self.hint.types:
            if type_ in self.stdtypes:
                return True
        return False

    @property
    def is_valid(self) -> bool:
        """validate value is not empty
        NOTE: "bool" and "type" values excluded, since "not blank" does not make sense with them
        """
        if not self.is_supported:
            return False
        if self.hint.annotation is bytes and self.value == b'':
            return False
        if self.hint.annotation is bytearray and self.value == bytearray():
            return False
        if self.hint.annotation is complex and self.value == 0j:
            return False
        if self.hint.annotation is dict and self.value == {}:
            return False
        if self.hint.annotation is float and self.value == 0.0:
            return False
        if self.hint.annotation is frozenset and self.value == frozenset():
            return False
        if self.hint.annotation is int and self.value == 0:
            return False
        if self.hint.annotation is list and self.value == []:
            return False
        if self.hint.annotation is memoryview and self.value == memoryview(b''):
            return False
        if self.hint.annotation is range and self.value == range(0):
            return False
        if self.hint.annotation is set and self.value == set():
            return False
        if self.hint.annotation is str and self.value == '':
            return False
        if self.hint.annotation is tuple and self.value == ():
            return False
        return True
