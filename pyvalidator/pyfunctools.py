#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

"""
pyfunctools.py

Python utilities to handle reflexion methods on functions.
"""

from platform import python_version
from typing import (Callable, Tuple, Dict)

if python_version()[0:3] < '3.7':
    print('\033[93m[!] Make sure you have Python 3.7+ installed, quitting.\n\n \033[0m')
    exit(1)


##################################################
# get_varnames
##################################################

def get_varnames(function: Callable) -> Tuple:
    """
    return tuple containing parameter names from function ignoring "self"
    """
    varnames = list(function.__code__.co_varnames)
    argcount = int(function.__code__.co_argcount)
    # fix varnames and argcount
    try:
        # ignore "self" in varnames and update argcount
        if varnames[0] == 'self':
            varnames.pop(0)
            argcount -= 1
    except IndexError:
        pass
    # truncate varnames list to keep function argument names only
    del varnames[argcount:]
    return tuple(varnames)


##################################################
# get_args
##################################################

def get_args(function: Callable, args: Tuple, kwargs: Dict) -> Tuple:
    """
    merge *args into **kwargs excluding 'self'
    """
    # source args and kwargs are not altered by reference
    args_ = list(args)
    kwargs_ = dict(kwargs)
    annotations = function.__annotations__
    for argument in get_varnames(function):
        # raise error when argument annotation not found
        if argument not in annotations.keys():
            raise AttributeError(f'annotation for "{argument}" not found')
    for argument in annotations.keys():
        # ignore "return" annotation
        if argument != 'return':
            # update kwargs_ dictionary with missing argument and appropriate value
            if argument not in kwargs_.keys():
                kwargs_.update({argument: args_[0]})
                # remove argument from args
                args_.pop(0)
    # convert args back to tuple
    return tuple(args_), kwargs_
