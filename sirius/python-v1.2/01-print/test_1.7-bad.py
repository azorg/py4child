#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Палиндромом называется число, которое читается одинаково слева направо и справа налево.
Например: 121, 4 и 123321 — палиндромы, а 12, 2312 и 123 — нет.

ЗАДАНИЕ:
Выведите на экран наименьшее число, которое содержит в десятичной записи все цифры от 0
до 9, делится на 9 и является палиндромом.

Запись числа не должна содержать ведущих нулей. Например, запись 01
содержит ведущие нули, а 1 — нет.
"""

from itertools import permutations

print(__doc__)

digits = tuple(range(10)) # 0..9

find = int("9" * 20)
for i in permutations(digits):
    if i[0] == 0: continue # исключаем "ведущие" нули
    s = "".join(map(str, i))
    m = int(s + s[::-1])
    if (m % 9) == 0 and find > m:
        find = m

print(find)

