#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico
#Tema: Muestreo Directo y Por Rechazo

#El muestreo directo y por rechazo son dos técnicas de muestreo que permiten generar muestras de una distribución de probabilidad dada.

import numpy as np     #se importa numpy para trabajar con arreglos
import matplotlib.pyplot as plt #se usa matplotlib para graficar
from scipy.stats import norm, cauchy    #se uttiliza scipy para importar las distribuciones normales y de cauchy

# Muestreo Directo
muestras_directas = np.random.normal(0, 1, 10000)   #se generan 10000 muestras de una distribución normal con media 0 y desviación estándar 1

# Muestreo por Rechazo
muestras_rechazo = []
M = cauchy.pdf(0) / norm.pdf(0)  # Escalar para la distribución de propuesta

while len(muestras_rechazo) < 10000:    #mientras el número de muestras sea menor a 10000
    propuesta = np.random.standard_cauchy()  #se genera una propuesta de una distribución de cauchy
    prob_aceptacion = norm.pdf(propuesta) / (M * cauchy.pdf(propuesta))  #cauchy.pdf(propuesta) es la distribución de cauchy evaluada en la propuesta

    if np.random.uniform(0, 1) < prob_aceptacion:   
        muestras_rechazo.append(propuesta)  #se añade la propuesta a las muestras de rechazo

# Visualización
plt.figure(figsize=(12, 6)) #se define el tamaño de la figura
plt.hist(muestras_directas, bins=30, alpha=0.5, label='Muestreo Directo')   #se grafican las muestras directas
plt.hist(muestras_rechazo, bins=30, alpha=0.5, label='Muestreo por Rechazo')    #se grafican las muestras por rechazo
plt.legend()    
plt.show()  #se muestra la gráfica


