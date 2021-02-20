#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Не запуская код, выберите, какие из программ
во время запуска получат ошибку выполнения.
"""

"""
# a)
def f():
    print(a)
    a = a
a = 5
f()
"""

"""
# b)
def f():
    a = a
    print(a)
a = 5
f()
"""

# c)
def f(a):
    a = a
    print(a)
a = 5
f(a)

"""
# d)
def f():
    print(a)
    global a
a = 5
f()
"""

