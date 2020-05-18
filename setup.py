#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyValidator package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled

 with this source code in the file LICENSE.
"""

from setuptools import setup

setup(
    name='tangoman-pyvalidator',
    url='https://github.com/tangoMan75/pyvalidator',
    author='Matthias Morin',
    author_email='mat@tangoman.io',
    packages=['pyvalidator', 'pyvalidator.constraints'],
    version='0.1.0',
    license='MIT',
    description='A dynamic runtime typing validation for members annotated with PEP 484',
    long_description=open('README.md').read(),
)
