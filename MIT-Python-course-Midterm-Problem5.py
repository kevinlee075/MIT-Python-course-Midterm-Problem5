# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 16:29:13 2021

@author: Lenovo
"""

#Write a Python function that returns a list of keys in aDict that map to integer\
#values that are unique (i.e. values appear exactly once in aDict).
#The list of keys you return should be sorted in increasing order.
#(If aDict does not contain any unique values, you should return an empty list.)

#This function takes in a dictionary and returns a list.

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    new_list = []
    new_dict = {}
    for item in aDict.keys():
        if aDict[item] in new_dict:
            new_dict[aDict[item]] += 1
        elif aDict[item] not in new_dict:
            new_dict[aDict[item]] = 1
    for count in new_dict.keys():
        if 
        
    
        
    