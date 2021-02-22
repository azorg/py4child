#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
По данному натуральному числу n выведите лесенку из n ступенек,
i-я ступенька состоит из чисел от 1 до i без пробелов.

Вывод:
    1
    12
    123
    1234
    ...
"""

n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()


