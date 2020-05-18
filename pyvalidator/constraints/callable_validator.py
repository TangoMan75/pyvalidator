#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled

 with this source code in the file LICENSE.
"""

from typing import (
    Any,
    _GenericAlias,
    _VariadicGenericAlias
)

from pyvalidator.constraints.abstract_validator import AbstractValidator
from pyvalidator.type_hint import TypeHint


class CallableValidator(AbstractValidator):
    """Validate callable alias ; Check value is callable"""

    def __init__(self, hint: TypeHint = None, value: Any = None) -> None:
        super().__init__(hint, value)

    @property
    def is_supported(self) -> bool:
        return isinstance(self.hint.annotation, (_VariadicGenericAlias, _GenericAlias)) and \
               self.hint.alias == 'Callable'

    @property
    def is_valid(self) -> bool:
        if self.is_supported:
            return callable(self.value)
        return False
