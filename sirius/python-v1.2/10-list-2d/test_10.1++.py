#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поменять столбцы
================
Дан двумерный массив и два числа: i и j.
Поменяйте в массиве столбцы с номерами i и j.

Входные данные:
Программа получает на вход в первой строке размеры массива n≤100 и m≤100,
затем элементы массива, а в последней строке числа i и j.

Выходные данные:
Выведите полученный массив.
"""

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
i, j = map(int, input().split())

#a = [['.'] * m for i in range(n)]

for k in range(n):
    a[k][i], a[k][j] = a[k][j], a[k][i]

for row in a:
    print(' '.join(map(str, row)))

