#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дан список чисел.
Если в нем есть два соседних элемента одного знака,
выведите эти числа.
Если соседних элементов одного знака нет - не выводите ничего.
Если таких пар соседей несколько — выведите первую пару.
"""

inp = list(map(int, input().split()))

p = inp[0]
for x in inp[1:]:
    if p * x >= 0:
        print(p, x)
        break
    p = x




