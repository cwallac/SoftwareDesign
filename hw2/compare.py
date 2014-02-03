# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:37:24 2014

@author: cwallace
"""

def compare(x,y):
    if x > y:
        return 1
        
    elif x == y:
        return 0
        
    elif x < y:
        return -1
        
print compare(2,1) #1
print compare(2,2) #0
print compare(1,2) #-1