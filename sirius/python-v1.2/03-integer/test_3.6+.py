#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Пирожок в столовой стоит a рублей и b копеек.
Определите, сколько рублей и копеек нужно заплатить за n пирожков.

Программа получает на вход три числа: a, b, n,
и должна вывести два числа: стоимость покупки в рублях и копейках.
"""

a = int(input())
b = int(input())
n = int(input())

sum = (a * 100 + b) * n
print(sum // 100, sum % 100)


