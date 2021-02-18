#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дано 10-значное число.
Выведите все цифры этого числа в обратном порядке по одной.
"""

n = int(input())

s = str(n)

for i in s[::-1]:
    print(i, '', end='')
print()

