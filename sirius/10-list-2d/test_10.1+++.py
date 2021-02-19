#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Симметричен ли массив?
======================
Дано число n и массив размером n×n.
Проверьте, является ли этот массив симметричным относительно главной диагонали.
Выведите слово “YES”, если массив симметричный, и слово “NO” в противном случае.

Входные данные:
В первой строке дано значение n≤10.
Далее идут n строк по n чисел — элементы матрицы.
"""

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

res = True
for i in range(n):
    for j in range(i+1, n):
        if a[i][j] != a[j][i]:
            res = False
            break

if res:
    print("YES")
else:
    print("NO")


