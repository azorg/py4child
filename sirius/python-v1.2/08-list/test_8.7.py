#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выведите значение наименьшего из всех положительных элементов в списке.
Известно, что в списке есть хотя бы один положительный элемент.
"""

inp = tuple(map(int, input().split()))

print(min(filter(lambda x: x > 0, inp)))


