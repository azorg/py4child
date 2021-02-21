#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ханойские башни
===============
Головоломка “Ханойские башни” состоит из трёх стержней,
пронумерованных числами 1, 2, 3. На стержень 1 надета 
пирамидка из n дисков различного диаметра в порядке
возрастания диаметра дисков, если рассматривать их сверху вниз.
Диски можно перекладывать с одного стержня на другой по одному,
при этом диск нельзя класть на диск меньшего диаметра.
Необходимо переложить всю пирамидку со стержня 1 на стержень 3,
используя стержень 2 как вспомогательный, за минимальное
число перекладываний.

Напишите функцию, которая решает головоломку:
для данного числа дисков n печатает последовательность
перекладываний в формате a b c, где
a — номер перекладываемого диска (1 - самый маленький),
b — номер стержня, с которого снимается данный диск,
c — номер стержня, на который надевается данный диск.

Например, строка 1 2 3 означает перемещение диска номер
1 со стержня 2 на стержень 3. В одной строке печатается
одна команда. Диски пронумерованы числами от 1 до n в
порядке возрастания диаметров.

    |       |       |
   *|*      |       |
  **|**     |       |
 ***|***    |       |
----+-------+-------+----
    1       2       3

Входные данные:
Задано натуральное число n≤10 — размер пирамидки.

Выходные данные:
Программа должна вывести минимальный (по количеству
произведённых операций) способ перекладывания пирамидки
из данного числа дисков.

Примеры:
n=3
1 1 3
2 1 2
1 3 2
3 1 3
1 2 1
2 2 3
1 1 3
"""

n = int(input())

# переложить n-дисков со стержня src (1-3) на стержень dsc(1-3)
def hanoy(n, src, dst):
    if n:
        free = 6 - src - dst
        hanoy(n - 1, src, free)
        print(n, src, dst)
        hanoy(n - 1, free, dst)
        
hanoy(n, 1, 3)

