#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
По данному натуральному числу выведите все его натуральные
делители в порядке возрастания.
"""

n = int(input())

for i in range(1, n + 1):
    if n % i == 0:
        print(i, '', end='')
print()


