# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:39:55 2022

@author: P70073624
"""
import numpy as np

with open('input_2.txt') as f:
    lines = f.readlines()

opp1, opp2 = [np.empty(len(lines), dtype = str) for _ in range(2)]  
for i, line in enumerate(lines):
    opp1[i], opp2[i] = line.split(" ")
    
d_opp1 = {"A":1, "B":2, "C":3}
d_opp2 = {"X":1, "Y":2, "Z":3}

opp1 = [d_opp1[key] for key in opp1]
opp2 = [d_opp2[key] for key in opp2]

score_draw = sum([x+3 for x,y in zip(opp1,opp2) if x == y])

win_opp1 = [(2,1), (3,2), (1,3)]

#win for opp2
score_win = sum([y+6 for x,y in zip(opp1,opp2) if (x,y) not in win_opp1 and x != y])

#loss for opp2
score_loss = sum([y for x,y in zip(opp1,opp2) if (x,y) in win_opp1 ])

print(score_draw+score_loss+score_win)