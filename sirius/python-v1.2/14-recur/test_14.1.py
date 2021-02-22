#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Не запуская код, ответьте на вопрос: что выведет на экран данная программа?
"""

def f(x):
    if x > 0:
        g(x - 1)

def g(x):
    print('*', end='#')
    if x > 1:
        f(x - 3)

f(11)



