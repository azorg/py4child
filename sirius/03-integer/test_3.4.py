#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дано четырёхзначное число. Найдите сумму его цифр.
"""

n = int(input())

print((n % 10) + 
      (n % 100)   // 10 +
      (n % 1000)  // 100 +
      (n % 10000) // 1000)

