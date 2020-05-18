#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled

 with this source code in the file LICENSE.
"""

from typing import (Any, Optional)

from pyvalidator.type_hint import TypeHint


class AbstractValidator:

    def __init__(self, hint: TypeHint = None, value: Any = None) -> None:
        """If you ever need to create your own custom validator extend this abstract class.
        NOTE: hint and value parameters are nullable
        """
        if hint is None:
            self._hint = None
        else:
            self.hint = hint
        self._value = value

    ##################################################

    @property
    def hint(self) -> Optional[TypeHint]:
        return self._hint

    @hint.setter
    def hint(self, hint: TypeHint) -> None:
        if not isinstance(hint, TypeHint):
            raise TypeError('{}.hint must be set to TypeHint'.format(self.__class__.__name__))
        self._hint = hint

    ##################################################

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        self._value = value

    ##################################################

    def supports(self, hint: TypeHint) -> bool:
        """Set TypeHint and check Validator can handle TypeHint"""
        self.hint = hint
        return self.is_supported

    @property
    def is_supported(self) -> bool:
        """Check Validator can handle TypeHint"""
        pass

    ##################################################

    def validate(self, value: Any) -> bool:
        """Set value and check type matches TypeHint"""
        if not isinstance(self._hint, TypeHint):
            raise UnboundLocalError(
                "{} local variable 'hint' referenced before assignment".format(self.__class__.__name__))
        self.value = value
        return self.is_valid

    @property
    def is_valid(self) -> bool:
        """Check value type matches TypeHint"""
        pass

    ##################################################

    def __bool__(self):
        return self.is_valid
