# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 16:39:14 2014

@author: cwallace
"""
from pattern.en import *

def open_Book(filename):
    '''
    Opens a File from the location inputted as a text and returns the sentiment of 
    that text file.'''
    
    f = open(filename,'r')
    fulltext = f.read()
    fulltext = fulltext[fulltext.index('***')+4:]
    fulltext = fulltext[fulltext.index('***')+4:]
    fulltext = fulltext[:fulltext.index('***')]

       
    

    
    f.close()
    return sentiment(fulltext)
    
  
        
   
        
                
   
    