#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico
#Tema: Monte Carlo para Cadenas de Markov

#Monte carlo para cadenas de markov se utiliza para simular un proceso estocástico, en el cual se generan muestras de una distribución de probabilidad deseada.

import numpy as np
import matplotlib.pyplot as plt

def metropolis_hastings(p, iter=1000):
    x = 0.5  #x representa el precio de las acciones
    muestras = np.zeros(iter)   #Generar un arreglo de ceros

    for i in range(iter):   #en las siguientes lineas se generan las muestras
        x_propuesta = np.random.normal(x, 0.5)  # Generar una propuesta
        if np.random.rand() < p(x_propuesta) / p(x):  # Aceptar la propuesta?
            x = x_propuesta # Si la propuesta es aceptada, se actualiza x
        muestras[i] = x # Guardar la muestra

    return muestras

#tenemos una función de probabilidad para los precios de las acciones
def p(x):
    return np.exp(-np.abs(x - 0.5)) # Función de probabilidad de las acciones

# Obtener muestras utilizando MCMC
muestras = metropolis_hastings(p, iter=10000)

# Visualizar las muestras
plt.hist(muestras, bins=30, density=True)   #Histograma de las muestras
plt.title('Distribución de precios de acciones')    
plt.show()  #Mostrar el histograma