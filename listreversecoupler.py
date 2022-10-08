# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 07:22:20 2022

@author: SHRESHTHANGSHU
"""

"""
l1=[100,200,300,400]
l2=[10,20,30,40]
using for loop print 
100 40
200 30
300 20
400 10
"""


l1=[100,200,300,400]
l2=[10,20,30,40]
l2.reverse()
for i in range(len(l1)):
    for j in range(len(l2)):
        if i == j:
            print(l1[i],l2[j])

