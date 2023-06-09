#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Шеренга
=======
Петя перешёл в другую школу.
На уроке физкультуры ему понадобилось определить своё место в строю.
Помогите ему это сделать.

Входные данные:
Программа получает на вход невозрастающую последовательность
натуральных чисел, означающих рост каждого человека в строю.
После этого вводится число X — рост Пети.
Все числа во входных данных натуральные и не превышают 200 по значению.

Выходные данные:
Выведите номер, под которым Петя должен встать в строй.
Если в строю есть люди с одинаковым ростом, таким же, как у Пети,
то он должен встать после них.
"""

h = list(map(int, input().split()))
x = int(input())
h.sort(reverse=True)
head = list(filter(lambda y: y >= x, h))
print(len(head) + 1)

