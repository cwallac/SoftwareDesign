# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import randint
from math import *
import Image

def build_random_function(min_depth, max_depth):
    # your doc string goes here
    ''' Inputs a minimum and maximum depth of recursion (min, max), creates a randomly nested list corresponding to function
    operations and parameters. Available operations are cos(pi*x), sin(pi*x), arctan(x),products(x,y), x**2 and then either the x or y value
    Outputs a nested listed in the form of [operation,[paramter],[parameter]]
    # your code goes here
    
    
    if min_depth > 0:
        choices = [['prod',['a'],['b']],['cos_pi',['a']],['sin_pi',['a']],['arctan',['a']],['squared',['a']]]
        randnum = randint(0,len(choices)-1)

        if choices[randnum] == ['prod',['a'],['b']]:
            return ['prod', build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]

        else:
            return [choices[randnum][0],build_random_function(min_depth-1,max_depth-1)]

    if max_depth == 0:
        choices = [['a'],['b']]
        randnum = randint(0,len(choices)-1)
        return choices[randnum]

    else:
        choices = [['prod',['a'],['b']],['cos_pi',['a']],['sin_pi',['a']],['arctan',['a']],['squared',['a']],['a'],['b']]
        randnum = randint(0,len(choices)-1)
        if randnum > 4:
            return choices[randnum]
        
        elif choices[randnum] == ['prod',['a'],['b']]:
            return ['prod', build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]

        else:
            return [choices[randnum][0],build_random_function(min_depth-1,max_depth-1)]



        
def evaluate_random_function(f, x, y):
    # your doc string goes here
    '''
    Takes three inputs(f,x,y), first of which being a function constructed using build_random_function. 
    General form is a list: ['operator,[parameter1],[parameter2]] parameters can be nested lists
    in the same form. Inputs of x and y must be between 1 and negative 1 that will be input into the function'''
    # your code goes here
    
    if f == ['a']:
        return x
    elif f == ['b']:
        return y
    elif f[0] == 'cos_pi' :
        
        return cos(pi*evaluate_random_function(f[1], x, y))
    elif f[0] == 'sin_pi':
        return sin(pi*evaluate_random_function(f[1], x, y))
    elif f[0] == 'arctan':
        return atan(evaluate_random_function(f[1], x, y))
    elif f[0] == 'squared':
        return evaluate_random_function(f[1], x, y)**2
    else:
        
        return evaluate_random_function(f[1], x, y)*evaluate_random_function(f[2], x, y)

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
       is an affine one (i.e. output = input*c + b).
       Inputs are: (val, input_interval_start, input_interval_end, output_interval_start, output_interval_end)
        
    """
    # your code goes here
    
    outputRange = abs(output_interval_start - output_interval_end)
    inputRange = abs(input_interval_start - input_interval_end)
    scale = outputRange/inputRange
    return val*scale+output_interval_start
 
# RUN AND GENERATE THE IMAGE, SAVE IT IN THE WORKING DIRECTORY   
img = Image.new("RGB",(350,350))
pixels = img.load()
blue = build_random_function(10,15)
red = build_random_function(10,15)
green = build_random_function(10,15)
for i in range(350):
    for j in range(350):
        xmap = remap_interval(j,0,349.0,-1,1)
        ymap = remap_interval(i,0,349.0,-1,1)
        blueval = int(remap_interval(evaluate_random_function(blue, xmap, ymap),-1,1.0,0,255))
        greenval = int(remap_interval(evaluate_random_function(green, xmap, ymap),-1,1.0,0,255))
        redval = int(remap_interval(evaluate_random_function(red, xmap, ymap),-1,1.0,0,255))
        
        pixels[i,j] = (redval, greenval, blueval)
       
img.save("4Deep.bmp")


 

        

    
    
    
    