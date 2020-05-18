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
    Optional,
)


class TypeHint:
    """
    Model argument typing annotations
    https://docs.python.org/3/library/typing.html
    https://docs.python.org/3/library/stdtypes.html
    https://github.com/agronholm/typeguard
    https://stackoverflow.com/questions/51171908/extracting-data-from-typing-types
    """

    def __init__(self, annotation: Any) -> None:
        if annotation == '':
            raise ValueError('{} annotation cannot be empty'.format(self.__class__.__qualname__))
        if annotation is None:
            self._annotation = type(None)
        else:
            self._annotation = annotation

    ##################################################
    # annotation Getter
    ##################################################

    @property
    def annotation(self) -> Any:
        return self._annotation

    ##################################################
    # types Getter
    ##################################################

    @property
    def types(self) -> Any:
        if hasattr(self._annotation, '__args__'):
            return self._annotation.__args__
        return (self._annotation,)

    ##################################################
    # category Getter
    ##################################################

    @property
    def category(self) -> Optional[str]:
        if hasattr(self._annotation, '__class__'):
            return self._annotation.__class__.__name__

    ##################################################
    # alias Getter
    ##################################################

    @property
    def alias(self) -> Optional[str]:
        if hasattr(self._annotation, '_name'):
            return self._annotation._name
        return None

    ##################################################
    # origin Getter
    ##################################################

    @property
    def origin(self) -> Any:
        if hasattr(self._annotation, '__origin__'):
            return self._annotation.__origin__
        return None

    ##################################################


if __name__ == '__main__':
    pass
