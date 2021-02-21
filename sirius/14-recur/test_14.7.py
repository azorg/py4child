#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Фишки
=====
Дана полоска из клеток, пронумерованных от 1 до N слева направо.
Разрешено:
 - Снимать или ставить фишку на клетку с номером 1.
 - Ставить фишку на клетку, следующую за самой левой
   из установленных фишек (правее неё), если она пуста.
 - Удалять фишку на клетке, следующей за самой левой из
   установленных фишек (правее неё), если она занята.

Изначально полоска пуста. Нужно разместить фишки во всех клетках.

Входные данные:
Программа получает на вход количество клеток в полоске N(1≤N≤10).

Выходные данные:
Программа должна вывести последовательность номеров клеток,
с которыми совершается действие. Если фишка снимается,
то номер клетки должен выводиться со знаком минус.
Количество действий не должно превышать 10**4.
Если существует несколько возможных решений задачи,
то разрешается вывести любое.

Пример:
n=3
1 2 -1 3 1
"""

n = int(input())

def prn(x):
    print(x, "", end="")

def erase(n):
    if n > 0:
        erase(n - 2)
        prn(-n)
        fill(n - 2)
        erase(n - 1)

def fill(n):
    if n == 1:
        prn(1)
    elif n > 1:
        fill(n - 1) 
        erase(n - 2)
        prn(n)
        fill(n - 2) 

fill(n)
print()


