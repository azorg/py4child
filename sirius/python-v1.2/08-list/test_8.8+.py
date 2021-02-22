#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, которая находит в массиве элемент,
самый близкий по величине к данному числу.
"""

inp = tuple(map(int, input().split()))
val = int(input())

ret = inp[0]
mod = abs(ret - val)
for seq in inp[1:]:
    dif = abs(seq - val)
    if dif < mod:
        ret = seq
        mod = dif

print(ret)

