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
    Union,
    TypeVar,
    _GenericAlias,
    _VariadicGenericAlias,
)

from pyvalidator.constraints.abstract_validator import AbstractValidator
from pyvalidator.constraints.alias_validator import AliasValidator
from pyvalidator.constraints.any_validator import AnyValidator
from pyvalidator.constraints.callable_validator import CallableValidator
from pyvalidator.constraints.class_validator import ClassValidator
from pyvalidator.constraints.nullable_validator import NullableValidator
from pyvalidator.constraints.stdtype_validator import StdtypeValidator
from pyvalidator.type_hint import TypeHint

# Cannot import modules that reference back to themselves, got to merge all classes in one ... stupid python


class DictValidator(AbstractValidator):
    """Validate typing.Dict aliases ; Check value matches dictionary annotation recursively
    eg: typing.Dict[int, str] will check keys and values match given constraints recursively.
    nested dictionaries will be validated as well : typing.Dict[int, typing.Dict[int, str]]
    """
    valid_aliases = (
        'Dict',
    )

    valid_types = (
        dict,
    )

    def __init__(self, hint: TypeHint = None, value: Any = None) -> None:
        super().__init__(hint, value)

    @property
    def is_supported(self) -> bool:
        # typing.Union have no attribute _name ... stupid python
        return isinstance(self.hint.annotation, _GenericAlias) and \
               self.hint.alias is not None and \
               self.hint.alias in self.valid_aliases

    @property
    def is_valid(self) -> bool:
        if not self.is_supported:
            return False
        # value does not match alias type
        if self.value is not self.hint.origin and not isinstance(self.value, self.valid_types):
            return False
        # Alias inconsitently returns TypeVar object or None when no parameters given ... stupid python
        # will not validate recursively, still value does match alias type though
        if len(self.hint.types) == 0 or isinstance(self.hint.types[0], TypeVar):
            return True

        # validate keys
        hint = TypeHint(self.hint.types[0])
        nullablevalidator = NullableValidator(hint)
        stdtypevalidator = StdtypeValidator(hint)
        unionvalidator = UnionValidator(hint)
        for value in self.value.keys():
            if not (nullablevalidator.validate(value) or
                    stdtypevalidator.validate(value) or
                    unionvalidator.validate(value)):
                return False

        # validate values
        hint = TypeHint(self.hint.types[1])
        # Any is always valid
        if AnyValidator().supports(hint):
            return True
        nullablevalidator = NullableValidator(hint)
        stdtypevalidator = StdtypeValidator(hint)
        classvalidator = ClassValidator(hint)
        callablevalidator = CallableValidator(hint)
        aliasvalidator = AliasValidator(hint)
        listvalidator = ListValidator(hint)
        dictvalidator = DictValidator(hint)
        unionvalidator = UnionValidator(hint)
        for value in self.value.values():
            if not (nullablevalidator.validate(value) or
                    stdtypevalidator.validate(value) or
                    classvalidator.validate(value) or
                    callablevalidator.validate(value) or
                    aliasvalidator.validate(value) or
                    listvalidator.validate(value) or
                    dictvalidator.validate(value) or
                    unionvalidator.validate(value)):
                return False

        return True

class ListValidator(AbstractValidator):
    """Validate lists recursively
    eg: typing.List[int] will check contained values match given constraint recursively.
    nested lists will be validated as well : typing.List[typing.List[int]]
    """

    valid_aliases = (
        'FrozenSet'
        'List'
        'Set'
        'Tuple'
    )

    valid_types = (
        frozenset, list, set, tuple
    )

    def __init__(self, hint: TypeHint = None, value: Any = None) -> None:
        super().__init__(hint, value)

    @property
    def is_supported(self) -> bool:
        # typing.Union have no attribute _name ... stupid python
        return isinstance(self.hint.annotation, (_GenericAlias, _VariadicGenericAlias)) and \
               self.hint.alias is not None and \
               self.hint.alias in self.valid_aliases

    @property
    def is_valid(self) -> bool:
        if not self.is_supported:
            return False
        # value does not match alias type
        if self.value is not self.hint.origin and not isinstance(self.value, self.valid_types):
            return False
        # Alias inconsitently returns TypeVar object or None when no parameters given ... stupid python
        # will not validate recursively, still value does match alias type though
        if len(self.hint.types) == 0 or isinstance(self.hint.types[0], TypeVar):
            return True
        hint = TypeHint(self.hint.types[0])
        # Any is always valid
        if AnyValidator().supports(hint):
            return True
        nullablevalidator = NullableValidator(hint)
        stdtypevalidator = StdtypeValidator(hint)
        classvalidator = ClassValidator(hint)
        callablevalidator = CallableValidator(hint)
        aliasvalidator = AliasValidator(hint)
        listvalidator = ListValidator(hint)
        dictvalidator = DictValidator(hint)
        unionvalidator = UnionValidator(hint)
        for value in self.value:
            if not (nullablevalidator.validate(value) or
                    stdtypevalidator.validate(value) or
                    classvalidator.validate(value) or
                    callablevalidator.validate(value) or
                    aliasvalidator.validate(value) or
                    listvalidator.validate(value) or
                    dictvalidator.validate(value) or
                    unionvalidator.validate(value)):
                return False

        return True

class UnionValidator(AbstractValidator):
    """Validate typing.Union alias
    eg: typing.Union[int, str, float] will check given values matches at least one constraint.
    nested aliases will be validated as well : typing.Union[int, typing.Dict[int, str], typing.List[str]]
    """

    def __init__(self, hint: TypeHint = None, value: Any = None) -> None:
        super().__init__(hint, value)

    @property
    def is_supported(self) -> bool:
        return isinstance(self.hint.annotation, _GenericAlias) and \
               self.hint.origin == Union
        # TypeError: typing.Union cannot be used with isinstance() ... stupid python

    @property
    def is_valid(self) -> bool:
        if self.is_supported:
            for annotation in self.hint.types:
                hint = TypeHint(annotation)
                if AnyValidator(hint, self.value) or \
                        NullableValidator(hint, self.value) or \
                        StdtypeValidator(hint, self.value) or \
                        ClassValidator(hint, self.value) or \
                        CallableValidator(hint, self.value) or \
                        AliasValidator(hint, self.value) or \
                        ListValidator(hint, self.value) or \
                        DictValidator(hint, self.value) or \
                        UnionValidator(hint, self.value):
                    return True
        return False
