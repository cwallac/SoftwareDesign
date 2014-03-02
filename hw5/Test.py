# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 16:06:55 2014

@author: cwallace
"""
from Functions import *
Books = {}
IlBooks = ['BuckleyIliad','ButlerIliad','PopeIliad'] ##Names Of File

Books['Iliad'] = IlBooks


AuthorAveragePos = {}
AuthorAveSub = {}
for Work in Books:
    Positivity = {}
    totalPos = 0
    totalSub = 0 
    Subjectivity = {}
    print Author
    for Book in Books[Work]:
        
        sentiment = open_Book(Book+'.txt')
        Positivity[Book] = sentiment[0]
        Subjectivity[Book] = sentiment[1]
        totalPos += sentiment[0]
        totalSub += sentiment[1]
    Positivity['AVERAGE'] = totalPos/len(Books)
    Subjectivity['AVERAGE'] = totalSub/len(Books)
    print Positivity
    AuthorAveragePos[Author] = Positivity['AVERAGE']
    AuthorAveSub[Author] = Subjectivity['AVERAGE']
     
print AuthorAveragePos, AuthorAveSub
    
    
    





