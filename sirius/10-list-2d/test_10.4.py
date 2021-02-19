#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дан двумерный массив размером n×n.
Транспонируйте его и результат запишите в этот же массив.
Вспомогательный массив использовать нельзя.
"""

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(i+1, n):
        a[i][j], a[j][i] = a[j][i], a[i][j]

for row in a:
    print(' '.join(map(str, row)))



