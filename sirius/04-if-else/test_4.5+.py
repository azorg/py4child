#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Даны три целых числа. Найдите наибольшее из них
(программа должна вывести ровно одно целое число).
Использовать функции max и min, а также логические операции and и or нельзя.
"""

a = int(input())
b = int(input())
c = int(input())

if a < b:
   a = b

if a < c:
   a = c

print(a)


