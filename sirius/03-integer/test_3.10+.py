#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дано целое число n. Выведите следующее за ним чётное число.
"""

n = int(input())

print(n - (n % 2) + 2)


