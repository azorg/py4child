#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дано число N.
Выведите N квадратов чисел от 1 до N (включительно) в формате [1, 4, 9, 16,…, N**2].
Используйте функцию print() для вывода списка.
"""

n = int(input())

print(list(map(lambda x: x*x, range(1, n + 1))))

