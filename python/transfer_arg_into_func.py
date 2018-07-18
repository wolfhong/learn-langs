# -*- coding: utf-8 -*-
def change_list1(arg):
    arg.append(1)


def change_list2(arg):
    arg += [1]


def change_list3(arg):
    arg = arg + [1]

# 改变
l = [1, 2, 3]
print(l)
change_list1(l)
print(l)

# 改变
l = [1, 2, 3]
print(l)
change_list2(l)
print(l)

# 不改变
l = [1, 2, 3]
print(l)
change_list3(l)
print(l)
