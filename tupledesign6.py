# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 15:05:16 2022

@author: SHRESHTHANGSHU
"""

def func1(person1,*person2):
    print(person1)
    print(person2)
def func2(person1,**person2):
    print(person1)
    print(person2)
    
func1(1,2,3,4,5,6)
func2(1,a=2,b=4)