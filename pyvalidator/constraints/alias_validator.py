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
)

from pyvalidator.constraints.abstract_validator import AbstractValidator
from pyvalidator.type_hint import TypeHint


class AliasValidator(AbstractValidator):
    """Validate typing aliases ; Check value matches annotation
    eg: typing.ByteString will check given value matches byte type.
    aliases parameters will be ignored : typing.Iterator[str] will not be checked recursively
    """

    valid_aliases = (
        # AttributeError: module 'typing' has no attribute 'AbstractAsyncContextManager' <- place these in the list
        # AttributeError: module 'typing' has no attribute 'AbstractContextManager' <- place these in the list
        # AttributeError: module 'contextlib' has no attribute 'AsyncContextManager'
        # AttributeError: module 'contextlib' has no attribute 'ContextManager'
        # ... stupid python
        'AbstractAsyncContextManager',
        'AbstractContextManager',
        'AbstractSet',
        'AsyncGenerator',
        'AsyncIterable',
        'AsyncIterator',
        'Awaitable',
        'ByteString',
        'ChainMap',
        'Collection',
        'Container',
        'Coroutine',
        'Counter',
        'DefaultDict',
        'Deque',
        'Generator',
        'Hashable',
        'ItemsView',
        'Iterable',
        'Iterator',
        'KeysView',
        'Mapping',
        'MappingView',
        'MutableMapping',
        'MutableSequence',
        'MutableSet',
        'OrderedDict',
        'Reversible',
        'Sequence',
        'Sized',
        'Type',
        'ValuesView',
    )

    def __init__(self, hint: TypeHint = None, value: Any = None) -> None:
        super().__init__(hint, value)

    @property
    def is_supported(self) -> bool:
        return isinstance(self.hint.annotation, _GenericAlias) and \
               self.hint.alias in self.valid_aliases

    @property
    def is_valid(self) -> bool:
        if self.is_supported:
            return self.value is self.hint.origin
        return False
