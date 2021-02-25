#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Циклические башни
=================
На дорогах Ханоя было введено одностороннее
круговое движение, поэтому теперь диск со стержня 1
можно перекладывать только на стержень 2,
со стержня 2 — на 3, а со стержня 3 — на 1.

Решите головоломку с учётом этих ограничений.
Вам не нужно находить минимальное решение, но количество
совершённых перемещений не должно быть больше 200000
при условии, что количество дисков не превосходит 10.

Входные данные:
Задано натуральное число n≤10 — размер пирамидки.
"""

n = int(input())

# переложить n-дисков со стержня src (1-3) на стержень dsc(1-3)
def hanoy_cyc(n, src, dst):
    if n:
        free = 6 - src - dst
        if (dst - src) % 3 == 1:
            hanoy_cyc(n - 1, src, free)
            print(n, src, dst)
            hanoy_cyc(n - 1, free, dst)
        else:
            hanoy_cyc(n - 1, src, dst)
            print(n, src, free)
            hanoy_cyc(n - 1, dst, src)
            print(n, free, dst)
            hanoy_cyc(n - 1, src, dst)

hanoy_cyc(n, 1, 3)
