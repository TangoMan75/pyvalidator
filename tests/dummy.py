#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

import collections.abc
import typing
from collections import OrderedDict

from pyvalidator.validator import Validator


class Dummy(Validator):

    def __init__(self):
        # collections.abc.AsyncGenerator
        self._abc_async_generator = None
        self._nullable_abc_async_generator = None
        # collections.abc.AsyncIterable
        self._abc_async_iterable = None
        self._nullable_abc_async_iterable = None
        # collections.abc.AsyncIterator
        self._abc_async_iterator = None
        self._nullable_abc_async_iterator = None
        # collections.abc.Awaitable
        self._abc_awaitable = None
        self._nullable_abc_awaitable = None
        # collections.abc.ByteString
        self._abc_byte_string = None
        self._nullable_abc_byte_string = None
        # collections.abc.Callable
        self._abc_callable = None
        self._nullable_abc_callable = None
        # collections.abc.Collection
        self._abc_collection = None
        self._nullable_abc_collection = None
        # collections.abc.Container
        self._abc_container = None
        self._nullable_abc_container = None
        # collections.abc.Coroutine
        self._abc_coroutine = None
        self._nullable_abc_coroutine = None
        # collections.abc.Generator
        self._abc_generator = None
        self._nullable_abc_generator = None
        # collections.abc.Hashable
        self._abc_hashable = None
        self._nullable_abc_hashable = None
        # collections.abc.ItemsView
        self._abc_items_view = None
        self._nullable_abc_items_view = None
        # collections.abc.Iterable
        self._abc_iterable = None
        self._nullable_abc_iterable = None
        # collections.abc.Iterator
        self._abc_iterator = None
        self._nullable_abc_iterator = None
        # collections.abc.KeysView
        self._abc_keys_view = None
        self._nullable_abc_keys_view = None
        # collections.abc.Mapping
        self._abc_mapping = None
        self._nullable_abc_mapping = None
        # collections.abc.MappingView
        self._abc_mapping_view = None
        self._nullable_abc_mapping_view = None
        # collections.abc.MutableMapping
        self._abc_mutable_mapping = None
        self._nullable_abc_mutable_mapping = None
        # collections.abc.MutableSequence
        self._abc_mutable_sequence = None
        self._nullable_abc_mutable_sequence = None
        # collections.abc.MutableSet
        self._abc_mutable_set = None
        self._nullable_abc_mutable_set = None
        # collections.abc.Reversible
        self._abc_reversible = None
        self._nullable_abc_reversible = None
        # collections.abc.Sequence
        self._abc_sequence = None
        self._nullable_abc_sequence = None
        # collections.abc.Set
        self._abc_set = None
        self._nullable_abc_set = None
        # collections.abc.Sized
        self._abc_sized = None
        self._nullable_abc_sized = None
        # collections.abc.ValuesView
        self._abc_values_view = None
        self._nullable_abc_values_view = None
        # bool
        self._stdtype_bool = None
        self._nullable_stdtype_bool = None
        # bytearray
        self._stdtype_bytearray = None
        self._nullable_stdtype_bytearray = None
        # bytes
        self._stdtype_bytes = None
        self._nullable_stdtype_bytes = None
        # complex
        self._stdtype_complex = None
        self._nullable_stdtype_complex = None
        # dict
        self._stdtype_dict = None
        self._nullable_stdtype_dict = None
        # float
        self._stdtype_float = None
        self._nullable_stdtype_float = None
        # frozenset
        self._stdtype_frozenset = None
        self._nullable_stdtype_frozenset = None
        # int
        self._stdtype_int = None
        self._nullable_stdtype_int = None
        # list
        self._stdtype_list = None
        self._nullable_stdtype_list = None
        # memoryview
        self._stdtype_memoryview = None
        self._nullable_stdtype_memoryview = None
        # range
        self._stdtype_range = None
        self._nullable_stdtype_range = None
        # set
        self._stdtype_set = None
        self._nullable_stdtype_set = None
        # str
        self._stdtype_str = None
        self._nullable_stdtype_str = None
        # tuple
        self._stdtype_tuple = None
        self._nullable_stdtype_tuple = None
        # type
        self._stdtype_type = None
        self._nullable_stdtype_type = None
        # typing.AbstractSet
        self._typing_abstract_set = None
        self._nullable_typing_abstract_set = None
        # typing.AsyncContextManager
        self._typing_async_context_manager = None
        self._nullable_typing_async_context_manager = None
        # typing.AsyncGenerator
        self._typing_async_generator = None
        self._nullable_typing_async_generator = None
        # typing.AsyncIterable
        self._typing_async_iterable = None
        self._nullable_typing_async_iterable = None
        # typing.AsyncIterator
        self._typing_async_iterator = None
        self._nullable_typing_async_iterator = None
        # typing.Awaitable
        self._typing_awaitable = None
        self._nullable_typing_awaitable = None
        # typing.ByteString
        self._typing_byte_string = None
        self._nullable_typing_byte_string = None
        # typing.Callable
        self._typing_callable = None
        self._nullable_typing_callable = None
        # typing.ChainMap
        self._typing_chain_map = None
        self._nullable_typing_chain_map = None
        # typing.Collection
        self._typing_collection = None
        self._nullable_typing_collection = None
        # typing.Container
        self._typing_container = None
        self._nullable_typing_container = None
        # typing.ContextManager
        self._typing_context_manager = None
        self._nullable_typing_context_manager = None
        # typing.Coroutine
        self._typing_coroutine = None
        self._nullable_typing_coroutine = None
        # typing.Counter
        self._typing_counter = None
        self._nullable_typing_counter = None
        # typing.DefaultDict
        self._typing_default_dict = None
        self._nullable_typing_default_dict = None
        # typing.Deque
        self._typing_deque = None
        self._nullable_typing_deque = None
        # typing.Dict
        self._typing_dict = None
        self._nullable_typing_dict = None
        # typing.FrozenSet
        self._typing_frozen_set = None
        self._nullable_typing_frozen_set = None
        # typing.Generator
        self._typing_generator = None
        self._nullable_typing_generator = None
        # typing.Hashable
        self._typing_hashable = None
        self._nullable_typing_hashable = None
        # typing.ItemsView
        self._typing_items_view = None
        self._nullable_typing_items_view = None
        # typing.Iterable
        self._typing_iterable = None
        self._nullable_typing_iterable = None
        # typing.Iterator
        self._typing_iterator = None
        self._nullable_typing_iterator = None
        # typing.KeysView
        self._typing_keys_view = None
        self._nullable_typing_keys_view = None
        # typing.List
        self._typing_list = None
        self._nullable_typing_list = None
        # typing.Mapping
        self._typing_mapping = None
        self._nullable_typing_mapping = None
        # typing.MappingView
        self._typing_mapping_view = None
        self._nullable_typing_mapping_view = None
        # typing.MutableMapping
        self._typing_mutable_mapping = None
        self._nullable_typing_mutable_mapping = None
        # typing.MutableSequence
        self._typing_mutable_sequence = None
        self._nullable_typing_mutable_sequence = None
        # typing.MutableSet
        self._typing_mutable_set = None
        self._nullable_typing_mutable_set = None
        # typing.OrderedDict
        self._typing_ordered_dict = None
        self._nullable_typing_ordered_dict = None
        # typing.Reversible
        self._typing_reversible = None
        self._nullable_typing_reversible = None
        # typing.Sequence
        self._typing_sequence = None
        self._nullable_typing_sequence = None
        # typing.Set
        self._typing_set = None
        self._nullable_typing_set = None
        # typing.Sized
        self._typing_sized = None
        self._nullable_typing_sized = None
        # typing.Tuple
        self._typing_tuple = None
        self._nullable_typing_tuple = None
        # typing.Type
        self._typing_type = None
        self._nullable_typing_type = None
        # typing.ValuesView
        self._typing_values_view = None
        self._nullable_typing_values_view = None

    ##################################################
    # abc_async_generator Setter / Getter
    ##################################################

    @property
    def abc_async_generator(self) -> collections.abc.AsyncGenerator:
        return self._abc_async_generator

    @abc_async_generator.setter
    @Validator.type_check
    def abc_async_generator(self, abc_async_generator_: collections.abc.AsyncGenerator) -> None:
        self._abc_async_generator = abc_async_generator_

    ##################################################
    # nullable_abc_async_generator Setter / Getter
    ##################################################

    @property
    def nullable_abc_async_generator(self) -> typing.Optional[collections.abc.AsyncGenerator]:
        return self._nullable_abc_async_generator

    @nullable_abc_async_generator.setter
    @Validator.type_check
    def nullable_abc_async_generator(self, nullable_abc_async_generator_: typing.Optional[collections.abc.AsyncGenerator]) -> None:
        self._nullable_abc_async_generator = nullable_abc_async_generator_

    ##################################################
    # abc_async_iterable Setter / Getter
    ##################################################

    @property
    def abc_async_iterable(self) -> collections.abc.AsyncIterable:
        return self._abc_async_iterable

    @abc_async_iterable.setter
    @Validator.type_check
    def abc_async_iterable(self, abc_async_iterable_: collections.abc.AsyncIterable) -> None:
        self._abc_async_iterable = abc_async_iterable_

    ##################################################
    # nullable_abc_async_iterable Setter / Getter
    ##################################################

    @property
    def nullable_abc_async_iterable(self) -> typing.Optional[collections.abc.AsyncIterable]:
        return self._nullable_abc_async_iterable

    @nullable_abc_async_iterable.setter
    @Validator.type_check
    def nullable_abc_async_iterable(self, nullable_abc_async_iterable_: typing.Optional[collections.abc.AsyncIterable]) -> None:
        self._nullable_abc_async_iterable = nullable_abc_async_iterable_

    ##################################################
    # abc_async_iterator Setter / Getter
    ##################################################

    @property
    def abc_async_iterator(self) -> collections.abc.AsyncIterator:
        return self._abc_async_iterator

    @abc_async_iterator.setter
    @Validator.type_check
    def abc_async_iterator(self, abc_async_iterator_: collections.abc.AsyncIterator) -> None:
        self._abc_async_iterator = abc_async_iterator_

    ##################################################
    # nullable_abc_async_iterator Setter / Getter
    ##################################################

    @property
    def nullable_abc_async_iterator(self) -> typing.Optional[collections.abc.AsyncIterator]:
        return self._nullable_abc_async_iterator

    @nullable_abc_async_iterator.setter
    @Validator.type_check
    def nullable_abc_async_iterator(self, nullable_abc_async_iterator_: typing.Optional[collections.abc.AsyncIterator]) -> None:
        self._nullable_abc_async_iterator = nullable_abc_async_iterator_

    ##################################################
    # abc_awaitable Setter / Getter
    ##################################################

    @property
    def abc_awaitable(self) -> collections.abc.Awaitable:
        return self._abc_awaitable

    @abc_awaitable.setter
    @Validator.type_check
    def abc_awaitable(self, abc_awaitable_: collections.abc.Awaitable) -> None:
        self._abc_awaitable = abc_awaitable_

    ##################################################
    # nullable_abc_awaitable Setter / Getter
    ##################################################

    @property
    def nullable_abc_awaitable(self) -> typing.Optional[collections.abc.Awaitable]:
        return self._nullable_abc_awaitable

    @nullable_abc_awaitable.setter
    @Validator.type_check
    def nullable_abc_awaitable(self, nullable_abc_awaitable_: typing.Optional[collections.abc.Awaitable]) -> None:
        self._nullable_abc_awaitable = nullable_abc_awaitable_

    ##################################################
    # abc_byte_string Setter / Getter
    ##################################################

    @property
    def abc_byte_string(self) -> collections.abc.ByteString:
        return self._abc_byte_string

    @abc_byte_string.setter
    @Validator.type_check
    def abc_byte_string(self, abc_byte_string_: collections.abc.ByteString) -> None:
        self._abc_byte_string = abc_byte_string_

    ##################################################
    # nullable_abc_byte_string Setter / Getter
    ##################################################

    @property
    def nullable_abc_byte_string(self) -> typing.Optional[collections.abc.ByteString]:
        return self._nullable_abc_byte_string

    @nullable_abc_byte_string.setter
    @Validator.type_check
    def nullable_abc_byte_string(self, nullable_abc_byte_string_: typing.Optional[collections.abc.ByteString]) -> None:
        self._nullable_abc_byte_string = nullable_abc_byte_string_

    ##################################################
    # abc_callable Setter / Getter
    ##################################################

    @property
    def abc_callable(self) -> collections.abc.Callable:
        return self._abc_callable

    @abc_callable.setter
    @Validator.type_check
    def abc_callable(self, abc_callable_: collections.abc.Callable) -> None:
        self._abc_callable = abc_callable_

    ##################################################
    # nullable_abc_callable Setter / Getter
    ##################################################

    @property
    def nullable_abc_callable(self) -> typing.Optional[collections.abc.Callable]:
        return self._nullable_abc_callable

    @nullable_abc_callable.setter
    @Validator.type_check
    def nullable_abc_callable(self, nullable_abc_callable_: typing.Optional[collections.abc.Callable]) -> None:
        self._nullable_abc_callable = nullable_abc_callable_

    ##################################################
    # abc_collection Setter / Getter
    ##################################################

    @property
    def abc_collection(self) -> collections.abc.Collection:
        return self._abc_collection

    @abc_collection.setter
    @Validator.type_check
    def abc_collection(self, abc_collection_: collections.abc.Collection) -> None:
        self._abc_collection = abc_collection_

    ##################################################
    # nullable_abc_collection Setter / Getter
    ##################################################

    @property
    def nullable_abc_collection(self) -> typing.Optional[collections.abc.Collection]:
        return self._nullable_abc_collection

    @nullable_abc_collection.setter
    @Validator.type_check
    def nullable_abc_collection(self, nullable_abc_collection_: typing.Optional[collections.abc.Collection]) -> None:
        self._nullable_abc_collection = nullable_abc_collection_

    ##################################################
    # abc_container Setter / Getter
    ##################################################

    @property
    def abc_container(self) -> collections.abc.Container:
        return self._abc_container

    @abc_container.setter
    @Validator.type_check
    def abc_container(self, abc_container_: collections.abc.Container) -> None:
        self._abc_container = abc_container_

    ##################################################
    # nullable_abc_container Setter / Getter
    ##################################################

    @property
    def nullable_abc_container(self) -> typing.Optional[collections.abc.Container]:
        return self._nullable_abc_container

    @nullable_abc_container.setter
    @Validator.type_check
    def nullable_abc_container(self, nullable_abc_container_: typing.Optional[collections.abc.Container]) -> None:
        self._nullable_abc_container = nullable_abc_container_

    ##################################################
    # abc_coroutine Setter / Getter
    ##################################################

    @property
    def abc_coroutine(self) -> collections.abc.Coroutine:
        return self._abc_coroutine

    @abc_coroutine.setter
    @Validator.type_check
    def abc_coroutine(self, abc_coroutine_: collections.abc.Coroutine) -> None:
        self._abc_coroutine = abc_coroutine_

    ##################################################
    # nullable_abc_coroutine Setter / Getter
    ##################################################

    @property
    def nullable_abc_coroutine(self) -> typing.Optional[collections.abc.Coroutine]:
        return self._nullable_abc_coroutine

    @nullable_abc_coroutine.setter
    @Validator.type_check
    def nullable_abc_coroutine(self, nullable_abc_coroutine_: typing.Optional[collections.abc.Coroutine]) -> None:
        self._nullable_abc_coroutine = nullable_abc_coroutine_

    ##################################################
    # abc_generator Setter / Getter
    ##################################################

    @property
    def abc_generator(self) -> collections.abc.Generator:
        return self._abc_generator

    @abc_generator.setter
    @Validator.type_check
    def abc_generator(self, abc_generator_: collections.abc.Generator) -> None:
        self._abc_generator = abc_generator_

    ##################################################
    # nullable_abc_generator Setter / Getter
    ##################################################

    @property
    def nullable_abc_generator(self) -> typing.Optional[collections.abc.Generator]:
        return self._nullable_abc_generator

    @nullable_abc_generator.setter
    @Validator.type_check
    def nullable_abc_generator(self, nullable_abc_generator_: typing.Optional[collections.abc.Generator]) -> None:
        self._nullable_abc_generator = nullable_abc_generator_

    ##################################################
    # abc_hashable Setter / Getter
    ##################################################

    @property
    def abc_hashable(self) -> collections.abc.Hashable:
        return self._abc_hashable

    @abc_hashable.setter
    @Validator.type_check
    def abc_hashable(self, abc_hashable_: collections.abc.Hashable) -> None:
        self._abc_hashable = abc_hashable_

    ##################################################
    # nullable_abc_hashable Setter / Getter
    ##################################################

    @property
    def nullable_abc_hashable(self) -> typing.Optional[collections.abc.Hashable]:
        return self._nullable_abc_hashable

    @nullable_abc_hashable.setter
    @Validator.type_check
    def nullable_abc_hashable(self, nullable_abc_hashable_: typing.Optional[collections.abc.Hashable]) -> None:
        self._nullable_abc_hashable = nullable_abc_hashable_

    ##################################################
    # abc_items_view Setter / Getter
    ##################################################

    @property
    def abc_items_view(self) -> collections.abc.ItemsView:
        return self._abc_items_view

    @abc_items_view.setter
    @Validator.type_check
    def abc_items_view(self, abc_items_view_: collections.abc.ItemsView) -> None:
        self._abc_items_view = abc_items_view_

    ##################################################
    # nullable_abc_items_view Setter / Getter
    ##################################################

    @property
    def nullable_abc_items_view(self) -> typing.Optional[collections.abc.ItemsView]:
        return self._nullable_abc_items_view

    @nullable_abc_items_view.setter
    @Validator.type_check
    def nullable_abc_items_view(self, nullable_abc_items_view_: typing.Optional[collections.abc.ItemsView]) -> None:
        self._nullable_abc_items_view = nullable_abc_items_view_

    ##################################################
    # abc_iterable Setter / Getter
    ##################################################

    @property
    def abc_iterable(self) -> collections.abc.Iterable:
        return self._abc_iterable

    @abc_iterable.setter
    @Validator.type_check
    def abc_iterable(self, abc_iterable_: collections.abc.Iterable) -> None:
        self._abc_iterable = abc_iterable_

    ##################################################
    # nullable_abc_iterable Setter / Getter
    ##################################################

    @property
    def nullable_abc_iterable(self) -> typing.Optional[collections.abc.Iterable]:
        return self._nullable_abc_iterable

    @nullable_abc_iterable.setter
    @Validator.type_check
    def nullable_abc_iterable(self, nullable_abc_iterable_: typing.Optional[collections.abc.Iterable]) -> None:
        self._nullable_abc_iterable = nullable_abc_iterable_

    ##################################################
    # abc_iterator Setter / Getter
    ##################################################

    @property
    def abc_iterator(self) -> collections.abc.Iterator:
        return self._abc_iterator

    @abc_iterator.setter
    @Validator.type_check
    def abc_iterator(self, abc_iterator_: collections.abc.Iterator) -> None:
        self._abc_iterator = abc_iterator_

    ##################################################
    # nullable_abc_iterator Setter / Getter
    ##################################################

    @property
    def nullable_abc_iterator(self) -> typing.Optional[collections.abc.Iterator]:
        return self._nullable_abc_iterator

    @nullable_abc_iterator.setter
    @Validator.type_check
    def nullable_abc_iterator(self, nullable_abc_iterator_: typing.Optional[collections.abc.Iterator]) -> None:
        self._nullable_abc_iterator = nullable_abc_iterator_

    ##################################################
    # abc_keys_view Setter / Getter
    ##################################################

    @property
    def abc_keys_view(self) -> collections.abc.KeysView:
        return self._abc_keys_view

    @abc_keys_view.setter
    @Validator.type_check
    def abc_keys_view(self, abc_keys_view_: collections.abc.KeysView) -> None:
        self._abc_keys_view = abc_keys_view_

    ##################################################
    # nullable_abc_keys_view Setter / Getter
    ##################################################

    @property
    def nullable_abc_keys_view(self) -> typing.Optional[collections.abc.KeysView]:
        return self._nullable_abc_keys_view

    @nullable_abc_keys_view.setter
    @Validator.type_check
    def nullable_abc_keys_view(self, nullable_abc_keys_view_: typing.Optional[collections.abc.KeysView]) -> None:
        self._nullable_abc_keys_view = nullable_abc_keys_view_

    ##################################################
    # abc_mapping Setter / Getter
    ##################################################

    @property
    def abc_mapping(self) -> collections.abc.Mapping:
        return self._abc_mapping

    @abc_mapping.setter
    @Validator.type_check
    def abc_mapping(self, abc_mapping_: collections.abc.Mapping) -> None:
        self._abc_mapping = abc_mapping_

    ##################################################
    # nullable_abc_mapping Setter / Getter
    ##################################################

    @property
    def nullable_abc_mapping(self) -> typing.Optional[collections.abc.Mapping]:
        return self._nullable_abc_mapping

    @nullable_abc_mapping.setter
    @Validator.type_check
    def nullable_abc_mapping(self, nullable_abc_mapping_: typing.Optional[collections.abc.Mapping]) -> None:
        self._nullable_abc_mapping = nullable_abc_mapping_

    ##################################################
    # abc_mapping_view Setter / Getter
    ##################################################

    @property
    def abc_mapping_view(self) -> collections.abc.MappingView:
        return self._abc_mapping_view

    @abc_mapping_view.setter
    @Validator.type_check
    def abc_mapping_view(self, abc_mapping_view_: collections.abc.MappingView) -> None:
        self._abc_mapping_view = abc_mapping_view_

    ##################################################
    # nullable_abc_mapping_view Setter / Getter
    ##################################################

    @property
    def nullable_abc_mapping_view(self) -> typing.Optional[collections.abc.MappingView]:
        return self._nullable_abc_mapping_view

    @nullable_abc_mapping_view.setter
    @Validator.type_check
    def nullable_abc_mapping_view(self, nullable_abc_mapping_view_: typing.Optional[collections.abc.MappingView]) -> None:
        self._nullable_abc_mapping_view = nullable_abc_mapping_view_

    ##################################################
    # abc_mutable_mapping Setter / Getter
    ##################################################

    @property
    def abc_mutable_mapping(self) -> collections.abc.MutableMapping:
        return self._abc_mutable_mapping

    @abc_mutable_mapping.setter
    @Validator.type_check
    def abc_mutable_mapping(self, abc_mutable_mapping_: collections.abc.MutableMapping) -> None:
        self._abc_mutable_mapping = abc_mutable_mapping_

    ##################################################
    # nullable_abc_mutable_mapping Setter / Getter
    ##################################################

    @property
    def nullable_abc_mutable_mapping(self) -> typing.Optional[collections.abc.MutableMapping]:
        return self._nullable_abc_mutable_mapping

    @nullable_abc_mutable_mapping.setter
    @Validator.type_check
    def nullable_abc_mutable_mapping(self, nullable_abc_mutable_mapping_: typing.Optional[collections.abc.MutableMapping]) -> None:
        self._nullable_abc_mutable_mapping = nullable_abc_mutable_mapping_

    ##################################################
    # abc_mutable_sequence Setter / Getter
    ##################################################

    @property
    def abc_mutable_sequence(self) -> collections.abc.MutableSequence:
        return self._abc_mutable_sequence

    @abc_mutable_sequence.setter
    @Validator.type_check
    def abc_mutable_sequence(self, abc_mutable_sequence_: collections.abc.MutableSequence) -> None:
        self._abc_mutable_sequence = abc_mutable_sequence_

    ##################################################
    # nullable_abc_mutable_sequence Setter / Getter
    ##################################################

    @property
    def nullable_abc_mutable_sequence(self) -> typing.Optional[collections.abc.MutableSequence]:
        return self._nullable_abc_mutable_sequence

    @nullable_abc_mutable_sequence.setter
    @Validator.type_check
    def nullable_abc_mutable_sequence(self, nullable_abc_mutable_sequence_: typing.Optional[collections.abc.MutableSequence]) -> None:
        self._nullable_abc_mutable_sequence = nullable_abc_mutable_sequence_

    ##################################################
    # abc_mutable_set Setter / Getter
    ##################################################

    @property
    def abc_mutable_set(self) -> collections.abc.MutableSet:
        return self._abc_mutable_set

    @abc_mutable_set.setter
    @Validator.type_check
    def abc_mutable_set(self, abc_mutable_set_: collections.abc.MutableSet) -> None:
        self._abc_mutable_set = abc_mutable_set_

    ##################################################
    # nullable_abc_mutable_set Setter / Getter
    ##################################################

    @property
    def nullable_abc_mutable_set(self) -> typing.Optional[collections.abc.MutableSet]:
        return self._nullable_abc_mutable_set

    @nullable_abc_mutable_set.setter
    @Validator.type_check
    def nullable_abc_mutable_set(self, nullable_abc_mutable_set_: typing.Optional[collections.abc.MutableSet]) -> None:
        self._nullable_abc_mutable_set = nullable_abc_mutable_set_

    ##################################################
    # abc_reversible Setter / Getter
    ##################################################

    @property
    def abc_reversible(self) -> collections.abc.Reversible:
        return self._abc_reversible

    @abc_reversible.setter
    @Validator.type_check
    def abc_reversible(self, abc_reversible_: collections.abc.Reversible) -> None:
        self._abc_reversible = abc_reversible_

    ##################################################
    # nullable_abc_reversible Setter / Getter
    ##################################################

    @property
    def nullable_abc_reversible(self) -> typing.Optional[collections.abc.Reversible]:
        return self._nullable_abc_reversible

    @nullable_abc_reversible.setter
    @Validator.type_check
    def nullable_abc_reversible(self, nullable_abc_reversible_: typing.Optional[collections.abc.Reversible]) -> None:
        self._nullable_abc_reversible = nullable_abc_reversible_

    ##################################################
    # abc_sequence Setter / Getter
    ##################################################

    @property
    def abc_sequence(self) -> collections.abc.Sequence:
        return self._abc_sequence

    @abc_sequence.setter
    @Validator.type_check
    def abc_sequence(self, abc_sequence_: collections.abc.Sequence) -> None:
        self._abc_sequence = abc_sequence_

    ##################################################
    # nullable_abc_sequence Setter / Getter
    ##################################################

    @property
    def nullable_abc_sequence(self) -> typing.Optional[collections.abc.Sequence]:
        return self._nullable_abc_sequence

    @nullable_abc_sequence.setter
    @Validator.type_check
    def nullable_abc_sequence(self, nullable_abc_sequence_: typing.Optional[collections.abc.Sequence]) -> None:
        self._nullable_abc_sequence = nullable_abc_sequence_

    ##################################################
    # abc_set Setter / Getter
    ##################################################

    @property
    def abc_set(self) -> collections.abc.Set:
        return self._abc_set

    @abc_set.setter
    @Validator.type_check
    def abc_set(self, abc_set_: collections.abc.Set) -> None:
        self._abc_set = abc_set_

    ##################################################
    # nullable_abc_set Setter / Getter
    ##################################################

    @property
    def nullable_abc_set(self) -> typing.Optional[collections.abc.Set]:
        return self._nullable_abc_set

    @nullable_abc_set.setter
    @Validator.type_check
    def nullable_abc_set(self, nullable_abc_set_: typing.Optional[collections.abc.Set]) -> None:
        self._nullable_abc_set = nullable_abc_set_

    ##################################################
    # abc_sized Setter / Getter
    ##################################################

    @property
    def abc_sized(self) -> collections.abc.Sized:
        return self._abc_sized

    @abc_sized.setter
    @Validator.type_check
    def abc_sized(self, abc_sized_: collections.abc.Sized) -> None:
        self._abc_sized = abc_sized_

    ##################################################
    # nullable_abc_sized Setter / Getter
    ##################################################

    @property
    def nullable_abc_sized(self) -> typing.Optional[collections.abc.Sized]:
        return self._nullable_abc_sized

    @nullable_abc_sized.setter
    @Validator.type_check
    def nullable_abc_sized(self, nullable_abc_sized_: typing.Optional[collections.abc.Sized]) -> None:
        self._nullable_abc_sized = nullable_abc_sized_

    ##################################################
    # abc_values_view Setter / Getter
    ##################################################

    @property
    def abc_values_view(self) -> collections.abc.ValuesView:
        return self._abc_values_view

    @abc_values_view.setter
    @Validator.type_check
    def abc_values_view(self, abc_values_view_: collections.abc.ValuesView) -> None:
        self._abc_values_view = abc_values_view_

    ##################################################
    # nullable_abc_values_view Setter / Getter
    ##################################################

    @property
    def nullable_abc_values_view(self) -> typing.Optional[collections.abc.ValuesView]:
        return self._nullable_abc_values_view

    @nullable_abc_values_view.setter
    @Validator.type_check
    def nullable_abc_values_view(self, nullable_abc_values_view_: typing.Optional[collections.abc.ValuesView]) -> None:
        self._nullable_abc_values_view = nullable_abc_values_view_

    ##################################################
    # stdtype_bool Setter / Getter
    ##################################################

    @property
    def stdtype_bool(self) -> bool:
        return self._stdtype_bool

    @stdtype_bool.setter
    @Validator.type_check
    def stdtype_bool(self, stdtype_bool_: bool) -> None:
        self._stdtype_bool = stdtype_bool_

    ##################################################
    # nullable_stdtype_bool Setter / Getter
    ##################################################

    @property
    def nullable_stdtype_bool(self) -> typing.Optional[bool]:
        return self._nullable_stdtype_bool

    @nullable_stdtype_bool.setter
    @Validator.type_check
    def nullable_stdtype_bool(self, nullable_stdtype_bool_: typing.Optional[bool]) -> None:
        self._nullable_stdtype_bool = nullable_stdtype_bool_

    ##################################################
    # stdtype_bytearray Setter / Getter
    ##################################################

    @property
    def stdtype_bytearray(self) -> bytearray:
        return self._stdtype_bytearray

    @stdtype_bytearray.setter
    @Validator.type_check
    def stdtype_bytearray(self, stdtype_bytearray_: bytearray) -> None:
        self._stdtype_bytearray = stdtype_bytearray_

    ##################################################
    # nullable_stdtype_bytearray Setter / Getter
    ##################################################

    @property
    def nullable_stdtype_bytearray(self) -> typing.Optional[bytearray]:
        return self._nullable_stdtype_bytearray

    @nullable_stdtype_bytearray.setter
    @Validator.type_check
    def nullable_stdtype_bytearray(self, nullable_stdtype_bytearray_: typing.Optional[bytearray]) -> None:
        self._nullable_stdtype_bytearray = nullable_stdtype_bytearray_

    ##################################################
    # stdtype_bytes Setter / Getter
    ##################################################

    @property
    def stdtype_bytes(self) -> bytes:
        return self._stdtype_bytes

    @stdtype_bytes.setter
    @Validator.type_check
    def stdtype_bytes(self, stdtype_bytes_: bytes) -> None:
        self._stdtype_bytes = stdtype_bytes_

    ##################################################
    # nullable_stdtype_bytes Setter / Getter
    ##################################################

    @property
    def nullable_stdtype_bytes(self) -> typing.Optional[bytes]:
        return self._nullable_stdtype_bytes

    @nullable_stdtype_bytes.setter
    @Validator.type_check
    def nullable_stdtype_bytes(self, nullable_stdtype_bytes_: typing.Optional[bytes]) -> None:
        self._nullable_stdtype_bytes = nullable_stdtype_bytes_

    ##################################################
    # stdtype_complex Setter / Getter
    ##################################################

    @property
    def stdtype_complex(self) -> complex:
        return self._stdtype_complex

    @stdtype_complex.setter
    @Validator.type_check
    def stdtype_complex(self, stdtype_complex_: complex) -> None:
        self._stdtype_complex = stdtype_complex_

    ##################################################
    # nullable_stdtype_complex Setter / Getter
    ##################################################

    @property
    def nullable_stdtype_complex(self) -> typing.Optional[complex]:
        return self._nullable_stdtype_complex

    @nullable_stdtype_complex.setter
    @Validator.type_check
    def nullable_stdtype_complex(self, nullable_stdtype_complex_: typing.Optional[complex]) -> None:
        self._nullable_stdtype_complex = nullable_stdtype_complex_

    ##################################################
    # stdtype_dict Setter / Getter
    ##################################################

    @property
    def stdtype_dict(self) -> dict:
        return self._stdtype_dict

    @stdtype_dict.setter
    @Validator.type_check
    def stdtype_dict(self, stdtype_dict_: dict) -> None:
        self._stdtype_dict = stdtype_dict_

    ##################################################
    # nullable_stdtype_dict Setter / Getter
    ##################################################

    @property
    def nullable_stdtype_dict(self) -> typing.Optional[dict]:
        return self._nullable_stdtype_dict

    @nullable_stdtype_dict.setter
    @Validator.type_check
    def nullable_stdtype_dict(self, nullable_stdtype_dict_: typing.Optional[dict]) -> None:
        self._nullable_stdtype_dict = nullable_stdtype_dict_

    ##################################################
    # stdtype_float Setter / Getter
    ##################################################

    @property
    def stdtype_float(self) -> float:
        return self._stdtype_float

    @stdtype_float.setter
    @Validator.type_check
    def stdtype_float(self, stdtype_float_: float) -> None:
        self._stdtype_float = stdtype_float_

    ##################################################
    # nullable_stdtype_float Setter / Getter
    ##################################################

    @property
    def nullable_stdtype_float(self) -> typing.Optional[float]:
        return self._nullable_stdtype_float

    @nullable_stdtype_float.setter
    @Validator.type_check
    def nullable_stdtype_float(self, nullable_stdtype_float_: typing.Optional[float]) -> None:
        self._nullable_stdtype_float = nullable_stdtype_float_

    ##################################################
    # stdtype_frozenset Setter / Getter
    ##################################################

    @property
    def stdtype_frozenset(self) -> frozenset:
        return self._stdtype_frozenset

    @stdtype_frozenset.setter
    @Validator.type_check
    def stdtype_frozenset(self, stdtype_frozenset_: frozenset) -> None:
        self._stdtype_frozenset = stdtype_frozenset_

    ##################################################
    # nullable_stdtype_frozenset Setter / Getter
    ##################################################

    @property
    def nullable_stdtype_frozenset(self) -> typing.Optional[frozenset]:
        return self._nullable_stdtype_frozenset

    @nullable_stdtype_frozenset.setter
    @Validator.type_check
    def nullable_stdtype_frozenset(self, nullable_stdtype_frozenset_: typing.Optional[frozenset]) -> None:
        self._nullable_stdtype_frozenset = nullable_stdtype_frozenset_

    ##################################################
    # stdtype_int Setter / Getter
    ##################################################

    @property
    def stdtype_int(self) -> int:
        return self._stdtype_int

    @stdtype_int.setter
    @Validator.type_check
    def stdtype_int(self, stdtype_int_: int) -> None:
        self._stdtype_int = stdtype_int_

    ##################################################
    # nullable_stdtype_int Setter / Getter
    ##################################################

    @property
    def nullable_stdtype_int(self) -> typing.Optional[int]:
        return self._nullable_stdtype_int

    @nullable_stdtype_int.setter
    @Validator.type_check
    def nullable_stdtype_int(self, nullable_stdtype_int_: typing.Optional[int]) -> None:
        self._nullable_stdtype_int = nullable_stdtype_int_

    ##################################################
    # stdtype_list Setter / Getter
    ##################################################

    @property
    def stdtype_list(self) -> list:
        return self._stdtype_list

    @stdtype_list.setter
    @Validator.type_check
    def stdtype_list(self, stdtype_list_: list) -> None:
        self._stdtype_list = stdtype_list_

    ##################################################
    # nullable_stdtype_list Setter / Getter
    ##################################################

    @property
    def nullable_stdtype_list(self) -> typing.Optional[list]:
        return self._nullable_stdtype_list

    @nullable_stdtype_list.setter
    @Validator.type_check
    def nullable_stdtype_list(self, nullable_stdtype_list_: typing.Optional[list]) -> None:
        self._nullable_stdtype_list = nullable_stdtype_list_

    ##################################################
    # stdtype_memoryview Setter / Getter
    ##################################################

    @property
    def stdtype_memoryview(self) -> memoryview:
        return self._stdtype_memoryview

    @stdtype_memoryview.setter
    @Validator.type_check
    def stdtype_memoryview(self, stdtype_memoryview_: memoryview) -> None:
        self._stdtype_memoryview = stdtype_memoryview_

    ##################################################
    # nullable_stdtype_memoryview Setter / Getter
    ##################################################

    @property
    def nullable_stdtype_memoryview(self) -> typing.Optional[memoryview]:
        return self._nullable_stdtype_memoryview

    @nullable_stdtype_memoryview.setter
    @Validator.type_check
    def nullable_stdtype_memoryview(self, nullable_stdtype_memoryview_: typing.Optional[memoryview]) -> None:
        self._nullable_stdtype_memoryview = nullable_stdtype_memoryview_

    ##################################################
    # stdtype_range Setter / Getter
    ##################################################

    @property
    def stdtype_range(self) -> range:
        return self._stdtype_range

    @stdtype_range.setter
    @Validator.type_check
    def stdtype_range(self, stdtype_range_: range) -> None:
        self._stdtype_range = stdtype_range_

    ##################################################
    # nullable_stdtype_range Setter / Getter
    ##################################################

    @property
    def nullable_stdtype_range(self) -> typing.Optional[range]:
        return self._nullable_stdtype_range

    @nullable_stdtype_range.setter
    @Validator.type_check
    def nullable_stdtype_range(self, nullable_stdtype_range_: typing.Optional[range]) -> None:
        self._nullable_stdtype_range = nullable_stdtype_range_

    ##################################################
    # stdtype_set Setter / Getter
    ##################################################

    @property
    def stdtype_set(self) -> set:
        return self._stdtype_set

    @stdtype_set.setter
    @Validator.type_check
    def stdtype_set(self, stdtype_set_: set) -> None:
        self._stdtype_set = stdtype_set_

    ##################################################
    # nullable_stdtype_set Setter / Getter
    ##################################################

    @property
    def nullable_stdtype_set(self) -> typing.Optional[set]:
        return self._nullable_stdtype_set

    @nullable_stdtype_set.setter
    @Validator.type_check
    def nullable_stdtype_set(self, nullable_stdtype_set_: typing.Optional[set]) -> None:
        self._nullable_stdtype_set = nullable_stdtype_set_

    ##################################################
    # stdtype_str Setter / Getter
    ##################################################

    @property
    def stdtype_str(self) -> str:
        return self._stdtype_str

    @stdtype_str.setter
    @Validator.type_check
    def stdtype_str(self, stdtype_str_: str) -> None:
        self._stdtype_str = stdtype_str_

    ##################################################
    # nullable_stdtype_str Setter / Getter
    ##################################################

    @property
    def nullable_stdtype_str(self) -> typing.Optional[str]:
        return self._nullable_stdtype_str

    @nullable_stdtype_str.setter
    @Validator.type_check
    def nullable_stdtype_str(self, nullable_stdtype_str_: typing.Optional[str]) -> None:
        self._nullable_stdtype_str = nullable_stdtype_str_

    ##################################################
    # stdtype_tuple Setter / Getter
    ##################################################

    @property
    def stdtype_tuple(self) -> tuple:
        return self._stdtype_tuple

    @stdtype_tuple.setter
    @Validator.type_check
    def stdtype_tuple(self, stdtype_tuple_: tuple) -> None:
        self._stdtype_tuple = stdtype_tuple_

    ##################################################
    # nullable_stdtype_tuple Setter / Getter
    ##################################################

    @property
    def nullable_stdtype_tuple(self) -> typing.Optional[tuple]:
        return self._nullable_stdtype_tuple

    @nullable_stdtype_tuple.setter
    @Validator.type_check
    def nullable_stdtype_tuple(self, nullable_stdtype_tuple_: typing.Optional[tuple]) -> None:
        self._nullable_stdtype_tuple = nullable_stdtype_tuple_

    ##################################################
    # stdtype_type Setter / Getter
    ##################################################

    @property
    def stdtype_type(self) -> type:
        return self._stdtype_type

    @stdtype_type.setter
    @Validator.type_check
    def stdtype_type(self, stdtype_type_: type) -> None:
        self._stdtype_type = stdtype_type_

    ##################################################
    # nullable_stdtype_type Setter / Getter
    ##################################################

    @property
    def nullable_stdtype_type(self) -> typing.Optional[type]:
        return self._nullable_stdtype_type

    @nullable_stdtype_type.setter
    @Validator.type_check
    def nullable_stdtype_type(self, nullable_stdtype_type_: typing.Optional[type]) -> None:
        self._nullable_stdtype_type = nullable_stdtype_type_

    ##################################################
    # typing_abstract_set Setter / Getter
    ##################################################

    @property
    def typing_abstract_set(self) -> typing.AbstractSet:
        return self._typing_abstract_set

    @typing_abstract_set.setter
    @Validator.type_check
    def typing_abstract_set(self, typing_abstract_set_: typing.AbstractSet) -> None:
        self._typing_abstract_set = typing_abstract_set_

    ##################################################
    # nullable_typing_abstract_set Setter / Getter
    ##################################################

    @property
    def nullable_typing_abstract_set(self) -> typing.Optional[typing.AbstractSet]:
        return self._nullable_typing_abstract_set

    @nullable_typing_abstract_set.setter
    @Validator.type_check
    def nullable_typing_abstract_set(self, nullable_typing_abstract_set_: typing.Optional[typing.AbstractSet]) -> None:
        self._nullable_typing_abstract_set = nullable_typing_abstract_set_

    ##################################################
    # typing_async_context_manager Setter / Getter
    ##################################################

    @property
    def typing_async_context_manager(self) -> typing.AsyncContextManager:
        return self._typing_async_context_manager

    @typing_async_context_manager.setter
    @Validator.type_check
    def typing_async_context_manager(self, typing_async_context_manager_: typing.AsyncContextManager) -> None:
        self._typing_async_context_manager = typing_async_context_manager_

    ##################################################
    # nullable_typing_async_context_manager Setter / Getter
    ##################################################

    @property
    def nullable_typing_async_context_manager(self) -> typing.Optional[typing.AsyncContextManager]:
        return self._nullable_typing_async_context_manager

    @nullable_typing_async_context_manager.setter
    @Validator.type_check
    def nullable_typing_async_context_manager(self, nullable_typing_async_context_manager_: typing.Optional[typing.AsyncContextManager]) -> None:
        self._nullable_typing_async_context_manager = nullable_typing_async_context_manager_

    ##################################################
    # typing_async_generator Setter / Getter
    ##################################################

    @property
    def typing_async_generator(self) -> typing.AsyncGenerator:
        return self._typing_async_generator

    @typing_async_generator.setter
    @Validator.type_check
    def typing_async_generator(self, typing_async_generator_: typing.AsyncGenerator) -> None:
        self._typing_async_generator = typing_async_generator_

    ##################################################
    # nullable_typing_async_generator Setter / Getter
    ##################################################

    @property
    def nullable_typing_async_generator(self) -> typing.Optional[typing.AsyncGenerator]:
        return self._nullable_typing_async_generator

    @nullable_typing_async_generator.setter
    @Validator.type_check
    def nullable_typing_async_generator(self, nullable_typing_async_generator_: typing.Optional[typing.AsyncGenerator]) -> None:
        self._nullable_typing_async_generator = nullable_typing_async_generator_

    ##################################################
    # typing_async_iterable Setter / Getter
    ##################################################

    @property
    def typing_async_iterable(self) -> typing.AsyncIterable:
        return self._typing_async_iterable

    @typing_async_iterable.setter
    @Validator.type_check
    def typing_async_iterable(self, typing_async_iterable_: typing.AsyncIterable) -> None:
        self._typing_async_iterable = typing_async_iterable_

    ##################################################
    # nullable_typing_async_iterable Setter / Getter
    ##################################################

    @property
    def nullable_typing_async_iterable(self) -> typing.Optional[typing.AsyncIterable]:
        return self._nullable_typing_async_iterable

    @nullable_typing_async_iterable.setter
    @Validator.type_check
    def nullable_typing_async_iterable(self, nullable_typing_async_iterable_: typing.Optional[typing.AsyncIterable]) -> None:
        self._nullable_typing_async_iterable = nullable_typing_async_iterable_

    ##################################################
    # typing_async_iterator Setter / Getter
    ##################################################

    @property
    def typing_async_iterator(self) -> typing.AsyncIterator:
        return self._typing_async_iterator

    @typing_async_iterator.setter
    @Validator.type_check
    def typing_async_iterator(self, typing_async_iterator_: typing.AsyncIterator) -> None:
        self._typing_async_iterator = typing_async_iterator_

    ##################################################
    # nullable_typing_async_iterator Setter / Getter
    ##################################################

    @property
    def nullable_typing_async_iterator(self) -> typing.Optional[typing.AsyncIterator]:
        return self._nullable_typing_async_iterator

    @nullable_typing_async_iterator.setter
    @Validator.type_check
    def nullable_typing_async_iterator(self, nullable_typing_async_iterator_: typing.Optional[typing.AsyncIterator]) -> None:
        self._nullable_typing_async_iterator = nullable_typing_async_iterator_

    ##################################################
    # typing_awaitable Setter / Getter
    ##################################################

    @property
    def typing_awaitable(self) -> typing.Awaitable:
        return self._typing_awaitable

    @typing_awaitable.setter
    @Validator.type_check
    def typing_awaitable(self, typing_awaitable_: typing.Awaitable) -> None:
        self._typing_awaitable = typing_awaitable_

    ##################################################
    # nullable_typing_awaitable Setter / Getter
    ##################################################

    @property
    def nullable_typing_awaitable(self) -> typing.Optional[typing.Awaitable]:
        return self._nullable_typing_awaitable

    @nullable_typing_awaitable.setter
    @Validator.type_check
    def nullable_typing_awaitable(self, nullable_typing_awaitable_: typing.Optional[typing.Awaitable]) -> None:
        self._nullable_typing_awaitable = nullable_typing_awaitable_

    ##################################################
    # typing_byte_string Setter / Getter
    ##################################################

    @property
    def typing_byte_string(self) -> typing.ByteString:
        return self._typing_byte_string

    @typing_byte_string.setter
    @Validator.type_check
    def typing_byte_string(self, typing_byte_string_: typing.ByteString) -> None:
        self._typing_byte_string = typing_byte_string_

    ##################################################
    # nullable_typing_byte_string Setter / Getter
    ##################################################

    @property
    def nullable_typing_byte_string(self) -> typing.Optional[typing.ByteString]:
        return self._nullable_typing_byte_string

    @nullable_typing_byte_string.setter
    @Validator.type_check
    def nullable_typing_byte_string(self, nullable_typing_byte_string_: typing.Optional[typing.ByteString]) -> None:
        self._nullable_typing_byte_string = nullable_typing_byte_string_

    ##################################################
    # typing_callable Setter / Getter
    ##################################################

    @property
    def typing_callable(self) -> typing.Callable:
        return self._typing_callable

    @typing_callable.setter
    @Validator.type_check
    def typing_callable(self, typing_callable_: typing.Callable) -> None:
        self._typing_callable = typing_callable_

    ##################################################
    # nullable_typing_callable Setter / Getter
    ##################################################

    @property
    def nullable_typing_callable(self) -> typing.Optional[typing.Callable]:
        return self._nullable_typing_callable

    @nullable_typing_callable.setter
    @Validator.type_check
    def nullable_typing_callable(self, nullable_typing_callable_: typing.Optional[typing.Callable]) -> None:
        self._nullable_typing_callable = nullable_typing_callable_

    ##################################################
    # typing_chain_map Setter / Getter
    ##################################################

    @property
    def typing_chain_map(self) -> typing.ChainMap:
        return self._typing_chain_map

    @typing_chain_map.setter
    @Validator.type_check
    def typing_chain_map(self, typing_chain_map_: typing.ChainMap) -> None:
        self._typing_chain_map = typing_chain_map_

    ##################################################
    # nullable_typing_chain_map Setter / Getter
    ##################################################

    @property
    def nullable_typing_chain_map(self) -> typing.Optional[typing.ChainMap]:
        return self._nullable_typing_chain_map

    @nullable_typing_chain_map.setter
    @Validator.type_check
    def nullable_typing_chain_map(self, nullable_typing_chain_map_: typing.Optional[typing.ChainMap]) -> None:
        self._nullable_typing_chain_map = nullable_typing_chain_map_

    ##################################################
    # typing_collection Setter / Getter
    ##################################################

    @property
    def typing_collection(self) -> typing.Collection:
        return self._typing_collection

    @typing_collection.setter
    @Validator.type_check
    def typing_collection(self, typing_collection_: typing.Collection) -> None:
        self._typing_collection = typing_collection_

    ##################################################
    # nullable_typing_collection Setter / Getter
    ##################################################

    @property
    def nullable_typing_collection(self) -> typing.Optional[typing.Collection]:
        return self._nullable_typing_collection

    @nullable_typing_collection.setter
    @Validator.type_check
    def nullable_typing_collection(self, nullable_typing_collection_: typing.Optional[typing.Collection]) -> None:
        self._nullable_typing_collection = nullable_typing_collection_

    ##################################################
    # typing_container Setter / Getter
    ##################################################

    @property
    def typing_container(self) -> typing.Container:
        return self._typing_container

    @typing_container.setter
    @Validator.type_check
    def typing_container(self, typing_container_: typing.Container) -> None:
        self._typing_container = typing_container_

    ##################################################
    # nullable_typing_container Setter / Getter
    ##################################################

    @property
    def nullable_typing_container(self) -> typing.Optional[typing.Container]:
        return self._nullable_typing_container

    @nullable_typing_container.setter
    @Validator.type_check
    def nullable_typing_container(self, nullable_typing_container_: typing.Optional[typing.Container]) -> None:
        self._nullable_typing_container = nullable_typing_container_

    ##################################################
    # typing_context_manager Setter / Getter
    ##################################################

    @property
    def typing_context_manager(self) -> typing.ContextManager:
        return self._typing_context_manager

    @typing_context_manager.setter
    @Validator.type_check
    def typing_context_manager(self, typing_context_manager_: typing.ContextManager) -> None:
        self._typing_context_manager = typing_context_manager_

    ##################################################
    # nullable_typing_context_manager Setter / Getter
    ##################################################

    @property
    def nullable_typing_context_manager(self) -> typing.Optional[typing.ContextManager]:
        return self._nullable_typing_context_manager

    @nullable_typing_context_manager.setter
    @Validator.type_check
    def nullable_typing_context_manager(self, nullable_typing_context_manager_: typing.Optional[typing.ContextManager]) -> None:
        self._nullable_typing_context_manager = nullable_typing_context_manager_

    ##################################################
    # typing_coroutine Setter / Getter
    ##################################################

    @property
    def typing_coroutine(self) -> typing.Coroutine:
        return self._typing_coroutine

    @typing_coroutine.setter
    @Validator.type_check
    def typing_coroutine(self, typing_coroutine_: typing.Coroutine) -> None:
        self._typing_coroutine = typing_coroutine_

    ##################################################
    # nullable_typing_coroutine Setter / Getter
    ##################################################

    @property
    def nullable_typing_coroutine(self) -> typing.Optional[typing.Coroutine]:
        return self._nullable_typing_coroutine

    @nullable_typing_coroutine.setter
    @Validator.type_check
    def nullable_typing_coroutine(self, nullable_typing_coroutine_: typing.Optional[typing.Coroutine]) -> None:
        self._nullable_typing_coroutine = nullable_typing_coroutine_

    ##################################################
    # typing_counter Setter / Getter
    ##################################################

    @property
    def typing_counter(self) -> typing.Counter:
        return self._typing_counter

    @typing_counter.setter
    @Validator.type_check
    def typing_counter(self, typing_counter_: typing.Counter) -> None:
        self._typing_counter = typing_counter_

    ##################################################
    # nullable_typing_counter Setter / Getter
    ##################################################

    @property
    def nullable_typing_counter(self) -> typing.Optional[typing.Counter]:
        return self._nullable_typing_counter

    @nullable_typing_counter.setter
    @Validator.type_check
    def nullable_typing_counter(self, nullable_typing_counter_: typing.Optional[typing.Counter]) -> None:
        self._nullable_typing_counter = nullable_typing_counter_

    ##################################################
    # typing_default_dict Setter / Getter
    ##################################################

    @property
    def typing_default_dict(self) -> typing.DefaultDict:
        return self._typing_default_dict

    @typing_default_dict.setter
    @Validator.type_check
    def typing_default_dict(self, typing_default_dict_: typing.DefaultDict) -> None:
        self._typing_default_dict = typing_default_dict_

    ##################################################
    # nullable_typing_default_dict Setter / Getter
    ##################################################

    @property
    def nullable_typing_default_dict(self) -> typing.Optional[typing.DefaultDict]:
        return self._nullable_typing_default_dict

    @nullable_typing_default_dict.setter
    @Validator.type_check
    def nullable_typing_default_dict(self, nullable_typing_default_dict_: typing.Optional[typing.DefaultDict]) -> None:
        self._nullable_typing_default_dict = nullable_typing_default_dict_

    ##################################################
    # typing_deque Setter / Getter
    ##################################################

    @property
    def typing_deque(self) -> typing.Deque:
        return self._typing_deque

    @typing_deque.setter
    @Validator.type_check
    def typing_deque(self, typing_deque_: typing.Deque) -> None:
        self._typing_deque = typing_deque_

    ##################################################
    # nullable_typing_deque Setter / Getter
    ##################################################

    @property
    def nullable_typing_deque(self) -> typing.Optional[typing.Deque]:
        return self._nullable_typing_deque

    @nullable_typing_deque.setter
    @Validator.type_check
    def nullable_typing_deque(self, nullable_typing_deque_: typing.Optional[typing.Deque]) -> None:
        self._nullable_typing_deque = nullable_typing_deque_

    ##################################################
    # typing_dict Setter / Getter
    ##################################################

    @property
    def typing_dict(self) -> typing.Dict:
        return self._typing_dict

    @typing_dict.setter
    @Validator.type_check
    def typing_dict(self, typing_dict_: typing.Dict) -> None:
        self._typing_dict = typing_dict_

    ##################################################
    # nullable_typing_dict Setter / Getter
    ##################################################

    @property
    def nullable_typing_dict(self) -> typing.Optional[typing.Dict]:
        return self._nullable_typing_dict

    @nullable_typing_dict.setter
    @Validator.type_check
    def nullable_typing_dict(self, nullable_typing_dict_: typing.Optional[typing.Dict]) -> None:
        self._nullable_typing_dict = nullable_typing_dict_

    ##################################################
    # typing_frozen_set Setter / Getter
    ##################################################

    @property
    def typing_frozen_set(self) -> typing.FrozenSet:
        return self._typing_frozen_set

    @typing_frozen_set.setter
    @Validator.type_check
    def typing_frozen_set(self, typing_frozen_set_: typing.FrozenSet) -> None:
        self._typing_frozen_set = typing_frozen_set_

    ##################################################
    # nullable_typing_frozen_set Setter / Getter
    ##################################################

    @property
    def nullable_typing_frozen_set(self) -> typing.Optional[typing.FrozenSet]:
        return self._nullable_typing_frozen_set

    @nullable_typing_frozen_set.setter
    @Validator.type_check
    def nullable_typing_frozen_set(self, nullable_typing_frozen_set_: typing.Optional[typing.FrozenSet]) -> None:
        self._nullable_typing_frozen_set = nullable_typing_frozen_set_

    ##################################################
    # typing_generator Setter / Getter
    ##################################################

    @property
    def typing_generator(self) -> typing.Generator:
        return self._typing_generator

    @typing_generator.setter
    @Validator.type_check
    def typing_generator(self, typing_generator_: typing.Generator) -> None:
        self._typing_generator = typing_generator_

    ##################################################
    # nullable_typing_generator Setter / Getter
    ##################################################

    @property
    def nullable_typing_generator(self) -> typing.Optional[typing.Generator]:
        return self._nullable_typing_generator

    @nullable_typing_generator.setter
    @Validator.type_check
    def nullable_typing_generator(self, nullable_typing_generator_: typing.Optional[typing.Generator]) -> None:
        self._nullable_typing_generator = nullable_typing_generator_

    ##################################################
    # typing_hashable Setter / Getter
    ##################################################

    @property
    def typing_hashable(self) -> typing.Hashable:
        return self._typing_hashable

    @typing_hashable.setter
    @Validator.type_check
    def typing_hashable(self, typing_hashable_: typing.Hashable) -> None:
        self._typing_hashable = typing_hashable_

    ##################################################
    # nullable_typing_hashable Setter / Getter
    ##################################################

    @property
    def nullable_typing_hashable(self) -> typing.Optional[typing.Hashable]:
        return self._nullable_typing_hashable

    @nullable_typing_hashable.setter
    @Validator.type_check
    def nullable_typing_hashable(self, nullable_typing_hashable_: typing.Optional[typing.Hashable]) -> None:
        self._nullable_typing_hashable = nullable_typing_hashable_

    ##################################################
    # typing_items_view Setter / Getter
    ##################################################

    @property
    def typing_items_view(self) -> typing.ItemsView:
        return self._typing_items_view

    @typing_items_view.setter
    @Validator.type_check
    def typing_items_view(self, typing_items_view_: typing.ItemsView) -> None:
        self._typing_items_view = typing_items_view_

    ##################################################
    # nullable_typing_items_view Setter / Getter
    ##################################################

    @property
    def nullable_typing_items_view(self) -> typing.Optional[typing.ItemsView]:
        return self._nullable_typing_items_view

    @nullable_typing_items_view.setter
    @Validator.type_check
    def nullable_typing_items_view(self, nullable_typing_items_view_: typing.Optional[typing.ItemsView]) -> None:
        self._nullable_typing_items_view = nullable_typing_items_view_

    ##################################################
    # typing_iterable Setter / Getter
    ##################################################

    @property
    def typing_iterable(self) -> typing.Iterable:
        return self._typing_iterable

    @typing_iterable.setter
    @Validator.type_check
    def typing_iterable(self, typing_iterable_: typing.Iterable) -> None:
        self._typing_iterable = typing_iterable_

    ##################################################
    # nullable_typing_iterable Setter / Getter
    ##################################################

    @property
    def nullable_typing_iterable(self) -> typing.Optional[typing.Iterable]:
        return self._nullable_typing_iterable

    @nullable_typing_iterable.setter
    @Validator.type_check
    def nullable_typing_iterable(self, nullable_typing_iterable_: typing.Optional[typing.Iterable]) -> None:
        self._nullable_typing_iterable = nullable_typing_iterable_

    ##################################################
    # typing_iterator Setter / Getter
    ##################################################

    @property
    def typing_iterator(self) -> typing.Iterator:
        return self._typing_iterator

    @typing_iterator.setter
    @Validator.type_check
    def typing_iterator(self, typing_iterator_: typing.Iterator) -> None:
        self._typing_iterator = typing_iterator_

    ##################################################
    # nullable_typing_iterator Setter / Getter
    ##################################################

    @property
    def nullable_typing_iterator(self) -> typing.Optional[typing.Iterator]:
        return self._nullable_typing_iterator

    @nullable_typing_iterator.setter
    @Validator.type_check
    def nullable_typing_iterator(self, nullable_typing_iterator_: typing.Optional[typing.Iterator]) -> None:
        self._nullable_typing_iterator = nullable_typing_iterator_

    ##################################################
    # typing_keys_view Setter / Getter
    ##################################################

    @property
    def typing_keys_view(self) -> typing.KeysView:
        return self._typing_keys_view

    @typing_keys_view.setter
    @Validator.type_check
    def typing_keys_view(self, typing_keys_view_: typing.KeysView) -> None:
        self._typing_keys_view = typing_keys_view_

    ##################################################
    # nullable_typing_keys_view Setter / Getter
    ##################################################

    @property
    def nullable_typing_keys_view(self) -> typing.Optional[typing.KeysView]:
        return self._nullable_typing_keys_view

    @nullable_typing_keys_view.setter
    @Validator.type_check
    def nullable_typing_keys_view(self, nullable_typing_keys_view_: typing.Optional[typing.KeysView]) -> None:
        self._nullable_typing_keys_view = nullable_typing_keys_view_

    ##################################################
    # typing_list Setter / Getter
    ##################################################

    @property
    def typing_list(self) -> typing.List:
        return self._typing_list

    @typing_list.setter
    @Validator.type_check
    def typing_list(self, typing_list_: typing.List) -> None:
        self._typing_list = typing_list_

    ##################################################
    # nullable_typing_list Setter / Getter
    ##################################################

    @property
    def nullable_typing_list(self) -> typing.Optional[typing.List]:
        return self._nullable_typing_list

    @nullable_typing_list.setter
    @Validator.type_check
    def nullable_typing_list(self, nullable_typing_list_: typing.Optional[typing.List]) -> None:
        self._nullable_typing_list = nullable_typing_list_

    ##################################################
    # typing_mapping Setter / Getter
    ##################################################

    @property
    def typing_mapping(self) -> typing.Mapping:
        return self._typing_mapping

    @typing_mapping.setter
    @Validator.type_check
    def typing_mapping(self, typing_mapping_: typing.Mapping) -> None:
        self._typing_mapping = typing_mapping_

    ##################################################
    # nullable_typing_mapping Setter / Getter
    ##################################################

    @property
    def nullable_typing_mapping(self) -> typing.Optional[typing.Mapping]:
        return self._nullable_typing_mapping

    @nullable_typing_mapping.setter
    @Validator.type_check
    def nullable_typing_mapping(self, nullable_typing_mapping_: typing.Optional[typing.Mapping]) -> None:
        self._nullable_typing_mapping = nullable_typing_mapping_

    ##################################################
    # typing_mapping_view Setter / Getter
    ##################################################

    @property
    def typing_mapping_view(self) -> typing.MappingView:
        return self._typing_mapping_view

    @typing_mapping_view.setter
    @Validator.type_check
    def typing_mapping_view(self, typing_mapping_view_: typing.MappingView) -> None:
        self._typing_mapping_view = typing_mapping_view_

    ##################################################
    # nullable_typing_mapping_view Setter / Getter
    ##################################################

    @property
    def nullable_typing_mapping_view(self) -> typing.Optional[typing.MappingView]:
        return self._nullable_typing_mapping_view

    @nullable_typing_mapping_view.setter
    @Validator.type_check
    def nullable_typing_mapping_view(self, nullable_typing_mapping_view_: typing.Optional[typing.MappingView]) -> None:
        self._nullable_typing_mapping_view = nullable_typing_mapping_view_

    ##################################################
    # typing_mutable_mapping Setter / Getter
    ##################################################

    @property
    def typing_mutable_mapping(self) -> typing.MutableMapping:
        return self._typing_mutable_mapping

    @typing_mutable_mapping.setter
    @Validator.type_check
    def typing_mutable_mapping(self, typing_mutable_mapping_: typing.MutableMapping) -> None:
        self._typing_mutable_mapping = typing_mutable_mapping_

    ##################################################
    # nullable_typing_mutable_mapping Setter / Getter
    ##################################################

    @property
    def nullable_typing_mutable_mapping(self) -> typing.Optional[typing.MutableMapping]:
        return self._nullable_typing_mutable_mapping

    @nullable_typing_mutable_mapping.setter
    @Validator.type_check
    def nullable_typing_mutable_mapping(self, nullable_typing_mutable_mapping_: typing.Optional[typing.MutableMapping]) -> None:
        self._nullable_typing_mutable_mapping = nullable_typing_mutable_mapping_

    ##################################################
    # typing_mutable_sequence Setter / Getter
    ##################################################

    @property
    def typing_mutable_sequence(self) -> typing.MutableSequence:
        return self._typing_mutable_sequence

    @typing_mutable_sequence.setter
    @Validator.type_check
    def typing_mutable_sequence(self, typing_mutable_sequence_: typing.MutableSequence) -> None:
        self._typing_mutable_sequence = typing_mutable_sequence_

    ##################################################
    # nullable_typing_mutable_sequence Setter / Getter
    ##################################################

    @property
    def nullable_typing_mutable_sequence(self) -> typing.Optional[typing.MutableSequence]:
        return self._nullable_typing_mutable_sequence

    @nullable_typing_mutable_sequence.setter
    @Validator.type_check
    def nullable_typing_mutable_sequence(self, nullable_typing_mutable_sequence_: typing.Optional[typing.MutableSequence]) -> None:
        self._nullable_typing_mutable_sequence = nullable_typing_mutable_sequence_

    ##################################################
    # typing_mutable_set Setter / Getter
    ##################################################

    @property
    def typing_mutable_set(self) -> typing.MutableSet:
        return self._typing_mutable_set

    @typing_mutable_set.setter
    @Validator.type_check
    def typing_mutable_set(self, typing_mutable_set_: typing.MutableSet) -> None:
        self._typing_mutable_set = typing_mutable_set_

    ##################################################
    # nullable_typing_mutable_set Setter / Getter
    ##################################################

    @property
    def nullable_typing_mutable_set(self) -> typing.Optional[typing.MutableSet]:
        return self._nullable_typing_mutable_set

    @nullable_typing_mutable_set.setter
    @Validator.type_check
    def nullable_typing_mutable_set(self, nullable_typing_mutable_set_: typing.Optional[typing.MutableSet]) -> None:
        self._nullable_typing_mutable_set = nullable_typing_mutable_set_

    ##################################################
    # typing_ordered_dict Setter / Getter
    ##################################################

    @property
    def typing_ordered_dict(self) -> OrderedDict:
        return self._typing_ordered_dict

    @typing_ordered_dict.setter
    @Validator.type_check
    def typing_ordered_dict(self, typing_ordered_dict_: OrderedDict) -> None:
        self._typing_ordered_dict = typing_ordered_dict_

    ##################################################
    # nullable_typing_ordered_dict Setter / Getter
    ##################################################

    @property
    def nullable_typing_ordered_dict(self) -> typing.Optional[OrderedDict]:
        return self._nullable_typing_ordered_dict

    @nullable_typing_ordered_dict.setter
    @Validator.type_check
    def nullable_typing_ordered_dict(self, nullable_typing_ordered_dict_: typing.Optional[OrderedDict]) -> None:
        self._nullable_typing_ordered_dict = nullable_typing_ordered_dict_

    ##################################################
    # typing_reversible Setter / Getter
    ##################################################

    @property
    def typing_reversible(self) -> typing.Reversible:
        return self._typing_reversible

    @typing_reversible.setter
    @Validator.type_check
    def typing_reversible(self, typing_reversible_: typing.Reversible) -> None:
        self._typing_reversible = typing_reversible_

    ##################################################
    # nullable_typing_reversible Setter / Getter
    ##################################################

    @property
    def nullable_typing_reversible(self) -> typing.Optional[typing.Reversible]:
        return self._nullable_typing_reversible

    @nullable_typing_reversible.setter
    @Validator.type_check
    def nullable_typing_reversible(self, nullable_typing_reversible_: typing.Optional[typing.Reversible]) -> None:
        self._nullable_typing_reversible = nullable_typing_reversible_

    ##################################################
    # typing_sequence Setter / Getter
    ##################################################

    @property
    def typing_sequence(self) -> typing.Sequence:
        return self._typing_sequence

    @typing_sequence.setter
    @Validator.type_check
    def typing_sequence(self, typing_sequence_: typing.Sequence) -> None:
        self._typing_sequence = typing_sequence_

    ##################################################
    # nullable_typing_sequence Setter / Getter
    ##################################################

    @property
    def nullable_typing_sequence(self) -> typing.Optional[typing.Sequence]:
        return self._nullable_typing_sequence

    @nullable_typing_sequence.setter
    @Validator.type_check
    def nullable_typing_sequence(self, nullable_typing_sequence_: typing.Optional[typing.Sequence]) -> None:
        self._nullable_typing_sequence = nullable_typing_sequence_

    ##################################################
    # typing_set Setter / Getter
    ##################################################

    @property
    def typing_set(self) -> typing.Set:
        return self._typing_set

    @typing_set.setter
    @Validator.type_check
    def typing_set(self, typing_set_: typing.Set) -> None:
        self._typing_set = typing_set_

    ##################################################
    # nullable_typing_set Setter / Getter
    ##################################################

    @property
    def nullable_typing_set(self) -> typing.Optional[typing.Set]:
        return self._nullable_typing_set

    @nullable_typing_set.setter
    @Validator.type_check
    def nullable_typing_set(self, nullable_typing_set_: typing.Optional[typing.Set]) -> None:
        self._nullable_typing_set = nullable_typing_set_

    ##################################################
    # typing_sized Setter / Getter
    ##################################################

    @property
    def typing_sized(self) -> typing.Sized:
        return self._typing_sized

    @typing_sized.setter
    @Validator.type_check
    def typing_sized(self, typing_sized_: typing.Sized) -> None:
        self._typing_sized = typing_sized_

    ##################################################
    # nullable_typing_sized Setter / Getter
    ##################################################

    @property
    def nullable_typing_sized(self) -> typing.Optional[typing.Sized]:
        return self._nullable_typing_sized

    @nullable_typing_sized.setter
    @Validator.type_check
    def nullable_typing_sized(self, nullable_typing_sized_: typing.Optional[typing.Sized]) -> None:
        self._nullable_typing_sized = nullable_typing_sized_

    ##################################################
    # typing_tuple Setter / Getter
    ##################################################

    @property
    def typing_tuple(self) -> typing.Tuple:
        return self._typing_tuple

    @typing_tuple.setter
    @Validator.type_check
    def typing_tuple(self, typing_tuple_: typing.Tuple) -> None:
        self._typing_tuple = typing_tuple_

    ##################################################
    # nullable_typing_tuple Setter / Getter
    ##################################################

    @property
    def nullable_typing_tuple(self) -> typing.Optional[typing.Tuple]:
        return self._nullable_typing_tuple

    @nullable_typing_tuple.setter
    @Validator.type_check
    def nullable_typing_tuple(self, nullable_typing_tuple_: typing.Optional[typing.Tuple]) -> None:
        self._nullable_typing_tuple = nullable_typing_tuple_

    ##################################################
    # typing_type Setter / Getter
    ##################################################

    @property
    def typing_type(self) -> typing.Type:
        return self._typing_type

    @typing_type.setter
    @Validator.type_check
    def typing_type(self, typing_type_: typing.Type) -> None:
        self._typing_type = typing_type_

    ##################################################
    # nullable_typing_type Setter / Getter
    ##################################################

    @property
    def nullable_typing_type(self) -> typing.Optional[typing.Type]:
        return self._nullable_typing_type

    @nullable_typing_type.setter
    @Validator.type_check
    def nullable_typing_type(self, nullable_typing_type_: typing.Optional[typing.Type]) -> None:
        self._nullable_typing_type = nullable_typing_type_

    ##################################################
    # typing_values_view Setter / Getter
    ##################################################

    @property
    def typing_values_view(self) -> typing.ValuesView:
        return self._typing_values_view

    @typing_values_view.setter
    @Validator.type_check
    def typing_values_view(self, typing_values_view_: typing.ValuesView) -> None:
        self._typing_values_view = typing_values_view_

    ##################################################
    # nullable_typing_values_view Setter / Getter
    ##################################################

    @property
    def nullable_typing_values_view(self) -> typing.Optional[typing.ValuesView]:
        return self._nullable_typing_values_view

    @nullable_typing_values_view.setter
    @Validator.type_check
    def nullable_typing_values_view(self, nullable_typing_values_view_: typing.Optional[typing.ValuesView]) -> None:
        self._nullable_typing_values_view = nullable_typing_values_view_

