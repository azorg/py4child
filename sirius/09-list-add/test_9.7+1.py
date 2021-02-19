#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дан список чисел. Посчитайте, сколько в нём пар элементов,
равных друг другу.
Считается, что любые два элемента, равные друг другу,
образуют одну пару, которую необходимо посчитать.
"""

a = tuple(map(int, input().split()))
n = len(a)
cnt = 0
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            cnt += 1
print(cnt)

