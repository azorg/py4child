#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Количество различных элементов — 2
==================================
Дан список.
Посчитайте, сколько в нём различных элементов, не изменяя самого списка.

Входные данные:
Вводится список чисел. Все числа списка находятся на одной строке.
Все числа целые неотрицательные и не больше 1000.
"""

a = tuple(map(int, input().split()))
cnt = 0
b = []
for i in a:
    if i not in b:
        b.append(i)
        cnt += 1
print(cnt)

