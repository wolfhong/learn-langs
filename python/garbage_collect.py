# -*- coding: utf-8 -*-
'''
Python垃圾回收机制的研究.
使用 sys.getrefcount(obj) 可返回引用数.
f1是正常情况
f2会导致循环引用,已经内存溢出了
f3会显式调用垃圾回收

引用计数+1的情况：
- 对象被创建: a = 24
- 对象被引用: b = a
- 对象作为参数传入函数: func(a)
- 对象作为一个元素放入容器
'''
import sys
import gc


def test_ref():
    def _(x):
        print('ref is: %s' % sys.getrefcount(x))

    a = [1, 2]
    a = 27
    print('ref 1 is: %s' % sys.getrefcount(a))
    b = a
    print('ref 2 is: %s' % sys.getrefcount(a))
    b = 1
    print('ref 3 is: %s' % sys.getrefcount(a))
    _(a)
    print('ref 5 is: %s' % sys.getrefcount(a))
    c = {'a': a}
    print('ref 6 is: %s' % sys.getrefcount(a))
    del c['a']
    print('ref 7 is: %s' % sys.getrefcount(a))
    del a
    print('ref 8 is: %s' % sys.getrefcount(a))


class ClassA():
    def __init__(self):
        print('object born, id: {}'.format(hex(id(self))), )

    def __del__(self):
        print('object  del, id: {}'.format(hex(id(self))), )


class ClassB():
    def __init__(self):
        print('object born, id: {}'.format(hex(id(self))), )

    def __del__(self):
        print('object  del, id: {}'.format(hex(id(self))), )


def f1():
    print('正常的内存回收')
    for i in range(1, 10):
        c1 = ClassA()
        del c1


def f2():
    print('循环引用的内存没有立即回收')
    for i in range(0, 10):
        c1 = ClassB()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
    print('------------- end ------------')


def f3():
    # 对循环引用的手动回收
    import time
    gc.set_debug(gc.DEBUG_LEAK)
    for i in range(0, 3):
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
        print('1:', len(gc.garbage))  # 储存回收
        print('2:', gc.collect())  # 回收数量
        print('3:', len(gc.garbage))  # 储存回收
        print('------------------')
        time.sleep(10)


if __name__ == '__main__':
    try:
        _type = sys.argv[1]
    except IndexError:
        print("usage: f1, f2, f3, test_ref")
    else:
        exec(_type + '()')
