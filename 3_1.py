# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:07:00 2022

@author: P70073624
"""

import numpy as np
import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase,1):
   values[letter] = index 
for index, letter in enumerate(string.ascii_uppercase,1):
   values[letter] = index + 26

with open('input_3.txt') as f:
    lines = f.readlines()
priority = 0
for i in lines:
    i = i.split('\n')[0]
    str1, str2 = i[:len(i)//2], i[len(i)//2:]
    common=list(set(str1)&set(str2))[0]
    priority = priority + values[common]