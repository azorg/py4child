#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дана строка.
Измените регистр символов в этой строке так,
чтобы первая буква каждого слова была заглавной,
а остальные буквы — строчными.

Решение оформите в виде функции Capitalize(S),
возвращающей новую строку.
"""


def Capitalize(S):
    def upCase(c):
        if ord('a') <= ord(c) <= ord('z'):
            return chr(ord(c) - (ord('a') - ord('A')))
        return c
    
    def downCase(c):
        if ord('A') <= ord(c) <= ord('Z'):
            return chr(ord(c) + (ord('a') - ord('A')))
        return c

    def isAlpha(c):
        return ord('A') <= ord(c) <= ord('Z') or \
               ord('a') <= ord(c) <= ord('z')

    ret = []
    word = False
    for c in S:
        if isAlpha(c):
            if word:
                ret.append(downCase(c))
            else:   
                ret.append(upCase(c))
                word = True
        else:
            word = False
            ret.append(c)
    return "".join(ret)

S = input()
print(Capitalize(S))

