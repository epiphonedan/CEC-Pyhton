# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:28:44 2019

@author: UPS

TEST DE VELICIDAD
"""
import numpy as np
import time
 
SIZE = 1000000
 
L1= range(SIZE)
L2= range(SIZE)
A1= np.arange(SIZE)
A2=np.arange(SIZE)
print ("\n"*1)
print ("RESULTADO USANDO LISTAS/TUPLAS EN PYTHON")
start= time.time()
result=[(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)
print ("\n"*2)
print ("RESULTADO USANDO NUMPY")
start=time.time()
result= A1+A2
print((time.time()-start)*1000)