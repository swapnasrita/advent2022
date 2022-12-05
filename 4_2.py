# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 20:16:28 2022

@author: P70073624
"""

import numpy as np

with open('input_4.txt') as f:
    lines = f.readlines()

elf1, elf2 = [np.empty(len(lines), dtype = object) for _ in range(2)]
    
for i,line in enumerate(lines):
    elf1[i],elf2[i] = line.split('\n')[0].split(',')
    elf1[i] = list(range(int(elf1[i].split("-")[0]), int(elf1[i].split("-")[1])+1))
    elf2[i] = list(range(int(elf2[i].split("-")[0]), int(elf2[i].split("-")[1])+1))
 
rep_elf =0
for x,y in zip(elf1,elf2):
    if set(x).intersection(set(y)):
        rep_elf = rep_elf+1