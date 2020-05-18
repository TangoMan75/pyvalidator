#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled

 with this source code in the file LICENSE.
"""

from functools import wraps
from platform import python_version
from typing import (
    Any,
    Callable,
    Dict,
    Tuple,
)

from pyvalidator.constraints.alias_validator import AliasValidator
from pyvalidator.constraints.callable_validator import CallableValidator
from pyvalidator.constraints.class_validator import ClassValidator
from pyvalidator.constraints.collections_validator import DictValidator
from pyvalidator.constraints.collections_validator import ListValidator
from pyvalidator.constraints.collections_validator import UnionValidator
from pyvalidator.constraints.not_blank_validator import NotBlankValidator
from pyvalidator.constraints.nullable_validator import NullableValidator
from pyvalidator.constraints.stdtype_validator import StdtypeValidator
from pyvalidator.pyfunctools import get_args
from pyvalidator.type_hint import TypeHint

if python_version()[0:3] < '3.7':
    print('\033[93m[!] Make sure you have Python 3.7+ installed, quitting.\n\n \033[0m')
    exit(1)


class Validator:
    """
    Handle runtime static typing with annotations and decorator
    https://docs.python.org/3/library/typing.html
    https://docs.python.org/3/library/stdtypes.html
    https://github.com/agronholm/typeguard
    https://stackoverflow.com/questions/51171908/extracting-data-from-typing-types
    """

    ##################################################
    # Decorators
    ##################################################

    # static method allows child classes to use decorator
    @staticmethod
    def type_check(function: Callable) -> Callable:
        if not callable(function):
            raise TypeError('Validator.type_check(function): function must be callable')

        @wraps(function)
        def inner(self, *args: Tuple, **kwargs: Dict) -> Callable:
            args_, kwargs_ = get_args(function, args, kwargs)
            _type_check(function, kwargs_)
            return function(self, *args, **kwargs)

        return inner

    # static method allows child classes to use decorator
    @staticmethod
    def not_blank(function: Callable) -> Callable:
        if not callable(function):
            raise TypeError('Validator.not_blank(function): function must be callable')

        @wraps(function)
        def inner(self, *args: Tuple, **kwargs: Dict) -> Callable:
            args_, kwargs_ = get_args(function, args, kwargs)
            _not_blank(function, kwargs_)
            return function(self, *args_, **kwargs_)

        return inner


##################################################
# Type Check
##################################################

def _type_check(function: Callable, fixed_kwargs: Dict[str, Any]) -> None:
    if not callable(function):
        raise TypeError('_type_check: function must be callable')
    if not isinstance(fixed_kwargs, dict):
        raise TypeError('_type_check: fixed_kwargs must be set to a dictionary')
    # get type hints (typing.get_type_hints method requires to import unnecessary module)
    for arg_name, arg_hint in function.__annotations__.items():
        # ignore "return" (will raise "KeyError" when accessing "fixed_kwargs[arg_name]")
        if arg_name == 'return':
            continue
        hint = TypeHint(arg_hint)
        # there is no way to validate custom property
        if hint.category == 'property':
            continue
        value = fixed_kwargs[arg_name]
        if not (NullableValidator(hint, value) or
                StdtypeValidator(hint, value) or
                ClassValidator(hint, value) or
                CallableValidator(hint, value) or
                AliasValidator(hint, value) or
                ListValidator(hint, value) or
                DictValidator(hint, value) or
                UnionValidator(hint, value)):
            raise TypeError('{} must be set to {}, {} given'.format(
                function.__qualname__, hint.types, type(value))
            )


##################################################
# Assert Not Blank
##################################################


def _not_blank(function: Callable, fixed_kwargs: Dict[str, Any]) -> None:
    if not callable(function):
        raise TypeError('_type_check: function must be callable')
    if not isinstance(fixed_kwargs, dict):
        raise TypeError('_type_check: fixed_kwargs must be set to a dictionary')
    # get type hints (typing.get_type_hints method requires to import unnecessary module)
    for arg_name, arg_hint in function.__annotations__.items():
        # ignore "return" (will raise "KeyError" when accessing "fixed_kwargs[arg_name]")
        if arg_name == 'return':
            continue
        hint = TypeHint(arg_hint)
        # there is no way to validate custom property
        if hint.category == 'property':
            continue
        value = fixed_kwargs[arg_name]
        if not NotBlankValidator(hint, value):
            raise ValueError('{} cannot be blank'.format(function.__qualname__))
