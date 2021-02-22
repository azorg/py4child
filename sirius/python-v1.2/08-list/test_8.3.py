#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выведите все чётные элементы списка.
"""

inp = map(int, input().split())

if True:
    out = []
    for i in inp:
        if i % 2 == 0:
            out.append(str(i))
else:
    out = map(str, filter(lambda x: x % 2 == 0, inp))

print(" ".join(out))


