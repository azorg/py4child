#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Даны числа a, b, c, d.
Выведите в порядке возрастания все целые числа от 0 до 1000,
которые являются корнями уравнения a * x**3 + b * x**2 + c * x + d = 0.
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for x in range(1000+1):
    x2 = x * x
    x3 = x * x2
    if a * x3 + b * x2 + c * x + d == 0:
        print(x)

