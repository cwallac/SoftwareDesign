# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 16:39:14 2014

@author: cwallace
"""

def open_Book(filename):
    text = ' '
    returnList = []
    f = open(filename,'r')
    fulltext = f.read()
    fulltext = fulltext[fulltext.index('***')+4:]
    fulltext = fulltext[fulltext.index('***')+4:]
    fulltext = fulltext[:fulltext.index('***')]
    fulltext = fulltext.lower()
    textList = fulltext.split()
    filterIn = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
#    filterIn = ['j','u','l','e','s']   
    for word in textList:
        text = ''
        for letter in word:
            
            if letter in filterIn:
                text += letter
        returnList.append(text)
    
    # fulltext = text.split()
    
    from pattern.en import *
    return sentiment(fulltext)
    
        
   
        
                
    f.close()
    return returnList