import numpy as np 
import matplotlib.pyplot as plt
from scipy import integrate 

#Definimos numerica de dy/dx, osea la funcion que vamos a resolver
def f(y,x): 
    return (x**2)*(1+y) 

#Definimos exacta de dy/dx, osea la funcion que vamos a resolver
def ex(x): 
    return 4*(np.exp(x**3/3)) - 1  

#Ahora vamos a definir la condicion inicial
y0=3.0 

#Definimos el rango donde vamos a obtener la solucion.
x=np.linspace(0,1,100) 

#Ahora la solucion 
result=integrate.odeint(f,y0,x) 

#Graficamos los datos de la solucion numerica
fig, axes=plt.subplots()
axes.plot(x,result,'--')
axes.plot(x,ex(x))
plt.show() 

#Graficamos los datos de la solucion exacta. 
fig, axes=plt.subplots() 
axes.plot(x,ex(x))
plt.show()   