# -*- coding: utf-8 -*-
# [Python 表达式 i += x 与 i = i + x 等价吗？](https://foofish.net/iadd_add.html)
# 讨论可变性,区分可变类型和不可变类型:int,float,str,tuple,list,dict,set,frozenset
a = 1
old_id = id(a)
a += 1
new_id = id(a)
print('int: %s' % (old_id == new_id))

a = 1.2
old_id = id(a)
a += 1.1
new_id = id(a)
print('float: %s' % (old_id == new_id))

a = 'a'
old_id = id(a)
a += 'b'
new_id = id(a)
print('str: %s' % (old_id == new_id))

a = (1, 2)
old_id = id(a)
a += (3, 4)
new_id = id(a)
print('tuple: %s' % (old_id == new_id))

a = [1, 2]
old_id = id(a)
a += [3, 4]
new_id = id(a)
print('list: %s' % (old_id == new_id))

a = {'a': 1}
old_id = id(a)
a['b'] = 2
new_id = id(a)
print('dict: %s' % (old_id == new_id))

a = {1, 2}
old_id = id(a)
a |= {3, 4}
new_id = id(a)
print('set: %s' % (old_id == new_id))

a = frozenset({1, 2})
old_id = id(a)
a |= frozenset({4, 3})
new_id = id(a)
print('frozenset: %s' % (old_id == new_id))


# x+=i 与 x=x+i 区别: list, set, frozenset
a = list(range(0, 3))
b = a
a += [3]
print('x+=i:', a, b)

a = list(range(0, 3))
b = a
a = a + [3]
print('x=x+i:', a, b)

a = set({1, 2})
b = a
a |= {3, 4}
print('x|=i:', a, b)

a = set({1, 2})
b = a
a = a | {3, 4}
print('x=x|i:', a, b)

a = frozenset({1, 2})
b = a
a |= frozenset({3, 4})
print('x|=i:', a, b)

a = frozenset({1, 2})
b = a
a = a | frozenset({3, 4})
print('x=x|i:', a, b)
