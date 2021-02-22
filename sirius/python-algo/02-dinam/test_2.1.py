#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Числа Фибоначчи
===============
Числа Фибоначчи определяются следующими формулами:
F0=0, F1=1, Fn=Fn−1+Fn–2 при n≥2.

Входные данные:
На вход программе подаётся целое неотрицательное n≤45.

Выходные данные:
Выведите n-е число Фибоначчи.
"""

m = 45
dp = [-1] * (m + 1)

def F(n):
    if dp[n] != -1:
        return dp[n]
    if n < 2:
        return n
    dp[n] = F(n - 1) + F(n - 2)
    return dp[n]

n = int(input())

print(F(n))


