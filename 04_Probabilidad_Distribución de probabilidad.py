#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Probabilidad
#Tema: Distribución de Probabilidad

# La distribución de probabilidad describe cómo se distribuyen las probabilidades de los posibles resultados en un experimento

import numpy as np
import matplotlib.pyplot as plt #usa matplotlib para graficar

#las ventas diarias promedio son de 100 unidades con una desviación estándar de 20 unidades
media_ventas = 100
std_ventas = 20

#ventas es un array de NumPy que contiene 365 valores generados aleatoriamente a partir de una distribución normal
ventas = np.random.normal(loc=media_ventas, scale=std_ventas, size=365) #loc=media, scale=desviación estándar, size=365: 365 valores

# histograma de las ventas
# El argumento density=True en la función plt.hist asegura que el histograma esté normalizado
plt.hist(ventas, bins=30, density=True, alpha=0.6, color='g')   #bins=30: 30 barras

# Agregamos títulos y etiquetas a la gráfica
plt.title('Distribución de ventas diarias') 
plt.xlabel('Ventas (unidades)') 
plt.ylabel('Probabilidad')

# Mostramos la gráfica
plt.show()

# Calculamos y mostramos algunas estadísticas de nuestras ventas
print(f'Ventas promedio: {ventas.mean():.2f}')  #mean(): promedio  
print(f'Desviación estándar de las ventas: {ventas.std():.2f}') #std(): desviación estándar
print(f'Venta máxima: {ventas.max():.2f}')  #max(): máximo
print(f'Venta mínima: {ventas.min():.2f}')  #min(): mínimo

