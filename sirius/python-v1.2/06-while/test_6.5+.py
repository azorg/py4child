#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Второй минимум
==============
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите значение второго минимального по величине элемента в этой
последовательности, то есть элемента, который будет наименьшим,
если из последовательности удалить наименьший элемент.
Последнее число 0 не учитывается.
Гарантируется, что в последовательности есть хотя бы два элемента
(кроме завершающего числа 0).
"""

min1 = int(input())
min2 = int(input())
if min1 > min2:
    min1, min2 = min2, min1 # -> min1 <= min2
val = int(input())
while val: # val != 0
    if min1 > val:
        min2 = min1
        min1 = val
    elif min2 > val:
        min2 = val
    val = int(input())

print(min2)
