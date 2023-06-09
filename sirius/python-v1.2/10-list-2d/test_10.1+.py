#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ходы коня
=========
На шахматной доске стоит конь.
Отметьте положение коня на доске и все клетки, которые он бьет.
Клетку, где стоит конь, отметьте английской буквой “K”.
Клетки, которые он бьёт, отметьте символами “*”.
Остальные клетки заполните точками.

Входные данные:
Программа получает на вход два числа — координаты коня на шахматной доске.
Координаты вводятся на одной строке через пробел.
Первое число обозначает номер строки, а второе — номер столбца.
Все числа принимают значения от 1 до 8.
"""

x, y = map(int, input().split())
x -= 1
y -= 1

n = 8
a = [['.'] * n for i in range(n)]

a[x][y] = 'K'

moves = []
for i, j in (1, 2), (2, 1):
    moves.append([ i,  j])
    moves.append([ i, -j])
    moves.append([-i,  j])
    moves.append([-i, -j])

for step in moves:
    i = x + step[0]
    j = y + step[1]
    if 0 <= i < n and 0 <= j < n:
        a[i][j] = '*'

for line in a:
    print(' '.join(line))

