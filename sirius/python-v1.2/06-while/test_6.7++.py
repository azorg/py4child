#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выдача сдачи
============
Имеется неограниченное количество монет в 1, 2, 5, 10 рублей.
Определите, сколькими способами можно выдать сдачу в n рублей.
Например, 5 рублей можно выдать четырьмя способами:
5 = 2 + 2 + 1 = 2 + 1 + 1 + 1 = 1 + 1 + 1 + 1 + 1.

Входные данные:
Программа получает на вход натуральное число n, не превышающее 100.
"""
n = int(input())
nmax = 1000 # максимальный размер сдачи
cnt = 0 # счеткик вариантов
i1 = i2 = i5 = i10 = 0 # счетчики монет
m1  = nmax
m2  = nmax // 2
m5  = nmax // 5
m10 = nmax // 10
m   = 0
while True:
    if m == n:
        cnt += 1
    i1 += 1
    if i1 > m1:
        i1 = 0
        i2 += 1
        if i2 > m2:
            i2 = 0
            i5 += 1
            if i5 > m5:
                i5 = 0
                i10 += 1
                if i10 > m10:
                    break
    m = i1 + i2 * 2 + i5 * 5 + i10 * 10
print(cnt)
