#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Четные числа
============
По данным двум натуральным числам A и B (A≤B)
выведите все чётные числа на отрезке от A до B.
В этой задаче нельзя использовать инструкцию if.
"""

A = int(input())
B = int(input())

begin = (A + 1) // 2 * 2
end   = B       // 2 * 2

for x in range(begin, end + 1, 2):
        print(x, '', end='')

print()

