#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Определите среднее значение всех элементов последовательности,
завершающейся числом 0.
Сам ноль в последовательность не входит.
"""

cnt = acc = 0
x = int(input())
while x: # x != 0
    acc += x
    cnt += 1
    x = int(input())
print(acc / cnt)

