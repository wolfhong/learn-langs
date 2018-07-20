# -*- coding: utf-8 -*-
import functools


def singleton(cls):
    data = {}

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in data:
            data[cls] = cls(*args, **kwargs)
        return data[cls]

    return wrapper


# only work on py3
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Foo(Singleton):
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)


@singleton
class Bar():
    pass


bar1 = Bar()
bar2 = Bar()
print(bar1 is bar2)
