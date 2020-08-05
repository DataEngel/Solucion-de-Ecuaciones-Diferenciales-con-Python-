# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 01:32:53 2020

@author: Engel
"""

import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
    return np.sin(x)   

g= lambda x: np.cos(x) 

v=[0,10,-4,4]  

x=np.linspace(0,10,100)  

plt.plot(x,f(x),'b--',label='Seno')      
plt.plot(x,g(x), label='coseno')  
plt.xlabel('tiempo')
plt.ylabel('posicion') 
plt.title('funcion seno') 
plt.legend(loc=1)
plt.text(4,0,'prueba')
plt.axis(v)
plt.grid()
