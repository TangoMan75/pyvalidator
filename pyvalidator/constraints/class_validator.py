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
    _SpecialForm,
    _GenericAlias,
    _VariadicGenericAlias
)

from pyvalidator.constraints.abstract_validator import AbstractValidator
from pyvalidator.type_hint import TypeHint


class ClassValidator(AbstractValidator):
    """Validate value is a class and matches annotation"""

    def __init__(self, hint: TypeHint = None, value: Any = None) -> None:
        super().__init__(hint, value)

    @property
    def is_supported(self) -> bool:
        # it doesn't make sense to have a typing alias checking itself
        if isinstance(self.hint.annotation, (_GenericAlias, _SpecialForm, _VariadicGenericAlias)):
            return False
        for type_ in self.hint.types:
            if isinstance(type(type_), type):
                return True
        return False

    @property
    def is_valid(self) -> bool:
        if self.is_supported:
            for type_ in self.hint.types:
                if self.value is type_:
                    return True
        return False
