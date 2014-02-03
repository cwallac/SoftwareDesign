# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:58:29 2014

@author: cwallace
"""
def gridPattern(n):
    
    def printRow(n):
        print '+' + ('-'*4 + '+')*n
    
    def printFiller(n):
        for i in range(4):
            print '|' + (' '*4 + '|')*n
    
    printRow(n)        
    for i in range(n):
        printFiller(n)
        printRow(n)
        
gridPattern(3)

        
    
    
    
