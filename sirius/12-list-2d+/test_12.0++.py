#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
По данным числам n и m заполните двумерный массив размером n×m
числами от 1 до n×m “змейкой”,
как показано в примере:
n=3 m=5
 1   2   3   4   5
10   9   8   7   6
11  12  13  14  15
"""

n, m = map(int, input().split())

def fn(i, j):
    if j & 1 == 0:
        return j * m + i + 1
    else:
        return j * m + m - i

a = [[fn(i, j) for i in range(m)] for j in range(n)]

for row in a:
    print(' '.join(map(lambda x: "%3i" % x, row)))

