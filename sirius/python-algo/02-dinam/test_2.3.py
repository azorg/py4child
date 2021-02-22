#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Мячик на лесенке
================
На вершине лесенки, содержащей N ступенек, находится мячик,
который начинает прыгать по ним вниз, к основанию.
Мячик может прыгнуть на следующую ступеньку, на ступеньку
через одну или через 2.
(То есть если мячик лежит на 8-ой ступеньке,
то он может переместиться на 5-ю, 6-ю, или 7-ю.)
Определите число всевозможных "маршрутов" мячика с вершины на землю.

Входные данные:
Вводится одно число 0<N<31.

Выходные данные:
Выведите одно число — количество маршрутов.
"""

n = int(input())

# Для простоты будим считать, что мячик прыгает вверх, а не вниз
d = [ 1,   # на нуевую ступеньку один вырожденный маршрут
      1,   # на первую ступеньку один маршрут
      2 ]  # на вторую ступеньку два маршрута

for i in range(2, n):
    d = d[1:] + [sum(d)]

if n <= 2:
    ans = d[n]
else:
    ans = d[2]

print(ans)


