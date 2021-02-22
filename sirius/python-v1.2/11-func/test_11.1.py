#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Треугольник
===========
Вам даны 4 отрезка.
Выведите YES, если среди них найдутся 3, из которых можно составить треугольник,
и NO в противном случае.

Для решения напишите функцию triangle(a, b, c),
которая будет возвращать True, если из трёх заданных отрезков
можно составить треугольник, и False иначе.
"""

def triangle(a, b, c):
    return a < b + c and b < a + c and c < a + b

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if triangle(a, b, c) or triangle(a, b, d) or \
   triangle(a, c, d) or triangle(b, c, d):
    print("YES")
else:
    print("NO")


