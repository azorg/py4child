#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Отношение
=========
Дан массив a1, a2, … an.
Необходимо выбрать в нём два элемента ai и aj такие,
что i < j, и отношение aj / ai максимально и больше 1.

Входные данные:
В первой строке задано целое число 2 ≤ n ≤ 100000 —
количество элементов в массиве.

Во второй строке заданы n
целых положительных чисел ai (1 ≤ i ≤ n, 1 ≤ ai ≤ 5000).

Выходные данные:
Выведите два числа — индексы элементов i и j. 
Если ответов несколько, то выведите любой из них.
Если ответа нет, то выведите два нуля, разделённых пробелом.

Пример:
Ввод:            Вывод:
6                2 5
10 3 5 3 11 9

4                3 4
3 6 2 5
"""

n = int(input())
a = tuple(map(int, input().split()))

imin = imax = jmax = 0
for j in range(2, n):
    if a[imin] > a[j - 1]:
        imin = j - 1
    if 1. < a[j] / a[imin] > a[jmax] / a[imax]:
        imax = imin
        jmax = j

if jmax:
    print(imax + 1, jmax + 1)
else:
    print("0 0")


