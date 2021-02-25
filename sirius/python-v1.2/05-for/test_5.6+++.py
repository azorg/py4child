#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Сумма произведений соседних чисел
=================================
По заданной последовательности a1, a2, …, an чисел вычислите
сумму a1*a2 + a2*a3+ ...

Входные данные:
Первая строка входных данных содержит число n≥2.
В следующих n строках вводится по одному числу.
В i+1 строке содержится значение i-того элемента последовательности.
Все числа во входном файле натуральные, не превосходящие 100.
"""

n = int(input())

summ = 0
prev = int(input())
for i in range(1, n):
    a = int(input())
    summ += a * prev
    prev = a

print(summ)

