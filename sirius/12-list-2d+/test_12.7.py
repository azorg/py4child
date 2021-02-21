#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Cамый дешёвый путь
==================
В каждой клетке прямоугольной таблицы N×M записано некоторое число.
Изначально игрок находится в левой верхней клетке.
За один ход ему разрешается перемещаться в соседнюю клетку
либо вправо, либо вниз (влево и вверх перемещаться запрещено).
При проходе через клетку с игрока берут столько килограммов еды,
какое число записано в этой клетке (еду берут также за первую
и последнюю клетки его пути).
Требуется найти минимальный вес еды в килограммах,
отдав которую игрок может попасть в правый нижний угол.

Входные данные:
Вводятся два числа N и M — размеры таблицы 1≤N≤20,1≤M≤20.
Затем идёт N строк по M чисел в каждой — размеры штрафов
в килограммах за прохождение через соответствующие клетки
(числа от 0 до 100).

Выходные данные:
Выведите минимальный вес еды в килограммах,
отдав которую можно попасть в правый нижний угол.
"""

n, m = map(int, input().split())
p = [list(map(int, input().split())) for i in range(n)]
a = [[0] * m for i in range(n)]

a[0][0] = p[0][0]
for j in range(1, m):
    a[0][j] = a[0][j-1] + p[0][j]
for i in range(1, n):
    a[i][0] = a[i-1][0] + p[i][0]
for i in range(1, n):
    for j in range(1, m):
        a[i][j] = p[i][j] + min(a[i-1][j], a[i][j-1])

#for row in a:
#    print(' '.join(map(lambda x: "%3i" % x, row)))

print(a[-1][-1])


