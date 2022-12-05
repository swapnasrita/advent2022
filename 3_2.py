# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:41:24 2022

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
for i in range(0,len(lines),3):
    str1 = lines[i].split('\n')[0]
    str2 = lines[i+1].split('\n')[0]
    str3 = lines[i+2].split('\n')[0]
    common=list(set(str1)&set(str2)&set(str3))[0]
    priority = priority + values[common]