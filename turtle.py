# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:03:53 2019

@author: CEC
"""
from turtle import *
color('magenta', 'blue')
begin_fill()
while True:
    forward(100)
    left(-120)
    if abs(pos()) < 1:
        break
end_fill()
done()