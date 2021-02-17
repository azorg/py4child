#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, которая будет считывать два целых числа
(каждое в отдельной строке) и выводить их сумму.
"""

a = int(input("a="))
b = int(input("b="))

a += b
b = a - b
a -= b

print("a=", a, sep='')
print("b=", b, sep='')


