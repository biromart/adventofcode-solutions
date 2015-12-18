# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:27:52 2015

@author: Marton.Biro
"""


sum = 0
step = 0
with open("C:\Marci\learn\AdventOfCode\input2.txt","r") as inputfile:
    for line in inputfile:
        step += 1
        print("Step: " + str(step))
        dims = [int(n) for n in line[:-1].split("x")]
        print(dims)
#        sum += dims[0] * dims[1] * 2 + dims[0] * dims[2] * 2 + dims[1] * dims[2] * 2
#        del dims[dims.index(max(dims))]
#        print("Min values: " + str(dims))
#        sum += dims[0] * dims[1]
        sum += dims[0] * dims[1] * dims[2]
        print(sum)
        del dims[dims.index(max(dims))]
        print("Min values: " + str(dims))
        sum += (dims[0] + dims[1]) * 2

print(sum)