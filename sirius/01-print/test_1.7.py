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

solve="""
Объяснение: Ну логично,что наименьшим началом числа были
цифры 1,0,2,3,4,5,6,7,8,9, а потом ставим их в обратном порядке исключая 9
т.к она находится по середине, чтобы число было палиндромом а также было кратно 9.Признак делимости на девять-если сумма цифр числа кратна 9,то и само число тоже кратно 9.Сумма цифр числа=81,81 кратно 9.
Результат получен

1023456789876543201
"""

print(1023456789876543201)
