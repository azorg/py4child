#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Даны целые неотрицательные числа a, b, c, d, при этом 0≤c<d.
Выведите в порядке возрастания все числа от a до b,
которые дают остаток c при делении на d.

В этой задаче нельзя использовать инструкцию if,
операторы сравнения (< и т.д.), должен быть только один цикл.
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

begin = (a - c + d  - 1) // d * d + c
end   = (b - c)          // d * d + c
step  = d

for x in range(begin, end + 1, step):
        print(x, '', end='')

print()

