#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Даны два целых числа.
Программа должна вывести 1, если первое число больше второго,
2, если второе больше первого, или число 0, если они равны.
"""

a = int(input())
b = int(input())

if a > b:
    retv = 1
elif a < b:
    retv = 2
else: # a == b
    retv = 0

print(retv)


