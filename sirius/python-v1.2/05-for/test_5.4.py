#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
По данному целому неотрицательному n вычислите значение n!.
"""

n = int(input())

if n == 0: n = 1

for i in range(2, n):
    n *= i

print(n)

