# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:12:48 2020

@author: Engel
"""

import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 

k = 1.0
m = 5.0
b = 0.4

def f(A, t): 
    x, v = A
    return [v, -(k/m)*x -(b/m)*b] 

f0 = [1.0, 0]
t = np.linspace(0, 50, 200)
result = odeint(f,f0,t) 

fig, axes = plt.subplots()
axes.plot(t, result[:,0], 'g')  
axes.plot(t, result[:,1], 'b')
plt.grid() 
plt.show()       
      