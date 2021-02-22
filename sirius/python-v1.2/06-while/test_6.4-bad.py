#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дано целое число, не меньшее 2.
Выведите его наименьший простой делитель.
"""

n = int(input())
d = 2
while n % d:
    d += 1
print(d)

