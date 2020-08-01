# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:05:40 2020

@author: Engel
"""

import numpy as np 
import matplotlib.pyplot as plt 

#Creamos una funcion para coseno 
g = lambda x: np.cos(x) + 2
#Creamos una fucnion exponencial 
h = lambda x: np.exp(x) 
#Creamos una funcion seno 
f = lambda x: np.sin(x)+1  

#Para definir el rango y numero de puntos 
x=np.arange(0,10,0.1)


#Vamos a hacer una matriz cuadrada de dos filas y dos columnas, 
#Para mostrar las fucniones en cuadros distintos 
plt.subplot(2,2,1) 
plt.plot(x,g(x))    

plt.subplot(2,2,2) 
plt.plot(x,h(x))

plt.subplot(2,2,3)  
plt.plot(x,f(x))

plt.savefig('Graficas.png')

