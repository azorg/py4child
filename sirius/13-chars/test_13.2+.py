#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выведите подряд, без пробелов, все символы, лежащие в таблице
ASCII между двумя заданными символами.

Пример на входе:
A
D

На выходе:
ABCD
"""

c1 = input()[0]
c2 = input()[0]
print("".join((chr(i) for i in range(ord(c1), ord(c2) + 1))))

