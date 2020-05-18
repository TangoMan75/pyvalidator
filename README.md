TangoMan PyValidator
====================

A dynamic runtime typing validation for members annotated with [PEP 484](https://www.python.org/dev/peps/pep-0484) type hints.

**TangoMan PyValidator** idea was inspired by [agronholm / typeguard](https://github.com/agronholm/typeguard) but enforces SOLID principles, and is based on the chain-of-responsibility design pattern which makes it more readable, extensible and maintenable.

**TangoMan PyValidator** provides `@Validator.type_check` decorator as a mean to dynamically check for type violations at runtime.

Install
-------

Enter following command to install locally

```bash
$ sudo python3 setup.py install
# or
$ pip3 install git+https://github.com/TangoMan75/pyvalidator
```

Features
--------

### Validator

- Validate typing aliases recursively.
- Validate standard python types.
- Validate classes.
- Validate nullable properties.
- Validate not blank properties.

### pyfunctools

Python utilities to handle reflexion methods on functions.

Usage
-----

Import `typing` module and extend your class with `Validator`

```python
import typing

from pyvalidator.validator import Validator

class Foobar(Validator):
	# ...
```

### type_check

Document your class with appropriate annotations and use `@Validator.type_check` decorator on your method and properties.

```python
    @property
    def nullable_str(self) -> typing.Optional[str]:
        return self._nullable_str

    @nullable_str.setter
    @Validator.type_check
    def nullable_str(self, nullable_str_: typing.Optional[str]) -> None:
        self._nullable_str = nullable_str_
```

At runtime if any given argument does not match expected type, `Validator` will raise a `TypeError`.

### not_blank

Use `@Validator.not_blank` decorator on your method and properties.

```python
    @Validator.not_blank
    def divide(self, a: int, b: int) -> None:
    	return a / b
```

At runtime `Validator` will raise a `ValueError` if any given argument is empty i.e:

- `bytes` equals `b''`
- `bytearray` equals `bytearray()`
- `complex` equals `0j`
- `dict` equals `{}`
- `float` equals `0.0`
- `frozenset` equals `frozenset()`
- `int` equals `0`
- `list` equals `[]`
- `memoryview` equals `memoryview(b'')`
- `range` equals `range(0)`
- `set` equals `set()`
- `str` equals `''`
- `tuple` equals `()`

> NOTE: "bool" and "type" values excluded, since "not blank" does not make sense with them.

### Decorator

Decorators are chainable, you can use `@Validator.type_check` and `@Validator.not_blank` on the same attribute.

```python
    @property
    def email(self) -> typing.Optional[str]:
        return self._email

    @email.setter
    @Validator.type_check
    @Validator.not_blank
    def email(self, email_: typing.Optional[str]) -> None:
        self._email = email_
```

Known bug
-----------

`typing.OrderedDict` causes `AttributeError` at runtime (which causes travis ci to fail):

```
AttributeError: module 'typing' has no attribute 'OrderedDict'
```

Seems like mypy maintainers don't want to fix the issue https://github.com/python/mypy/issues/6904

Continuous Integration
----------------------

[![Build Status](https://travis-ci.org/TangoMan75/pyvalidator.svg?branch=master)](https://travis-ci.org/TangoMan75/pyvalidator) 
If you find any bug please report here : [Issues](https://github.com/TangoMan75/pyvalidator/issues/new)

License
-------

Copyrights (c) 2020 &quot;Matthias Morin&quot; &lt;mat@tangoman.io&gt;

[![License](https://img.shields.io/badge/Licence-MIT-green.svg)](LICENCE)
Distributed under the MIT license.

If you like **TangoMan PyValidator** please star, follow or tweet:

[![GitHub stars](https://img.shields.io/github/stars/TangoMan75/pyvalidator?style=social)](https://github.com/TangoMan75/pyvalidator/stargazers)
[![GitHub followers](https://img.shields.io/github/followers/TangoMan75?style=social)](https://github.com/TangoMan75)
[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FTangoMan75%2Fpyvalidator)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FTangoMan75%2Fpyvalidator)

... And check my other cool projects.

[![LinkedIn](https://img.shields.io/static/v1?style=social&logo=linkedin&label=LinkedIn&message=morinmatthias)](https://www.linkedin.com/in/morinmatthias)
