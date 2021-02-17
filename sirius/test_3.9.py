#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
На каждой странице книги напечатано ровно k строк:
на первой странице находятся строки с 1 по k, на второй — c k+1 по 2k и т.д.
Определите, на какой странице находится строка номер n
и какой по счёту будет эта строка на странице.
Даны натуральные числа k
и n, каждое в отдельной строке.
Программа должна считать их и вывести два числа:
номер страницы и номер строки на странице.
"""
k = int(input()) # число строк на странице
n = int(input()) # номер строки (начианя с 1)

print((n - 1) // k + 1,
      (n - 1) %  k + 1)



