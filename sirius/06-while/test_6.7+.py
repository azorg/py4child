#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Последовательность состоит из натуральных чисел,
причем какое-то из чисел составляет более половины от 
общего числа членов последовательности. Найдите это число.

Для решения этой задачи запрещено использование массивов и списков.
"""

x = int(input())
n1 = n2 = n3 = n4 = 0
x1 = x2 = x3 = x4 = 0
while x: # x != 0
    if   x == x1: n1 += 1
    elif x == x2: n2 += 1
    elif x == x3: n3 += 1
    elif x == x4: n4 += 1
    else:
        nmin = min(n1, n2, n3, n4)
        if   n1 == nmin: n1, x1 = 1, x
        elif n2 == nmin: n2, x2 = 1, x
        elif n3 == nmin: n3, x3 = 1, x
        elif n4 == nmin: n4, x4 = 1, x
    x = int(input())

nmax = max(n1, n2, n3, n4)
if   n1 != 0 and n1 == nmax: print(x1)
elif n2 != 0 and n2 == nmax: print(x2)
elif n3 != 0 and n3 == nmax: print(x3)
elif n4 != 0 and n4 == nmax: print(x4)

