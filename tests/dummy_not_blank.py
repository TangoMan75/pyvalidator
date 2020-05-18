#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from typing import Optional

from pyvalidator.validator import Validator


class DummyNotBlank(Validator):

    def __init__(self):
        self._not_blank_bytearray = None
        self._not_blank_bytes = None
        self._not_blank_complex = None
        self._not_blank_dict = None
        self._not_blank_float = None
        self._not_blank_frozenset = None
        self._not_blank_int = None
        self._not_blank_list = None
        self._not_blank_memoryview = None
        self._not_blank_range = None
        self._not_blank_set = None
        self._not_blank_str = None
        self._not_blank_tuple = None
        self._not_blank_type = None

    ##################################################
    # not_blank_bytearray Setter / Getter
    ##################################################

    @property
    def not_blank_bytearray(self) -> Optional[bytearray]:
        return self._not_blank_bytearray

    @not_blank_bytearray.setter
    @Validator.not_blank
    def not_blank_bytearray(self, not_blank_bytearray: bytearray) -> None:
        self._not_blank_bytearray = not_blank_bytearray

    ##################################################
    # not_blank_bytes Setter / Getter
    ##################################################

    @property
    def not_blank_bytes(self) -> Optional[bytes]:
        return self._not_blank_bytes

    @not_blank_bytes.setter
    @Validator.not_blank
    def not_blank_bytes(self, not_blank_bytes: bytes) -> None:
        self._not_blank_bytes = not_blank_bytes

    ##################################################
    # not_blank_complex Setter / Getter
    ##################################################

    @property
    def not_blank_complex(self) -> Optional[complex]:
        return self._not_blank_complex

    @not_blank_complex.setter
    @Validator.not_blank
    def not_blank_complex(self, not_blank_complex: complex) -> None:
        self._not_blank_complex = not_blank_complex

    ##################################################
    # not_blank_dict Setter / Getter
    ##################################################

    @property
    def not_blank_dict(self) -> Optional[dict]:
        return self._not_blank_dict

    @not_blank_dict.setter
    @Validator.not_blank
    def not_blank_dict(self, not_blank_dict: dict) -> None:
        self._not_blank_dict = not_blank_dict

    ##################################################
    # not_blank_float Setter / Getter
    ##################################################

    @property
    def not_blank_float(self) -> Optional[float]:
        return self._not_blank_float

    @not_blank_float.setter
    @Validator.not_blank
    def not_blank_float(self, not_blank_float: float) -> None:
        self._not_blank_float = not_blank_float

    ##################################################
    # not_blank_frozenset Setter / Getter
    ##################################################

    @property
    def not_blank_frozenset(self) -> Optional[frozenset]:
        return self.not_blank__frozenset

    @not_blank_frozenset.setter
    @Validator.not_blank
    def not_blank_frozenset(self, not_blank_frozenset: frozenset) -> None:
        self.not_blank__frozenset = not_blank_frozenset

    ##################################################
    # not_blank_int Setter / Getter
    ##################################################

    @property
    def not_blank_int(self) -> Optional[int]:
        return self._not_blank_int

    @not_blank_int.setter
    @Validator.not_blank
    def not_blank_int(self, not_blank_int: int) -> None:
        self._not_blank_int = not_blank_int

    ##################################################
    # not_blank_list Setter / Getter
    ##################################################

    @property
    def not_blank_list(self) -> Optional[list]:
        return self._not_blank_list

    @not_blank_list.setter
    @Validator.not_blank
    def not_blank_list(self, not_blank_list: list) -> None:
        self._not_blank_list = not_blank_list

    ##################################################
    # not_blank_memoryview Setter / Getter
    ##################################################

    @property
    def not_blank_memoryview(self) -> Optional[memoryview]:
        return self._not_blank_memoryview

    @not_blank_memoryview.setter
    @Validator.not_blank
    def not_blank_memoryview(self, not_blank_memoryview: memoryview) -> None:
        self._not_blank_memoryview = not_blank_memoryview

    ##################################################
    # not_blank_range Setter / Getter
    ##################################################

    @property
    def not_blank_range(self) -> Optional[range]:
        return self._not_blank_range

    @not_blank_range.setter
    @Validator.not_blank
    def not_blank_range(self, not_blank_range: range) -> None:
        self._not_blank_range = not_blank_range

    ##################################################
    # not_blank_set Setter / Getter
    ##################################################

    @property
    def not_blank_set(self) -> Optional[set]:
        return self._not_blank_set

    @not_blank_set.setter
    @Validator.not_blank
    def not_blank_set(self, not_blank_set: set) -> None:
        self._not_blank_set = not_blank_set

    ##################################################
    # not_blank_str Setter / Getter
    ##################################################

    @property
    def not_blank_str(self) -> Optional[str]:
        return self._not_blank_str

    @not_blank_str.setter
    @Validator.not_blank
    def not_blank_str(self, not_blank_str: str) -> None:
        self._not_blank_str = not_blank_str

    ##################################################
    # not_blank_tuple Setter / Getter
    ##################################################

    @property
    def not_blank_tuple(self) -> Optional[tuple]:
        return self._not_blank_tuple

    @not_blank_tuple.setter
    @Validator.not_blank
    def not_blank_tuple(self, not_blank_tuple: tuple) -> None:
        self._not_blank_tuple = not_blank_tuple

    ##################################################
    # not_blank_type Setter / Getter
    ##################################################

    @property
    def not_blank_type(self) -> Optional[type]:
        return self._not_blank_type

    @not_blank_type.setter
    @Validator.not_blank
    def not_blank_type(self, not_blank_type: type) -> None:
        self._not_blank_type = not_blank_type

