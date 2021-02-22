#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дан список чисел.
Определите, сколько в этом списке элементов,
которые больше двух своих соседей,
и выведите количество таких элементов.
"""

inp = tuple(map(int, input().split()))
cnt = 0
for i in range(1, len(inp)-1):
    if inp[i-1] < inp[i] > inp[i+1]:
        cnt += 1

print(cnt)


