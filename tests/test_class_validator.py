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

from pyvalidator.constraints.class_validator import ClassValidator
from pyvalidator.type_hint import TypeHint


class Dummy:
    pass


class TestClassValidator(TestCase):
    class_fixtures = (
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
        Dummy,
    )

    alias_fixtures = (
        typing.AsyncContextManager,
        typing.ContextManager,
        typing.AsyncGenerator,
        typing.AsyncIterable,
        typing.AsyncIterator,
        typing.Awaitable,
        typing.ByteString,
        typing.Coroutine,
        typing.Counter,
        typing.Generator,
        typing.Hashable,
        typing.ItemsView,
        typing.Iterable,
        typing.Iterator,
        typing.KeysView,
        typing.Mapping,
        typing.MappingView,
        typing.MutableMapping,
        typing.Reversible,
        typing.Sized,
        typing.Type,
        typing.ValuesView,
        typing.AbstractSet[str],
        typing.Collection[str],
        typing.Container[str],
        typing.Deque[str],
        typing.FrozenSet[str],
        typing.List[str],
        typing.MutableSequence[str],
        typing.MutableSet[str],
        typing.Sequence[str],
        typing.Set[str],
        typing.Tuple[str],
        typing.ChainMap[int, str],
        typing.DefaultDict[int, str],
        typing.Dict[int, str],
        # typing.OrderedDict[int, str],
        typing.Union[int, str],
        typing.Optional[int],
    )

    special_fixtures = (
        typing.Any,
        typing.Callable[[int, str], str],
        typing.ClassVar,
        typing.NoReturn,
    )

    #################################################

    def test_class_validator_invalid_value_should_return_false(self):
        """==> class validator invalid value should return False"""
        for annotation in self.class_fixtures:
            self.assertFalse(ClassValidator(TypeHint(annotation), 'invalid_value'))

    def test_class_validator_valid_value_should_return_true(self):
        """==> class validator valid value should return True"""
        for annotation in self.class_fixtures:
            self.assertTrue(ClassValidator(TypeHint(annotation), annotation))

    def test_class_validator_aliases_should_return_false(self):
        """==> class validator aliases should return False"""
        for annotation in self.alias_fixtures:
            self.assertFalse(ClassValidator(TypeHint(annotation), annotation))

    def test_class_validator_special_aliases_should_return_false(self):
        """==> class validator special aliases should return False"""
        for annotation in self.special_fixtures:
            self.assertFalse(ClassValidator(TypeHint(annotation), annotation))
