#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите функцию CaseChange (c), меняющую регистр символа,
то есть переводящую заглавные буквы в строчные,
а строчные — в заглавные, остальные символы меняться не должны.
В решении нельзя использовать циклы.
В решении нельзя использовать константы с неочевидным значением.
"""

def CaseChange(c):
    off = ord('a') - ord('A')
    code = ord(c)
    if   ord('a') <= code <= ord('z'): code -= off
    elif ord('A') <= code <= ord('Z'): code += off
    return chr(code)

a = input()
ans = CaseChange(a)
print(ans)

