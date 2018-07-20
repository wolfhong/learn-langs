import functools
# see https://stackoverflow.com/questions/6394511/python-functools-wraps-equivalent-for-classes


class Counter(object):
    def __init__(self, func):
        self.count = 0
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


@Counter
def foo():
    ''' test docstring '''


for i in range(0, 10):
    foo()
print("call foo %s times." % getattr(foo, 'count', None))
print(foo.__doc__)
print(getattr(foo, '__name__', None))
