#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дан список. Выведите те его элементы, которые встречаются
в списке только один раз. Элементы нужно выводить в том порядке,
в котором они встречаются в списке.
В данной задаче запрещено пользоваться всеми операциями
над списками (find, count, index и так далее).
"""

a = tuple(map(int, input().split()))
b = []
for i in range(len(a)):
    x = a[i]
    if x not in a[:i] and \
       x not in a[i+1:]:
        b.append(x)

print(" ".join(map(str, b)))

