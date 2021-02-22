#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Найдите индексы первого вхождения максимального элемента в двумерном массиве.
"""

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

val = a[0][0]
x = y = 0
for i in range(n):
    for j in range(m):
        if val < a[i][j]:
            val = a[i][j]
            x, y = i, j

print(x, y)



