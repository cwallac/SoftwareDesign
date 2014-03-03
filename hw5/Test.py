
#-*- coding: utf-8 -*-
"""
Created on Sun Mar  2 16:06:55 2014

@author: cwallace
"""
from Functions import open_Book
Works = {}
IlBooks = ['BuckleyIliad','PopeIliad','ButlerIliad']

Works['Iliad'] = IlBooks


TransPos = {}
TransSub = {}
for Work in Works:
    Positivity = {}
    totalPos = 0
    totalSub = 0 
    Subjectivity = {}
    print Work
    for Book in Works[Work]:
        
        sentiment = open_Book(Book+'.txt')
        Positivity[Book] = sentiment[0]
        Subjectivity[Book] = sentiment[1]
        totalPos += sentiment[0]
        totalSub += sentiment[1]
        
    print Positivity, Subjectivity
    Positivity['AVERAGE'] = totalPos/len(Works[Work])
    Subjectivity['AVERAGE'] = totalSub/len(Works[Work])
    TransPos[Work] = Positivity['AVERAGE']
    TransSub[Work] = Subjectivity['AVERAGE']
     
print TransPos, TransSub
    