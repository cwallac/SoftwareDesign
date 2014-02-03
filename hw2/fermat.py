# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:55:59 2014

@author: cwallace
"""

def check_fermat(a,b,c,n):
    if n > 2:
        if (a**n + b**n == c**n):
            print 'FERMAT WAS WRONG'
        else: 
            print "No, that doesn't work"
            
    else: 
            print "N must be greater than two"
            
check_fermat(1,2,3,1)

def user_check():
   a = int(raw_input('Give a value for a'))
   b = int(raw_input('Give a value for b'))
   c = int(raw_input('Give a value for c'))
   n = int(raw_input('Give a value for n (greater than 2)'))
   check_fermat(a,b,c,n)
   
user_check()