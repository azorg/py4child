#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Количество разбиений на слагаемые
=================================
Дано натуральное число N.
Найдите количество его разбиений на натуральные слагаемые.
Два разбиения, отличающиеся только порядком слагаемых,
будем считать за одно.

Например, для N=5 существует 7
различных разбиений:
1. 5=5
2. 5=4+1
3. 5=3+2
4. 5=3+1+1
5. 5=2+2+1
6. 5=2+1+1+1
7. 5=1+1+1+1+1
"""

n = int(input())

def num(n, k):
    if n == 0: return 1
    ans = 0
    for d in range(1, min(n, k) + 1):
        ans += num(n - d, d)
    return ans

print(num(n, n))




