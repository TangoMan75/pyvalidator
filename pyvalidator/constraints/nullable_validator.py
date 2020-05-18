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


class NullableValidator(AbstractValidator):
    """Returns True if property is nullable AND value is None"""

    def __init__(self, hint: TypeHint = None, value: Any = None) -> None:
        super().__init__(hint, value)

    @property
    def is_supported(self) -> bool:
        return type(None) in self.hint.types or self.hint.annotation is Any

    @property
    def is_valid(self) -> bool:
        return self.value is None and self.is_supported
