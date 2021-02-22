#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дан квадратный массив.
Поменяйте местами в каждом столбце элементы, стоящие на главной и побочной диагонали.
"""

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    a[i][i], a[-i-1][i] = a[-i-1][i], a[i][i]

for row in a:
    print(' '.join(map(str, row)))



