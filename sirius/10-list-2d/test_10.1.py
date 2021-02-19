#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дано нечётное число n.
Создайте двумерный массив из n×n элементов, заполнив его символами "."
(каждый элемент массива является строкой из одного символа).
Затем заполните символами "∗" среднюю строку массива, 
средний столбец массива, главную диагональ и побочную диагональ.
Для этого не нужно использовать вложенные циклы.

В результате символы "звёздочка" в массиве должны образовывать
изображение снежинки. Выведите полученный массив на экран,
разделяя элементы массива пробелами.
"""

n = int(input())
n2 = n >> 1
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][i]    = '*' # главная диагональ
    a[i][-i-1] = '*' # второстопенная диагональ
    a[n2][i]   = '*' # средняя строка
    a[i][n2]   = '*' # среднний столбец

for line in a:
    print(' '.join(line))

