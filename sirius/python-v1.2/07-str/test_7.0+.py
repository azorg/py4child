#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дана строка, состоящая из n цифр (т.е. однозначных чисел),
между которыми стоит n−1 знак операции,
каждый из которых может быть либо +, либо −.
Вычислите значение данного выражения.

Входные данные:
На вход подаётся строка, состоящая из цифр, а также символов + и −.
"""

s = input()
acc = 0
op = 1 # {-1, 1}
index = begin = end = 0
state = 0
last = len(s) - 1
for c in s:
    if state == 0:
        if   c == '-': op = -1
        elif c == '+': op = 1
        elif c == ' ': pass
        else: # if c in "0123456789"
            begin = end = index
            state = 1
    else: # if state == 1
        if c == "+" or c == '-' or c == ' ':
            acc += op * int(s[begin: end + 1])
            if   c == '-': op = -1
            elif c == '+': op = 1
            state = 0
        else: # if c in "0123456789"
            end = index
    index += 1

if state == 1:
    acc += op * int(s[begin:])

print(acc)

