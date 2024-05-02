#       ENFOQUE: PROBABILIDAD    #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Probabilidad - Incertidumbre

#Incertidumbre en probabilidad trata de la aleatoriedad de los eventos, es decir, la incertidumbre de los resultados de un experimento.

import numpy as np
import matplotlib.pyplot as plt

# Definimos la media y la desviación estándar de nuestras ventas diarias
# Suponemos que las ventas diarias promedio son de 100 unidades con una desviación estándar de 20 unidades
media_ventas = 100
std_ventas = 20

# Generamos 365 días de ventas utilizando una distribución normal
# loc es la media de la distribución, scale es la desviación estándar y size es el número de muestras a generar
ventas = np.random.normal(loc=media_ventas, scale=std_ventas, size=365)

# Creamos un histograma de las ventas
# bins define el número de barras en el histograma, density=True normaliza los datos para que el área bajo el histograma sea 1
# alpha define la transparencia de las barras y color define el color de las barras
plt.hist(ventas, bins=30, density=True, alpha=0.6, color='g')

# Agregamos títulos y etiquetas a la gráfica
plt.title('Distribución de ventas diarias')
plt.xlabel('Ventas (unidades)')
plt.ylabel('Probabilidad')

# Mostramos la gráfica
plt.show()

# Calculamos y mostramos algunas estadísticas de nuestras ventas
# La función mean calcula la media de las ventas, std calcula la desviación estándar, max devuelve la venta máxima y min la venta mínima
print(f'Ventas promedio: {ventas.mean():.2f}')
print(f'Desviación estándar de las ventas: {ventas.std():.2f}')
print(f'Venta máxima: {ventas.max():.2f}')
print(f'Venta mínima: {ventas.min():.2f}')