#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Вам дан список целых чисел. Разверните элементы с нечетными индексами.
"""

a = input().split()
a[1::2] = a[1::2][::-1]
print(" ".join(a))

