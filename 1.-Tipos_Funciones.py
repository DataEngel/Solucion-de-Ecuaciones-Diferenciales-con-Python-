# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 

def funcion(x,y=2): 
    return x + 2 + y

print('El resultado de la funcion basica es: ', funcion(2))  

def funcion_basic(x):
    return np.sin(x)

print('El resultado operacion de la funcion lamda es: ', funcion_basic(np.pi/2))

 
f = lambda x,y=3 : x + 2

print('El resultado de la funcion lambda ', f(2))   
