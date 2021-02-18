#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выведите все элементы списка с чётными индексами
(то есть A[0], A[2], A[4], ...).
"""

inp = map(int, input().split())
out = map(str, tuple(inp)[::2])

print(" ".join(out))


