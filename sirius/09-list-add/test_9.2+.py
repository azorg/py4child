#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выведите элементы данного списка в обратном порядке.
Все числа списка находятся на одной строке.
"""

a = [int(s) for s in input().split()]
b = [str(i) for i in a[::-1]]
print(" ".join(b))

