# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:56:23 2020

@author: Engel
"""

import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
    return np.sin(x)   

g= lambda x: np.cos(x) 

v=[0,10,-1,1]  

x=np.linspace(0,10,100)  

plt.plot(x,f(x),'b--',label='Seno')     
plt.plot(x,g(x), label='coseno')  
#Agragamos un simbolo con latex en el tiempo eje x  
plt.xlabel('tiempo ' r'$\tau$')   
plt.ylabel('posicion') 
plt.title('funcion seno') 
plt.legend(loc=1)
plt.text(4,0,'prueba')
plt.axis(v)
plt.grid()   
#Guardamos la grafica en pdf 
plt.savefig('Seno_Coseno.pdf')    

 


