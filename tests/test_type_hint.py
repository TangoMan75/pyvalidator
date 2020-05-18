#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

# AttributeError: module 'typing' has no attribute 'OrderedDict'
# https://github.com/python/mypy/issues/6904

import collections.abc
import typing
from unittest import TestCase

from pyvalidator import TypeHint


class TestTypeHint(TestCase):

    stdtypes_fixtures = (
        bool,
        bytearray,
        bytes,
        complex,
        dict,
        float,
        frozenset,
        int,
        list,
        memoryview,
        object,
        range,
        set,
        str,
        tuple,
        type,
    )

    typing_aliases_fixtures = (
        typing.AsyncContextManager,
        typing.ContextManager,
        typing.AbstractSet[str],
        typing.AsyncGenerator,
        typing.AsyncIterable,
        typing.AsyncIterator,
        typing.Awaitable,
        typing.ByteString,
        typing.ChainMap[int, str],
        typing.Collection[str],
        typing.Container[str],
        typing.Coroutine,
        typing.Counter,
        typing.DefaultDict[int, str],
        typing.Deque[str],
        typing.Dict[int, str],
        typing.FrozenSet[str],
        typing.Generator,
        typing.Hashable,
        typing.ItemsView,
        typing.Iterable,
        typing.Iterator,
        typing.KeysView,
        typing.List[str],
        typing.Mapping,
        typing.MappingView,
        typing.MutableMapping,
        typing.MutableSequence[str],
        typing.MutableSet[str],
        # typing.OrderedDict[int, str],
        typing.Reversible,
        typing.Sequence[str],
        typing.Set[str],
        typing.Sized,
        typing.Tuple[str],
        typing.Type,
        typing.ValuesView,
        typing.Any,                       
        typing.Callable[[int, str], str], 
    )

    special_aliases_fixtures = (
        typing.Any,
        typing.ClassVar,
        typing.NoReturn,
        typing.Optional[str],
        typing.Union[int, str, None],     
    )

    collections_abc_fixtures = (
        collections.abc.AsyncGenerator,
        collections.abc.AsyncIterable,
        collections.abc.AsyncIterator,
        collections.abc.Awaitable,
        collections.abc.ByteString,
        collections.abc.Callable,
        collections.abc.Collection,
        collections.abc.Container,
        collections.abc.Coroutine,
        collections.abc.Generator,
        collections.abc.Hashable,
        collections.abc.ItemsView,
        collections.abc.Iterable,
        collections.abc.Iterator,
        collections.abc.KeysView,
        collections.abc.Mapping,
        collections.abc.MappingView,
        collections.abc.MutableMapping,
        collections.abc.MutableSequence,
        collections.abc.MutableSet,
        collections.abc.Reversible,
        collections.abc.Sequence,
        collections.abc.Set,
        collections.abc.Sized,
        collections.abc.ValuesView,
    )

    #################################################
    # Test Constructor
    #################################################

    def test_type_hint_constructor_ValueError(self):
        """==> invalid value should raise ValueError"""
        with self.assertRaises(ValueError):
            TypeHint('')

    #################################################
    # Test Setter
    #################################################

    def test_type_hint_setter(self):
        """==> setting type hint should not raise Exception"""
        try:
            for annotation in self.stdtypes_fixtures:
                TypeHint(annotation)

            for annotation in self.collections_abc_fixtures:
                TypeHint(annotation)

            for annotation in self.typing_aliases_fixtures:
                TypeHint(annotation)

            for annotation in self.special_aliases_fixtures:
                TypeHint(annotation)
        except Exception as e:
            self.fail(e)
