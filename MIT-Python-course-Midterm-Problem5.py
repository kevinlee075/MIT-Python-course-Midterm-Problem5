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
    
    for item in aDict.keys():                                                  #the keys in new_dict are the values of aDict, and the values will be the counts
                                                                               #i.e. {value3 : 2times, value4 : 1time, value6 : 3time, value1: 1time...}
        if aDict[item] in new_dict:                                            #if a certain key in new_dict exists a certain value in aDict, add 1 to that key in new_dict
            new_dict[aDict[item]] += 1
            
        elif aDict[item] not in new_dict:                                      #if a certain key in new_dict is an unique value in aDict, the value of that key is 1 (time)
            new_dict[aDict[item]] = 1

    for aDict_value in new_dict.keys():                                        #after the new_dict is formed, search all unique keys and add them to the new_list
        
        if new_dict[aDict_value] == 1:                                         #search keys with value == 1
            
            for unique in aDict.keys():                                        #check every key in aDict
                
                if aDict[unique] == aDict_value:                               #if the values in aDict are equal to the keys of new_dict, it means that key in aDict is unique, so it should be added to the new_list
                    new_list.append(unique)
    
    new_list.sort()                                                            #mutate the new_list the one with increasing ordered elements
    return new_list
                
        
    
        
    