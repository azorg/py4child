#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дано 10-значное число.
Выведите все цифры этого числа в обратном порядке по одной.
"""

n = int(input())

for i in range(10):
    d = n % 10
    n //= 10
    print(d, '', end='')
print()

