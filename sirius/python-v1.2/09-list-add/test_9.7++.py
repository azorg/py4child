#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дан список чисел. В списке все элементы различны.
Поменяйте местами минимальный и максимальный элемент этого списка.
"""

a = list(map(int, input().split()))
i_min = a.index(min(a))
i_max = a.index(max(a))
a[i_min], a[i_max] = a[i_max], a[i_min]
print(" ".join(map(str, a)))

