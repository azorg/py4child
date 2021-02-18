#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Последовательность Фибоначчи определяется так:

f0=0,f1=1,f2=1,f[n]=f[n−1]+f[n−2]

Дано натуральное число A.
Определите, каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что f[n]=A.
Если A не является числом Фибоначчи, выведите число −1.

Входные данные:
Вводится натуральное число A
(2 ≤ A ≤ 2**109).
"""

a = int(input()) # a >= 2

i  = 3
f1 = f2 = 1
f3 = 2 # f1 + f2
while f3 < a:
    f1, f2 = f2, f3
    f3 = f1 + f2
    i += 1
if f3 == a:
    print(i)
else:
    print(-1)

