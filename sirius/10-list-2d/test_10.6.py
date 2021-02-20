#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Кинотеатр
=========
В кинотеатре n ядов по m мест в каждом.
В двумерном массиве хранится информация о проданных билетах,
число 1 означает, что билет на данное место уже продан,
число 0 означает, что место свободно.
Поступил запрос на продажу k билетов на соседние места в одном ряду.
Определите, можно ли выполнить такой запрос.

Входные данные:
Программа получает на вход числа n≤30 и m≤30.
Далее идут n строк, содержащих m чисел (0 или 1),
разделённых пробелами.
Затем дано число k.

Выходные данные:
Программа должна вывести номер ряда, в котором есть k
подряд идущих свободных мест.
Если таких рядов несколько, то выведите номер наименьшего подходящего ряда.
Если подходящего ряда нет, выведите число 0.
"""

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
k = int(input())

ans = 0
for i in range(n): # идем по рядам
    cnt = 0 # счетчик свободных мест на одном ряду
    for j in range(m): # идем по ряду (ищем свободные места подряд)
        if a[i][j] == 0:
            cnt += 1
            if cnt >= k:
                ans = i + 1
                break
        else: # a[i][j] == 1
            cnt = 0
    if ans: break
print(ans)

