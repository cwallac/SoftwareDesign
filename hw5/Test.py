
"# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 16:06:55 2014

@author: cwallace
"""
from Functions import *
Authors = {}
CDBooks = ['AChristmasCarol','OliverTwist','ATaleofTwoCities','DavidCopperField','GreatExpectations']
MTBooks = ['HuckFinn','TomSawyer','RoughingIt','ATrampAbroad','LifeOnTheMississippi']
Romance = ['TheRomanceOfLust']
Authors['CharlesDickens'] = CDBooks
Authors['MarkTwain'] = MTBooks

AuthorAveragePos = {}
AuthorAveSub = {}
for Author in Authors:
    Positivity = {}
    totalPos = 0
    totalSub = 0 
    Subjectivity = {}
    print Author
    for Book in Authors[Author]:
        
        sentiment = open_Book(Book+'.txt')
        Positivity[Book] = sentiment[0]
        Subjectivity[Book] = sentiment[1]
        totalPos += sentiment[0]
        totalSub += sentiment[1]
    Positivity['AVERAGE'] = totalPos/len(Books)
    Subjectivity['AVERAGE'] = totalSub/len(Books)
    AuthorAveragePos[Author] = Positivity['AVERAGE']
    AuthorAveSub[Author] = Subjectivity['AVERAGE']
     
print AuthorAveragePos, AuthorAveSub
    