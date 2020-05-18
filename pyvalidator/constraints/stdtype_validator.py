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


class StdtypeValidator(AbstractValidator):
    """Validate value matches annotation
    https://docs.python.org/3/library/stdtypes.html
    https://docs.python.org/3/reference/datamodel.html
    """

    stdtypes = (
        bool, bytes, bytearray, complex, dict, float, frozenset, int, list, memoryview, range, set, str, tuple, type
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
        if self.is_supported:
            return type(self.value) in self.hint.types
        return False
