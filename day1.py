# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv

print("Hello PÓK")
i = 0
step = 0
with open("C:\Marci\learn\AdventOfCode\input1.txt","r") as inputfile:
    while 1:
        char = inputfile.read(1)
        if char:
            step = step+1
            if char == '(':
                i = i+1
            else:
                i = i-1
            if i == -1:
                print(step)
                break
        else:
            break