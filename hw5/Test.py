
#-*- coding: utf-8 -*-
"""
Created on Sun Mar  2 16:06:55 2014

@author: cwallace
"""
from Functions import open_Book
Works = {}
returnList = []
OdBooks = ['ButlerOdyssey','PopeOdyssey','CowperOdyssey']
IlBooks = ['BuckleyIliad','PopeIliad','ButlerIliad']

Works['Iliad'] = IlBooks
Works['Odyysey'] = OdBooks

TransPos = {}
TransSub = {}
resultsFile = open('RESULTS.txt','w+')
for Work in Works:
    Positivity = {}

    Subjectivity = {}
    
    for Book in Works[Work]:
        
        sentiment = open_Book(Book+'.txt')
        Positivity[Book] = sentiment[0]
        Subjectivity[Book] = sentiment[1]
        
        
    for key, value in Positivity.iteritems():
        resultsFile.write(str(key) + ',' + 'Positivity' + ',' + str(value)+ '\n')
        
    resultsFile.write('\n')
    for key, value in Subjectivity.iteritems():
        resultsFile.write(str(key) + ',' + 'Subjectivity' + ',' + str(value)+ '\n')
    resultsFile.write('\n')
    
    

resultsFile.close()
 #First Dictionary is Positivity Second is Subjectivity


    