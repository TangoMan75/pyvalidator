#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

import collections.abc
from unittest import TestCase

from pyvalidator.validator import Validator
from tests.dummy import Dummy


class Empty():
    def __init__(self, alias=None):
        pass


class TestValidator(TestCase):

    def setUp(self):
        self.dummy = Dummy()
        self.validator = Validator()

    ##################################################
    # Test ABC Collections
    ##################################################

    def test_validator_invalid_values_for_abc_collections_should_raise_typeerror(self):
        """==> validator invalid values for ABC collections should raise TypeError"""
        with self.assertRaises(TypeError):
            self.dummy.abc_async_generator = Empty('AsyncGenerator')
        with self.assertRaises(TypeError):
            self.dummy.abc_async_iterable = Empty('AsyncIterable')
        with self.assertRaises(TypeError):
            self.dummy.abc_async_iterator = Empty('AsyncIterator')
        with self.assertRaises(TypeError):
            self.dummy.abc_awaitable = Empty('Awaitable')
        with self.assertRaises(TypeError):
            self.dummy.abc_byte_string = Empty('ByteString')
        with self.assertRaises(TypeError):
            self.dummy.abc_callable = Empty('Callable')
        with self.assertRaises(TypeError):
            self.dummy.abc_collection = Empty('Collection')
        with self.assertRaises(TypeError):
            self.dummy.abc_container = Empty('Container')
        with self.assertRaises(TypeError):
            self.dummy.abc_coroutine = Empty('Coroutine')
        with self.assertRaises(TypeError):
            self.dummy.abc_generator = Empty('Generator')
        with self.assertRaises(TypeError):
            self.dummy.abc_hashable = Empty('Hashable')
        with self.assertRaises(TypeError):
            self.dummy.abc_items_view = Empty('ItemsView')
        with self.assertRaises(TypeError):
            self.dummy.abc_iterable = Empty('Iterable')
        with self.assertRaises(TypeError):
            self.dummy.abc_iterator = Empty('Iterator')
        with self.assertRaises(TypeError):
            self.dummy.abc_keys_view = Empty('KeysView')
        with self.assertRaises(TypeError):
            self.dummy.abc_mapping = Empty('Mapping')
        with self.assertRaises(TypeError):
            self.dummy.abc_mapping_view = Empty('MappingView')
        with self.assertRaises(TypeError):
            self.dummy.abc_mutable_mapping = Empty('MutableMapping')
        with self.assertRaises(TypeError):
            self.dummy.abc_mutable_sequence = Empty('MutableSequence')
        with self.assertRaises(TypeError):
            self.dummy.abc_mutable_set = Empty('MutableSet')
        with self.assertRaises(TypeError):
            self.dummy.abc_reversible = Empty('Reversible')
        with self.assertRaises(TypeError):
            self.dummy.abc_sequence = Empty('Sequence')
        with self.assertRaises(TypeError):
            self.dummy.abc_set = Empty('Set')
        with self.assertRaises(TypeError):
            self.dummy.abc_sized = Empty('Sized')
        with self.assertRaises(TypeError):
            self.dummy.abc_values_view = Empty('ValuesView')

    def test_validator_valid_values_for_abc_collections_should_not_raise_exception(self):
        """==> validator valid values for ABC collections should not raise Exception"""
        try:
            self.dummy.abc_async_generator = collections.abc.AsyncGenerator
            self.dummy.abc_async_iterable = collections.abc.AsyncIterable
            self.dummy.abc_async_iterator = collections.abc.AsyncIterator
            self.dummy.abc_awaitable = collections.abc.Awaitable
            self.dummy.abc_byte_string = collections.abc.ByteString
            self.dummy.abc_callable = collections.abc.Callable
            self.dummy.abc_collection = collections.abc.Collection
            self.dummy.abc_container = collections.abc.Container
            self.dummy.abc_coroutine = collections.abc.Coroutine
            self.dummy.abc_generator = collections.abc.Generator
            self.dummy.abc_hashable = collections.abc.Hashable
            self.dummy.abc_items_view = collections.abc.ItemsView
            self.dummy.abc_iterable = collections.abc.Iterable
            self.dummy.abc_iterator = collections.abc.Iterator
            self.dummy.abc_keys_view = collections.abc.KeysView
            self.dummy.abc_mapping = collections.abc.Mapping
            self.dummy.abc_mapping_view = collections.abc.MappingView
            self.dummy.abc_mutable_mapping = collections.abc.MutableMapping
            self.dummy.abc_mutable_sequence = collections.abc.MutableSequence
            self.dummy.abc_mutable_set = collections.abc.MutableSet
            self.dummy.abc_reversible = collections.abc.Reversible
            self.dummy.abc_sequence = collections.abc.Sequence
            self.dummy.abc_set = collections.abc.Set
            self.dummy.abc_sized = collections.abc.Sized
            self.dummy.abc_values_view = collections.abc.ValuesView
        except Exception as e:
            self.fail(e)

    def test_validator_nullable_properties_for_abc_collection_should_not_raise_valueerror(self):
        """==> validator nullable properties for abc collection should not raise ValueError"""
        try:
            self.dummy.nullable_abc_async_generator = None
            self.dummy.nullable_abc_async_iterable = None
            self.dummy.nullable_abc_async_iterator = None
            self.dummy.nullable_abc_awaitable = None
            self.dummy.nullable_abc_byte_string = None
            self.dummy.nullable_abc_callable = None
            self.dummy.nullable_abc_collection = None
            self.dummy.nullable_abc_container = None
            self.dummy.nullable_abc_coroutine = None
            self.dummy.nullable_abc_generator = None
            self.dummy.nullable_abc_hashable = None
            self.dummy.nullable_abc_items_view = None
            self.dummy.nullable_abc_iterable = None
            self.dummy.nullable_abc_iterator = None
            self.dummy.nullable_abc_keys_view = None
            self.dummy.nullable_abc_mapping = None
            self.dummy.nullable_abc_mapping_view = None
            self.dummy.nullable_abc_mutable_mapping = None
            self.dummy.nullable_abc_mutable_sequence = None
            self.dummy.nullable_abc_mutable_set = None
            self.dummy.nullable_abc_reversible = None
            self.dummy.nullable_abc_sequence = None
            self.dummy.nullable_abc_set = None
            self.dummy.nullable_abc_sized = None
            self.dummy.nullable_abc_values_view = None
        except Exception as e:
            self.fail(e)

    ##################################################
    # Test Builtin Types
    ##################################################

    def test_validator_invalid_values_for_stdtype_should_raise_typeerror(self):
        """==> invalid values for stdtype should raise TypeError"""
        with self.assertRaises(TypeError):
            self.dummy.stdtype_bytearray = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.stdtype_bytes = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.stdtype_complex = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.stdtype_dict = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.stdtype_float = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.stdtype_frozenset = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.stdtype_int = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.stdtype_list = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.stdtype_memoryview = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.stdtype_range = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.stdtype_set = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.stdtype_str = ['invalid_type']
        with self.assertRaises(TypeError):
            self.dummy.stdtype_tuple = 'invalid_type'

    def test_validator_valid_stdtype_values_should_not_raise_exception(self):
        """==> valid stdtype values should not raise exception"""
        try:
            self.dummy.stdtype_bool = True
            self.dummy.stdtype_bytearray = bytearray(b'bytearray')
            self.dummy.stdtype_bytes = b'bytes'
            self.dummy.stdtype_complex = 1j
            self.dummy.stdtype_dict = {'Dictionary': True}
            self.dummy.stdtype_float = 1.1
            self.dummy.stdtype_frozenset = frozenset({1, 2, 3})
            self.dummy.stdtype_int = 666
            self.dummy.stdtype_list = ['List']
            self.dummy.stdtype_memoryview = memoryview(b'')
            self.dummy.stdtype_range = range(1, 10)
            self.dummy.stdtype_set = {1, 2, 3}
            self.dummy.stdtype_str = 'String'
            self.dummy.stdtype_tuple = ('Tuple',)
            self.dummy.stdtype_type = type
        except Exception as e:
            self.fail(e)

    def test_validator_nullable_properties_for_stdtype_should_not_raise_valueerror(self):
        """==> validator nullable properties for stdtype should not raise ValueError"""
        try:
            self.dummy.nullable_stdtype_bool = None
            self.dummy.nullable_stdtype_bytearray = None
            self.dummy.nullable_stdtype_bytes = None
            self.dummy.nullable_stdtype_complex = None
            self.dummy.nullable_stdtype_dict = None
            self.dummy.nullable_stdtype_float = None
            self.dummy.nullable_stdtype_frozenset = None
            self.dummy.nullable_stdtype_int = None
            self.dummy.nullable_stdtype_list = None
            self.dummy.nullable_stdtype_range = None
            self.dummy.nullable_stdtype_set = None
            self.dummy.nullable_stdtype_str = None
            self.dummy.nullable_stdtype_tuple = None
            self.dummy.nullable_stdtype_type = None
        except Exception as e:
            self.fail(e)

    def test_validator_invalid_values_in_nullable_properties_should_raise_typeerror(self):
        """==> invalid values in nullable properties should raise TypeError"""
        with self.assertRaises(TypeError):
            self.dummy.nullable_stdtype_bytearray = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.nullable_stdtype_bytes = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.nullable_stdtype_complex = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.nullable_stdtype_dict = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.nullable_stdtype_float = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.nullable_stdtype_frozenset = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.nullable_stdtype_int = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.nullable_stdtype_list = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.nullable_stdtype_memoryview = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.nullable_stdtype_range = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.nullable_stdtype_set = 'invalid_type'
        with self.assertRaises(TypeError):
            self.dummy.nullable_stdtype_str = ['invalid_type']
        with self.assertRaises(TypeError):
            self.dummy.nullable_stdtype_tuple = 'invalid_type'

    def test_validator_non_nullable_properties_should_raise_typeerror(self):
        """==> non-nullable properties should raise TypeError"""
        with self.assertRaises(TypeError):
            self.dummy.stdtype_bytearray = None
        with self.assertRaises(TypeError):
            self.dummy.stdtype_bytes = None
        with self.assertRaises(TypeError):
            self.dummy.stdtype_complex = None
        with self.assertRaises(TypeError):
            self.dummy.stdtype_dict = None
        with self.assertRaises(TypeError):
            self.dummy.stdtype_float = None
        with self.assertRaises(TypeError):
            self.dummy.stdtype_frozenset = None
        with self.assertRaises(TypeError):
            self.dummy.stdtype_int = None
        with self.assertRaises(TypeError):
            self.dummy.stdtype_list = None
        with self.assertRaises(TypeError):
            self.dummy.stdtype_memoryview = None
        with self.assertRaises(TypeError):
            self.dummy.stdtype_range = None
        with self.assertRaises(TypeError):
            self.dummy.stdtype_set = None
        with self.assertRaises(TypeError):
            self.dummy.stdtype_str = None
        with self.assertRaises(TypeError):
            self.dummy.stdtype_tuple = None

    ##################################################
    # Test Aliases
    ##################################################

    def test_validator_invalid_values_for_alias_should_raise_typeerror(self):
        """==> invalid values for alias should raise TypeError"""
        with self.assertRaises(TypeError):
            self.dummy.typing_async_generator = Empty('AsyncGenerator')
        with self.assertRaises(TypeError):
            self.dummy.typing_async_iterable = Empty('AsyncIterable')
        with self.assertRaises(TypeError):
            self.dummy.typing_async_iterator = Empty('AsyncIterator')
        with self.assertRaises(TypeError):
            self.dummy.typing_abstract_set = Empty('AbstractSet')
        with self.assertRaises(TypeError):
            self.dummy.typing_async_context_manager = Empty('AsyncContextManager')
        with self.assertRaises(TypeError):
            self.dummy.typing_awaitable = Empty('Awaitable')
        with self.assertRaises(TypeError):
            self.dummy.typing_byte_string = Empty('ByteString')
        with self.assertRaises(TypeError):
            self.dummy.typing_callable = Empty('Callable')
        with self.assertRaises(TypeError):
            self.dummy.typing_chain_map = Empty('ChainMap')
        with self.assertRaises(TypeError):
            self.dummy.typing_collection = Empty('Collection')
        with self.assertRaises(TypeError):
            self.dummy.typing_container = Empty('Container')
        with self.assertRaises(TypeError):
            self.dummy.typing_context_manager = Empty('ContextManager')
        with self.assertRaises(TypeError):
            self.dummy.typing_coroutine = Empty('Coroutine')
        with self.assertRaises(TypeError):
            self.dummy.typing_counter = Empty('Counter')
        with self.assertRaises(TypeError):
            self.dummy.typing_default_dict = Empty('DefaultDict')
        with self.assertRaises(TypeError):
            self.dummy.typing_deque = Empty('Deque')
        with self.assertRaises(TypeError):
            self.dummy.typing_dict = Empty('Dict')
        with self.assertRaises(TypeError):
            self.dummy.typing_frozen_set = Empty('FrozenSet')
        with self.assertRaises(TypeError):
            self.dummy.typing_generator = Empty('Generator')
        with self.assertRaises(TypeError):
            self.dummy.typing_hashable = Empty('Hashable')
        with self.assertRaises(TypeError):
            self.dummy.typing_items_view = Empty('ItemsView')
        with self.assertRaises(TypeError):
            self.dummy.typing_iterable = Empty('Iterable')
        with self.assertRaises(TypeError):
            self.dummy.typing_iterator = Empty('Iterator')
        with self.assertRaises(TypeError):
            self.dummy.typing_keys_view = Empty('KeysView')
        with self.assertRaises(TypeError):
            self.dummy.typing_list = Empty('List')
        with self.assertRaises(TypeError):
            self.dummy.typing_mapping = Empty('Mapping')
        with self.assertRaises(TypeError):
            self.dummy.typing_mapping_view = Empty('MappingView')
        with self.assertRaises(TypeError):
            self.dummy.typing_mutable_mapping = Empty('MutableMapping')
        with self.assertRaises(TypeError):
            self.dummy.typing_mutable_sequence = Empty('MutableSequence')
        with self.assertRaises(TypeError):
            self.dummy.typing_mutable_set = Empty('MutableSet')
        with self.assertRaises(TypeError):
            self.dummy.typing_ordered_dict = Empty('OrderedDict')
        with self.assertRaises(TypeError):
            self.dummy.typing_reversible = Empty('Reversible')
        with self.assertRaises(TypeError):
            self.dummy.typing_sequence = Empty('Sequence')
        with self.assertRaises(TypeError):
            self.dummy.typing_set = Empty('Set')
        with self.assertRaises(TypeError):
            self.dummy.typing_sized = Empty('Sized')
        with self.assertRaises(TypeError):
            self.dummy.typing_tuple = Empty('Tuple')
        with self.assertRaises(TypeError):
            self.dummy.typing_type = Empty('Type')
        with self.assertRaises(TypeError):
            self.dummy.typing_values_view = Empty('ValuesView')

    def test_validator_nullable_properties_for_aliases_should_not_raise_valueerror(self):
        """==> validator nullable properties for aliases should not raise ValueError"""
        try:
            self.dummy.nullable_abstract_set = None
            self.dummy.nullable_any = None
            self.dummy.nullable_async_context_manager = None
            self.dummy.nullable_async_generator = None
            self.dummy.nullable_async_iterable = None
            self.dummy.nullable_async_iterator = None
            self.dummy.nullable_awaitable = None
            self.dummy.nullable_byte_string = None
            self.dummy.nullable_callable = None
            self.dummy.nullable_chain_map = None
            self.dummy.nullable_collection = None
            self.dummy.nullable_container = None
            self.dummy.nullable_context_manager = None
            self.dummy.nullable_coroutine = None
            self.dummy.nullable_counter = None
            self.dummy.nullable_default_dict = None
            self.dummy.nullable_deque = None
            self.dummy.nullable_dict = None
            self.dummy.nullable_frozen_set = None
            self.dummy.nullable_generator = None
            self.dummy.nullable_hashable = None
            self.dummy.nullable_items_view = None
            self.dummy.nullable_iterable = None
            self.dummy.nullable_iterator = None
            self.dummy.nullable_keys_view = None
            self.dummy.nullable_list = None
            self.dummy.nullable_mapping = None
            self.dummy.nullable_mapping_view = None
            self.dummy.nullable_mutable_mapping = None
            self.dummy.nullable_mutable_sequence = None
            self.dummy.nullable_mutable_set = None
            self.dummy.nullable_ordered_dict = None
            self.dummy.nullable_reversible = None
            self.dummy.nullable_sequence = None
            self.dummy.nullable_set = None
            self.dummy.nullable_sized = None
            self.dummy.nullable_tuple = None
            self.dummy.nullable_type = None
            self.dummy.nullable_values_view = None
        except Exception as e:
            self.fail(e)
