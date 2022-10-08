# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 04:37:55 2022

@author: SHRESHTHANGSHU
"""

#create 2 list, then create a set such that it shows the element from both list in a pair.(without Using zip function)
l1=['a','b','c','d']
l2=['m','n','o','p']

res = {(l1[i], l2[j]) for i in range(len(l1)) for j in range(len(l2)) if i==j}

print(res)
#print(type(res))