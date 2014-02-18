# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:55:59 2014

@author: cwallace
"""

def check_fermat(a,b,c,n):
    if n > 2:                             # you can combind these two
        if (a**n + b**n == c**n):         # conditionals to make it a single conditional
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

'''
Once again, excellent work.
One comment: you can combine the two conditionals 
to make it a single conditional and not have the
"N must be greater than two" print line
'''