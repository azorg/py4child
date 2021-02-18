#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выведите все чётные элементы списка.
"""

inp = map(int, input().split())
out = map(str, tuple(inp)[1::2])

print(" ".join(out))


