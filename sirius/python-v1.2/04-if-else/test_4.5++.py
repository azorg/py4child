#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Даны три целых числа.
Определите, сколько среди них совпадающих.
Программа должна вывести одно из чисел:
  3 (если все числа совпадают),
  2 (если два совпадает) или
  0 (если все числа различны).
"""

a = int(input())
b = int(input())
c = int(input())

cnt = 0

if a == b:
    cnt += 1

if b == c:
    cnt += 1

if a == c:
    cnt += 1

if cnt == 1:
    cnt = 2

print(cnt)


