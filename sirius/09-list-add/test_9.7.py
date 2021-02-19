#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дан список. Не изменяя его и не используя дополнительные
списки, определите, какое число в этом списке встречается чаще всего.
Если таких чисел несколько, выведите любое из них.
"""

a = tuple(map(int, input().split()))

res = a[0]
resc = a.count(res) 
for x in a[1:]:
    cnt = a.count(x)
    if resc < cnt:
        resc = cnt;
        res = x

print(res)

