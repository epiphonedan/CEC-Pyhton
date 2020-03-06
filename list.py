# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:10:46 2020

@author: CEC
"""

def createList(n):
    myList=[]
    for i in range(n):
        myList.append(i)
    return myList
print(createList(5))