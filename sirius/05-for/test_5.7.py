#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Сумма факториалов
=================
По данному натуральном n вычислите сумму 1! + 2! + 3! +... +n!.
В решении этой задачи можно использовать только один цикл.
"""

n = int(input())

if n == 0: n = 1

summ = 0
fact = 1

for i in range(1, n + 1):
    fact *= i
    summ += fact

print(summ)


