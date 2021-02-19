#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Дана строка.
Замените в этой строке все появления буквы h на букву H,
кроме первого и последнего вхождения.
"""

s = input()

i = s.find("h")
if i < 0: i = 0
else: i += 1

j = s[i:].rfind("h")
if j < 0: j = len(s)
else: j += i

#print("".join((s[:i], s[i:j].replace("h", "H"), s[j:])))
print(s[:i] + s[i:j].replace("h", "H") + s[j:])

