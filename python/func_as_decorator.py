import functools


# all of three methods are OK.
def log(func):
    # @functools.wraps(func)  # OK
    def wrapper(*args, **kwargs):
        print('print a line')
        return func(*args, **kwargs)
    # return functools.wraps(func)(wrapper)  # OK
    return functools.update_wrapper(wrapper, func)  # OK


@log
def foo():
    ''' test docstring '''
    print('foo')


foo()
print(getattr(foo, '__doc__', None))
print(getattr(foo, '__name__', None))
