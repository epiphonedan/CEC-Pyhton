# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:23:46 2020

@author: CEC
"""
switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)
        