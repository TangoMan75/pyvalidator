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
import contextlib
import typing
from unittest import TestCase

from pyvalidator.constraints.alias_validator import AliasValidator
from pyvalidator.type_hint import TypeHint


class TestAliasValidator(TestCase):
    alias_fixtures = (
        {'alias': 'ChainMap',    'annotation': typing.ChainMap[int, str],    'category': typing._GenericAlias, 'origin': collections.ChainMap},
        {'alias': 'Counter',     'annotation': typing.Counter[str],          'category': typing._GenericAlias, 'origin': collections.Counter},
        {'alias': 'DefaultDict', 'annotation': typing.DefaultDict[int, str], 'category': typing._GenericAlias, 'origin': collections.defaultdict},
        {'alias': 'Deque',       'annotation': typing.Deque[str],            'category': typing._GenericAlias, 'origin': collections.deque},
        {'alias': 'ItemsView',   'annotation': typing.ItemsView[int, str],   'category': typing._GenericAlias, 'origin': collections.abc.ItemsView},
        {'alias': 'KeysView',    'annotation': typing.KeysView[str],         'category': typing._GenericAlias, 'origin': collections.abc.KeysView},
        {'alias': 'MappingView', 'annotation': typing.MappingView[str],      'category': typing._GenericAlias, 'origin': collections.abc.MappingView},
        # {'alias': 'OrderedDict', 'annotation': typing.OrderedDict[int, str], 'category': typing._GenericAlias, 'origin': collections.OrderedDict},
        {'alias': 'Type',        'annotation': typing.Type[str],             'category': typing._GenericAlias, 'origin': type},
        {'alias': 'ValuesView',  'annotation': typing.ValuesView[str],       'category': typing._GenericAlias, 'origin': collections.abc.ValuesView},
    )

    alias_no_argument_fixtures = (
        {'alias': 'AbstractSet',        'annotation': typing.AbstractSet[str],           'category': typing._GenericAlias, 'origin': collections.abc.Set},
        {'alias': 'AsyncContextManager','annotation': typing.AsyncContextManager[str],   'category': typing._GenericAlias, 'origin': contextlib.AbstractAsyncContextManager},
        {'alias': 'AsyncGenerator',     'annotation': typing.AsyncGenerator[int, str],   'category': typing._GenericAlias, 'origin': collections.abc.AsyncGenerator},
        {'alias': 'AsyncIterable',      'annotation': typing.AsyncIterable[str],         'category': typing._GenericAlias, 'origin': collections.abc.AsyncIterable},
        {'alias': 'AsyncIterator',      'annotation': typing.AsyncIterator[str],         'category': typing._GenericAlias, 'origin': collections.abc.AsyncIterator},
        {'alias': 'Awaitable',          'annotation': typing.Awaitable[str],             'category': typing._GenericAlias, 'origin': collections.abc.Awaitable},
        {'alias': 'ByteString',         'annotation': typing.ByteString,                 'category': typing._GenericAlias, 'origin': collections.abc.ByteString,},
        {'alias': 'Collection',         'annotation': typing.Collection[str],            'category': typing._GenericAlias, 'origin': collections.abc.Collection},
        {'alias': 'Container',          'annotation': typing.Container[str],             'category': typing._GenericAlias, 'origin': collections.abc.Container},
        {'alias': 'ContextManager',     'annotation': typing.ContextManager[str],        'category': typing._GenericAlias, 'origin': contextlib.AbstractContextManager},
        {'alias': 'Coroutine',          'annotation': typing.Coroutine[int, str, float], 'category': typing._GenericAlias, 'origin': collections.abc.Coroutine},
        {'alias': 'Generator',          'annotation': typing.Generator[int, str, float], 'category': typing._GenericAlias, 'origin': collections.abc.Generator},
        {'alias': 'Hashable',           'annotation': typing.Hashable,                   'category': typing._GenericAlias, 'origin': collections.abc.Hashable,},
        {'alias': 'Iterable',           'annotation': typing.Iterable[str],              'category': typing._GenericAlias, 'origin': collections.abc.Iterable},
        {'alias': 'Iterator',           'annotation': typing.Iterator[str],              'category': typing._GenericAlias, 'origin': collections.abc.Iterator},
        {'alias': 'Mapping',            'annotation': typing.Mapping[int, str],          'category': typing._GenericAlias, 'origin': collections.abc.Mapping},
        {'alias': 'MutableMapping',     'annotation': typing.MutableMapping[int, str],   'category': typing._GenericAlias, 'origin': collections.abc.MutableMapping},
        {'alias': 'MutableSequence',    'annotation': typing.MutableSequence[str],       'category': typing._GenericAlias, 'origin': collections.abc.MutableSequence},
        {'alias': 'MutableSet',         'annotation': typing.MutableSet[str],            'category': typing._GenericAlias, 'origin': collections.abc.MutableSet},
        {'alias': 'Reversible',         'annotation': typing.Reversible[str],            'category': typing._GenericAlias, 'origin': collections.abc.Reversible},
        {'alias': 'Sequence',           'annotation': typing.Sequence[str],              'category': typing._GenericAlias, 'origin': collections.abc.Sequence},
        {'alias': 'Sized',              'annotation': typing.Sized,                      'category': typing._GenericAlias, 'origin': collections.abc.Sized,},
    )

    # these "_SpecialForm" are just here for reference, they are not handled
    special_form_fixtures = (
        {'alias': 'ClassVar', 'annotation': typing.ClassVar, 'category': typing._SpecialForm, 'origin': None},
        {'alias': 'NoReturn', 'annotation': typing.NoReturn, 'category': typing._SpecialForm, 'origin': None},
    )

    #################################################

    def test_alias_validator_invalid_value_should_return_false(self):
        """==> alias validator invalid value should return False"""
        for item in self.alias_fixtures:
            hint = TypeHint(item.get('annotation'))
            validator = AliasValidator(hint, None)
            self.assertFalse(validator)

    def test_alias_validator_invalid_value_should_return_false(self):
        """==> alias validator invalid value should return False"""
        for item in self.alias_no_argument_fixtures:
            # seems like every object is hashable ... stupid python
            if item.get('alias') != 'Hashable':
                hint = TypeHint(item.get('annotation'))
                validator = AliasValidator(hint, None)
                self.assertFalse(validator)

    def test_alias_validator_valid_value_should_return_true(self):
        """==> alias validator valid value should return True"""
        for item in self.alias_fixtures:
            hint = TypeHint(item.get('annotation'))
            validator = AliasValidator(hint, item.get('origin'))
            self.assertTrue(validator)

    def test_alias_validator_valid_value_should_return_true(self):
        """==> alias validator valid value should return True"""
        for item in self.alias_no_argument_fixtures:
            hint = TypeHint(item.get('annotation'))
            validator = AliasValidator(hint, item.get('origin'))
            self.assertTrue(validator)
